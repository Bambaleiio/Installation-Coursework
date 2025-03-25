import os
import sys
import subprocess
from __Display import _Display

class _ServerLibs:
    @staticmethod
    def installed(libs: list[str]) -> dict[str, bool]:
        _verdict: dict[str, bool] = {}
        for lib in libs:
            try:
                __import__(lib)
                _verdict[lib] = True
            except ImportError:
                _verdict[lib] = False
        return _verdict

    @staticmethod
    def installed_all(libs: list[str]) -> bool:
        return all(_ServerLibs.installed(libs).values())

    @staticmethod
    def install(packages: list[str]) -> None:
        try:
            if os.name == 'nt':
                cmd: list[str] = [
                    'cmd.exe', '/k', 'pip', 'install'
                ] + packages

                subprocess.Popen(
                    cmd,
                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
                )
            else:
                install_cmd = f'{sys.executable} -m pip install {" ".join(packages)}; read'
                subprocess.Popen(
                    ['xterm', '-e', 'bash', '-c', install_cmd],
                    start_new_session=True
                )

        except Exception as e:
            _Display.Status(f"Installation failed: {str(e)}")