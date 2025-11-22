#!/bin/bash
# Username Recon Script by 0xV4RGR

if [ -z "$1" ]; then
    echo "Usage: ./username_recon.sh <username>"
    exit 1
fi

echo "🔍 Scanning for username: $1"
sites=(
    "https://instagram.com/$1"
    "https://twitter.com/$1"
    "https://github.com/$1"
    "https://tiktok.com/@$1"
    "https://facebook.com/$1"
)

for site in "${sites[@]}"; do
    code=$(curl -o /dev/null -s -w "%{http_code}" "$site")
    if [ "$code" -eq 200 ]; then
        echo "[FOUND] $site"
    else
        echo "[---] $site"
    fi
done
