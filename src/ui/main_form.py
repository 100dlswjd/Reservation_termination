# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(193, 163)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_help = QLabel(self.centralwidget)
        self.label_help.setObjectName(u"label_help")

        self.verticalLayout.addWidget(self.label_help)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_timer = QLabel(self.centralwidget)
        self.label_timer.setObjectName(u"label_timer")
        self.label_timer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_timer)

        self.spinBox_timer = QSpinBox(self.centralwidget)
        self.spinBox_timer.setObjectName(u"spinBox_timer")
        self.spinBox_timer.setMaximum(36000)
        self.spinBox_timer.setValue(600)

        self.horizontalLayout.addWidget(self.spinBox_timer)

        self.label_sec = QLabel(self.centralwidget)
        self.label_sec.setObjectName(u"label_sec")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sec.sizePolicy().hasHeightForWidth())
        self.label_sec.setSizePolicy(sizePolicy)
        self.label_sec.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_sec)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 193, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\uc608\uc57d\uc885\ub8cc", None))
        self.label_help.setText(QCoreApplication.translate("MainWindow", u"1\ubd84 = 60\ucd08, 1\uc2dc\uac04 = 3600\ucd08", None))
        self.label_timer.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04", None))
        self.label_sec.setText(QCoreApplication.translate("MainWindow", u"\ucd08", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
    # retranslateUi

