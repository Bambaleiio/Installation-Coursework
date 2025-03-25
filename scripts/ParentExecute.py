from __ParentInput import _ParentInput

def onValueChange(par, prev) -> None:
	_ParentInput.on_change(par, prev)

def onPulse(par) -> None:
	_ParentInput.on_pulse(par)

