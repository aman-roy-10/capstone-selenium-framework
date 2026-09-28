"""Runs the Unittest suite AND writes an HTML report to reports/unittest_report.html.

Run from the project root:
    python -m legacy_unittest.run_suite
"""
import base64
import html
import sys
import time
import unittest
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START_DIR = Path(__file__).resolve().parent
REPORT_PATH = ROOT / "reports" / "unittest_report.html"


class HtmlTestResult(unittest.TextTestResult):
    """Normal console result that also remembers every outcome for the HTML report."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records = []
        self._started = {}

    def startTest(self, test):
        self._started[id(test)] = time.time()
        super().startTest(test)

    def _add(self, test, status, detail=""):
        seconds = time.time() - self._started.get(id(test), time.time())
        self.records.append({"test": test, "status": status, "detail": detail, "seconds": seconds})

    def addSuccess(self, test):
        super().addSuccess(test)
        self._add(test, "PASSED")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self._add(test, "FAILED", self._exc_info_to_string(err, test))

    def addError(self, test, err):
        super().addError(test, err)
        self._add(test, "ERROR", self._exc_info_to_string(err, test))

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self._add(test, "SKIPPED", reason)


def write_report(result, report_path=REPORT_PATH):
    counts = {"PASSED": 0, "FAILED": 0, "ERROR": 0, "SKIPPED": 0}
    rows = []
    for rec in result.records:
        counts[rec["status"]] += 1
        test = rec["test"]
        shot_html = ""
        shot = getattr(test, "screenshot_path", None)
        if shot and Path(shot).exists():
            encoded = base64.b64encode(Path(shot).read_bytes()).decode()
            shot_html = f'<br><img src="data:image/png;base64,{encoded}" width="600">'
        detail = f"<pre>{html.escape(rec['detail'])}</pre>" if rec["detail"] else ""
        rows.append(
            f"<tr class='{rec['status']}'><td>{html.escape(test.id())}</td>"
            f"<td>{rec['status']}</td><td>{rec['seconds']:.1f}s</td><td>{detail}{shot_html}</td></tr>"
        )

    page = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Unittest Report</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 24px; }}
table {{ border-collapse: collapse; width: 100%; }}
td, th {{ border: 1px solid #ccc; padding: 6px 10px; vertical-align: top; text-align: left; }}
th {{ background: #f0f0f0; }}
tr.PASSED td:nth-child(2) {{ color: #1a7f37; font-weight: bold; }}
tr.FAILED td:nth-child(2), tr.ERROR td:nth-child(2) {{ color: #cf222e; font-weight: bold; }}
pre {{ white-space: pre-wrap; margin: 0; }}
</style></head><body>
<h1>Unittest Report</h1>
<p>Generated {datetime.now():%Y-%m-%d %H:%M:%S} &nbsp;|&nbsp; Total: {len(result.records)}
 &nbsp;|&nbsp; Passed: {counts['PASSED']} &nbsp;|&nbsp; Failed: {counts['FAILED']}
 &nbsp;|&nbsp; Errors: {counts['ERROR']} &nbsp;|&nbsp; Skipped: {counts['SKIPPED']}</p>
<table><tr><th>Test</th><th>Result</th><th>Time</th><th>Details / screenshot</th></tr>
{''.join(rows)}
</table></body></html>"""
    report_path = Path(report_path)
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text(page, encoding="utf-8")
    return report_path


def main(start_dir=START_DIR, top_dir=ROOT, report_path=REPORT_PATH) -> int:
    suite = unittest.TestLoader().discover(str(start_dir), pattern="test_*.py", top_level_dir=str(top_dir))
    runner = unittest.TextTestRunner(verbosity=2, resultclass=HtmlTestResult)
    result = runner.run(suite)
    path = write_report(result, report_path)
    print(f"\nHTML report: {path}")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
