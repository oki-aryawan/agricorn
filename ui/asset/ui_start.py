# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/syauqiarham/Desktop/Pemtek/Project/Agricorn/start.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Agricorn(object):
    def setupUi(self, Agricorn):
        Agricorn.setObjectName("Agricorn")
        Agricorn.resize(900, 600)
        Agricorn.setStyleSheet("background-color: rgb(251, 255, 250);")
        self.centralwidget = QtWidgets.QWidget(Agricorn)
        self.centralwidget.setObjectName("centralwidget")
        self.img_bg = QtWidgets.QLabel(self.centralwidget)
        self.img_bg.setGeometry(QtCore.QRect(-70, -60, 1011, 641))
        self.img_bg.setText("")
        self.img_bg.setPixmap(QtGui.QPixmap("/Users/syauqiarham/Desktop/Pemtek/Project/Agricorn/asset/5498894.jpg"))
        self.img_bg.setScaledContents(True)
        self.img_bg.setObjectName("img_bg")
        self.img_corn = QtWidgets.QLabel(self.centralwidget)
        self.img_corn.setGeometry(QtCore.QRect(360, 120, 161, 161))
        self.img_corn.setStyleSheet("background-color: transparent;\n"
"")
        self.img_corn.setText("")
        self.img_corn.setPixmap(QtGui.QPixmap("/Users/syauqiarham/Desktop/Pemtek/Project/Agricorn/asset/corn (1)22.png"))
        self.img_corn.setScaledContents(True)
        self.img_corn.setObjectName("img_corn")
        self.img_text = QtWidgets.QLabel(self.centralwidget)
        self.img_text.setGeometry(QtCore.QRect(280, 160, 321, 321))
        self.img_text.setStyleSheet("background-color: transparent\n"
"")
        self.img_text.setText("")
        self.img_text.setPixmap(QtGui.QPixmap("/Users/syauqiarham/Desktop/Pemtek/Project/Agricorn/asset/agricorn.png"))
        self.img_text.setScaledContents(True)
        self.img_text.setObjectName("img_text")
        self.Started = QtWidgets.QPushButton(self.centralwidget)
        self.Started.setGeometry(QtCore.QRect(390, 430, 101, 21))
        self.Started.setStyleSheet("border:1px solid black; \n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 10px; \n"
"border-bottom-left-radius : 10px; \n"
"border-bottom-right-radius : 10px;\n"
"background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")
        self.Started.setObjectName("Started")
        self.img_upld = QtWidgets.QLabel(self.centralwidget)
        self.img_upld.setGeometry(QtCore.QRect(383, 390, 21, 21))
        self.img_upld.setText("")
        self.img_upld.setPixmap(QtGui.QPixmap("/Users/syauqiarham/Desktop/Pemtek/Project/Agricorn/asset/upload.png"))
        self.img_upld.setScaledContents(True)
        self.img_upld.setObjectName("img_upld")
        self.UploadImage = QtWidgets.QPushButton(self.centralwidget)
        self.UploadImage.setGeometry(QtCore.QRect(364, 380, 151, 41))
        font = QtGui.QFont()
        font.setBold(False)
        self.UploadImage.setFont(font)
        self.UploadImage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.UploadImage.setStyleSheet("border:1px solid black; \n"
"border-top-left-radius : 10px;\n"
"border-top-right-radius : 10px; \n"
"border-bottom-left-radius : 10px; \n"
"border-bottom-right-radius : 10px;\n"
"background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"Text-align:right\n"
"")
        self.UploadImage.setObjectName("UploadImage")
        self.img_bg.raise_()
        self.img_text.raise_()
        self.img_corn.raise_()
        self.Started.raise_()
        self.UploadImage.raise_()
        self.img_upld.raise_()
        Agricorn.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Agricorn)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        self.menuAgricorn = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setBold(True)
        self.menuAgricorn.setFont(font)
        self.menuAgricorn.setStyleSheet("color: rgb(0, 0, 0);")
        self.menuAgricorn.setObjectName("menuAgricorn")
        Agricorn.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Agricorn)
        self.statusbar.setObjectName("statusbar")
        Agricorn.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAgricorn.menuAction())

        self.retranslateUi(Agricorn)
        QtCore.QMetaObject.connectSlotsByName(Agricorn)

    def retranslateUi(self, Agricorn):
        _translate = QtCore.QCoreApplication.translate
        Agricorn.setWindowTitle(_translate("Agricorn", "MainWindow"))
        self.Started.setText(_translate("Agricorn", "About Us"))
        self.UploadImage.setText(_translate("Agricorn", "Upload Image    "))
        self.menuAgricorn.setTitle(_translate("Agricorn", "About us"))
