from langchain_community.llms import Ollama
from core.state import AgentState

llm = Ollama(model="llama3.2")


def reporter_agent(state: AgentState) -> AgentState:
    print("\n📋 Reporter Agent working...")

    prompt = f"""You are a technical project manager. Create a final report.

Task: {state['task']}
Plan: {state['plan']}
Research: {state['research']}
Code: {state['code']}
Test Results: {state['test_results']}

Write a clean final report with:
- What was built
- How to run it
- Key decisions made
- Known limitations
- Next steps to improve it"""

    report = llm.invoke(prompt)

    state['final_report'] = report
    state['messages'].append(f"[REPORTER]: {report}")
    state['current_agent'] = 'done'

    print(f"✅ Report ready")
    return state