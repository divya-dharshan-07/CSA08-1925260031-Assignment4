# Task 03 – Custom Exceptions

Run:

```bash
python task3.py
```

Expected output:

```text
(1, 1, [(3, 'expected 3 fields, found 2'), (4, "invalid status 'L'")])
```

The program defines `InvalidRecord`, validates each line, records malformed records, and chains a clearer `FileNotFoundError`.
