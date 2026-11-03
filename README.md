# lab9-playwright-ci

Лабораторная работа №9 (ТПО): запуск UI-тестов Playwright/pytest в GitHub Actions.

Локальный запуск:

```
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m playwright install chromium
.venv\Scripts\python.exe -m http.server 8000 --bind 127.0.0.1
.venv\Scripts\python.exe -m pytest -v --browser chromium
```

CI: workflow `.github/workflows/ui-tests.yml` запускается при push, pull_request и вручную (workflow_dispatch).
