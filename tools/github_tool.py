import requests

def search_github(query: str) -> list:
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "sort": "stars", "order": "desc"}
    res = requests.get(url, params=params)
    res.raise_for_status()
    items = res.json()["items"][:3]

    return [
        {
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"]
        }
        for repo in items
    ]
