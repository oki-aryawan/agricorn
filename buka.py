# Ketik 5 baris perintah untuk meng-import beberapa modul yang dibutuhkan
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtGui
import torch
import cv2
from PIL import Image
from torchvision.utils import save_image


class Agricorn(QMainWindow):
    def __init__(self):
        super(Agricorn, self).__init__()
        loadUi("start.ui", self)

        self.started.clicked.connect(self.gotodashboard)
        self.about_us.clicked.connect(self.gotoaboutus)
    
    def gotodashboard(self):
        halamanutama=Dashboard()
        widget.addWidget(halamanutama)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoaboutus(self):
        aboutwindow=AboutUs()
        widget.addWidget(aboutwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Dashboard(QMainWindow):
    def __init__(self):
        super(Dashboard, self).__init__()
        loadUi("dashboard.ui", self)

        self.UploadImage.clicked.connect(self.uploadfoto)
        self.Kembali.clicked.connect(self.gotostart)

    def uploadfoto(self):
        # Menampilkan dialog untuk membuka file, gambar yang dipilih disimpan di variabel 'namaf'
        namaf = QFileDialog.getOpenFileName(self, 'Pilih file gambar', 'c:')
        # Menampilkan file gambar 'namaf' yang dipilih pada QLabel yang bernama 'photo'

        self.photo.setPixmap(QtGui.QPixmap('Agricorn/Corn_Blight (118).jpg'))
        
        cv2.imwrite('prediction.jpg', showimg)
        self.result = cv2.cvtColor(showimg, cv2.COLOR_BGR2BGRA)
        self.result = cv2.resize(
            self.result, (640, 480), interpolation=cv2.INTER_AREA)
        self.QtImg = QtGui.QImage(
            self.result.data, self.result.shape[1], self.result.shape[0], QtGui.QImage.Format_RGB32)
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
        

    def gotostart(self):
        startwindow=Agricorn()
        widget.addWidget(startwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class AboutUs(QMainWindow):
    def __init__(self):
        super(AboutUs, self).__init__()
        loadUi("window_about.ui", self)

        self.Kembali.clicked.connect(self.gotohomepage)

    def gotohomepage(self):
        mainwindow = Agricorn ()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
# Pendefinisian Class
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Memanggil file Design GUI yang sudah dibuat
        loadUi("LoadPicture.ui", self)
        # Mendefinisikan Perilaku obyek Push Button yang bernama "buka"
        # jika di Click maka akan menjalankan sub/fungsi 'buka_gambar'
        self.buka.clicked.connect(self.buka_gambar)
        self.keluar.clicked.connect(self.menu_keluar)

    # Membuat/Mendefinisikan fungsi yang bernama 'buka_gambar' 
    def buka_gambar(self):
        # Menampilkan dialog untuk membuka file, gambar yang dipilih disimpan di variabel 'namaf'
        namaf = QFileDialog.getOpenFileName(self, 'Pilih file gambar', 'c:')
        # Menampilkan file gambar 'namaf' yang dipilih pada QLabel yang bernama 'photo'

        self.photo.setPixmap(QtGui.QPixmap('Agricorn/Corn_Blight (118).jpg'))
        
        cv2.imwrite('prediction.jpg', showimg)
        self.result = cv2.cvtColor(showimg, cv2.COLOR_BGR2BGRA)
        self.result = cv2.resize(
            self.result, (640, 480), interpolation=cv2.INTER_AREA)
        self.QtImg = QtGui.QImage(
            self.result.data, self.result.shape[1], self.result.shape[0], QtGui.QImage.Format_RGB32)
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
        

    def menu_keluar(self):
        sys.exit(app.exec_())


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1920)
widget.setFixedHeight(1000)
widget.show()
sys.exit(app.exec_())
