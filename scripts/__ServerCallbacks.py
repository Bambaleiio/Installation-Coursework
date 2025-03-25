from __Server import _Server

def onConnect(dat, peer) -> None:
	_Server.onConnect(dat, peer)
	return

def onReceive(dat, rowIndex, message, byteData, peer) -> None:
	_Server.onReceive(dat, rowIndex, message, byteData, peer)

def onClose(dat, peer) -> None:
	_Server.onClose(dat, peer)

