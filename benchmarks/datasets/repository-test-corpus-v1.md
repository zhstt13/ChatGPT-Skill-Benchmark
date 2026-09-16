# Repository Test Corpus v1

هدف این Dataset ساخت کیس‌های کنترل‌شده برای ارزیابی Skillهای مهندسی Repository است.

## Case Types

### Case 01 — Legacy Monolith

هدف:
بررسی توانایی Skill در تشخیص مرزهای نامشخص و وابستگی‌های زیاد.

Expected analysis:
- Repository map
- Boundary detection
- Refactor risks
- Migration suggestions

---

### Case 02 — AI Agent Project

هدف:
بررسی معماری پروژه‌های مبتنی بر Agent.

Expected analysis:
- Skill ownership
- Context flow
- Tool boundaries
- Instruction hierarchy

---

### Case 03 — Growing Frontend Repository

هدف:
بررسی کنترل رشد پروژه.

Expected analysis:
- Component structure
- State ownership
- Documentation gaps
- Maintainability risks

---

## Evaluation Rule

هر Skill باید:

1. Facts را از Assumptions جدا کند.
2. قبل از پیشنهاد تغییر، وضعیت فعلی را توضیح دهد.
3. Impact تغییرات را مشخص کند.
4. از پیچیده‌سازی بدون نیاز جلوگیری کند.
