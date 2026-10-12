# EduEagle Automated Verification Suites

This directory contains the automated test suites for the EduEagle platform:

| Test File | Focus | Test Count |
|---|---|---|
| `test_new_modules.py` | 6 Core Modules & RBAC Verification | 57 Tests |
| `test_frontend_seo.py` | 9 Frontend, SEO & Metadata Requirements | 40 Tests |
| `test_mobile_ux.py` | Mobile Breakpoints, UX & Compliance | 14 Tests |
| `test_security.py` | Security, Cryptographic Signatures & Rate Limiting | 20+ Tests |
| `test_untrusted_user.py` | 20-Point Defensive Security & Untrusted User Audit | 35 Tests |
| `test_ai_chatbot.py` | EagleMentor AI Copilot & NEP 2020 Derivations | 13 Tests |

## Running Tests

To run all test suites at once:
```bash
python scripts/run_tests.py
```

To run an individual suite:
```bash
python tests/test_new_modules.py
python tests/test_frontend_seo.py
python tests/test_mobile_ux.py
python tests/test_security.py
python tests/test_untrusted_user.py
python tests/test_ai_chatbot.py
```
