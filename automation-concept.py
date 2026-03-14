from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REQUIRED_CATEGORIES = {
    "basic_navigation",
    "transaction_support",
    "safety_guidelines",
    "escalation_triggers",
    "edge_cases",
}


@dataclass
class ApprovalRecord:
    change_type: str
    approvers: list[str]
    approved: bool


@dataclass
class TestSummary:
    total_cases: int
    blocker_failures: int
    pass_rate: float
    notes: list[str]


@dataclass
class PromptBundle:
    version: str
    git_sha: str
    created_at: str
    files: list[str]


class MarketplacePromptPipeline:
    """Concept pipeline for versioning, testing, approving, and releasing prompt updates."""

    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root
        self.artifacts_dir = repo_root / "resources" / "artifacts"

    def current_git_sha(self) -> str:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=self.repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return "unknown"

    def load_test_cases(self) -> dict[str, Any]:
        with (self.repo_root / "test-cases.json").open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def validate_test_suite(self) -> TestSummary:
        payload = self.load_test_cases()
        cases = payload["test_cases"]

        if not 30 <= len(cases):
            raise ValueError("Golden suite must contain at least 30 cases.")

        category_counts = {name: 0 for name in REQUIRED_CATEGORIES}
        notes: list[str] = []

        for case in cases:
            category = case["category"]
            if category not in REQUIRED_CATEGORIES:
                raise ValueError(f"Unexpected category: {category}")
            category_counts[category] += 1

        missing = [name for name, count in category_counts.items() if count < 5]
        if missing:
            raise ValueError(f"Each required category needs at least 5 cases. Missing: {missing}")

        for category, count in sorted(category_counts.items()):
            notes.append(f"{category}: {count} cases")

        return TestSummary(
            total_cases=len(cases),
            blocker_failures=0,
            pass_rate=1.0,
            notes=notes,
        )

    def build_prompt_bundle(self) -> PromptBundle:
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        version = f"prompt-{timestamp}"
        files = [
            "prompt.md",
            "prompt-analysis.md",
            "test-cases.json",
            "testing-framework.md",
        ]
        return PromptBundle(
            version=version,
            git_sha=self.current_git_sha(),
            created_at=timestamp,
            files=files,
        )

    def request_approvals(self, change_type: str) -> ApprovalRecord:
        required_approvers = {
            "content_tweak": ["product_reviewer"],
            "workflow_change": ["product_reviewer", "prompt_owner"],
            "policy_change": ["product_owner", "trust_safety_owner"],
            "emergency_patch": ["on_call_owner", "trust_safety_owner"],
        }
        approvers = required_approvers.get(change_type, ["product_reviewer"])
        return ApprovalRecord(change_type=change_type, approvers=approvers, approved=True)

    def run_golden_tests(self, dry_run: bool = True) -> TestSummary:
        suite_summary = self.validate_test_suite()
        notes = list(suite_summary.notes)

        if dry_run:
            notes.append("Dry run only: external model evaluation not executed.")
            return TestSummary(
                total_cases=suite_summary.total_cases,
                blocker_failures=0,
                pass_rate=1.0,
                notes=notes,
            )

        # Pseudocode for actual test run
        payload = self.load_test_cases()
        cases = payload["test_cases"]

        passed_cases = 0
        blocker_failures = 0

        for case in cases:
            # PSEUDO-CODE: send the test input to a staging chatbot endpoint
            # response = call_staging_chatbot(
            #     prompt_bundle=self.build_prompt_bundle(),
            #     user_input=case["input"],
            # )
            # reply_text = response["output_text"]

            reply_text = "<simulated model reply>"

            # PSEUDO-CODE: evaluate the reply against the golden expectations
            # evaluation = evaluate_response(
            #     reply_text=reply_text,
            #     expected_elements=case["expected_elements"],
            #     success_criteria=case["success_criteria"],
            #     category=case["category"],
            # )

            # Simulated evaluation outcome
            evaluation = {
                "passed": True,
                "missing_elements": [],
                "is_blocker": False,
            }

            if evaluation["passed"]:
                passed_cases += 1
                notes.append(f"{case['id']} passed")
            else:
                notes.append(
                    f"{case['id']} failed: missing {evaluation['missing_elements']}"
                )
                if evaluation["is_blocker"]:
                    blocker_failures += 1

        pass_rate = passed_cases / len(cases) if cases else 0.0

        return TestSummary(
            total_cases=len(cases),
            blocker_failures=blocker_failures,
            pass_rate=pass_rate,
            notes=notes,
        )

    def deploy(self, environment: str, bundle: PromptBundle, summary: TestSummary) -> Path:
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        deployment_record = {
            "environment": environment,
            "bundle": asdict(bundle),
            "test_summary": asdict(summary),
            "deployed_at": datetime.now(timezone.utc).isoformat(),
        }
        target = self.artifacts_dir / f"{environment}-deployment.json"
        target.write_text(json.dumps(deployment_record, indent=2), encoding="utf-8")
        return target

    def rollback(self, environment: str, target_version: str) -> Path:
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        rollback_record = {
            "environment": environment,
            "rollback_to": target_version,
            "rolled_back_at": datetime.now(timezone.utc).isoformat(),
            "reason": "Manual or automated rollback trigger.",
        }
        target = self.artifacts_dir / f"{environment}-rollback.json"
        target.write_text(json.dumps(rollback_record, indent=2), encoding="utf-8")
        return target

    def run_release(self, change_type: str, environment: str, dry_run: bool = True) -> dict[str, Any]:
        approvals = self.request_approvals(change_type)
        if not approvals.approved:
            raise RuntimeError("Required approvals were not granted.")

        bundle = self.build_prompt_bundle()
        summary = self.run_golden_tests(dry_run=dry_run)

        if summary.blocker_failures > 0:
            raise RuntimeError("Release blocked by blocker failures.")

        if summary.pass_rate < 0.95:
            raise RuntimeError("Release blocked by pass-rate threshold.")

        deployment_record = self.deploy(environment, bundle, summary)
        return {
            "approvals": asdict(approvals),
            "bundle": asdict(bundle),
            "test_summary": asdict(summary),
            "deployment_record": str(deployment_record),
        }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Concept pipeline for marketplace prompt updates.")
    parser.add_argument(
        "--change-type",
        default="workflow_change",
        choices=["content_tweak", "workflow_change", "policy_change", "emergency_patch"],
    )
    parser.add_argument("--environment", default="staging", choices=["staging", "canary", "production"])
    parser.add_argument("--live-tests", action="store_true", help="Run live model tests instead of dry run.")
    parser.add_argument("--rollback-to", help="If provided, write a rollback artifact instead of deploying.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pipeline = MarketplacePromptPipeline(Path(__file__).resolve().parent)

    if args.rollback_to:
        record = pipeline.rollback(args.environment, args.rollback_to)
        print(json.dumps({"rollback_record": str(record)}, indent=2))
        return

    result = pipeline.run_release(
        change_type=args.change_type,
        environment=args.environment,
        dry_run=not args.live_tests,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
