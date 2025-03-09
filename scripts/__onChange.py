from typing import Callable
from GeneralLLM import GeneralLLM
from ServerLLMHandler import ServerLLMHandler
from __LLM_Parameneter_Input import _LLM_Parameneter_Input as _lpi
from __LLM_Parameneter_Options import _LLM_Parameneter_Options as _lpo

class _OnChangeConfig:
    _ActivateLocalLlm : str = "Activatelocalllm"
    _ActivateServerLlm : str = "Activateserverlllm"
    _SingleWord : str = "Singleword"
    _AutoLLMParsing : str = "Autollmparsing"
    _NetworkAddress : str = "Networkaddress"
    _Port : str = "Port"

class _onChange:
    _FunctionDict : dict[str, Callable] | None = None

    @staticmethod
    def _define_dict(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            if(_onChange._FunctionDict): return _f(*args, **kwargs)

            _onChange._FunctionDict = {}
            _d: dict[str, Callable] = _onChange._FunctionDict
            _c = _OnChangeConfig

            def _SingleWord(par, prev) -> None:
                if(_lpo.AutoLLMParsing()):
                    GeneralLLM.process_llm_input(str(_lpi.SingleWord()))

            def _AutoLLMParsing(par, prev) -> None:
                pass

            def _ReconnectServer(par, prev) -> None:
                ServerLLMHandler.connect()

            def _ChangeLLMType(par,prev) -> None:
                GeneralLLM.llm_type()

            _d[_c._ActivateLocalLlm] = _ChangeLLMType
            _d[_c._ActivateServerLlm] = _ChangeLLMType
            _d[_c._SingleWord] = _SingleWord
            _d[_c._AutoLLMParsing] = _AutoLLMParsing
            _d[_c._NetworkAddress] = _ReconnectServer
            _d[_c._Port] = _ReconnectServer

            return _f(*args, **kwargs)
        return _w


    @_define_dict
    @staticmethod
    def call(par, prev) -> None:
        _function : callable | None = _onChange._FunctionDict.get(par.name)
        if(_function): _function(par, prev)