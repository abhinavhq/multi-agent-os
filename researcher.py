from langchain_community.llms import Ollama
from core.state import AgentState

llm = Ollama(model="llama3.2")


def researcher_agent(state: AgentState) -> AgentState:
    print("\n🔍 Researcher Agent working...")

    prompt = f"""You are a senior developer and technical researcher.

Original Task: {state['task']}
Development Plan: {state['plan']}

Research the best approach for this task. Include:
- Best libraries/frameworks to use and why
- Common pitfalls to avoid
- Best practices and patterns
- Any important technical considerations"""

    research = llm.invoke(prompt)

    state['research'] = research
    state['messages'].append(f"[RESEARCHER]: {research}")
    state['current_agent'] = 'coder'

    print(f"✅ Research complete")
    return state