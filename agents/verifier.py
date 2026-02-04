def verify_and_format(execution_result: dict) -> dict:
    """
    Verifier Agent:
    Since LLM is disabled, this verifier performs
    deterministic validation and formatting.
    """

    # Basic validation
    if "results" not in execution_result:
        raise ValueError("Invalid execution result")

    return {
        "status": "success",
        "data": execution_result["results"]
    }
