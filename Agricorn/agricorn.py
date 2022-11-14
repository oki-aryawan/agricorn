import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtGui
import torch
import cv2
from PIL import Image


#model = torch.hub.load('ultralytics/yolov5', 'custom', path='agricorn.pt')

class Agricorn(QMainWindow):
    def __init__(self):
        super(Agricorn, self).__init__()
        loadUi("start.ui", self)

        self.Started.clicked.connect(self.gotodashboard)
        # self.AboutUs.clicked.connect (self.gotoaboutus)

    def gotodashboard(self):
        halamanutama = Dashboard()
        widget.addWidget(halamanutama)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoaboutus(self):
        aboutwindow = AboutUs()
        widget.addWidget(aboutwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Dashboard(QMainWindow):
    def __init__(self):
        super(Dashboard, self).__init__()
        loadUi("dashboard.ui", self)

        self.InputImage.clicked.connect(self.uploadfoto)

    def uploadfoto(self):
        namaf = QFileDialog.getOpenFileName(self, 'Pilih file gambar', 'c:')
        #self.image.setPixmap(QtGui.QPixmap('Corn_Blight (118).jpg'))


class AboutUs(QMainWindow):
    def __init__(self):
        super(AboutUs, self).__init__()
        loadUi("window_about.ui", self)

        # self.Kembali.clicked.connect (self.gotohomepage)

    def gotohomepage(self):
        mainwindow = Agricorn()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
mainwindow = Agricorn()
halamanutama = Dashboard()
aboutwindow = AboutUs()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.addWidget(halamanutama)
widget.addWidget(aboutwindow)
# Setingan Width dan Height untuk Fullscreen
# widget.setFixedWidth(1920)
# widget.setFixedHeight(1000)
widget.setFixedWidth(911)
widget.setFixedHeight(600)
widget.show()
sys.exit(app.exec_())
