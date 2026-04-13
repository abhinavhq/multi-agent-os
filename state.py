from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    task: str
    plan: Optional[str]
    research: Optional[str]
    code: Optional[str]
    test_results: Optional[str]
    final_report: Optional[str]
    messages: List[str]
    current_agent: Optional[str]