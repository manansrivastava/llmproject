from tools.weather_tool import get_weather
from tools.github_tool import search_github

def execute_plan(plan: dict) -> dict:
    results = []

    for step in plan["steps"]:
        action = step["action"]
        params = step["params"]

        if action == "get_weather":
            results.append({"weather": get_weather(**params)})

        elif action == "search_github":
            results.append({"github": search_github(**params)})

    return {"results": results}
