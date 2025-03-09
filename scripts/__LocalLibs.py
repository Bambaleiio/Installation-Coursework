from __TD_Pip import _TD_PIP

class _LocalLibs:
    @staticmethod
    def installed(libs : list[str]) -> dict[str,bool]:
        _verdict : dict[str, bool] = {}
        for _lib in libs:
            if(not _TD_PIP.import_module(_lib)):
                _verdict[_lib] = False
            else:
                _verdict[_lib] = True
        return _verdict

    @staticmethod
    def installed_all(libs : list[str]) -> bool:
        return any(_LocalLibs.installed(libs).values())

    @staticmethod
    def install(libs : list[str]) -> None:
        _verdict : dict[str, bool] = _LocalLibs.installed(libs)
        for _lib, _status in _verdict.items():
            if(_status):
                _TD_PIP.install_module(_lib)