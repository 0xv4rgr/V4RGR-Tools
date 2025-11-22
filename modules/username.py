import subprocess

SITES = [
    "https://twitter.com/{u}",
    "https://instagram.com/{u}",
    "https://github.com/{u}",
    "https://tiktok.com/@{u}",
    "https://facebook.com/{u}",
]


def check_url_exists(url: str) -> bool:
    """
    Uses curl to check if a profile URL returns HTTP 200.
    """
    try:
        result = subprocess.run(
            ["curl", "-o", "/dev/null", "-s", "-w", "%{http_code}", url],
            capture_output=True,
            text=True,
            timeout=10,
        )
        return result.stdout.strip() == "200"
    except Exception:
        return False


def run_username_scan(username: str):
    """
    Very simple username OSINT:
    - Checks a few major platforms for the username.
    - Returns a list of findings.
    """
    findings = []

    for tmpl in SITES:
        url = tmpl.format(u=username)
        exists = check_url_exists(url)
        if exists:
            findings.append(f"[FOUND] {url}")
        else:
            findings.append(f"[---] {url}")

    return findings
