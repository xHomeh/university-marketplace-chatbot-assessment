# University Marketplace Chatbot Assessment

## Overview

This repository contains a prompt-first design for a university marketplace support chatbot. The submission focuses on four practical concerns: giving users clear marketplace help, handling trust-and-safety issues correctly, validating prompt behaviour with golden tests, and making prompt updates safe to ship as marketplace rules evolve.

The prompt design assumes a campus-only marketplace used by students, staff, and other verified university members. That context changes the support problem in important ways: transactions are often in person, dorm and residence hall policies matter, academic calendar timing affects demand, and escalation sometimes needs to involve moderators, residence staff, student affairs, or campus security.

## How To Review This Submission

Start with the prompt and then move outward to the testing and operations artifacts.

- `prompt.md`: Main system prompt for the support chatbot.
- `prompt-analysis.md`: Rationale for the prompt structure, safety model, and output contract.
- `test-cases.json`: Golden test suite with 35 structured cases across the required categories.
- `testing-framework.md`: How the golden tests are organized, scored, and used in release gates.
- `testing-result.md`: Pre-deployment test artifact summarizing static validation and manual prompt-fit review.
- `update-process.md`: Workflow for prompt changes, approvals, testing, deployment, and rollback.
- `automation-concept.py`: Python concept for automating prompt packaging, testing, approval checks, deployment, and rollback.
- `marketplace-insights.md`: Domain analysis of university marketplace behavior, safety, and seasonal patterns.
- `Sample-Chatbot-info.md`: Prototype recommendation, implementation rationale, and prototype limitations.
- `PROCESS_LOG.md`: Sanitized work log describing the design process and decision sequence.
- `streamlit_app.py`: Streamlit chatbot prototype for local demo or Streamlit Community Cloud deployment.
- `resources/chatbot_knowledge/`: Lightweight knowledge files used by the prototype for policy and example grounding.

## Approach Summary

The submission uses a prompt-first support design with explicit risk tiers and structured response modes. Routine navigation questions are answered directly. Medium-risk issues such as disputes and suspicious behavior are handled with concrete steps plus reporting guidance. High-risk issues such as threats, harassment, theft indicators, or prohibited items trigger a safety-first or refusal flow.

The testing strategy mirrors that structure. Instead of checking only whether answers sound helpful, the golden tests also check for policy alignment, escalation correctness, and response-format compliance. That matters because marketplace failures are often not "wrong facts" but unsafe omissions: missing a scam signal, forgetting to preserve evidence, or helping with a prohibited listing.

## Assumptions About The University Marketplace

- Access is limited to verified university community members, typically via university email or SSO.
- The marketplace supports listing creation, in-app messaging, user reporting, and moderator review.
- Payments are mostly peer-to-peer and the platform is not the merchant of record.
- Moderators can review disputes, fraud reports, harassment reports, and account issues during staffed hours.
- Urgent physical safety issues should be escalated outside the chatbot to campus security or emergency services.
- Residence hall and dorm policies vary, so the chatbot should give general guidance and avoid claiming building-specific rules unless the platform has that data.
- Seasonal demand spikes happen around semester start, move-in, move-out, and graduation.

## Time Breakdown

Time breakdown of effort allocation:

- Prompt design and refinement: 40 minutes
- Golden test design and scoring framework: 60 minutes
- Update process and automation concept: 25 minutes
- Marketplace domain analysis: 15 minutes
- Prototype selection and documentation: 25 minutes
- README, process log, and QA pass: 20 minutes

## Next Steps For A Real Project

- Validate marketplace policy language with operations, legal, and student affairs stakeholders.
- Connect the prompt to real product surfaces such as listing creation, report submission, and case status lookup.
- Run red-team testing focused on fraud, stalking, extortion, and prohibited-item evasion.
- Add telemetry for escalation rate, unresolved intent rate, repeat-contact rate, and moderator overturn rate.
- Launch in staged environments with canary traffic before full rollout.
- Replace assumption-based rules with live policy/config data from the university marketplace backend.

## Reflection On The Most Challenging Component

The most challenging part was deciding where the chatbot’s helpfulness should stop. In a university marketplace, the assistant should solve routine problems directly, but it also needs to avoid overreaching in disputes, policy interpretation, fraud cases, and personal safety situations. Designing those escalation boundaries clearly — without making the bot either too passive or too confident — was the hardest part.

## Alternative Approaches Considered And Rejected

1. A single large plain-language prompt without explicit structure.
   Rejected because it would be harder to keep response behavior stable across low-risk support, refusals, and high-risk safety incidents.

2. A test suite focused only on happy-path navigation questions.
   Rejected because it would miss the most expensive failures: unsafe advice, weak refusals, and missed escalation triggers.

3. Fully automatic prompt deployment after test pass.
   Rejected because policy and trust-and-safety changes need human approval even when automated checks are green.

## Buyer/Seller Perspective

From the buyer side, the biggest needs are trust and speed. Students often want inexpensive items quickly, but they also need confidence that the seller is real, the item condition is accurate, and the meetup will be safe. A shared campus identity lowers some friction, but it does not remove scam risk, no-shows, or misrepresentation.

From the seller side, the main frustrations are repetitive questions, last-minute cancellations, unclear pricing, and pickup logistics around dorm rules or class schedules. Sellers benefit from guidance on how to write clear listings, set expectations, and avoid unsafe handoffs. Those realities shaped the prompt's emphasis on concise actions, evidence preservation, and escalation pathways.
