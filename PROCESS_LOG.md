# PROCESS_LOG.md

## Purpose

This file records how I approached the University Marketplace Chatbot take-home assessment, including the main design decisions, trade-offs, and sequencing of work across the prompt, test suite, update workflow, marketplace analysis, and prototype.

I treated this assessment as a prompt-first systems design exercise rather than a full product build. My goal was to produce something that felt realistic for a campus marketplace setting, was easy for reviewers to evaluate, and stayed proportionate to the time and scope of an internship take-home.

---

## 1. Initial Framing

My first step was to identify what the assessment was really testing. Although it included a prototype component, the deliverables suggested that the main evaluation areas were:

- prompt quality and structure
- testing discipline
- safety and escalation thinking
- update and release design
- understanding of the university marketplace domain

Because of that, I decided early on that the submission should be centered on a **prompt-first support design** rather than a feature-heavy prototype. I wanted the repository to show that I could think about the chatbot as an operational system, not just as a one-off prompt.

---

## 2. Overall Working Strategy

I approached the work in the same order as the deliverables:

1. define the chatbot’s role and response behavior in `prompt.md`
2. design the golden test suite in `test-cases.json`
3. document how those tests would be used in `testing-framework.md`
4. design update, approval, deployment, and rollback logic in `update-process.md`
5. create a lightweight automation concept in `automation-concept.py`
6. write marketplace-specific domain observations in `marketplace-insights.md`
7. build and document a prototype
8. finish with the README and process log so the repository reads coherently

This order helped because each deliverable informed the next. The prompt defined the intended behavior, the tests defined what counted as success or failure, and the update workflow defined how that behavior could change safely over time.

---

## 3. Prompt Design Process

### Core idea

I framed the chatbot as a **university marketplace support assistant** rather than a generic FAQ bot. That meant it needed to do more than answer listing questions. It also needed to handle:

- disputes
- suspicious behavior
- prohibited item requests
- harassment and threat cases
- reporting and escalation
- new user guidance

### Prompt structure

I chose a strongly structured prompt because I wanted the system behavior to be inspectable and maintainable. I broke the prompt into sections such as:

- role and mission
- supported user types
- university context
- policy rules
- risk tiers
- scenario logic
- escalation rules
- output format requirements
- examples

The reason for doing this was simple: for a safety-sensitive support bot, a loose plain-language prompt felt harder to reason about and harder to test. A structured prompt also made it easier to keep low-risk support behavior separate from refusal behavior and high-risk safety behavior.

### Main design priorities

The prompt was built around four main priorities:

#### a. Clear marketplace help
The bot should be able to answer common support questions directly without forcing the user through unnecessary clarification.

#### b. Trust-and-safety awareness
The bot should be able to spot scam indicators, coercive behavior, prohibited item requests, and unsafe meetup situations.

#### c. Escalation discipline
The bot should help directly when appropriate, but should not overreach in cases involving threats, fraud, policy ambiguity, evidence review, or possible account actions.

#### d. Structured outputs
I wanted responses to follow predictable formats so that they would be easier to evaluate and more usable in a support setting.

### University-specific tailoring

I made a deliberate effort to avoid writing a generic resale-marketplace prompt. I included university-specific concerns such as:

- dorm and residence hall restrictions
- semester start and move-out demand spikes
- campus meetup norms
- student budget sensitivity
- moderators, residence staff, student affairs, and campus security as possible escalation points

This was important because the assignment specifically framed the chatbot as part of a university marketplace rather than a general commerce platform.

---

## 4. The Hardest Design Problem

The hardest part of the assessment was deciding where the chatbot’s helpfulness should stop.

Routine marketplace questions are easy to answer directly. The difficulty comes from cases that look like normal support questions at first, but are actually trust-and-safety-sensitive, evidence-sensitive, or policy-sensitive. Examples include:

- disputes where one party has already paid
- users asking about suspicious payment pressure
- ongoing harassment from another account
- prohibited item requests framed casually
- dorm or campus policy conflicts that could affect user safety

I found that the key design challenge was defining escalation boundaries clearly enough that the bot would not become either:

- **too passive**, where it avoids being helpful in normal situations, or
- **too confident**, where it gives definitive guidance in cases that should be reviewed by humans

That design boundary influenced almost every other part of the submission: the risk tiers, the test cases, the update approval logic, and the prototype evaluation.

---

## 5. Golden Test Suite Design

### What I wanted the tests to do

I wanted the golden tests to measure more than surface-level helpfulness. A marketplace support chatbot can sound useful while still failing in important ways, especially if it:

- misses a scam signal
- forgets to preserve evidence
- fails to escalate a harassment case
- helps with a prohibited listing
- breaks the required response structure

Because of that, the golden test suite was designed to check both task support and behavioral correctness.

### Category coverage

I organized the test cases around the required categories:

- basic navigation
- transaction support
- safety and guidelines
- escalation triggers
- edge cases

I used 35 cases total to meet the required range while still giving each category meaningful coverage.

### Test case structure

Each test case includes:

- an ID
- category
- input
- expected elements
- success criteria
- edge-case metadata where relevant

I chose this format because it is simple, readable, and compatible with later automation. It also makes it easier to discuss the suite as a reusable release gate rather than just a list of sample prompts.

---

## 6. Testing Framework Design

The testing framework was designed to explain how the golden tests would actually be used.

I focused on four ideas:

### a. coverage
The suite should cover both normal support flows and sensitive trust-and-safety flows.

### b. release gating
Prompt changes should not be released if they break important safety, refusal, or escalation behavior.

### c. blocker failures
Some failures matter more than others. A missed safety escalation or prohibited-item compliance issue should stop release even if the overall pass rate is high.

