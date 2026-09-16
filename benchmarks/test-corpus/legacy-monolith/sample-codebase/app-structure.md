# Legacy Monolith Sample Codebase

## Structure
```
src/
├── users/
├── orders/
├── payments/
├── notifications/
└── database/
```

## Known Architecture Problems
- Multiple domains directly access the same database layer.
- Business rules are duplicated between modules.
- No clear ownership boundaries exist.

## Expected Skill Analysis
The agent should identify current architecture before proposing migration steps.
