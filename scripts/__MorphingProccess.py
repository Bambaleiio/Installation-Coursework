from typing import Callable


class _MorphingConfig:
	_Timer : str = "timer"

class _Morphing:
	_go_up : list = []
	_go_down : list = []
	_OPTimer = None

	@staticmethod
	def _set_op(_f : Callable) -> None:
		def _w(*args, **kwargs) -> None:

			if(not _Morphing._OPTimer):
				_Morphing._OPTimer = op(_MorphingConfig._Timer)

			return _f(*args, **kwargs)
		return _w

	@_set_op
	@staticmethod
	def start(seconds : float) -> None:
		_Morphing._OPTimer.par.length = float(seconds)
		_Morphing._OPTimer.par.initialize.pulse()
		_Morphing._OPTimer.par.start.pulse()

	@staticmethod
	def set_go(go_up : list, go_down : list) -> None:
		_Morphing._go_up = go_up
		_Morphing._go_down = go_down

	@_set_op
	@staticmethod
	def on_cook()-> None:
		_cur_fraction: list[str] = float(_Morphing._OPTimer['timer_fraction'])
		for op in _Morphing._go_up:
			op.par.volume = _cur_fraction
		for op in _Morphing._go_down:
			op.par.volume = 1 - _cur_fraction if op.par.volume != 0 else 0
