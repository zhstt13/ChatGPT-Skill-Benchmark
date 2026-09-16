# ChatGPT Skill Benchmark

یک بنچمارک نسخه‌دار و evidence-grounded برای مقایسه‌ی Skillهای Agent روی مسئله‌های یکسانِ مهندسی Repository.

## وضعیت Canonical

هسته‌ی **Canonical v1** آماده است: سه Case دارای fixture واقعی، ground truth قابل‌ردیابی، قرارداد یکتای Run و Score، validator محلی و CI دارد.

هنوز **هیچ نتیجه‌ی امتیازدهی‌شده‌ی Canonical** منتشر نشده است؛ زیرا اجرای واقعی هر Candidate باید با مدل، ابزارها، ورژن Skill و خروجی خامِ ثبت‌شده همراه باشد. فایل‌های قدیمی زیر `evaluation/` تاریخچه‌ی prototype هستند و نباید به‌عنوان نتایج معتبر v1 خوانده شوند.

## اصل پروژه

هدف، پیدا کردن «پیچیده‌ترین Skill» نیست؛ هدف، پیدا کردن کوچک‌ترین معماری‌ای است که یک Task را با شواهد کافی، ایمنی تغییر و قابلیت نگهداری حل کند.

هر مقایسه باید شرایط یکسان داشته باشد:

1. یک fixture و task یکسان برای همه‌ی Candidateها؛
2. ثبت دقیق مدل، ابزارها، دسترسی نوشتن و revision خود Skill؛
3. نگهداری خروجی خام؛
4. ارتباط هر Finding با مسیر و anchor واقعی در fixture؛
5. امتیازدهی فقط با مدل ۱۰۰امتیازی canonical؛
6. تفکیک صریحِ چیزهای اجراشده از چیزهای اجرا‌نشده.

## اجرای کنترل‌های محلی

```bash
python tools/validate_benchmark.py
python -m unittest discover -s tests -v
```

کنترل اول manifest، candidate registry، fixtureها، ground truthها و run recordهای ثبت‌شده را بررسی می‌کند. کنترل دوم خود validator و محاسبه‌ی score را تست می‌کند. هیچ‌کدام ادعای اجرای مدل یا runtime یک Skill را نمی‌سازند.

## ثبت یک اجرای واقعی

1. Candidate و revision آن را از `benchmark/candidates.json` قفل کنید.
2. همان `case.json` و همان پوشه‌ی `fixture/` را به همه‌ی Candidateها بدهید.
3. خروجی دست‌نخورده را در `benchmark/runs/<run-id>.md` ذخیره کنید.
4. یک Run Record مطابق `benchmark/run.schema.json` بسازید؛ از `benchmark/RUN_TEMPLATE.json` شروع کنید.
5. شواهد مسیر/anchor، validationهای واقعاً اجراشده و scoreها را ثبت کنید.
6. `python tools/validate_benchmark.py` و سپس `python tools/score_run.py <run-record.json>` را اجرا کنید.

## ساختار

```text
benchmark/
├── manifest.json             # entry point canonical
├── scoring.json              # تنها مدل امتیازدهی
├── candidates.json           # Candidateها و blobهای قفل‌شده
├── run.schema.json           # قرارداد یک Run واقعی
├── cases/                    # task + fixture + ground truth
├── runs/                     # خروجی‌های واقعی و recordهای اعتبارسنجی‌شده
└── results/                  # summaryهای مشتق‌شده، نه template

reference-skills/             # Candidateهای تحت آزمایش
research/SOURCE_LOCK.json     # pinهای قابل‌تکرارِ منابع خارجی
tools/                        # validator و score renderer
tests/                        # آزمون‌های خود framework
```

جزئیات طراحی و قراردادها در [BENCHMARK_SPEC.md](BENCHMARK_SPEC.md) آمده است.

## Candidateهای فعلی

- `baseline-repository-skill` — baseline عمداً کوچک برای مقایسه.
- `ai-repository-engineer` — Candidate ترکیبی با modeهای Create / Analyze / Evolve.

وجود یک Candidate در ریپو به‌معنای برنده‌بودنش نیست؛ فقط یعنی آماده‌ی اجرای منصفانه است.

## تاریخچه‌ی Prototype

ساختارهای قدیمی در `evaluation/` و `benchmarks/` حفظ شده‌اند تا تاریخچه از بین نرود. Canonical v1 فقط از `benchmark/manifest.json` شروع می‌شود. نتایج یا scorecardهایی که Run Record معتبر ندارند، در گزارش رسمی لحاظ نمی‌شوند.

