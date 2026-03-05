"""Python script for getting the number of stars and last update for a GitHub repo."""

import datetime
import json
import urllib.request


def get_stars_and_abandonware(organisation, repository, threshold=5):
    """Query the GitHub API to determine a repo's number of stars and last commit date.

    :arg organisation: the GitHub organisation
    :arg repository: the repository name
    :kwarg threshold: number of years of inactivity after which a repo is considered
        abandonware
    :returns: dictionary containing the number of stars and a bool to indicate if it can
        be classed as abandonware
    """
    github_api_url = f"https://api.github.com/repos/{organisation}/{repository}"
    page = urllib.request.urlopen(github_api_url)
    github_metadata = json.loads(page.read())
    stargazers = github_metadata["stargazers_count"]
    last_update = datetime.datetime.fromisoformat(github_metadata["updated_at"])
    time_elapsed_days = (datetime.datetime.now().date() - last_update.date()).days
    abandonware = time_elapsed_days / 365.25 > threshold
    return {"stars": stargazers, "abandonware": abandonware}


if __name__ == "__main__":
    org = "Cambridge-ICCS"
    repo = "FTorch"
    metadata = get_stars_and_abandonware(org, repo)
    stars = metadata["stars"]
    abandonware = metadata["abandonware"]
    print(f"Repo '{repo}' from organisation '{org}' has {stars} stars.")
    print(f"It is{'' if abandonware else ' not'} abandonware")
