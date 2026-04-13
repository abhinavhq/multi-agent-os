from langchain_community.llms import Ollama
from core.state import AgentState

llm = Ollama(model="llama3.2")


def coder_agent(state: AgentState) -> AgentState:
    print("\n💻 Coder Agent working...")

    prompt = f"""You are an expert software engineer. Write production-quality code.

Original Task: {state['task']}
Plan: {state['plan']}
Research & Best Practices: {state['research']}

Write complete, working, well-commented code that fully implements the task.
Include proper error handling. Make it production ready."""

    code = llm.invoke(prompt)

    state['code'] = code
    state['messages'].append(f"[CODER]: {code}")
    state['current_agent'] = 'tester'

    print(f"✅ Code written")
    return state