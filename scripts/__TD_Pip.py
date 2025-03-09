from typing import Callable

class _TD_PIP:
    _TD_Pip : str = "td_pip"
    _TD_Pip_OP = None

    @staticmethod
    def _set_op(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            if(not _TD_PIP._TD_Pip_OP):
                _TD_PIP._TD_Pip_OP = op(_TD_PIP._TD_Pip)
            return _f(*args, **kwargs)
        return _w

    @_set_op
    @staticmethod
    def import_module(module_name : str):
        return _TD_PIP._TD_Pip_OP.Import_Module(module_name)

    @_set_op
    @staticmethod
    def install_module(module_name : str) -> None:
        _TD_PIP._TD_Pip_OP.InstallPackage(module_name)