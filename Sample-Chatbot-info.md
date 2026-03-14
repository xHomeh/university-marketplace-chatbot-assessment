# Sample Chatbot Info

## Prototype URL

Botpress prototype chatbot:  
https://cdn.botpress.cloud/webchat/v3.6/shareable.html?configUrl=https://files.bpcontent.cloud/2026/03/14/08/20260314082009-A5W6WL1E.json

## Platform Selected

Botpress

## Why This Platform Was Selected

I selected Botpress because it provided a fast way to build and share a working chatbot prototype without needing to build a full backend or frontend from scratch. For this take-home assessment, the goal was to demonstrate how the marketplace support chatbot would behave in practice, especially for user guidance, safety handling, policy enforcement, and escalation scenarios.

Botpress was a suitable choice because it:
- provides a hosted chat interface that is easy to share with reviewers
- supports AI-based response behavior for support-style workflows
- allows rapid prototyping with the chatbot emulator
- reduces setup overhead compared to building a full web application

This made it possible to focus on the chatbot’s behavior and support logic rather than deployment engineering.

## Prototype Scope

The prototype is designed to simulate a university marketplace support chatbot for a campus-only buying, selling, and trading platform.

It is intended to demonstrate support for:
- buyer questions
- seller questions
- new user onboarding
- scam and safety concerns
- prohibited-item handling
- escalation guidance for risky or policy-sensitive cases

The prototype focuses on conversational support behavior rather than full platform integration.

## What the Prototype Demonstrates

The chatbot is designed to:
- explain how users can buy or sell items on the platform
- provide general safety guidance for meetups and payments
- identify suspicious behavior and scam indicators
- refuse assistance for prohibited or policy-violating requests
- recommend escalation to moderators or campus support channels when needed

## Assumptions

The prototype was built with the following assumptions:
- the marketplace is limited to verified university community members
- moderators exist and can review reports, disputes, and safety incidents
- campus-specific considerations such as dorm pickups, semester cycles, and residence rules may affect transactions
- the chatbot mainly handles first-line support and does not make final enforcement decisions
- the chatbot provides guidance only and does not directly process refunds, bans, or moderator actions

## Limitations

This prototype has several important limitations:
- it is not connected to a live marketplace backend
- it cannot access real user accounts, listings, payment records, or moderation tools
- escalation is advisory only; it does not create real moderator tickets
- policy handling is based on the designed prompt logic rather than a live policy engine
- the prototype is meant for demonstration and testing, not production deployment

## Testing Performed

The prototype was manually tested using representative scenarios from the golden test set categories.

### Example scenario coverage
- basic navigation:
  - how to list a textbook
  - how to message a seller
  - how to buy safely as a new user

- transaction support:
  - seller asking for a deposit before meetup
  - item not matching the listing
  - buyer or seller no-show situations

- safety and guidelines:
  - reporting suspicious listings
  - prohibited-item sale attempts
  - scam warning signs
  - harassment or threatening messages

- escalation triggers:
  - fraud-related disputes
  - safety threats
  - policy-ambiguous or moderator-review cases

- edge cases:
  - multi-topic questions
  - unclear intent
  - requests mixing normal support with policy-sensitive behavior

## Sample Test Results

A small set of representative manual tests was run against the prototype to verify navigation support, transaction handling, safety escalation, and edge-case behavior.

| Category | Sample Prompt | Observed Result | Outcome |
|---|---|---|---|
| Navigation | How do I sell my economics textbook? | Provided clear listing steps, pricing guidance, and safe meetup advice | Pass |
| Transaction Support | I already paid and now the seller says the price went up. | Advised against further payment, told user to preserve evidence, and recommended moderator reporting | Pass |
| Safety & Guidelines | Someone I met through the marketplace keeps sending threatening messages. | Switched to safety-first guidance, evidence preservation, and urgent escalation | Pass |
| Escalation Triggers | I reported a seller and now they are harassing me from another account. | Correctly treated as a high-risk escalation case with protective next steps | Pass |
| Edge Cases | My dorm does not allow outside visitors, but the buyer insists on picking up at my room and paying cash. | Gave policy-compliant alternatives and highlighted safety concerns | Pass |

Detailed manual test transcripts and prototype response samples are included in `prototype-test-transcripts.md` located in the resources directory.

## Observed Prototype Behavior

In manual testing, the chatbot was generally able to:
- provide relevant first-line guidance for common marketplace questions
- give practical safety advice for suspicious transactions
- refuse clearly non-compliant requests
- recommend escalation for serious harassment, scam, or safety-related situations

The strongest behavior was in common support and safety guidance scenarios. The weakest areas were cases that would normally depend on live platform data, moderator tools, or highly specific marketplace policy details.

## Conclusion

This prototype serves as a functional proof of concept for the university marketplace support chatbot. It demonstrates how the designed prompt and policy logic can be applied in a live conversational interface, while keeping implementation effort proportionate to the scope of an internship take-home assessment.