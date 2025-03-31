from typing import Callable
from __CookingHandler import _CookingHandler

class _SceneL:
	_present_dict: dict[str, str] = {
		"void" : "Preset0",
		"calm" : "Preset1",
		"anger" : "Preset2",
		"fear" : "Preset3",
		"neutral" : "Preset4",
		"sadness" : "Preset5",
		"joy" : "Preset6",
	}
	_Name : str = "PresetManager"
	_OP = None

	@staticmethod
	def _set_op(_f : Callable) -> None:
		def _w(*args, **kwargs) -> None:
			if(not _SceneL._OP):
				_SceneL._OP = op(_SceneL._Name)

			return _f(*args, **kwargs)
		return _w

	@_set_op
	@staticmethod
	def set_scene(scene: str) -> None:
		_present : str = _SceneL._present_dict.get(scene, "Preset0")
		_SceneL._OP.par.Target = _present
		_SceneL._OP.par.Morph.pulse()

class _OnChangeStr:
	_Inputword : str = "Inputword"

class _OnChangeConfig:
	_FunctionDict : dict[str, Callable] | None = None

	@staticmethod
	def _define_dict(_f : Callable) -> None:
		def _w(*args, **kwargs) -> None:
			if(_OnChangeConfig._FunctionDict): return _f(*args, **kwargs)
			_OnChangeConfig._FunctionDict = {}
			_d: dict[str, Callable] = _OnChangeConfig._FunctionDict
			_c = _OnChangeStr

			def InputWord(par, prev) -> None:
				_CookingHandler.set_dict({
					"calm" : op("Emote0"),
					"anger" : op("Emote1"),
					"fear" : op("Emote2"),
					"neutral" : op("Emote3"),
					"sadness" : op("Emote4"),
					"joy" : op("Emote5"),
				})
				_CookingHandler.set_uncook(str(par))
				_SceneL.set_scene(str(par))

			_d[_c._Inputword] = InputWord
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
	return

