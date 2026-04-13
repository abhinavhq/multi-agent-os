from langchain_community.llms import Ollama
from core.state import AgentState

llm = Ollama(model="llama3.2")


def tester_agent(state: AgentState) -> AgentState:
    print("\n🧪 Tester Agent working...")

    prompt = f"""You are a senior QA engineer and code reviewer.

Original Task: {state['task']}
Code to Review: {state['code']}

1. Review the code for bugs, security issues, and edge cases
2. Write comprehensive unit tests for this code
3. List any improvements needed
4. Give it an overall quality score out of 10"""

    test_results = llm.invoke(prompt)

    state['test_results'] = test_results
    state['messages'].append(f"[TESTER]: {test_results}")
    state['current_agent'] = 'reporter'

    print(f"✅ Testing complete")
    return state