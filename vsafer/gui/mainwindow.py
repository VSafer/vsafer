import os
import threading

from PyQt5.QtCore import Qt, pyqtSlot, QThread, QVariant
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTreeWidget,
    QSizePolicy,
    QHeaderView,
    QMenuBar,
    QMenu,
    QAction,
    QMessageBox,
    QTreeWidgetItem,
    QLabel,
    QDialogButtonBox,
)

import vsafer.gui.utils as guiutils
import vsafer.scan as scan

from vsafer.gui.targetlistdialog import TargetListDialog
from vsafer.gui.updater import Updater
from vsafer.__version__ import __version__, __date__


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.setMinimumSize(960, 480)
        self.setWindowTitle("VSafer")

        self.targetlistdialog = TargetListDialog()
        self.updatewidget = Updater()
        self.__threads = []

        self.__setup_layout()

        self.__setup_menu_bar()
        self.__setup_tree_widget()
        self.__setup_vuln_buttonbox()

        self.setAttribute(Qt.WA_DontShowOnScreen, True)
        self.show()
        self.layout.invalidate()
        self.hide()
        self.setAttribute(Qt.WA_DontShowOnScreen, False)

    def show_scan(self):
        self.show()
        self.__do_scan()

    def resizeEvent(self, event):
        self.__tree_widget.setColumnWidth(0, self.__central_widget.width() // 3)
        self.__tree_widget.setColumnWidth(1, self.__central_widget.width() // 3)
        super().resizeEvent(event)

    def __setup_layout(self):
        self.__central_widget = QWidget(parent=self)
        self.layout = QVBoxLayout()
        self.__central_widget.setLayout(self.layout)
        self.setCentralWidget(self.__central_widget)

    def __setup_tree_widget(self):
        self.__tree_widget = QTreeWidget(parent=self.__central_widget)
        self.__tree_widget.setColumnCount(5)

        header = self.__tree_widget.header()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        header.resizeSection(1, 300)
        header.resizeSection(2, 300)
        header.resizeSection(4, 10)

        header_item = self.__tree_widget.headerItem()
        header_item.setText(0, "이름")
        header_item.setText(1, "상세")
        header_item.setText(2, "설치된 버전")
        header_item.setText(3, "취약점 해결 버전")
        header_item.setText(4, "")

        self.layout.addWidget(self.__tree_widget)

    def __setup_menu_bar(self):
        self.menubar = QMenuBar()
        self.menubar.setObjectName("menubar")

        self.menu_scan = QMenu(parent=self.menubar)
        self.menu_scan.setObjectName("menu_scan")
        self.menu_scan.setTitle("검사")
        self.menubar.addAction(self.menu_scan.menuAction())

        self.action_scan = QAction("action_scan")
        self.action_scan.setText("다시 검사")
        self.action_scan.triggered.connect(self.__do_scan)
        self.menu_scan.addAction(self.action_scan)

        self.menu_help = QMenu(parent=self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_help.setTitle("도움말")
        self.menubar.addAction(self.menu_help.menuAction())

        self.action_targetlist = QAction("action_targetlist")
        self.action_targetlist.setText("검사 대상")
        self.action_targetlist.triggered.connect(self.targetlistdialog.open)
        self.menu_help.addAction(self.action_targetlist)

        self.action_update = QAction("action_update")
        self.action_update.setText("업데이트")
        self.action_update.triggered.connect(self.updatewidget.start_update)
        self.menu_help.addAction(self.action_update)

        self.action_about = QAction("action_about")
        self.action_about.setText("정보")
        self.action_about.triggered.connect(self.__display_about)
        self.menu_help.addAction(self.action_about)

        self.layout.setMenuBar(self.menubar)

    def __do_scan(self, show_msgbox=True):
        self.__scan_result = scan.scan_all()

        if len(self.__scan_result) == 0 and show_msgbox:
            text = "취약점을 가진 버전의 프로그램이 발견되지 않았습니다."
            messagebox = QMessageBox(
                QMessageBox.Icon.Information, "검사 결과", text, parent=self
            )
            messagebox.exec()

        self.__tree_widget.clear()
        for res in self.__scan_result:
            target_item = QTreeWidgetItem(self.__tree_widget)

            flags = (
                Qt.ItemFlag.ItemIsSelectable
                | Qt.ItemFlag.ItemIsEnabled
                | Qt.ItemFlag.ItemIsUserCheckable
            )
            target_item.setFlags(flags)
            target_item.setCheckState(4, Qt.Unchecked)

            target_item.setText(0, res.target.name)
            target_item.setText(1, res.target.description)
            target_item.setExpanded(True)

            target_item.target = res.target

            for vuln in res.vulns_found:
                vuln_item = QTreeWidgetItem(target_item)
                vuln_item.setText(0, vuln.name)
                url_label = QLabel()
                url_label.setText(f'<a href="{vuln.source.url}">{vuln.source.name}</a>')
                url_label.setTextInteractionFlags(
                    Qt.TextInteractionFlag.TextBrowserInteraction
                )
                url_label.setOpenExternalLinks(True)
                self.__tree_widget.setItemWidget(vuln_item, 1, url_label)
                vuln_item.setText(2, guiutils.version_tostring(res.system_ver))
                vuln_item.setText(3, guiutils.version_tostring(vuln.resolved_version))
                if res.target.uninstaller == None:
                    target_item.setData(4, Qt.CheckStateRole, QVariant())
                    # flags = target_item.flags()
                    # flags &= ~Qt.ItemFlag.ItemIsUserCheckable
                    # target_item.setFlags(flags)
                    # target_item.setDisabled(True)

    def _do_scan_quiet(self):
        self.__do_scan(show_msgbox=False)

    def __setup_vuln_buttonbox(self):
        self.__vuln_buttonbox = QDialogButtonBox()
        rescan = self.__vuln_buttonbox.addButton(
            "다시 검사", QDialogButtonBox.ButtonRole.ActionRole
        )
        rescan.clicked.connect(self.__do_scan)
        quarantine = self.__vuln_buttonbox.addButton(
            "격리", QDialogButtonBox.ButtonRole.ActionRole
        )
        quarantine.clicked.connect(self.__do_quarantine)
        clean = self.__vuln_buttonbox.addButton(
            "제거", QDialogButtonBox.ButtonRole.ActionRole
        )
        clean.clicked.connect(self.__do_clean)

        cleanall = self.__vuln_buttonbox.addButton(
            "모두 제거", QDialogButtonBox.ButtonRole.ActionRole
        )
        cleanall.clicked.connect(self.__do_cleanall)

        self.layout.addWidget(self.__vuln_buttonbox)
        quarantine.setVisible(False)

    def __get_all_targets(self):
        targets = list()
        for res in self.__scan_result:
            targets.append(res.target)
        return targets

    def __get_checked_targets(self):
        targets = list()
        root = self.__tree_widget.invisibleRootItem()
        for i in range(root.childCount()):
            item = root.child(i)
            if item.checkState(4) == Qt.Checked:
                targets.append(item.target)
        return targets

    @pyqtSlot(bool)
    def __do_quarantine(self, _):
        targets = self.__get_checked_targets()
        for t in targets:
            print(t.quarantine_path.join())
        pass

    def clean_targets(self, targets):
        class CleanThread(QThread):
            def __init__(self, target, slotOnFinished=None):
                super(CleanThread, self).__init__()
                self.target = target
                if slotOnFinished:
                    self.finished.connect(slotOnFinished)

            def run(self, *args, **kwargs):
                self.target(*args, **kwargs)

        for t in targets:
            if t.uninstaller == None:
                continue
            ct = CleanThread(t.uninstall, self._do_scan_quiet)
            self.__threads.append(ct)
            ct.start()

    @pyqtSlot(bool)
    def __do_clean(self, _):
        targets = self.__get_checked_targets()
        self.clean_targets(targets)

    @pyqtSlot(bool)
    def __do_cleanall(self, _):
        targets = self.__get_all_targets()
        self.clean_targets(targets)

    def __display_about(self):
        title = "Vsafer"
        text = f"""
        <big>Vsafer</big>

        <p>컴퓨터에 설치된 개인 뱅킹 프로그램의 버전을 검사해 구버전 프로그램에 존재하는
        보안 취약점들을 탐지합니다.</p>
        <p>버전: {__version__}</p>
        <p>날짜: {__date__}</p>
        <p>제작: 이재용 - <a href="https://interlab.or.kr">디지털안전연구소 인터랩</a></p>
        <p>
            문의 연락처: <a href="mailto:contact@interlab.or.kr">contact@interlab.or.kr</a>
        </p>
        """

        messagebox = QMessageBox(parent=self, icon=QMessageBox.Icon.Information)
        pixmap = QPixmap(os.path.join(guiutils.assets_path(), "icon.png"))
        pixmap = pixmap.scaled(128, 128, Qt.AspectRatioMode.KeepAspectRatio)
        messagebox.setIconPixmap(pixmap)
        messagebox.setWindowTitle(title)
        messagebox.setText(text)

        messagebox.exec()
