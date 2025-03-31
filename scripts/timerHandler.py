from __BASBlend import _BASBlend

def onDone(timerOp, segment, interrupt) -> None:
	_BASBlend.set_blending(False)
