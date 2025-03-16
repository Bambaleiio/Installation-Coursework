from typing import Callable
from _LLM_Type import _LLM_Type

class _LLM_Parameneter_Folders:
    _Parent = None

    _ActivateLocalLlm = None
    _ActivateServerLlm = None
    _ActivateInternetLlm = None

    _InternetLLMBase = None

    _Connected = None
    _ServerLaunched = None

    _Serverfile = None

    _NetworkAddress = None
    _Port = None


    @staticmethod
    def set_all_par(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            _l = _LLM_Parameneter_Folders
            if(not _l._Parent):
                _l._Parent = parent().par

            if(not _l._ActivateServerLlm):
                _l._ActivateServerLlm = _l._Parent.Activateserverlllm

            if(not _l._ActivateLocalLlm):
                _l._ActivateLocalLlm = _l._Parent.Activatelocalllm

            if(not _l._ActivateInternetLlm):
                _l._ActivateInternetLlm = _l._Parent.Activateinternetllm

            if(not _l._InternetLLMBase):
                _l._InternetLLMBase = _l._Parent.Llmbase

            if(not _l._NetworkAddress):
                _l._NetworkAddress = _l._Parent.Networkaddress

            if(not _l._Port):
                _l._Port = _l._Parent.Port

            if(not _l._Connected):
                _l._Connected = _l._Parent.Connected

            if(not _l._ServerLaunched):
                _l._ServerLaunched = _l._Parent.Serverlaunched

            if(not _l._Serverfile):
                _l._Serverfile = _l._Parent.Serverfile

            return _f(*args, **kwargs)
        return _w

    @set_all_par
    @staticmethod
    def ActivateLocalLlm() -> bool:
        _l = _LLM_Parameneter_Folders
        return bool(_l._ActivateLocalLlm.eval())

    @set_all_par
    @staticmethod
    def ActivateServerLlm() -> bool:
        _l = _LLM_Parameneter_Folders
        return bool(_l._ActivateServerLlm.eval())

    @set_all_par
    @staticmethod
    def InternetLLMBase() -> str:
        _l = _LLM_Parameneter_Folders
        return str(_l._InternetLLMBase.eval())

    @set_all_par
    @staticmethod
    def NetworkAddress() -> str:
        _l = _LLM_Parameneter_Folders
        return str(_l._NetworkAddress.eval())

    @set_all_par
    @staticmethod
    def Port() -> int:
        _l = _LLM_Parameneter_Folders
        return int(_l._Port.eval())

    @set_all_par
    @staticmethod
    def Connected() -> bool:
        _l = _LLM_Parameneter_Folders
        return bool(_l._Connected.eval())

    @set_all_par
    @staticmethod
    def ServerLaunched() -> bool:
        _l = _LLM_Parameneter_Folders
        return bool(_l._Connected.eval())

    @set_all_par
    @staticmethod
    def ServerFile() -> str:
        _l = _LLM_Parameneter_Folders
        return str(_l._Serverfile.eval())

    @set_all_par
    @staticmethod
    def set_Connected(value : bool = False) -> None:
        _l = _LLM_Parameneter_Folders
        _l._Connected.val = bool(value)

    @set_all_par
    @staticmethod
    def set_ServerLaunched(value : bool = False) -> None:
        _l = _LLM_Parameneter_Folders
        _l._ServerLaunched.val = bool(value)

    @set_all_par
    @staticmethod
    def AllActivationLLMStatus() -> dict[_LLM_Type,bool]:
        _l = _LLM_Parameneter_Folders
        return {
            _LLM_Type.local : bool(_l._ActivateLocalLlm.eval()),
            _LLM_Type.server : bool(_l._ActivateServerLlm.eval()),
            _LLM_Type.internet : bool(_l._ActivateInternetLlm.eval()),
        }


