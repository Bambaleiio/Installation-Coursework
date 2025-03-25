from typing import Callable

class _LLM_Parameneter_Options:
    _Parent = None
    _AutoLLM_Parsing = None
    _ParseSingleWord = None
    _UpdateTable = None

    @staticmethod
    def set_all_par(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            _l = _LLM_Parameneter_Options
            if(not _l._Parent):
                _l._Parent = parent().par

            if(not _l._AutoLLM_Parsing):
                _l._AutoLLM_Parsing = _l._Parent.Autollmparsing

            if(not _l._ParseSingleWord):
                _l._ParseSingleWord = _l._Parent.Parsesingleword

            if(not _l._UpdateTable):
                _l._UpdateTable = _l._Parent.Updatetable
            return _f(*args, **kwargs)
        return _w

    @set_all_par
    @staticmethod
    def AutoLLMParsing() -> bool:
        _l = _LLM_Parameneter_Options
        return bool(_l._AutoLLM_Parsing.eval())
