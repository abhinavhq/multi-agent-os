from core.graph import build_graph
from core.state import AgentState
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()


def run_agent_os(task: str):
    console.print(Panel(f"[bold green]🚀 Multi-Agent OS Starting[/bold green]\n[white]{task}[/white]"))

    initial_state: AgentState = {
        "task": task,
        "plan": None,
        "research": None,
        "code": None,
        "test_results": None,
        "final_report": None,
        "messages": [],
        "current_agent": "planner"
    }

    graph = build_graph()
    final_state = graph.invoke(initial_state)

    console.print("\n")
    console.print(Panel("[bold blue]📋 FINAL REPORT[/bold blue]"))
    console.print(Markdown(final_state['final_report']))

    return final_state


if __name__ == "__main__":
    task = input("\n🎯 Enter your task: ")
    run_agent_os(task)