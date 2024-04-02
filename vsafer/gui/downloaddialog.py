import os
import subprocess
from typing import Optional

from PyQt5.QtCore import (
    Qt,
    pyqtSlot,
    QSaveFile,
    QIODevice,
    QUrl,
    QDir,
    QCoreApplication,
    QFile,
)
from PyQt5.QtWidgets import (
    QDialog,
    QProgressBar,
    QVBoxLayout,
    QDialogButtonBox,
    QAbstractButton,
    QFileDialog,
    QMessageBox,
)
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest


class DownloadDialog(QDialog):
    def __init__(self) -> None:
        super(DownloadDialog, self).__init__()

        self.manager = QNetworkAccessManager(self)
        self.progress_bar = QProgressBar()

        self.setWindowTitle("다운로드")
        self.setWindowFlags(
            self.windowFlags() & ~Qt.WindowType.WindowContextHelpButtonHint  # type: ignore[arg-type]
        )
        self.setLayout(QVBoxLayout(self))
        self.layout().addWidget(self.progress_bar)

        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Abort)
        self.button_box.clicked.connect(self.__on_button_clicked)
        self.layout().addWidget(self.button_box)

    @pyqtSlot(QAbstractButton)
    def __on_button_clicked(self, button: QAbstractButton) -> None:
        button_role = self.button_box.buttonRole(button)
        if button_role == QDialogButtonBox.ButtonRole.RejectRole:
            self.file.cancelWriting()
            self._die()

    def start_download(self, url: str) -> None:
        savefilename = self.__select_file(url.rsplit("/", 1)[-1])
        if savefilename == "":
            return

        self.file = QSaveFile(savefilename)
        if self.file.open(QIODevice.OpenModeFlag.WriteOnly) == False:
            # TODO: Error handling
            return

        req = QNetworkRequest(QUrl(url))
        req.setAttribute(QNetworkRequest.FollowRedirectsAttribute, True)
        self.reply: Optional[QNetworkReply] = self.manager.get(req)
        self.reply.downloadProgress.connect(self.__on_progress)
        self.reply.finished.connect(self.__on_finished)
        self.reply.readyRead.connect(self.__on_ready_read)
        self.reply.errorOccurred.connect(self.__on_error)
        self.open()

    def __select_file(self, filename: str) -> str:
        default_path = os.path.join(QDir.currentPath(), filename)
        default_path = os.path.splitext(default_path)[0]
        selected_name, _ = QFileDialog.getSaveFileName(
            directory=f"{default_path}", filter="응용 프로그램 (*.exe)"
        )
        return selected_name

    @pyqtSlot("qint64", "qint64")
    def __on_progress(self, bytes_received: int, bytes_total: int) -> None:
        self.progress_bar.setRange(0, bytes_total)
        self.progress_bar.setValue(bytes_received)

    @pyqtSlot()
    def __on_ready_read(self) -> None:
        if self.reply is None:
            return
        self.file.write(self.reply.readAll())

    @pyqtSlot()
    def __on_finished(self) -> None:
        if self.reply is None:
            return
        self.reply.deleteLater()
        if self.file:
            self.file.commit()
            if self.file.error() == QFile.FileError.NoError:
                filename = self.file.fileName()
                self.close()
                subprocess.Popen([filename])
                QCoreApplication.quit()
        self.close()

    @pyqtSlot(QNetworkReply.NetworkError)
    def __on_error(self, error: QNetworkReply.NetworkError) -> None:
        if self.reply is None:
            return
        if error == QNetworkReply.NetworkError.OperationCanceledError:
            return
        text = (
            f"<p>서버에서 파일을 내려받던 중 오류가 발생했습니다.<br /><br />{self.reply.errorString()}</p>"
        )
        msgbox = QMessageBox(QMessageBox.Icon.Warning, "네트워크 오류", text)
        msgbox.exec()
        self._die()

    def _die(self):
        if self.reply is None:
            return
        self.reply.downloadProgress.disconnect()
        self.reply.finished.disconnect()
        self.reply.readyRead.disconnect()
        self.file.cancelWriting()
        self.file.commit()
        self.reply.abort()
        self.reply.deleteLater()
        self.reply = None
        self.close()
