import tempfile
from pathlib import Path
from __WebServer import _WebServer
from __TD_Pip import _TD_PIP


class QRCode:
    _OP = None
    _Libs : list[str] = [
        "pillow",
        "qrcode"
    ]
    _QRLib : str = "qrcode"
    _OPName: str = "QROut"
    _TempPath: Path = Path(tempfile.gettempdir()) / "WebServerInputQRcode.png"

    @staticmethod
    def _set_op(func: callable) -> callable:
        def wrapper(*args, **kwargs):
            if not QRCode._OP:
                QRCode._OP = op(QRCode._OPName)
            return func(*args, **kwargs)
        return wrapper

    @_set_op
    @staticmethod
    def _generate_qr(data: str) -> None:
        try:
            _qrcode = _TD_PIP.import_module(QRCode._QRLib)
            qr = _qrcode.QRCode(
                version=1,
                error_correction=_qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            img= qr.make_image(fill_color="black", back_color="white")
            img.save(QRCode._TempPath)

            QRCode._OP.par.file = str(QRCode._TempPath)
            QRCode._OP.par.reload.pulse()
        except Exception as e:
            print(e)

    @_set_op
    @staticmethod
    def generate(data: str) -> None:
        QRCode._generate_qr(data)

    @_set_op
    @staticmethod
    def generate_server_url() -> None:
        url: str = _WebServer.get_server_location()
        QRCode._generate_qr(url)

    @_set_op
    @staticmethod
    def download_libs() -> None:
        for lib in QRCode._Libs:
            _TD_PIP.install_module(lib)

    @_set_op
    @staticmethod
    def delete_qr() -> None:
        try:
            if QRCode._TempPath.exists():
                QRCode._TempPath.unlink()

            QRCode._OP.par.file = ""
            QRCode._OP.par.reload.pulse()
        except Exception as e:
            print(e)