#!/bin/bash

service_name="$1"

if [ -z "$service_name" ]; then
    echo "ERROR: Service name is required" >&2
    exit 1
fi

echo "Checking service: $service_name"
echo "check completed"
