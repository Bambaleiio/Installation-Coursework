from typing import Callable
from __Input import _Input
import json

class _WebServer:
    _OP = None
    _ServerLocation : str = "http://localhost"
    _OPName : str = "webServer"
    _RequestOutputStr : str = "__RequestData"
    _RequestOutput = None

    @staticmethod
    def _set_op(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            if(not _WebServer._OP):
                _WebServer._OP = op(_WebServer._OPName)
            if(not _WebServer._RequestOutput):
                _WebServer._RequestOutput = op(_WebServer._RequestOutputStr)
            return _f(*args, **kwargs)
        return _w

    @_set_op
    @staticmethod
    def get_server_location() -> str:
        return f"http://localhost:{str(_WebServer._OP.par.port)}/"

    @staticmethod
    def _set_status(response : dict) -> dict:
        response['statusCode'] = 200
        response['statusReason'] = 'OK'
        return response

    @staticmethod
    def _set_HTML(response : dict) -> dict:
        response['data'] = _Input.get_HTML()
        return response

    @_set_op
    @staticmethod
    def _parce_data(request) -> None:
        try:
            data: dict = json.loads(request["data"])
            data = str(data).replace("'", "\"")
            _WebServer._RequestOutput.text = data
        except Exception as e:
            debug(e)

    @staticmethod
    def send_back(response : dict) -> dict:
        _ws = _WebServer
        _r : dict = _ws._set_HTML(response)
        _r = _ws._set_status(_r)
        return response

    @staticmethod
    def on_HTTP_request(webServerDAT, request, response) -> dict:
        _WebServer._parce_data(request)
        return _WebServer.send_back(response)

    @staticmethod
    def server_start(webServerDAT) -> None:
        return

    @staticmethod
    def server_stop(webServerDAT) -> None:
        return

    @_set_op
    @staticmethod
    def restart() -> None:
        _WebServer._OP.par.restart.pulse()

    @_set_op
    @staticmethod
    def activate(value : bool) -> None:
        _WebServer._OP.par.active = bool(value)

    @_set_op
    @staticmethod
    def set_port(port: int) -> None:
        _WebServer._OP.par.port = int(port)