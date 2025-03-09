from __LLM import _LLM
from __LocalLibs import _LocalLibs
from __Output import _Output

class _LocalLLMConfig:
    _Packages : list[str] = [
        "transformers",
        "torch torchvision torchaudio"
    ]

    _Libs : list[str] = [
        "transformers",
        "torch",
        "numpy"
    ]

    _AllEmotes : list[str] = [
        'joy',
        'sadness',
        'anger',
        'fear',
        'surprise',
        'disgust',
        'calm',
        'excitement'
    ]

class LocalLLMHandler:

    @staticmethod
    def process_llm_input(input : str) -> None:
        _word : str = _LLM.proccess_word(input)
        _Output.export_emote(_word)

    @staticmethod
    def install_libs() -> None:
        if(not _LocalLibs.installed_all(_LocalLLMConfig._Libs)):
            _LocalLibs.install(_LocalLLMConfig._Packages)

    @staticmethod
    def get_possible_emotions() -> None:
        _Output.possible_emotions(_LocalLLMConfig._AllEmotes)