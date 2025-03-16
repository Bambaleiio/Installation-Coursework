from enum import Enum

class _LLM_Type(Enum):
    local = 0
    server = 1
    internet = 2