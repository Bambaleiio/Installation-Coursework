import os
import signal
import subprocess
from typing import Callable
from __Output import _Output
from __Display import _Display
from __LLM_Parameneter_Folders import _LLM_Parameneter_Folders as _lpf

class _Server:
    _tcpipConnection: str = "__tcpipConnection"
    _tcpipOP = None

    _NetworkAddress : str = "localhost"
    _Port : int = 8686

    _process = None

    @staticmethod
    def _set_op(_f: Callable) -> None:
        def _w(*args, **kwargs) -> None:
            if not _Server._tcpipOP:
                _Server._tcpipOP = op(_Server._tcpipConnection)
            return _f(*args, **kwargs)
        return _w

    @staticmethod
    def _set_parameters(_f: Callable) -> None:
        def _w(*args, **kwargs) -> None:
            _Server._tcpipOP.par.port = _lpf.Port()
            _Server._tcpipOP.par.address = _lpf.NetworkAddress()
            return _f(*args, **kwargs)
        return _w

    @_set_op
    @staticmethod
    def init_server() -> None:
        if not _lpf.ServerLaunched():
            host : str = _lpf.NetworkAddress()
            port : int = _lpf.Port()
            script_path : str = os.path.join(project.folder, _lpf.ServerFile())

            if os.name == 'nt':
                _Server._process = subprocess.Popen(
                    ['cmd.exe', '/k', 'python', script_path, host, str(port)],
                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
                )
            else:
                _Server._process = subprocess.Popen(
                    ['xterm', '-e', 'python', script_path, host, str(port), ';', 'read'],
                    start_new_session=True
                )

            _lpf.set_ServerLaunched(True)
            _Display.Status(f"Server started on {host}:{port}")

    @_set_op
    @_set_parameters
    @staticmethod
    def send(message: str) -> None:
        if(_lpf.Connected()):
            _Server._tcpipOP.send(message, terminator='\r\n')

    @_set_op
    @_set_parameters
    @staticmethod
    def connect() -> None:
        _sop = _Server._tcpipOP.par

        _sop.port = _Server._Port
        _sop.address  = _Server._NetworkAddress
        _sop.active = True

    @_set_op
    @_set_parameters
    @staticmethod
    def stop() -> None:
        if not _Server.is_launched():
            try:
                if _Server._process.poll() is None:
                    if os.name == 'nt':
                        try:
                            _Server._process.send_signal(signal.CTRL_BREAK_EVENT)
                        except AttributeError:
                            _Server._process.terminate()
                    else:
                        try:
                            pgid = os.getpgid(_Server._process.pid)
                            os.killpg(pgid, signal.SIGTERM)
                        except ProcessLookupError:
                            _Display.Status("Process group already terminated")
                            return
                        except Exception as e:
                            _Display.Status(f"Unix termination error: {str(e)}")
                            return

                    try:
                        _Server._process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        _Display.Status("Force killing server process")
                        _Server._process.kill()
                        _Server._process.wait()

                _Display.Status("Server stopped")
            except ProcessLookupError:
                _Display.Status("Process already terminated")
            except Exception as e:
                _Display.Status(f"Termination error: {str(e)}")
            finally:
                _Server._process = None

        _lpf.set_ServerLaunched(False)
        _sop = _Server._tcpipOP.par
        _sop.active = False

    @staticmethod
    def is_launched() -> bool:
        return not _Server._process or _Server._process.poll() is not None

    @staticmethod
    def onConnect(dat, peer) -> None:
        _lpf.set_Connected(True)

    @staticmethod
    def onClose(dat, peer) -> None:
        _lpf.set_Connected(False)
        _lpf.set_ServerLaunched(False)

        _sop = _Server._tcpipOP.par
        _sop.active = False

    @staticmethod
    def onReceive(dat, rowIndex, message, byteData, peer) -> None:

        try:
            _Output.export_emote(message)
        except Exception as e:
            _Display.Status(f"Processing error: {str(e)}")
        #_Server._tcpipOP.clear()
