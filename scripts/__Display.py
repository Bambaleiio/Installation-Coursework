

class _Display:
    _TextTrim : int = 20
    _LibStatus : str = "LibStatus"
    _LibStatusOP = None

    @staticmethod
    def _set_op(_f) -> None:
        def _w(*args, **kwargs) -> None:
            if(not _Display._LibStatusOP):
                _Display._LibStatusOP = op(_Display._LibStatus)
            return _f(*args, **kwargs)
        return _w

    @_set_op
    @staticmethod
    def Status(message : str = "")->None:
        print(message)
        _Display._LibStatusOP.text = message
