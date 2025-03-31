from typing import Callable
from enum import Enum
from __MorphingProccess import _Morphing

class _AudioCur(Enum):
    default = 0
    audio1 = 1
    audio2 = 2

class _BASBlendConfig:
    _defaultBuffer : str = "d"
    _audioBuffer1 : str = "a1"
    _audioBuffer2 : str = "a2"

class _BASBlend:
    _AudioCurVolume : _AudioCur | None = None
    _OPdefaultBuffer = None
    _OPaudioBuffer1 = None
    _OPaudioBuffer2 = None

    _BlendTime : float = float(parent().par.Blendtime.eval())
    _IsBlending : bool = False

    @staticmethod
    def _set_audio_cur_volume() -> None:
        if(_BASBlend._OPdefaultBuffer.par.volume > 0):
            _BASBlend._AudioCurVolume = _AudioCur.default

        if(_BASBlend._OPaudioBuffer1.par.volume > 0):
            _BASBlend._AudioCurVolume = _AudioCur.audio1

        if(_BASBlend._OPaudioBuffer2.par.volume > 0):
            _BASBlend._AudioCurVolume = _AudioCur.audio2

    @staticmethod
    def _set_op(_f : Callable) -> None:
        def _w(*args, **kwargs) -> None:

            if(not _BASBlend._OPdefaultBuffer):
                _BASBlend._OPdefaultBuffer = op(_BASBlendConfig._defaultBuffer)

            if(not _BASBlend._OPaudioBuffer1):
                _BASBlend._OPaudioBuffer1 = op(_BASBlendConfig._audioBuffer1)

            if(not _BASBlend._OPaudioBuffer2):
                _BASBlend._OPaudioBuffer2 = op(_BASBlendConfig._audioBuffer2)

            _BASBlend._set_audio_cur_volume()

            return _f(*args, **kwargs)
        return _w

    @_set_op
    @staticmethod
    def set_blending(value : bool) -> None:
        _BASBlend._IsBlending = bool(value)
        _BASBlend._set_audio_cur_volume()

    @_set_op
    @staticmethod
    def blend_to_default() -> None:
        _Morphing.set_go(
            [_BASBlend._OPdefaultBuffer],
            [_BASBlend._OPaudioBuffer1, _BASBlend._OPaudioBuffer2]
        )
        _Morphing.start(_BASBlend._BlendTime)

    @_set_op
    @staticmethod
    def blend_to(file_name : str, input_dict : dict[str,str]) -> None:
        if(_BASBlend._IsBlending): return
        _BASBlend._IsBlending = True

        _path : str | None = input_dict.get(file_name)
        if(not _path):
            _BASBlend.blend_to_default()
            return

        _volume1, _volume0 = None, None
        if(_BASBlend._AudioCurVolume == _AudioCur.default or _BASBlend._AudioCurVolume == _AudioCur.audio1):
            _volume1 = _BASBlend._OPaudioBuffer1
            _volume0 = _BASBlend._OPaudioBuffer2
        else:
            _volume1 =  _BASBlend._OPaudioBuffer2
            _volume0 = _BASBlend._OPaudioBuffer1

        _volume0.par.file = str(_path)
        _volume0.par.reloadpulse.pulse()

        _Morphing.set_go(
            [_volume0],
            [_volume1]
        )
        _Morphing.start(_BASBlend._BlendTime)


    @staticmethod
    def set_blend_time(time : float)-> None:
        _BASBlend._BlendTime = float(time)

    @_set_op
    @staticmethod
    def set_repeat(value : bool) -> None:
        _d = _BASBlend._OPdefaultBuffer
        _a1 = _BASBlend._OPaudioBuffer1
        _a2 = _BASBlend._OPaudioBuffer2

        _mode : str = "On" if value else "Off"

        _d.par.repeat = _mode
        _a1.par.repeat = _mode
        _a2.par.repeat = _mode
