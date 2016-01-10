#!/usr/bin/env python3
import coverage
import os

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
NORMAL = "\033[0m"

PERCENTAGE = 95

cov = coverage.Coverage(
    source=["project"],
    omit=["*/wsgi.py", "*/settings.py", "*/migrations/*.py", "*/__init__*"]
)

cov.start()
print(YELLOW + "Running Tests..." + NORMAL)
os.system('manage.py test')
cov.stop()

print(YELLOW + "Collecting Coverage..." + NORMAL)
covered = cov.report()
if covered <= PERCENTAGE:
    print(RED + "ERROR: Your coverage needs to be higher. Current coverage: {}%. Required: {}%.".format(covered, PERCENTAGE) + NORMAL)
    exit(1)

print(GREEN + "Coverage Complete." + NORMAL)
