# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QPushButton, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(252, 175)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"   background-color: #5A639C;\n"
"}\n"
"\n"
"QLabel,\n"
"QPushButton{\n"
"     color:  #E2BBE9;\n"
"     font-size: 18pt;\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal{\n"
"   background-color:  #E8C5E5; \n"
"   border-radius: 12px;\n"
"   width: 25px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal{\n"
"   height: 5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"   background-color: #7776B3;\n"
"   border: none; \n"
"   border-radius: 10px; \n"
"   padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: #9B86BD;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        font.setPointSize(18)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.height_layout = QHBoxLayout()
        self.height_layout.setObjectName(u"height_layout")
        self.height_slider = QSlider(self.centralwidget)
        self.height_slider.setObjectName(u"height_slider")
        self.height_slider.setOrientation(Qt.Orientation.Horizontal)

        self.height_layout.addWidget(self.height_slider)

        self.height_label = QLabel(self.centralwidget)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setFont(font)
        self.height_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.height_layout.addWidget(self.height_label)


        self.verticalLayout.addLayout(self.height_layout)

        self.weight_layout = QHBoxLayout()
        self.weight_layout.setObjectName(u"weight_layout")
        self.weight_slider = QSlider(self.centralwidget)
        self.weight_slider.setObjectName(u"weight_slider")
        self.weight_slider.setOrientation(Qt.Orientation.Horizontal)

        self.weight_layout.addWidget(self.weight_slider)

        self.weight_label = QLabel(self.centralwidget)
        self.weight_label.setObjectName(u"weight_label")
        self.weight_label.setFont(font)
        self.weight_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.weight_layout.addWidget(self.weight_label)


        self.verticalLayout.addLayout(self.weight_layout)

        self.calculate_button = QPushButton(self.centralwidget)
        self.calculate_button.setObjectName(u"calculate_button")

        self.verticalLayout.addWidget(self.calculate_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BMI CALCULATOR", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"BMI CALCULATOR", None))
        self.height_label.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.weight_label.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.calculate_button.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
    # retranslateUi

