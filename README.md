# ChatGPT-Skill-Benchmark

## AI Skill Engineering Benchmark

این ریپو یک محیط آزمایش برای **پیدا کردن، ترکیب، ساخت، ارزیابی و تکامل Skillهای حرفه‌ای Agent** است.

هدف فقط این نیست که ببینیم «یک Skill جواب بهتری می‌دهد یا نه». سؤال اصلی بزرگ‌تر است:

> آیا این Skill از نظر معماری، Context، Repository integration، نگهداری و رشد بلندمدت واقعاً قابل اتکاست؟

---

## Core Idea

چرخه اصلی پروژه:

```text
Discover
   ↓
Verify Sources
   ↓
Synthesize Candidate Skill
   ↓
Benchmark on Real Tasks
   ↓
Score + Compare
   ↓
Evolve the Skill
   ↓
Repeat for the next Skill
```

بنابراین این ریپو هم‌زمان سه نقش دارد:

1. **Skill Research Lab** — پیدا کردن و بررسی Skillهای موجود.
2. **Skill Architecture Workshop** — ترکیب ایده‌ها و ساخت Candidateهای جدید.
3. **Benchmark Environment** — مقایسه‌ی Skillهای تخصصی و Skillهای ترکیبی روی Taskهای یکسان.

---

## Benchmark Layers

### 1. Output Quality

- Accuracy
- Completeness
- Reliability
- Consistency

### 2. Skill Architecture

- کیفیت `SKILL.md`
- Progressive disclosure
- Module separation
- Rule/workflow ownership
- Context efficiency
- Conflict resistance

### 3. Repository Engineering

- Repository understanding
- Architecture mapping
- Dependency/boundary analysis
- Change-impact reasoning
- Refactor/hardening strategy

### 4. Template Generation

- Repository shape
- Canonical ownership
- Documentation
- Validation strategy
- Scalability without speculative complexity

### 5. Evolution & Drift Resistance

- Migration safety
- Preservation of existing behavior
- Architecture drift control
- Long-term maintainability
- Multi-skill composition

---

## First Composite Candidate: AI Repository Engineer

اولین Candidate واقعی پروژه از ترکیب الگوهای چند Skill/Repository معماری ساخته شده است:

```text
reference-skills/ai-repository-engineer/
├── SKILL.md
└── workflows/
    ├── create.md
    ├── analyze.md
    └── evolve.md
```

سه Mode اصلی:

- **Create** — ساخت Repository/Template جدید.
- **Analyze** — فهم و Audit کردن Repository موجود.
- **Evolve** — Refactor، Migration، Hardening و کنترل Drift.

این Candidate به‌عنوان «برنده از پیش تعیین‌شده» در نظر گرفته نمی‌شود. Benchmark باید مشخص کند چه زمانی Skill ترکیبی بهتر است و چه زمانی Skill تخصصی کوچک‌تر عملکرد بهتری دارد.

---

## Current Repository Structure

```text
ChatGPT-Skill-Benchmark/
├── README.md
├── benchmarks/
│   ├── repository-engineering/
│   ├── skill-architecture/
│   └── template-generation/
├── evaluation/
│   └── README.md
├── reference-skills/
│   ├── README.md
│   └── ai-repository-engineer/
├── research/
│   ├── SOURCE_CATALOG.md
│   └── repository-engineering/
└── rubrics/
    ├── scoring-model.md
    └── skill-engineering-rubric.md
```

---

## Scoring

مدل پیش‌فرض ۱۰۰ امتیازی:

| Dimension | Weight |
|---|---:|
| Correctness & Evidence | 25 |
| Architecture Quality | 20 |
| Context Management | 15 |
| Maintainability | 15 |
| Preservation & Change Safety | 10 |
| Documentation & Explainability | 10 |
| Efficiency | 5 |

جزئیات و Hard-Failها در `rubrics/scoring-model.md` ثبت شده‌اند.

---

## Source Discipline

هر Skill خارجی قبل از اینکه به‌عنوان Reference استفاده شود باید Verify شود.

فهرست منابع تأییدشده و نقش هرکدام:

`research/SOURCE_CATALOG.md`

این کار مانع از این می‌شود که Benchmark بر پایه لینک‌های اشتباه، Repoهای حذف‌شده یا توضیحات حدسی ساخته شود.

---

## Benchmark Principle

هدف انتخاب پیچیده‌ترین Skill نیست.

هدف پیدا کردن **کوچک‌ترین معماری‌ای است که Task را به‌صورت قابل اتکا، مستند، evidence-grounded و قابل توسعه حل کند.**

به همین دلیل پروژه باید همیشه این مقایسه را ممکن نگه دارد:

```text
Specialist Skill
      vs
Composite Skill
      vs
No Skill / Baseline
```

---

## Long-Term Direction

در ادامه هر حوزه جدید همین چرخه را طی می‌کند:

```text
چند Skill پیدا می‌شوند
→ منابع Verify می‌شوند
→ نقاط قوت/ضعف استخراج می‌شود
→ Candidate جدید ساخته می‌شود
→ Benchmark اجرا می‌شود
→ نتیجه ثبت می‌شود
→ محیط برای Skill بعدی آماده می‌ماند
```

در نتیجه، این Repository قرار است به‌مرور تبدیل شود به یک **Skill Engineering System**؛ نه صرفاً یک لیست Skill و نه صرفاً یک Benchmark خروجی.
