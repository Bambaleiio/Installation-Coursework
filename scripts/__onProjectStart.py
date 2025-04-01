from _LLM_Type import _LLM_Type
from GeneralLLM import GeneralLLM

def onStart() -> None:
	GeneralLLM.llm_type(_LLM_Type.local)
