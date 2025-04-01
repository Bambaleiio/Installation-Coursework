from typing import Callable
from __BASInput import _BASInput
from __BASBlend import _BASBlend

class _OnPulseStr:
    _Help : str = "Help"

class _OnPulseConfig:
	_FunctionDict: dict[str, Callable] | None = None

	@staticmethod
	def _define_dict(_f : Callable) -> None:
		def _w(*args, **kwargs) -> None:
			if(_OnPulseConfig._FunctionDict): return _f(*args, **kwargs)
			_OnPulseConfig._FunctionDict = {}
			_d: dict[str, Callable] = _OnPulseConfig._FunctionDict
			_p = _OnPulseStr

			def Help(par) -> None:
				print("Not implemented")


			_d[_p._Help] = Help
			return _f(*args, **kwargs)
		return _w

	@_define_dict
	@staticmethod
	def call(par) -> None:
		_function : Callable | None = _OnPulseConfig._FunctionDict.get(par.name)
		if(_function): _function(par)

class _OnChangeStr:
	_AudioFileName : str = "Audiofilename"
	_Blendtime : str = "Blendtime"
	_Repeat : str = "Repeat"

class _OnChangeConfig:
	_FunctionDict : dict[str, Callable] | None = None

	@staticmethod
	def _define_dict(_f : Callable) -> None:
		def _w(*args, **kwargs) -> None:
			if(_OnChangeConfig._FunctionDict): return _f(*args, **kwargs)
			_OnChangeConfig._FunctionDict = {}
			_d: dict[str, Callable] = _OnChangeConfig._FunctionDict
			_c = _OnChangeStr

			def Repeat(par, prev) -> None:
				_BASBlend.set_repeat(bool(par.eval()))

			def AudioFile(par, prev) -> None:
				_BASBlend.blend_to(str(par), _BASInput.get_table_info())

			def BlendTime(par, prev) -> None:
				_BASBlend.set_blend_time(float(par))

			_d[_c._Blendtime] = BlendTime
			_d[_c._AudioFileName] = AudioFile
			_d[_c._Repeat] = Repeat
			return _f(*args, **kwargs)
		return _w

	@_define_dict
	@staticmethod
	def call(par, prev) -> None:
		_function : callable | None = _OnChangeConfig._FunctionDict.get(par.name)
		if(_function): _function(par, prev)

def onValueChange(par, prev) -> None:
	_OnChangeConfig.call(par,prev)
	return

def onPulse(par) -> None:
	_OnPulseConfig.call(par)
	return


