from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QScrollArea,
    QFrame,
    QDialogButtonBox,
)

import vsafer.scan.targets as scantargets


class TargetListDialog(QDialog):
    def __init__(self) -> None:
        super(TargetListDialog, self).__init__()
        self.setFixedSize(400, 300)
        self.setWindowTitle("검사 대상")

        self.setWindowFlags(
            self.windowFlags() & ~Qt.WindowType.WindowContextHelpButtonHint
        )

        self.setLayout(QVBoxLayout(self))
        self.__setup_title_label()
        self.__setup_targetlist()
        self.__setup_buttonbox()

    def __setup_title_label(self) -> None:
        title_label = QLabel()
        title_label.setText("<big>검사 대상 프로그램</big>")
        self.layout().addWidget(title_label)

    def __setup_targetlist(self) -> None:
        self.targetlist_area = QScrollArea()
        self.targetlist_area.setWidgetResizable(True)
        self.targetlist_area.setFrameShape(QFrame.Shape.NoFrame)

        self.targetlist = QLabel()
        self.targetlist.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextBrowserInteraction
        )
        self.targetlist.setOpenExternalLinks(True)

        self.targetlist.setText(self.__stringify_targets())

        self.targetlist_area.setWidget(self.targetlist)
        self.layout().addWidget(self.targetlist_area)

    def __stringify_targets(self) -> str:
        text = "<ul>"

        for target in scantargets.targets:
            text += f"<li>{target.name}"
            for vuln in target.vulnerabilities:
                text += f'<br /><a href="{vuln.source.url}">{vuln.name}</a>'
            text += "</li>"

        text += "</ul>"

        return text

    def __setup_buttonbox(self) -> None:
        self.buttonbox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.buttonbox.clicked.connect(self.close)
        self.layout().addWidget(self.buttonbox)
