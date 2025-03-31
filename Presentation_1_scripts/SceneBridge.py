from typing import Callable

class _SceneBridgeConfig:
	_BackroundAudioSwitcher : str = "BackroundAudioSwitcher"
	_Instalation : str = "Instalation"

class _SceneBridge:
	_OPInstalation = None
	_OPBackroundAudioSwitcher = None

	@staticmethod
	def _set_op(_f : Callable) -> None:
		def _w(*args, **kwargs) -> None:

			if(not _SceneBridge._OPBackroundAudioSwitcher):
				_SceneBridge._OPBackroundAudioSwitcher = op(_SceneBridgeConfig._BackroundAudioSwitcher)

			if(not _SceneBridge._OPInstalation):
				_SceneBridge._OPInstalation = op(_SceneBridgeConfig._Instalation)

			return _f(*args, **kwargs)
		return _w

	@_set_op
	@staticmethod
	def set_music(text : str) -> None:
		_SceneBridge._OPBackroundAudioSwitcher.par.Audiofilename = str(text)
		_SceneBridge._OPInstalation.par.Inputword = str(text)

def onTableChange(dat) -> None:
	_text : str = dat.text
	_SceneBridge.set_music(_text)

