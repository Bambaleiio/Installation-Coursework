from typing import Callable
from __ILLMBase import _ILLMBase
from __Display import _Display
from __LLM_Parameneter_Folders import _LLM_Parameneter_Folders as _lpf

class _YandexGPT(_ILLMBase):
    _sdk = None
    _model = None

    _TextClassifier : str = "yandexgpt"

    _AllEmotes : list[str] = [
        "neutral",
        "fear",
        "anger",
        "calm",
        "sadness",
        "joy"
    ]

    @staticmethod
    def _setup(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:
            if(_YandexGPT._sdk and _YandexGPT._model): return _f(*args, **kwargs)

            try:
                from yandex_cloud_ml_sdk import YCloudML
                _YandexGPT._sdk = YCloudML(
                    folder_id=_lpf.get_folder_id(),
                    auth=_lpf.get_auth()
                )

                _YandexGPT._model = _YandexGPT._sdk.models.text_classifiers(_YandexGPT._TextClassifier).configure(
                    task_description="определи эмоцию текста",
                    labels=_YandexGPT._AllEmotes
                )
            except Exception as e:
                print(e)

            return _f(*args, **kwargs)
        return _w

    @_setup
    @staticmethod
    def proccess_word(word : str) -> str:
        _result = _YandexGPT._model.run(word)
        emotion, highestConfidence = max(
            ((prediction.label, prediction.confidence) for prediction in _result),
            key=lambda x: x[1],
            default=(None, -1)
        )

        return emotion

    @staticmethod
    def all_emotes() -> list[str]:
        return _YandexGPT._AllEmotes

class _ILLMInfo:
    _cls : None
    _Libs : list[str]
    _Packages : list[str]

    def __init__(self, cls, libs : list[str], packages : list[str]) -> None:
        self._Libs = libs
        self._Packages = packages
        self._cls = cls

    def cls(self):
        return self._cls

    def libs(self) -> list[str]:
        return self._Libs

    def packages(self) ->list[str]:
        return self._Packages

class _LLMInfoConfig:
    _LLMinfo : dict[str,_ILLMInfo] = {
        "YandexGPT" : _ILLMInfo(
            _YandexGPT,
            [
                "yandex-cloud-ml-sdk"
            ],
            [
                "YCloudML"
            ]
        )
    }

class _ILLM:
    _ImplementationName : str = None
    _Implementation : _ILLMBase | None = None

    @staticmethod
    def setLLMBase(llmName : str) ->None:
        if(_ILLM._ImplementationName == llmName): return

        _info: _ILLMInfo | None = _LLMInfoConfig._LLMinfo.get(llmName, None)
        if(not _info.cls()): raise NameError
        _ILLM._Implementation = _info.cls()
        _ILLM._ImplementationName = llmName

    @staticmethod
    def _cur_llm_base(_f : Callable):
        def _w(*args, **kwargs) -> None:
            _ILLM.setLLMBase(_lpf.InternetLLMBase())
            return _f(*args, **kwargs)
        return _w

    @_cur_llm_base
    @staticmethod
    def proccess_word(word : str) -> str:
        try:
            return _ILLM._Implementation.proccess_word(word)
        except Exception as e:
            _Display.Status(e)

    @_cur_llm_base
    @staticmethod
    def all_emotes() -> list[str]:
        return _ILLM._Implementation.all_emotes()

    @_cur_llm_base
    @staticmethod
    def libs() -> list[str]:
        _info : _ILLMInfo = _LLMInfoConfig._LLMinfo.get(_ILLM._ImplementationName)
        if(not _info): return []
        return _info.libs()

    @_cur_llm_base
    @staticmethod
    def packages() -> list[str]:
        _info : _ILLMInfo = _LLMInfoConfig._LLMinfo.get(_ILLM._ImplementationName)
        if(not _info): return []
        return _info.packages()