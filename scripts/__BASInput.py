from typing import Callable

class _BASInputConfig:
    _AudioKeys : str = "basename"
    _AudioPaths : str = "path"
    _audioFolder : str = "audioFolder"

class _BASInput:
    _OPAudioFolder = None

    @staticmethod
    def _set_op(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:

            if(not _BASInput._OPAudioFolder):
                _BASInput._OPAudioFolder = op(_BASInputConfig._audioFolder)

            return _f(*args, **kwargs)
        return _w

    @_set_op
    @staticmethod
    def get_table_info() -> dict[str,str]:
        h: list = [c.val for c in _BASInput._OPAudioFolder.row(0)]
        bn, p = h.index('basename'), h.index('path')
        result: dict = {r[bn].val: r[p].val for r in _BASInput._OPAudioFolder.rows()[1:] if max(bn, p) < len(r)}
        return result