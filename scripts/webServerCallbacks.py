from __WebServer import _WebServer

def onHTTPRequest(webServerDAT, request, response) -> dict:
	return _WebServer.on_HTTP_request(webServerDAT, request, response)

def onWebSocketOpen(webServerDAT, client, uri) -> None:
	return

def onWebSocketClose(webServerDAT, client) -> None:

	return

def onWebSocketReceiveText(webServerDAT, client, data) -> None:
	webServerDAT.webSocketSendText(client, data)
	return

def onWebSocketReceiveBinary(webServerDAT, client, data) -> None:
	webServerDAT.webSocketSendBinary(client, data)
	return

def onWebSocketReceivePing(webServerDAT, client, data) -> None:
	webServerDAT.webSocketSendPong(client, data=data);
	return

def onWebSocketReceivePong(webServerDAT, client, data) -> None:
	return

def onServerStart(webServerDAT) -> None:
	_WebServer.server_start(webServerDAT)

def onServerStop(webServerDAT) -> None:
	_WebServer.server_stop(webServerDAT)
