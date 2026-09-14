import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Add the parent directory to sys.path
from utils import llm_pick

llm_obj=llm_pick.pick_llm("low")
print(llm_obj.invoke("What is the capital of France?"))  # Output: gpt-5.6-luna