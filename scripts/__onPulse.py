import webbrowser
from typing import Callable
from GeneralLLM import GeneralLLM
from _LLM_Type import _LLM_Type
from __Server import _Server
from __LLM_Parameneter_Input import _LLM_Parameneter_Input as _lpi


class _onPulseConfig:
    _ParseSingleWord : str = "Parsesingleword"

    _UpdateTable : str = "Updatetable"

    _DownloadPythonLibs : str = "Downloadpythonlibs"
    _DownloadServerPythonLibs : str = "Downloadserverpythonlibs"
    _DownloadInternetPythonLibs : str = "Downloadpythoninternet"

    _StartServer : str = "Startserver"
    _ConnectServer : str = "Connectserver"
    _TeminateServer : str = "Teminateserver"

    _ActivateLocalLlm : str = "Activatelocalllm"
    _ActivateServerLlm : str = "Activateserverlllm"
    _ActivateInternetLlm : str = "Activateinternetllm"

    _ReadMe : str = "Readme"


class _onPulse:
    _FunctionDict : dict[str, Callable] | None = None

    @staticmethod
    def _define_dict(_f : Callable) -> None:
        def _w(*args, **kwargs) ->None:
            if(_onPulse._FunctionDict): return _f(*args, **kwargs)

            _onPulse._FunctionDict = {}
            _d: dict[str, Callable] = _onPulse._FunctionDict
            _c = _onPulseConfig

            def _ParseSingleWord(par) -> None:
                GeneralLLM.process_llm_input(str(_lpi.SingleWord()))

            def _UpdateTable(par) -> None:
                GeneralLLM.update_table()

            def _ReadMe(par) -> None:
                github_readme_url : str = "https://github.com/Bambaleiio/Installation-Coursework/blob/main/README.md"
                webbrowser.open(github_readme_url)

            def _DownloadPythonLibs(par) -> None:
                GeneralLLM.install_libs()

            def _StartServer(par) -> None:
                _Server.init_server()

            def _TeminateServer(par) -> None:
                _Server.stop()

            def _ConnectServer(par) -> None:
                GeneralLLM.connect()

            def _LocalLLM(par) -> None:
                GeneralLLM.llm_type(_LLM_Type.local)

            def _ServerLLM(par) -> None:
                GeneralLLM.llm_type(_LLM_Type.server)

            def _InternetLLM(par) -> None:
                GeneralLLM.llm_type(_LLM_Type.internet)

            _d[_c._ParseSingleWord] = _ParseSingleWord

            _d[_c._UpdateTable] = _UpdateTable

            _d[_c._ActivateLocalLlm] = _LocalLLM
            _d[_c._ActivateServerLlm] = _ServerLLM
            _d[_c._ActivateInternetLlm] = _InternetLLM

            _d[_c._DownloadPythonLibs] = _DownloadPythonLibs
            _d[_c._DownloadServerPythonLibs] = _DownloadPythonLibs
            _d[_c._DownloadInternetPythonLibs] = _DownloadPythonLibs

            _d[_c._ConnectServer] = _ConnectServer
            _d[_c._TeminateServer] = _TeminateServer
            _d[_c._StartServer] = _StartServer

            _d[_c._ReadMe] = _ReadMe

            return _f(*args, **kwargs)
        return _w


    @_define_dict
    @staticmethod
    def call(par) -> None:
        _function : Callable | None = _onPulse._FunctionDict.get(par.name)
        if(_function): _function(par)