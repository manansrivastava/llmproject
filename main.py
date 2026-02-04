from dotenv import load_dotenv
load_dotenv()

from agents.planner import plan_task
from agents.executor import execute_plan
from agents.verifier import verify_and_format

def main():
    user_task = input("Enter task: ")

    plan = plan_task(user_task)
    print("\nPlan:", plan)

    execution = execute_plan(plan)
    print("\nExecution:", execution)

    final_output = verify_and_format(execution)
    print("\nFinal Output:")
    print(final_output)

if __name__ == "__main__":
    main()
