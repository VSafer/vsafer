import os
import platform
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt, QLocale, QLibraryInfo, QTranslator
from PyQt5.QtWidgets import QMessageBox, QApplication

import vsafer.gui.utils as guiutils

from vsafer.utils import python_bits
from vsafer.gui.introwindow import IntroWindow
from vsafer.gui.mainwindow import MainWindow


def main(args) -> None:
    QLocale.setDefault(QLocale(QLocale.Language.Korean, QLocale.Country.SouthKorea))
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(args)

    translator = QTranslator()
    translator.load(
        QLocale(),
        "qt",
        "_",
        QLibraryInfo.location(QLibraryInfo.TranslationsPath),
    )
    app.installTranslator(translator)
    translator.load(
        QLocale(),
        "qtbase",
        "_",
        QLibraryInfo.location(QLibraryInfo.TranslationsPath),
    )
    app.installTranslator(translator)

    app.setWindowIcon(QIcon(os.path.join(guiutils.assets_path(), "icon.png")))

    font = app.font()
    font.setFamilies(["Malgun Gothic", "Segoe UI"])
    font.setPointSize(10)
    app.setFont(font)

    wrong_arch_abort()

    introwindow = IntroWindow()
    mainwindow = MainWindow()

    introwindow.scan_button.clicked.connect(mainwindow.show_scan)

    app.exec()


def wrong_arch_abort() -> None:
    if python_bits() == "32bit" and platform.machine() == "AMD64":
        messagebox = QMessageBox(
            QMessageBox.Icon.Information,
            "Vsafer",
            "64비트 버전의 PC에서는 32비트 버전의 프로그램을 실행할 수 없습니다.",
        )
        messagebox.exec()
        sys.exit(1)
