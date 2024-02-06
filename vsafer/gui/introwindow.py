import os

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

import vsafer.gui.utils as guiutils


class IntroWindow(QWidget):
    def __init__(self) -> None:
        super(IntroWindow, self).__init__()
        self.setObjectName("IntroWindow")
        self.setFixedSize(640, 480)
        self.setWindowTitle("Vsafer")

        self._setup_logo()
        self._setup_description()
        self._setup_scan_button()
        self._setup_footer()
        self.show()

    def _setup_logo(self) -> None:
        self.logo_label = QLabel(self)
        pixmap = QPixmap(os.path.join(guiutils.assets_path(), "icon.png"))
        pixmap = pixmap.scaled(160, 160, Qt.AspectRatioMode.KeepAspectRatio)
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setGeometry(240, 30, 160, 160)

    def _setup_description(self) -> None:
        self.description_label = QLabel(self)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setGeometry(0, 180, 640, 180)

        font = self.description_label.font()
        font.setPointSize(16)
        self.description_label.setFont(font)

        text = """
        <big>Vsafer</big>
        <p>TouchEn nxKey, Veraport V3 등의 뱅킹 프로그램들을 검사해<br />
        설치된 버전에 존재하는 알려진 보안 취약점들을 탐지합니다.</p>
        """
        self.description_label.setText(text)

    def _setup_scan_button(self) -> None:
        self.scan_button = QPushButton("검사", self)

        font = self.scan_button.font()
        font.setPointSize(16)
        self.scan_button.setFont(font)

        self.scan_button.setGeometry(270, 360, 100, 50)

        self.scan_button.clicked.connect(self.close)

    def _setup_footer(self) -> None:
        self.footer_label = QLabel(self)
        self.footer_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.footer_label.setGeometry(0, 440, 640, 40)

        font = self.footer_label.font()
        font.setPointSize(10)
        self.footer_label.setFont(font)

        text = (
            '디지털안전연구소 인터랩 (<a href="https://interlab.or.kr">https://interlab.or.kr</a>)'
        )
        self.footer_label.setText(text)
