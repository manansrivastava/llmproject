import json
from llm_dir.client import call_llm

def plan_task(user_task: str) -> dict:
    """
    Planner Agent:
    - Tries LLM
    - Falls back to rule-based plan if LLM fails
    """

    prompt = f"""
Return ONLY valid JSON.
Schema:
{{
  "steps": [
    {{
      "action": "get_weather" | "search_github",
      "params": {{}}
    }}
  ]
}}

User task:
{user_task}
"""

    try:
        response = call_llm(prompt).strip()
        if response.startswith("{"):
            return json.loads(response)
    except Exception as e:
        print("⚠️ LLM unavailable, using fallback planner:", e)

    
    plan = {"steps": []}

    text = user_task.lower()

    if "weather" in text:
        plan["steps"].append({
            "action": "get_weather",
            "params": {"city": "Pune"}
        })

    if "github" in text or "repository" in text:
        plan["steps"].append({
            "action": "search_github",
            "params": {"query": "LangChain"}
        })

    return plan
