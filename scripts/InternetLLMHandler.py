from __ILLM import _ILLM
from __InternetLibs import _InternetLibs
from __Output import _Output

class InternetLLMHandler:

    @staticmethod
    def process_llm_input(input : str) -> None:
        _word : str = _ILLM.proccess_word(input)
        _Output.export_emote(_word)

    @staticmethod
    def install_libs() -> None:
        _libs : list[str] = _ILLM.libs()
        _Packages : list[str] = _ILLM.packages()
        if(not _InternetLibs.installed_all(_libs)):
            _InternetLibs.install(_Packages)

    @staticmethod
    def get_possible_emotions() -> None:
        _Output.possible_emotions(_ILLM.all_emotes())