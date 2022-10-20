import sys
import os
import ctypes
import time
from PySide6.QtWidgets import QMainWindow, QApplication, QSystemTrayIcon, QMenu
from PySide6.QtCore import QProcess, Slot
from PySide6.QtGui import QPixmap, QCloseEvent

from ui.main_form import Ui_MainWindow

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        myappid = 'ddat_off_helper' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        super(Mainwindow, self).__init__()
        self.setupUi(self)

        self.shutdown_time = 0
        self.remain_time = 0
        self.ready_close = False

        self.ddat = resource_path("src/icon/ddat_off.ico")
        self.ddat_pixmap = QPixmap(self.ddat)

        self.shutdwon_set = False
        self.pushButton.clicked.connect(self.btn_handler)

        menu = QMenu()
        menu.addAction("열기", self.menu_show)
        menu.addAction("닫기", self.menu_close)
        menu.addAction("남은시간", self.menu_remain_time)

        self.tray = QSystemTrayIcon(self.ddat_pixmap, self)
        self.tray.setContextMenu(menu)
        self.tray.activated.connect(self.tray_activated_handler)
        self.tray.show()
    
    def menu_show(self):
        self.show()

    def menu_close(self):
        self.ready_close = True
        self.show()
        self.close()

    @Slot(QSystemTrayIcon.ActivationReason)
    def tray_activated_handler(self, reason : QSystemTrayIcon.ActivationReason):
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.show()

    def menu_remain_time(self):
        if self.shutdwon_set:
            message = ""
            self.remain_time = self.shutdown_time - time.time()
            h = int(self.remain_time // 3600)
            if h > 0:
                message = message + f"{h}시간 "
            m = int(self.remain_time % 3600 // 60)
            if m > 0:
                message = message + f"{m}분 "
            s = int(self.remain_time % 3600 % 60)
            if s > 0:
                message = message + f"{s}초 "
            
            message = message + "남았습니땃 !"
            self.tray.showMessage("ddat", message)
        else:
            self.tray.showMessage("ddat", "예약종료 하지 않았습니땃")

    @Slot()
    def btn_handler(self):
        self.shutdwon_set = not self.shutdwon_set
        if self.shutdwon_set:
            set_timer = int(self.spinBox_timer.value())
            self.spinBox_timer.setEnabled(False)
            self.shutdown(set_timer)
            self.shutdown_time = time.time() + set_timer
            self.pushButton.setText("예약 취소")
        else:
            self.shutdown_cancle()
            self.spinBox_timer.setEnabled(True)
            self.pushButton.setText("확인")
    
    def shutdown(self, timer):
        self.process = QProcess()
        self.process.start("shutdown.exe",["-s","-t", str(timer)])
        self.process.waitForFinished(-1)

    def shutdown_cancle(self):
        self.process = QProcess()
        self.process.start("shutdown.exe",["-a"])
        self.process.waitForFinished(-1)
    
    def closeEvent(self, event: QCloseEvent) -> None:
        if self.ready_close == False:
            self.hide()
            event.ignore()
        else:
            return super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ddat = resource_path("src/icon/ddat_off.ico")
    ddat_pixmap = QPixmap(ddat)
    app.setWindowIcon(ddat_pixmap)
    window = Mainwindow()
    window.show()
    app.exec()
