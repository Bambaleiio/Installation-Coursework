from typing import Callable

class _Output:
    _TextTrim : int = 20

    _LLM_Emote = "LLMEmote"
    _LLM_EmoteOP = None

    _LLM_EmoteTable : str = "LLMEmoteTable"
    _LLM_EmoteTableOP = None

    @staticmethod
    def _set_all_op(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            if(not _Output._LLM_EmoteOP):
                _Output._LLM_EmoteOP = op(_Output._LLM_Emote)

            if(not _Output._LLM_EmoteTableOP):
                _Output._LLM_EmoteTableOP = op(_Output._LLM_EmoteTable)
            return _f(*args, **kwargs)
        return _w

    @_set_all_op
    @staticmethod
    def export_emote(emote : str) -> None:
        _Output._LLM_EmoteOP.text = str(emote)[:_Output._TextTrim]

    @_set_all_op
    @staticmethod
    def possible_emotions(emotes : list[str]) -> None:
        _Output._LLM_EmoteTableOP.setSize(len(emotes), 0)
        for i, emote in enumerate(emotes):
            _Output._LLM_EmoteTableOP.replaceRow(int(i), str(emote)[:_Output._TextTrim])

