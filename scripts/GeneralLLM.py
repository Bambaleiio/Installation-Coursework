import os
from enum import Enum
from typing import Callable
from LocalLLMHandler import LocalLLMHandler
from ServerLLMHandler import ServerLLMHandler
from __LLM_Parameneter_Folders import _LLM_Parameneter_Folders

os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

class _LLM_Type(Enum):
    local = 0
    server = 1

class _LLM_Type_t:
    _dict: dict[_LLM_Type, type] = {
        _LLM_Type.local : LocalLLMHandler,
        _LLM_Type.server : ServerLLMHandler
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
    def _llm_type(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            _l = _LLM_Parameneter_Folders
            _server : bool = _l.ActivateServerLlm()
            _local : bool = _l.ActivateLocalLlm()
            if _server and _local:
                GeneralLLM._cur_LLM_Type = _LLM_Type.local
                _l._ActivateServerLlm.val = False
            elif _server:
                GeneralLLM._cur_LLM_Type = _LLM_Type.server
                _l._ActivateLocalLlm.val = False
            else:
                GeneralLLM._cur_LLM_Type = _LLM_Type.local
                _l._ActivateServerLlm.val = False

            return _f(*args, **kwargs)
        return _w

    @_llm_type
    @staticmethod
    def llm_type() -> None:
        pass

    @staticmethod
    def _find_and_call(attr : str, *kwargs) -> None:
        _t: _LLM_Type = GeneralLLM._cur_LLM_Type
        _r: Callable | None = _LLM_Type_t.getattr(_t, attr)
        if(_r): _r(*kwargs)

    @_llm_type
    @staticmethod
    def process_llm_input(input : str) -> None:
        GeneralLLM._find_and_call("process_llm_input", input)

    @_llm_type
    @staticmethod
    def update_table() -> None:
        GeneralLLM._find_and_call("get_possible_emotions")

    @_llm_type
    @staticmethod
    def install_libs() -> None:
        GeneralLLM._find_and_call("install_libs")

    @_llm_type
    @staticmethod
    def connect() -> None:
        GeneralLLM._find_and_call("connect")
