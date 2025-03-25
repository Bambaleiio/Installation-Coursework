from __Output import _Output
from __ServerLibs import _ServerLibs
from __Server import _Server

class ServerLLMHandler:
    _Packages: list[str] = [
        "torch",
        "transformers",
        "huggingface_hub",
        "python-dotenv",
        "bitsandbytes"
    ]

    _Libs: list[str] = [
        "torch",
        "transformers",
        "huggingface_hub",
        "bitsandbytes"
    ]

    _AllEmotes: list[str] = [
        "Happy",
        "Sad",
        "Angry",
        "Fearful",
        "Surprised",
        "Neutral"
    ]

    @staticmethod
    def process_llm_input(input : str) -> None:
        _Server.send(input)

    @staticmethod
    def install_libs() -> None:
        if(not _ServerLibs.installed_all(ServerLLMHandler._Libs)):
            _ServerLibs.install(ServerLLMHandler._Packages)

    @staticmethod
    def get_possible_emotions() -> None:
        _Output.possible_emotions(ServerLLMHandler._AllEmotes)

    @staticmethod
    def connect() -> None:
        _Server.connect()

    @staticmethod
    def disconnect() -> None:
        _Server.stop()