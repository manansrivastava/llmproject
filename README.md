# AI Operations Assistant

## Overview

This project implements an **AI Operations Assistant** that accepts a natural-language task, plans the required steps, executes real tools (APIs), and returns a structured final result.

The system is built using a **multi-agent architecture** consisting of a **Planner**, **Executor**, and **Verifier**, and is designed to run **locally on localhost**.

## Approach

The AI Operations Assistant is built using an **agent-based approach** that separates planning, execution, and verification into independent components.

The system follows an **LLM-first design** for task planning, where a language model is used to convert natural-language input into a structured execution plan. To handle real-world constraints such as API quotas, model deprecations, or service downtime, a **deterministic fallback planner** is implemented to ensure reliable local execution.

Once a plan is generated, the Executor agent performs the required actions by calling real third-party APIs. The Verifier agent then validates the execution results and formats the final structured output.

This approach ensures:
- clear separation of responsibilities between agents
- robustness against external service failures
- consistent end-to-end execution for local demos

## LLM Integration

The system is designed with an **LLM-first Planner and Verifier**.  
During development, the Hugging Face Inference API was used to experiment with open-source instruction-tuned models for structured planning.

However, public LLM endpoints may experience quota limits, model deprecations, or downtime.  
To ensure reliable local execution and a guaranteed working demo, the system includes a **deterministic fallback planner**, which is automatically used when LLM services are unavailable.

## Architecture Overview

The system follows a **three-agent design**:

### 1. Planner Agent
- Accepts natural language input
- Converts the task into a structured execution plan (JSON)
- Designed as **LLM-first**, with a **deterministic fallback planner** to ensure reliability when external LLM services are unavailable

### 2. Executor Agent
- Iterates over the plan steps
- Calls real third-party APIs
- Collects raw results from tools

### 3. Verifier Agent
- Validates execution results
- Ensures completeness
- Formats the final structured output

## Tools

- **Weather Tool**
- **GitHub Repository Search Tool**



## Integrated Third-Party APIs

The project integrates **real, live APIs**:

### OpenWeather API
- Fetches current weather data by city

### GitHub REST API
- Searches repositories and retrieves stars and URLs

## Setup Instructions (Local)

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <repo-name>


```
### Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

###  Install dependencies
```bash
pip install -r requirements.txt

```
## Environment Variables
Create a .env file in the project root.

```env
OPENAPI_KEY=your key
OPENWEATHER_API_KEY=your_openweather_api_key_here

```
Note:
LLM integration is abstracted and can be enabled by adding an LLM API key.
The system includes a deterministic fallback planner to ensure the project always runs locally.

## Running the Project
The project runs locally using a single command:
```bash
python main.py

```
You will be prompted to enter a task in natural language.

## Example Prompts (Deterministic)
The following prompts can be used to test the system.
Given the fallback planner, these produce consistent execution plans and outputs
```txt
1. Get current weather in Pune and find top GitHub repositories for LangChain
2. Find GitHub repositories for LangChain
3. Tell me the current weather in Pune
4. Plan and execute steps to retrieve the weather in Pune and list popular GitHub repositories related to LangChain
5. I want to check today’s weather in Pune and explore GitHub projects built using LangChain
```

## Sample Output
```json
{
  "status": "success",
  "data": [
    {
      "weather": {
        "city": "Pune",
        "temperature": 23.56,
        "description": "broken clouds"
      }
    },
    {
      "github": [
        {
          "name": "langchain-ai/langchain",
          "stars": 125936,
          "url": "https://github.com/langchain-ai/langchain"
        }
      ]
    }
  ]
}

```
## Known Limitations
```txt
1. External LLM providers may experience:
-quota limits
-model deprecations
-endpoint downtime
2. To ensure reliable local execution, the Planner and Verifier include deterministic fallback logic
3. The fallback planner uses keyword-based intent detection and does not perform deep semantic parsing
4. Weather values vary in real time based on live API responses
```
## Design Rationale

The system is designed with an LLM-first architecture while prioritizing operational reliability.

A deterministic fallback planner ensures that the assistant produces valid plans and completes execution even when AI services are unavailable, a common requirement in production AI operations systems.
