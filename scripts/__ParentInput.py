from typing import Callable
from __WebServer import _WebServer
from __QR import QRCode
import webbrowser

class _OnPulseStr:
    _OpenServer : str = "Openserver"
    _Restart : str = "Restart"
    _CreateQR : str = "Create"
    _InstallLibs : str = "Downloadpythonlibs"
    _Help : str = "Help"

class _OnPulseConfig:
    _FunctionDict: dict[str, Callable] | None = None

    @staticmethod
    def _define_dict(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            if(_OnPulseConfig._FunctionDict): return _f(*args, **kwargs)
            _OnPulseConfig._FunctionDict = {}
            _d: dict[str, Callable] = _OnPulseConfig._FunctionDict
            _p = _OnPulseStr

            def OpenServer(par) -> None:
                webbrowser.open(_WebServer.get_server_location())

            def Restart(par) -> None:
                _WebServer.restart()
                if(_ParentInput.AutoUpdate()):
                    QRCode.generate_server_url()

            def CreateQR(par) -> None:
                QRCode.generate_server_url()

            def InstallLibs(par) -> None:
                QRCode.download_libs()

            def Help(par) -> None:
                webbrowser.open("https://github.com/Bambaleiio/Installation-Coursework/blob/web-site-input/README.md")

            _d[_p._CreateQR] = CreateQR
            _d[_p._OpenServer] = OpenServer
            _d[_p._Restart] = Restart
            _d[_p._InstallLibs] = InstallLibs
            _d[_p._Help] = Help

            return _f(*args, **kwargs)
        return _w

    @_define_dict
    @staticmethod
    def call(par) -> None:
        _function : Callable | None = _OnPulseConfig._FunctionDict.get(par.name)
        if(_function): _function(par)

class _OnChangeStr:
    _Port : str = "Port"
    _Activate : str = "Activate"
    _QRAutoUpdate : str = "Autoupdate"
    _Intergrateddatasender : str = "Intergrateddatasender"

class _OnChangeConfig:
    _FunctionDict : dict[str, Callable] | None = None

    @staticmethod
    def _define_dict(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            if(_OnChangeConfig._FunctionDict): return _f(*args, **kwargs)

            _OnChangeConfig._FunctionDict = {}
            _d: dict[str, Callable] = _OnChangeConfig._FunctionDict
            _c = _OnChangeStr

            def Activate(par, prev) -> None:
                _WebServer.activate(_ParentInput.activate())

            def Port(par, prev) -> None:
                _WebServer.set_port(_ParentInput.get_port())
                if(_ParentInput.AutoUpdate()):
                    QRCode.generate_server_url()

            def DataSerner(par, prev) -> None:
                _WebServer.set_IntegratedSerder(_ParentInput.IntergratedDataSender())

            _d[_c._Intergrateddatasender] = DataSerner
            _d[_c._Port] = Port
            _d[_c._Activate] = Activate

            return _f(*args, **kwargs)
        return _w


    @_define_dict
    @staticmethod
    def call(par, prev) -> None:
        _function : callable | None = _OnChangeConfig._FunctionDict.get(par.name)
        if(_function): _function(par, prev)


class _ParentInput:
    _Parent = None

    _Activate = None
    _Port = None

    _QRAutoUpdate = None
    _Intergrateddatasender = None

    @staticmethod
    def set_all_par(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            _pi = _ParentInput

            if(not _pi._Parent):
                _pi._Parent = parent().par

            if(not _pi._Activate):
                _pi._Activate = _pi._Parent.Activate

            if(not _pi._Port):
                _pi._Port = _pi._Parent.Port

            if(not _pi._QRAutoUpdate):
                _pi._QRAutoUpdate = _pi._Parent.Autoupdate

            if(not _pi._Intergrateddatasender):
                _pi._Intergrateddatasender = _pi._Parent.Intergrateddatasender

            return _f(*args, **kwargs)
        return _w

    @set_all_par
    @staticmethod
    def activate() -> bool:
        return bool(_ParentInput._Activate.eval())

    @set_all_par
    @staticmethod
    def get_port() -> int:
        return int(_ParentInput._Port.eval())

    @set_all_par
    @staticmethod
    def AutoUpdate() -> bool:
        return bool(_ParentInput._QRAutoUpdate.eval())

    @set_all_par
    @staticmethod
    def IntergratedDataSender() -> bool:
        return bool(_ParentInput._Intergrateddatasender.eval())

    @staticmethod
    def on_pulse(par) -> None:
        _OnPulseConfig.call(par)

    @staticmethod
    def on_change(par, prev) -> None:
        _OnChangeConfig.call(par, prev)