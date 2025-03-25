from typing import Callable
from __Input import _Input
import json
import re
import subprocess

class _WebServer:
    _OP = None
    _OPName : str = "webServer"

    _localhost : str = "localhost"
    _RequestOutputStr : str = "__RequestData"
    _RequestOutput = None

    _IntegratedSerder : bool = True
    _IntegratedSerderStr : str = "__DataSender"
    _OPIntegratedSerder = None

    _IPConfigIncoding : str = "cp437"

    @staticmethod
    def _set_op(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            if(not _WebServer._OP):
                _WebServer._OP = op(_WebServer._OPName)

            if(not _WebServer._RequestOutput):
                _WebServer._RequestOutput = op(_WebServer._RequestOutputStr)

            if(not _WebServer._OPIntegratedSerder):
                _WebServer._OPIntegratedSerder = op(_WebServer._IntegratedSerderStr)

            return _f(*args, **kwargs)
        return _w

    @staticmethod
    def get_local_ip_address() -> str:
        try:
            output: str = subprocess.check_output('ipconfig', encoding=_WebServer._IPConfigIncoding)
        except subprocess.CalledProcessError:
            return _WebServer._localhost

        ip_pattern: re.Pattern[str] = re.compile(
            r'IPv4[^:]*:[^\d]*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
            re.IGNORECASE
        )
        ips: list[str] = ip_pattern.findall(output)

        filtered_ips: list[str] = [
            ip for ip in ips
            if not ip.startswith('127.') and not ip.startswith('169.254.')
        ]

        return filtered_ips[0] if filtered_ips else _WebServer._localhost

    @_set_op
    @staticmethod
    def get_server_location() -> str:
        return f"http://{str(_WebServer.get_local_ip_address())}:{str(_WebServer._OP.par.port)}/"

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
            _WebServer._RequestOutput.text = "{}"

    @_set_op
    @staticmethod
    def _set_sender(response: dict) -> dict:
        if(not _WebServer._IntegratedSerder): return response
        try:
            inject_content = str(_WebServer._OPIntegratedSerder.text)
            body_close_pattern = re.compile(r'<\/body\s*>', re.IGNORECASE)

            if body_close_pattern.search(response["data"]):
                response["data"] = body_close_pattern.sub(f"\n{inject_content}\n</body>", response["data"])
            else:
                response["data"] += f"\n{inject_content}\n</body></html>"
        except Exception as e:
            response["data"] += "\n<!-- Inegrated Data Sender: Injection Error -->"

        return response


    @staticmethod
    def send_back(response : dict) -> dict:
        _ws = _WebServer
        _r : dict = _ws._set_HTML(response)
        _r = _ws._set_status(_r)
        _r = _ws._set_sender(_r)
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

    @staticmethod
    def set_IntegratedSerder(value : bool) -> None:
        _WebServer._IntegratedSerder = bool(value)

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