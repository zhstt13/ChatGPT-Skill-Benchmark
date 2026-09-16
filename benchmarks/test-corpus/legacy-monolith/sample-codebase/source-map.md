# Legacy Monolith Sample Source Map

## Repository Simulation

```
app/
├── users/
├── orders/
├── payments/
├── notifications/
├── shared/
└── database/
```

## Hidden Architecture Issues

- Multiple domains share direct database access.
- Business rules exist inside controllers.
- Shared utilities contain unrelated responsibilities.
- No clear ownership boundaries.

## Expected Skill Analysis

The evaluator should identify coupling, ownership problems, and safe migration steps without proposing a full rewrite immediately.
