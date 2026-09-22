# M01 — Computer and Cybersecurity Foundations

Navigation: [Course map](../README.md) · [Learning guide](../H-SETS-Student-Learning-Guide.md) · [Module start](README.md) · [Next module](../Module-02/README.md)

**Read in this order: L01 → L07.** Lesson IDs are permanent references, not reading-order numbers. Use the links in the module route.

## Practical route — no virtual machine required

Use a normal text editor or paper and the synthetic material below. First complete the file-handling practice in the L01 notes. Then work through the business-risk case and L07 message/access workshop. Do not install a hypervisor, alter host networking or execute links from a message. All controls in these workshops are proposals, not implemented changes.

**Pause after L01:** locate your saved evidence note and explain one risk using asset, weakness, event and impact.

**Pause after L07:** explain one allowed and one denied access decision and an independent verification route for the message.

<a id="practice-l01"></a>
## Lab 1A — Explain the business risk before choosing a control

### Purpose and setup

Use the fictional case in the workbook. Work locally in your own notes; do not sign in to or investigate any real organisation. Allow about 50 guided minutes, with completion in independent study if needed.

Create a folder on your **computer** called `HSETS-Portfolio`, with a `Module-01` subfolder. Use a location you control, such as Documents. The instructor may give you a designated class directory. No virtual machine is needed. Keep this folder for later evidence.

Inside `Module-01`, create `evidence` and `private-evidence` folders. Save a README, scope, risk table, test record, and change log using the workbook headings. Do not store passwords in any of them.

### Procedure

1. Read the Cedarbridge case once for business context and once for evidence. Underline only facts actually supplied.
2. List at least five assets. Give each an owner, purpose, and dependency. If an owner is unknown, label it unknown and state who you would ask.
3. Choose three different security concerns from the case. For each, identify the asset, plausible threat event, weakness, business consequence, and affected CIA property or properties.
4. Write a complete risk statement for each concern. Use conditional language for harm that has not been observed.
5. Rate each Low/Medium/High for classroom prioritisation and give a reason. Record assumptions instead of turning them into facts.
6. Propose complementary controls. Across the three concerns, include prevention, detection, and correction/recovery.
7. For each control, state how someone would test it. Include at least one permitted action and one action that should be denied.
8. Identify the business owner who should approve the response and the technical person who could implement it.
9. Explain one residual risk after your proposed response.
10. Give a two-minute handover: the most important concern, the evidence, the recommendation, and the decision needed.

### Expected result and success criteria

The output is a reasoned risk/control assessment, not a tool report. It should contain five assets, three complete risk statements, proposed owners, evidence limitations, and realistic verification. It must not accuse a named person of misuse when the case provides no supporting activity evidence.

### Independent variation

The instructor releases this new fact after you finish the first draft: 'The backup file exists, but nobody has tested restoration, and the only stored copy is on the same device as the working file.' Reconsider the relevant risk and explain what would need to be tested. Keep both revisions and explain the change.

### Common errors

| Error | Better approach |
|---|---|
| 'The risk is a hacker' | Name the weakness, possible event, affected asset, and consequence |
| Every risk receives High | Explain likelihood/impact and distinguish urgency |
| 'Install antivirus' for every issue | Choose a control that addresses the actual path to harm |
| A written policy is treated as enforcement | Identify the process/technical actions and test them |
| Proposed controls are marked working | Record them as proposals until executed and verified |


<a id="practice-l07"></a>
## L07 — Message and access workshop

Read this invented message as plain text; do not browse its domain:

```text
Display name: Cedarbridge Supplier Accounts
From: accounts@cedarbridge-supplier.example
Reply-To: urgent-payments@accounts-review.example
Subject: URGENT: change our settlement account today
We need you to replace the bank details before the afternoon payment.
Do not call the usual contact because they are unavailable.
Reply here with the payment spreadsheet and your approval code.
```

Create a table with observation, possible significance, alternative explanation, and next check. The address mismatch and request to bypass known contact are observations; “a specific criminal sent it” is unsupported. Draft a verification route through the fictional supplier contact already held in approved records. Draft an escalation note without repeating financial data or requesting secrets. Do not send it.

Create the following access matrix from business requirements: Alice/Finance edits invoice drafts; Cara/Audit reads final reports; Ben/Operations has neither permission; Dana/contractor reads one approved draft until a stated end date. Include resource, action, owner approval, expiry, allowed test, and denied test. Explain what must change when Dana leaves and Alice moves to Operations. No accounts are changed in this paper exercise; later modules implement the pattern.

Independent variation: the instructor supplies a message that uses a legitimate-looking address but asks for an unusual file transfer. Evaluate the action and workflow rather than deciding solely from spelling or domain appearance.


Finish both assignments in the [workbook](03-Student-Workbook.md), then continue to [M02](../Module-02/README.md). Keep the risk record for P01.
