from langchain_community.llms import Ollama
from core.state import AgentState

llm = Ollama(model="llama3.2")


def planner_agent(state: AgentState) -> AgentState:
    print("\n🧠 Planner Agent working...")

    prompt = f"""You are a senior software architect and project planner.

User Task: {state['task']}

Break this task into clear, actionable steps for a development team.
Be specific. List exactly what needs to be built, in what order, and why.
Output a numbered plan."""

    plan = llm.invoke(prompt)

    state['plan'] = plan
    state['messages'].append(f"[PLANNER]: {plan}")
    state['current_agent'] = 'researcher'

    print(f"✅ Plan created")
    return state