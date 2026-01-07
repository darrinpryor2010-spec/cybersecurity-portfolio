"""
01_variables_and_loops.py

Goal:
Learn basic Python variables, loops, and conditional logic
using a simple security-related example.
"""

logs = [
    "2026-01-01 09:00:01 user=darrin action=login status=SUCCESS ip=10.0.0.5",
    "2026-01-01 09:02:11 user=alex action=login status=FAILED ip=10.0.0.8",
    "2026-01-01 09:03:44 user=alex action=login status=FAILED ip=10.0.0.8",
    "2026-01-01 09:05:02 user=sam action=login status=SUCCESS ip=10.0.0.9",
]

failed_count = 0
success_count = 0

for line in logs:
    if "status=FAILED" in line:
        failed_count += 1
    elif "status=SUCCESS" in line:
        success_count += 1

print("Failed logins:", failed_count)
print("Successful logins:", success_count)
