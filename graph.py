from langgraph.graph import StateGraph, END
from core.state import AgentState
from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.coder import coder_agent
from agents.tester import tester_agent
from agents.reporter import reporter_agent


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_agent)
    graph.add_node("researcher", researcher_agent)
    graph.add_node("coder", coder_agent)
    graph.add_node("tester", tester_agent)
    graph.add_node("reporter", reporter_agent)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "coder")
    graph.add_edge("coder", "tester")
    graph.add_edge("tester", "reporter")
    graph.add_edge("reporter", END)

    return graph.compile()