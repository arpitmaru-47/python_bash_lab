import subprocess

service = "nginx"

result = subprocess.run(
    ["bash", "check_service.sh", service],
    capture_output=True,
    text=True
)

print(result.stdout)

if result.returncode != 0:
    print("ERROR:", result.stderr)
