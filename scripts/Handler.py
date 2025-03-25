from __onChange import _onChange
from __onPulse import _onPulse


# TD FUNCTIONS
def onValueChange(par, prev) -> None:
    _onChange.call(par, prev)

def onPulse(par) -> None:
    _onPulse.call(par)
