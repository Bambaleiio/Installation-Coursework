from typing import Callable
class _LLM_Parameneter_Input:
    _Parent = None
    _SingleWord = None

    @staticmethod
    def set_all_par(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            _l = _LLM_Parameneter_Input
            if(not _l._Parent):
                _l._Parent = parent().par

            if(not _l._SingleWord):
                _l._SingleWord = _l._Parent.Singleword

            return _f(*args, **kwargs)
        return _w

    @set_all_par
    @staticmethod
    def SingleWord() -> str:
        _l = _LLM_Parameneter_Input
        return _l._SingleWord.eval()
