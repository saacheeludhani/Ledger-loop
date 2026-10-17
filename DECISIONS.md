# Decisions and the brief problems they answer (Case 2: LedgerLoop)

| # | Brief problem | Decision | Why it is defensible |
|---|---|---|---|
| 1 | Absent or afterthought in AI answers | Answer-first hero and a facts list (`dl`) stating what LedgerLoop is, who it is for, features, plans, location | AI assistants quote short, self-contained statements; the first screen carries the whole entity description |
| 2 | Weaker rival recommended first | “When LedgerLoop fits / when it doesn’t” section with honest limits | Gives assistants a recommendation rule based on real features, without attacking named competitors or inventing claims |
| 3 | Wrong pricing | “Exactly three plans” statement, review date, and `Offer` JSON-LD (₹0, ₹399, ₹899 per month) | Explicitly marks any other price as out of date; structured data repeats the same numbers |
| 4 | Wrong features | Explicit yes/no on UPI links, multi-currency, payroll in body, FAQ and `FAQPage` JSON-LD | Directly corrects both errors in the brief (false multi-currency, false “no UPI”) |
| 5 | Wrong instructions | Five step-by-step how-to guides with review dates and a “follow this page” note | Gives assistants current steps to draw on instead of guessing |
| 6 | No reliable measure | First-touch source capture (AI referrer domains, UTM, search, referral, direct), tied to the verified account; optional self-report asked only after verification | Measured behaviour replaces an untrusted optional question |
| 7 | Sign-in friction, throwaway accounts | MiniMoth phone OTP replaces email + password; one free account per verified number via `identity_id` | Removes the password step and reset tickets; a real phone number is harder to fake than an email |
| — | Rules | Visible competition-demo notice (top banner and footer); key kept server-side via `server.py` | Required by the brief; avoids exposing credentials |

## Honest limits
- Per-plan feature limits are not in the brief, so the page does not state any.
- How-to steps are generic because the brief gives no UI details.
- One page with anchored sections; separate URLs per guide would be a further improvement.
- AI citation results vary by model and time; nothing here guarantees inclusion.
- The demo account store is browser-local, for demonstration only.
