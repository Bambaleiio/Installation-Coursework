import os
from typing import Callable
from _LLM_Type import _LLM_Type
from LocalLLMHandler import LocalLLMHandler
from ServerLLMHandler import ServerLLMHandler
from InternetLLMHandler import InternetLLMHandler
from __Display import _Display

os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

class _LLM_Type_t:
    _dict: dict[_LLM_Type, type] = {
        _LLM_Type.local : LocalLLMHandler,
        _LLM_Type.server : ServerLLMHandler,
        _LLM_Type.internet : InternetLLMHandler
    }

    @staticmethod
    def get(t : _LLM_Type) -> type | None:
        return _LLM_Type_t._dict.get(t)

    @staticmethod
    def getattr(t: _LLM_Type, atr : str):
        return getattr(_LLM_Type_t.get(t), atr)

class GeneralLLM:
    _cur_LLM_Type : _LLM_Type = _LLM_Type.local

    @staticmethod
    def llm_type(type : _LLM_Type) -> None:
        if(not type):
            type = _LLM_Type.local

        GeneralLLM._cur_LLM_Type = type
        _Display.llm_type(GeneralLLM._cur_LLM_Type)

    @staticmethod
    def _find_and_call(attr : str, *kwargs) -> None:
        _t: _LLM_Type = GeneralLLM._cur_LLM_Type
        _r: Callable | None = _LLM_Type_t.getattr(_t, attr)
        if(_r): _r(*kwargs)

    @staticmethod
    def process_llm_input(input : str) -> None:
        GeneralLLM._find_and_call("process_llm_input", input)

    @staticmethod
    def update_table() -> None:
        GeneralLLM._find_and_call("get_possible_emotions")

    @staticmethod
    def install_libs() -> None:
        GeneralLLM._find_and_call("install_libs")

    @staticmethod
    def connect() -> None:
        GeneralLLM._find_and_call("connect")
