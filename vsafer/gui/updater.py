from distutils.version import StrictVersion
from typing import Optional, cast

from PyQt5.QtCore import QObject, QUrl, pyqtSlot
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

from vsafer.__version__ import __version__
from vsafer.utils import python_bits
from vsafer.gui.downloaddialog import DownloadDialog

BASE_URL = "https://raw.githubusercontent.com/VSafer/vsafer/master/update/"


class Updater(QObject):
    def __init__(self) -> None:
        super(Updater, self).__init__()

        self.download_dialog = DownloadDialog()
        self.manager = QNetworkAccessManager(self)

    def start_update(self) -> None:
        result = self.__allow_network_messagebox()
        if result == QMessageBox.StandardButton.Cancel:
            return
        self.__fetch_latest_version()

    def __fetch_latest_version(self) -> None:
        self.reply: Optional[QNetworkReply] = self.manager.get(
            QNetworkRequest(QUrl(f"{BASE_URL}latest/version"))
        )
        self.reply.finished.connect(self.__on_fetch_latest_version_finished)
        self.reply.errorOccurred.connect(self.__on_error)

    @pyqtSlot()
    def __on_fetch_latest_version_finished(self) -> None:
        if self.reply is None:
            return

        resp = self.reply.readAll().data().decode()
        if resp == "":
            return
        # Remove possible newline before EOF
        if resp[-1] == "\n":
            resp = resp[:-1]
        latest_version = StrictVersion(resp)
        self.reply.deleteLater()
        current_version = StrictVersion(__version__)

        if latest_version > current_version:
            self.__check_release()
        else:
            self.__already_latest_messagebox()

    def __already_latest_messagebox(self) -> None:
        msgbox = QMessageBox()
        msgbox.setWindowTitle("업데이트")
        text = """
            <p>이미 최신 버전입니다.</p>
        """
        msgbox.setText(text)
        msgbox.exec()

    def __check_release(self) -> None:
        if python_bits() == "64bit":
            endpoint = "latest/windows/64bit"
        elif python_bits() == "32bit":
            endpoint = "latest/windows/32bit"
        self.reply = self.manager.get(QNetworkRequest(QUrl(f"{BASE_URL}{endpoint}")))
        self.reply.finished.connect(self.__on_check_release_finished)
        self.reply.errorOccurred.connect(self.__on_error)

    @pyqtSlot()
    def __on_check_release_finished(self) -> None:
        if self.reply is None:
            return

        url = self.reply.readAll().data().decode()
        self.reply.deleteLater()
        # Remove possible newline before EOF
        if url[-1] == "\n":
            url = url[:-1]
        self.__download_to_path(url)

    @pyqtSlot(QNetworkReply.NetworkError)
    def __on_error(self, _) -> None:
        if self.reply is None:
            return

        text = (
            f"<p>GitHub 서버와 통신 중 오류가 발생했습니다.<br /><br />{self.reply.errorString()}</p>"
        )
        msgbox = QMessageBox(QMessageBox.Icon.Warning, "네트워크 오류", text)
        msgbox.exec()

        self.reply.finished.disconnect()
        self.reply.deleteLater()
        self.reply = None

    def __download_to_path(self, url) -> None:
        self.download_dialog.start_download(url)

    def __allow_network_messagebox(self) -> QMessageBox.StandardButton:
        text = """
            <p>업데이트를 위해 GitHub 서버와 통신을 시도합니다.<br />
            인터랩 홈페이지에서 직접 최신 버전을 내려받으실 수 있습니다.</p>
        """
        buttons = QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        msgbox = QMessageBox(QMessageBox.Icon.Information, "업데이트", text, buttons)
        msgbox.exec()
        return cast(QMessageBox.StandardButton, msgbox.result())
