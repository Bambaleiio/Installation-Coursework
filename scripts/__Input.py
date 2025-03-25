from typing import Callable


class _InputConfig:
    _OpHTMLInput : str = "HTML"

class _Input:
    _HTML : str | None = None

    @staticmethod
    def _init(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:

            if(not _Input._HTML):
                try:
                    _Input._HTML = op(_InputConfig._OpHTMLInput)
                except Exception as e:
                    print(e)

            return _f(*args, **kwargs)
        return _w

    @_init
    @staticmethod
    def get_HTML() -> str:
        return _Input._HTML.text