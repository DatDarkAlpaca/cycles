# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(370, 300)
        MainWindow.setMinimumSize(QSize(370, 300))
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_label = QLabel(self.central_widget)
        self.main_label.setObjectName(u"main_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_label.sizePolicy().hasHeightForWidth())
        self.main_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.main_label.setFont(font)
        self.main_label.setStyleSheet(u"")
        self.main_label.setScaledContents(False)
        self.main_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.main_label)

        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.current_label = QLabel(self.central_widget)
        self.current_label.setObjectName(u"current_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.current_label.sizePolicy().hasHeightForWidth())
        self.current_label.setSizePolicy(sizePolicy1)
        self.current_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.current_label)

        self.cycle_name_label = QLabel(self.central_widget)
        self.cycle_name_label.setObjectName(u"cycle_name_label")
        sizePolicy.setHeightForWidth(self.cycle_name_label.sizePolicy().hasHeightForWidth())
        self.cycle_name_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.cycle_name_label.setFont(font1)
        self.cycle_name_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.cycle_name_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.previous_btn = QPushButton(self.central_widget)
        self.previous_btn.setObjectName(u"previous_btn")

        self.horizontalLayout.addWidget(self.previous_btn)

        self.next_btn = QPushButton(self.central_widget)
        self.next_btn.setObjectName(u"next_btn")

        self.horizontalLayout.addWidget(self.next_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.central_widget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.menu_bar = QMenuBar(MainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 370, 22))
        self.menu_file = QMenu(self.menu_bar)
        self.menu_file.setObjectName(u"menu_file")
        MainWindow.setMenuBar(self.menu_bar)

        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_exit)

        self.retranslateUi(MainWindow)
        self.action_exit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cycles v1.0", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.action_exit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.main_label.setText(QCoreApplication.translate("MainWindow", u"Cycles", None))
        self.current_label.setText(QCoreApplication.translate("MainWindow", u"Current:", None))
        self.cycle_name_label.setText(QCoreApplication.translate("MainWindow", u"Cycle Name", None))
        self.previous_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

