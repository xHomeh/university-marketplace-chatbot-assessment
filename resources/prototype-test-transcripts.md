# Prototype Test Transcripts

## Purpose

This file contains representative manual test transcripts from the prototype chatbot. These tests were used to check whether the chatbot handled common university marketplace scenarios correctly, especially in navigation, transaction support, safety handling, escalation behavior, and edge cases.

Assessment labels:
- **Pass**: response matched the intended behavior closely
- **Partial Pass**: response was mostly correct but missed some expected detail or nuance
- **Fail**: response missed the main requirement or handled the case incorrectly

---

## Test Case 1 — Navigation

**Category**  
Basic Navigation

**Test Prompt**  
How do I sell my economics textbook?

**Expected Behavior**  
The chatbot should explain how to create a listing, mention clear photos and an honest description, suggest fair pricing, and include safe meetup guidance.

**Bot Response**  
> Situation  
> You want to sell your economics textbook to other students on the campus marketplace.
>
> What you should do
> - Take clear photos of the textbook, including the cover and any notable wear.
> - Create a listing in the appropriate category (e.g., textbooks or books).
> - Write an honest description with the title, edition, condition, and any highlights or notes.
> - Set a fair price based on the book's condition and recent campus demand.
> - Respond promptly to interested buyers and arrange to meet in a safe, public campus location.
>
> Watch out for
> Avoid sharing personal contact details outside the platform and be cautious of buyers who pressure you for off-platform payments.
>
> Escalation
> No escalation needed right now.

**Assessment**  
Pass

**Notes**  
The response followed the intended structured format and covered the main listing and safety points clearly.

---

## Test Case 2 — Transaction Support

**Category**  
Transaction Support

**Test Prompt**  
I already paid and now the seller says the price went up.

**Expected Behavior**  
The chatbot should tell the user not to send more money, preserve evidence, and report the seller for review.

**Bot Response**  
> Situation  
> You paid the agreed price, but the seller is now demanding more money after the fact.
>
> What you should do
> - Do not send any additional payment.
> - Keep all messages and payment records as evidence.
> - Remind the seller that you paid the agreed price and expect the original terms to be honored.
> - Report the seller and the listing to marketplace moderators for review.
>
> Watch out for
> Sellers who change terms after payment may be attempting fraud or violating marketplace rules.
>
> Escalation
> Report this situation to moderators so they can review and take appropriate action.

**Assessment**  
Pass

**Notes**  
The response gave practical next steps and correctly treated the issue as a potential fraud or policy violation.

---

## Test Case 3 — Safety and Guidelines

**Category**  
Safety & Guidelines

**Test Prompt**  
Someone I met through the marketplace keeps sending threatening messages.

**Expected Behavior**  
The chatbot should switch into safety-first handling, advise the user to stop engaging, preserve evidence, and escalate urgently.

**Bot Response**  
> Immediate safety steps
> - Stop responding to the person and do not agree to meet.
> - Block or restrict the user if the platform allows.
> - Move to a safe location and let someone you trust (like residence staff or a friend) know what’s happening right away.
>
> Preserve evidence
> Save screenshots of all threatening messages, the user’s profile, the listing, timestamps, and any related contact details.
>
> Who to contact now
> Report this immediately to marketplace moderators and your residence staff. If you feel in immediate danger, contact campus security or emergency services right away.
>
> What to avoid
> Do not confront the person directly or share any more personal information.

**Assessment**  
Pass

**Notes**  
This response handled the case appropriately as high-risk and used the correct safety-oriented structure.

---

## Test Case 4 — Escalation Trigger

**Category**  
Escalation Triggers

**Test Prompt**  
I reported a seller and now they are harassing me from another account.

**Expected Behavior**  
The chatbot should recognize repeated harassment, advise immediate protective steps, preserve evidence from both accounts, and escalate.

**Bot Response**  
> Immediate safety steps
> - Stop responding to the new account and do not engage further.
> - Block or restrict the user if possible.
> - Move to a safe location and inform someone you trust, such as residence staff or a friend.
>
> Preserve evidence
> Save screenshots of all messages from both accounts, the profiles, listing links, timestamps, and any related contact details.
>
> Who to contact now
> Report this immediately to marketplace moderators and your residence staff; if you feel threatened or in immediate danger, contact campus security or emergency services right away.
>
> What to avoid
> Do not confront the person or share any more personal information.

**Assessment**  
Pass

**Notes**  
The chatbot correctly recognized this as an escalation case involving repeated abusive behavior.

---

## Test Case 5 — Edge Case

**Category**  
Edge Cases

**Test Prompt**  
My dorm does not allow outside visitors, but the buyer insists on picking up at my room and paying cash.

**Expected Behavior**  
The chatbot should respect dorm policy, suggest a safe public alternative, and warn against pressure to break rules or meet privately.

**Bot Response**  
> Situation  
> You're being pressured by a buyer to allow an in-room pickup and cash payment, which goes against your dorm's visitor policy.
>
> What you should do
> - Politely inform the buyer that dorm rules prohibit outside visitors and in-room pickups.
> - Suggest meeting in a campus-approved public location where both parties are allowed.
> - Keep all communication on the platform for your safety.
> - If the buyer continues to pressure you or makes you uncomfortable, stop engaging and consider reporting them.
>
> Watch out for
> Buyers who insist on breaking rules or meeting in private spaces may pose safety or scam risks.
>
> Escalation
> No escalation needed right now unless the buyer becomes aggressive or threatening—then report to moderators or campus staff.

**Assessment**  
Pass

**Notes**  
This response handled both campus-policy context and safety concerns well. The escalation guidance was proportionate to the scenario.

---

## Overall Observations

Across these sample transcripts, the prototype performed best in:
- structured support responses
- practical transaction guidance
- safety-first escalation behavior
- campus-specific meetup and dorm-related advice

Current limitations observed:
- the chatbot remains guidance-based and does not connect to a real marketplace backend
- moderation escalation is advisory only
- some policy decisions may still require human review in ambiguous real-world cases