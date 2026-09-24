# Capstone Selenium Framework

Selenium 4 + PyTest (primary) + Unittest (separate suite), Page Object Model,
CSV data-driven tests, logging, HTML reports and screenshots on failure.
Target site: https://automationexercise.com

## Setup (Windows)

```
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

In PowerShell, if activation is blocked ("running scripts is disabled"):
`Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
(or use Command Prompt / `venv\Scripts\activate.bat`).

Requirements: Python 3.9+ and Google Chrome. webdriver-manager downloads ChromeDriver by itself.

Before running, put your own email in `data/signup_users.csv`
(a dot-alias such as `name.surname@gmail.com` works well).

## Run the PyTest suite (15 tests)

```
python -m pytest
python -m pytest tests\test_search.py      # one file
python -m pytest -m smoke                  # smoke tests only
python -m pytest --headless                # no browser window
python -m pytest --browser edge            # another browser
```
HTML report: `reports/report.html`

## Run the Unittest suite (4 tests)

```
python -m legacy_unittest.run_suite
```
HTML report: `reports/unittest_report.html`
(Plain alternative without the HTML report: `python -m unittest discover -s legacy_unittest -t . -v`)

## Output folders

| Folder | Content |
|---|---|
| reports/ | `report.html` (PyTest) and `unittest_report.html` (Unittest) |
| screenshots/ | one PNG for every failed test (both suites) |
| logs/ | `framework.log` - every page action, test start/end and failure |

## Test coverage

- Login page loads (sanity)
- Invalid login shows an error (data-driven, CSV)
- Valid login and logout (account created and deleted automatically by a fixture)
- New user signup form; duplicate signup shows an error
- Signup validation: missing name/email, bad email formats (data-driven, CSV)
- Product search, including a term with zero results (data-driven, CSV)
- Unittest suite: login page load, invalid login, search with results, search with zero results

## Structure

| Folder | Purpose |
|---|---|
| config/ | config.ini (base URL, browser, headless, timeouts) |
| data/ | CSV test data |
| pages/ | Page Objects: base, home, login, search, signup |
| tests/ | PyTest tests + conftest.py (fixtures, screenshot hook, logging) |
| legacy_unittest/ | Unittest suite + HTML runner (ignored by PyTest) |
| utils/ | driver factory, config reader, CSV reader, screenshot helper, logger |

## Built-in fixes for known site issues

1. **Ad click interception** - `BasePage.click()` falls back to a JavaScript click.
2. **Zero-results wait bug** - `SearchPage.get_result_count()` uses a 1-second pause and `find_elements()`
   instead of a waiting helper (see the comment in the code).

## Windows gotchas

- Use `python`, not `python3`; use `venv\Scripts\activate`, not `source venv/bin/activate`.
- Run every command from the project root folder (where pytest.ini is).
- Paths in code use `pathlib`, so no hard-coded `\` or `/`.
- Saving CSVs from Excel adds a hidden BOM; the CSV reader already handles it.
- Avoid OneDrive-synced or very deep folders (file locking / long-path errors).
- Antivirus or a company proxy can block the ChromeDriver download.
- Do not click around in the test browser while tests run.
