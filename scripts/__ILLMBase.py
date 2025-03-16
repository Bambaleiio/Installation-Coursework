from typing import NoReturn


class _ILLMBase:

    def _setup() -> NoReturn:
        raise NotImplemented

    def proccess_word(word : str) -> NoReturn:
        raise NotImplemented

    def all_emotes() -> NoReturn:
        raise NotImplemented