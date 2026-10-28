#!/bin/bash

echo "===== DEV SYSTEM REPORT ====="
echo "Date: $(date)"
echo "User: $(whoami)"

echo ""
echo "===== DISK USAGE ====="
df -h

echo ""
echo "===== MEMORY USAGE ====="

if command -v free >/dev/null 2>&1; then
    free -h
else
    echo "free command is unavailable"
fi

echo ""
echo "===== REPORT COMPLETE ====="
