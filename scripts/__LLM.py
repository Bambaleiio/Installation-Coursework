from __Display import _Display
from __TD_Pip import _TD_PIP

class _LLM_CONFIG:
    _Task : str = "text-classification"
    _LLM_Model : str = "transformers"
    _ModelName: str = "bhadresh-savani/distilbert-base-uncased-emotion"
    _Tokenizer : str = "bhadresh-savani/distilbert-base-uncased-emotion"

    @staticmethod
    def pipeline():
        try:
            _pipeline = _TD_PIP.import_module(_LLM_CONFIG._LLM_Model).pipeline
            return _pipeline(
                _LLM_CONFIG._Task,
                model=_LLM_CONFIG._ModelName,
                tokenizer=_LLM_CONFIG._Tokenizer,
                return_all_scores=True
            )
        except Exception as e:
            _Display.Status(e)

        return None

class _LLM:
    _Pipline = None

    @staticmethod
    def _set_pipeline(_f) -> None:
        def _w(*args, **kwargs) -> None:
            if(not _LLM._Pipline):
                _LLM._Pipline = _LLM_CONFIG.pipeline()
            return _f(*args, **kwargs)
        return _w

    @_set_pipeline
    @staticmethod
    def proccess_word(word : str) -> str:
        try:
            _response = _LLM._Pipline(word)
            _emotions = { pred['label']: pred['score'] for pred in _response[0] }
            _main_emotion = max(_emotions, key=_emotions.get)
            return _main_emotion
        except Exception as e:
            _Display.Status(e)
