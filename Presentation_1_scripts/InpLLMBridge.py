from typing import Callable

class _Bridge:
	_ColName : str = "phrase"
	_DefaultWord : str = "Stone"
	_OPLLMHandlerStr : str = "LLMHandler"
	_OPLLMHandler = None

	def _set_op(_f: Callable) -> None:
		def _w(*args, **kwargs) -> None:
			if(not _Bridge._OPLLMHandler):
				_Bridge._OPLLMHandler = op(_Bridge._OPLLMHandlerStr)
			return _f(*args, **kwargs)
		return _w

	@_set_op
	@staticmethod
	def on_row_change(dat, rows : list[int]) -> None:
		if not rows:
			_Bridge.single_word(_Bridge._DefaultWord)
			return

		if(dat[0,0] == _Bridge._ColName):
			word : str = dat[rows[0], 0]
			_Bridge.single_word(word)

	@staticmethod
	def single_word(word: str) -> None:
		_Bridge._OPLLMHandler.par.Singleword = str(word)


def onTableChange(dat):
	return

def onRowChange(dat, rows) -> None:
	_Bridge.on_row_change(dat, rows)

def onColChange(dat, cols):
	return

def onCellChange(dat, cells, prev):
	return

def onSizeChange(dat):
	return