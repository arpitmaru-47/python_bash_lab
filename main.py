import subprocess
from pathlib import Path

script = Path(__file__).with_name("system_report.sh")

try:
    result = subprocess.run(
        ["bash", str(script)],
        capture_output=True,
        text=True,
        check=True,
        timeout=30
    )

    report = result.stdout

    output_file = script.parent /"system_report.txt"
    output_file.write_text(report,encoding="utf-8")
    print(report)
    print(f"Report saved to: {output_file}")

except subprocess.CalledProcessError as error:
    print("System report failed.")
    print("Exit code:", error.returncode)
    print(error.stderr)

except subprocess.TimeoutExpired:
    print("System report timeout.")

except OSError as error:
    print("Could not execute the script:", error)
