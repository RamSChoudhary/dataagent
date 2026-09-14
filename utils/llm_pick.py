from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def pick_llm(Level: str):
    """
    Pick the appropriate LLM based on the level of complexity.

    Args:
        Level (str): The level of complexity ('simple', 'medium', 'complex').

    Returns:
        str: The name of the selected LLM.
    """
    if Level.lower() == 'low':
        return ChatOpenAI(model_name="gpt-5.6-luna", temperature=0)
    elif Level.lower() == 'medium':
        return ChatOpenAI(model_name="gpt-5.6-terra", temperature=0)
    elif Level.lower() == 'high':
        return ChatOpenAI(model_name="gpt-5.6-sol", temperature=0)
    else:
        raise ValueError("Invalid level. Choose from 'simple', 'medium', or 'complex'.")

    return llm


llm_obj=pick_llm("low")
print(llm_obj.invoke("What is the capital of France?"))  # Output: gpt-5.6-luna