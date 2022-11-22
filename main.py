import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QFileDialog, QMenu
from PyQt5.uic import loadUi
from PyQt5 import QtGui
import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best-2.pt')


class Agricorn(QMainWindow):
    def __init__(self):
        super(Agricorn, self).__init__()
        loadUi("ui/start.ui", self)

        self.started.clicked.connect(self.gotodashboard)
        self.about_us.clicked.connect(self.gotoaboutus)

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
        loadUi("ui/dashboard.ui", self)

        self.UploadImage.clicked.connect(self.uploadfoto)
        self.Kembali.clicked.connect(self.gotostart)

    def uploadfoto(self):
        namaf = QFileDialog.getOpenFileName(self, 'Pilih file gambar', 'c:')
        filename = namaf[0].split('/')[-1]
        if filename:
            result = model(namaf[0], size=640)
            result.save(save_dir='result/')
            deteksi = result.pandas().xyxy[0].to_dict()
            deteksi = deteksi["name"][0]
            deteksi = str(deteksi)
            print(deteksi)
            img = cv2.imread(f'result/{filename}', cv2.IMREAD_UNCHANGED)

            h = 631
            w = 491
            s = (h, w)
            global resized
            resized = cv2.resize(img, s, interpolation=cv2.INTER_AREA)
            cv2.imwrite('result2.jpg', resized)
            self.image.setPixmap(QtGui.QPixmap('result2.jpg'))

            self.hasil.setText(deteksi.upper())

            #if deteksi == 'hawar':
                #self.penanganan.setPixmap(QtGui.QPixmap())

        else:
            pass


    def gotostart(self):
        startwindow = Agricorn()
        widget.addWidget(startwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class AboutUs(QMainWindow):
    def __init__(self):
        super(AboutUs, self).__init__()
        loadUi("ui/window_about.ui", self)

        self.Kembali.clicked.connect(self.gotohomepage)

    def gotohomepage(self):
        mainwindow = Agricorn()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
mainwindow = Agricorn()
halamanutama = Dashboard()
halamandepan = Agricorn()
aboutwindow = AboutUs()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.addWidget(halamandepan)
widget.addWidget(halamanutama)
widget.addWidget(aboutwindow)
# Setingan Width dan Height untuk Fullscreen
# widget.setFixedWidth(1920)
# widget.setFixedHeight(1000)
widget.setFixedWidth(911)
widget.setFixedHeight(600)
widget.show()
sys.exit(app.exec_())
