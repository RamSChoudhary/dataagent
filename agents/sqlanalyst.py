import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Add the parent directory to sys.path
from utils import llm_pick
from models import AgentSchema

def curate_question(state: AgentSchema) -> AgentSchema:
    user_question = state.user_question
    llm = llm_pick.pick_llm("low")  # Pick the appropriate LLM based on the level of complexity
    response = llm.invoke(f"Curate the following user question: {user_question}")
    state.curated_ques = response
    return state

def prompt_query_context(state: AgentSchema) -> AgentSchema:
    curated_ques = state.curated_ques
    llm = llm_pick.pick_llm("medium")  # Pick the appropriate LLM based on the level of complexity
    response = llm.invoke(f"Generate a detailed prompt with SQL DB context for the following curated question: {curated_ques}")
    state.prompt_query_context = response
    return state