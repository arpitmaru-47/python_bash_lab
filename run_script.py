import subprocess

try:
    result = subprocess.run(
        ["bash", "check_service.sh"],
        capture_output=True,
        text=True,
        check=True
    )

    print("Script output:")
    print(result.stdout)

except subprocess.CalledProcessError as error:
    print("Script failed")
    print("Exit code:", error.returncode)
    print("Error:", error.stderr)
