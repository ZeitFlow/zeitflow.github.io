#!/usr/bin/env python3
"""Read the existing Pages production branch so a push cannot become a preview."""

import json
import os
import re
from urllib.request import Request, urlopen


ACCOUNT = "64962783605a1e749a4ea11b02405af0"
PROJECT = "zeitflow-website"


def main():
    request = Request(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/pages/projects/{PROJECT}",
        headers={"Authorization": f"Bearer {os.environ['CLOUDFLARE_API_TOKEN']}"},
    )
    with urlopen(request, timeout=30) as response:
        data = json.load(response)
    if not data.get("success"):
        raise RuntimeError("Cloudflare could not read the Pages project")
    branch = data["result"]["production_branch"]
    # The branch becomes an action command argument and a GitHub step output.
    if not isinstance(branch, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]*", branch):
        raise ValueError("Unexpected Pages production branch")
    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
        output.write(f"branch={branch}\n")
    print(f"Deploying to the existing production branch: {branch}")


if __name__ == "__main__":
    main()
