from _LLM_Type import _LLM_Type

class _Display:
    _TextTrim : int = 20
    _LibStatus : str = "LibStatus"
    _LLMType : str = "LLMType"

    _LibStatusOP = None
    _LLMTypeOP = None

    @staticmethod
    def _set_op(_f) -> None:
        def _w(*args, **kwargs) -> None:
            if(not _Display._LibStatusOP):
                _Display._LibStatusOP = op(_Display._LibStatus)

            if(not _Display._LLMTypeOP):
                _Display._LLMTypeOP = op(_Display._LLMType)

            return _f(*args, **kwargs)
        return _w

    @_set_op
    @staticmethod
    def Status(message : str = "")->None:
        _Display._LibStatusOP.text = message

    @_set_op
    @staticmethod
    def llm_type(type : _LLM_Type) -> None:
        if(type == _LLM_Type.local):
            _Display._LLMTypeOP.par.Widgetlabel = "Local"
            return

        if(type == _LLM_Type.server):
            _Display._LLMTypeOP.par.Widgetlabel = "Server"
            return

        if(type == _LLM_Type.internet):
            _Display._LLMTypeOP.par.Widgetlabel = "Internet"
            return