### d. regression thinking
The point of golden tests is not only to validate the current prompt, but also to catch degradation after future changes.

This framework was intentionally more operational than academic. I wanted it to read like something that could plausibly be used by a small product or trust-and-safety team.

---

## 7. Update Process Design

### Goal

The update process was designed to make prompt changes fast enough for marketplace operations, while still protecting users from unsafe or unreviewed policy changes.

### Main decisions

I treated prompt changes as versioned releases rather than ad hoc edits. That led to a workflow with:

- change request
- prompt update
- pull request
- automated checks
- approval
- staging validation
- limited rollout
- production release
- rollback path

I also added a simple change classification system:

- content tweak
- workflow change
- policy change
- emergency patch

This made the approval path easier to explain and tied review depth to update risk.

### Why human review mattered

One of the clearest conclusions from the exercise was that policy-impacting changes should not auto-deploy just because tests pass. For a marketplace support bot, there is too much risk in letting safety or policy behavior change without human review.

That principle drove both the written workflow and the automation concept.

---

## 8. Automation Concept

The `automation-concept.py` file was written as a lightweight PromptOps concept, not as a production-ready system.

Its purpose was to demonstrate that I understood how a prompt release pipeline could include:

- prompt bundle versioning
- test suite validation
- approval routing by change type
- deployment artifacts
- rollback artifacts

I kept it intentionally simple and readable. For this assessment, I thought it was more useful to show the logic of the release process clearly than to over-engineer an incomplete tool.

---

## 9. Marketplace Domain Analysis

This part of the work focused on what makes a university marketplace distinct.

### Main observations

#### a. students often need practical, fast support
Many likely questions are simple but urgent: how to list an item, how to price a textbook, what to do about a no-show, or how to meet safely.

#### b. shared campus identity does not eliminate risk
Even in a campus-only platform, users can still face scams, impersonation, coercion, harassment, and risky in-person situations.

#### c. timing matters
Marketplace activity likely changes around semester start, move-in, move-out, graduation, and exchange periods. That affects both the kinds of items listed and the kinds of support questions users ask.

#### d. institutional context matters
A real university marketplace may need to connect with:

- email or SSO verification
- moderation systems
- residence hall rules
- student affairs
- campus security

These observations shaped both the prompt content and the assumptions stated in the README.

---

## 10. Prototype Decisions

### Options considered

I considered several prototype approaches, including:

- Custom GPT
- Botpress
- Streamlit
- other lightweight chatbot builders

### Trade-offs

#### Custom GPT
This was attractive because it was closest to the one-prompt setup I originally wanted. However, instruction-length limits made it less convenient, and I was less confident that it would feel like a standalone prototype for reviewers.

#### Streamlit
This would have given more direct control over the prompt and interaction flow, but it introduced more setup friction and potential API cost concerns than I wanted for a take-home submission.

#### Botpress
Botpress was less natural for a single-prompt design, but it provided the fastest path to a shareable, hosted prototype that reviewers could open directly.

### Final choice

I chose Botpress because it was the best practical trade-off between:

- speed of setup
- shareability
- low engineering overhead
- ability to demonstrate support and escalation behavior

The prototype was intentionally lightweight. I treated it as a proof of concept for conversation behavior, not as a full marketplace implementation.

---

## 11. Manual Prototype Review

After building the prototype, I manually tested a representative sample of scenarios drawn from the golden test categories, including:

- listing a textbook
- post-payment price change
- threatening messages
- repeated harassment from another account
- dorm-policy-related pickup pressure

The main things I checked were:

- whether the bot followed the expected support structure
- whether it gave concrete next steps
- whether it escalated correctly
- whether it avoided unsafe advice
- whether it felt aligned with the intended marketplace role

Overall, the prototype performed best on structured support and clear safety-escalation cases. The main limitations were cases that would require:

- real platform integrations
- real account and listing data
- exact policy configuration
- real moderator workflows

I considered that acceptable for a prototype whose purpose was to demonstrate prompt-guided behavior rather than complete product integration.

---

## 12. Main Trade-Offs Across The Submission

Several trade-offs were made deliberately:

### completeness over overbuilding
I wanted every required deliverable to be present and coherent rather than spending too much time polishing only one component.

### realism over unnecessary complexity
I tried to make the design realistic enough to reflect actual marketplace risk, without pretending to build a full production system.

### structure over looseness
I preferred a more explicit and reviewable design for the prompt, tests, and update process because that made the repository easier to assess.

### practical prototype over ideal tooling
Botpress was not my ideal prompt-native tool, but it was the best fit once I balanced time, simplicity, and shareability.

---

## 13. What I Would Improve With More Time

If this were extended beyond take-home scope, the next improvements I would make are:

- run live golden tests against a real staging model endpoint
- expand adversarial testing around fraud, harassment, and prohibited-item evasion
- create a more explicit prohibited-item taxonomy
- add telemetry for escalation correctness and unresolved cases
- connect the prototype to a mock reporting or moderation workflow
- compare multiple prompt variants against the same golden suite

I would also spend more time tightening the connection between the written prompt design and the prototype implementation so that the live demo matched the intended response behavior even more closely.

---

## 14. Final Reflection

The part of this assessment I found most valuable was that it pushed me to think about the chatbot as a bounded support system rather than just a helpful model.

A university marketplace assistant should absolutely reduce friction for normal users. But it also has to know when to stop, when to warn, when to refuse, and when to escalate. That boundary-setting turned out to be more important than any single wording choice in the prompt.

Overall, I tried to make the submission feel realistic, reviewable, and grounded in how a campus marketplace would actually work, while keeping the implementation effort proportionate to the scope of an internship take-home.