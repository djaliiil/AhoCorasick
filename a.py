from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout, QListWidget, QComboBox, QLineEdit, QFileDialog, QLabel, QCalendarWidget, QSizePolicy,\
    QSplashScreen, QProgressBar, QLCDNumber, QFrame, QShortcut, QAction
from PyQt5.QtCore import QSize, QThread, QTime, QTimer
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from random import randint
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtQuick import QQuickView
import time
from datetime import datetime



# On va tout d'abord créer notre fenetre (window)
#-------------------------------------------------------
class window(QtWidgets.QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        #------ positionner la fenetre
        self.setGeometry(200, 120, 1000, 570)
        #----- titre de la fenetre
        self.setWindowTitle("Strings matching patterns")
        #----- icon de la fenetre
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        #---- on va creer l'arriere plan
        """
        oImage = QImage("image.jpg")
        sImage = oImage.scaled(QSize(950, 650))
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(sImage))
        self.setPalette(palette)
        """
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 950, 500))
        self.groupBox.setObjectName("groupBox")

        self.groupBox2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox2.setGeometry(QtCore.QRect(20, 30, 350, 440))
        self.groupBox2.setObjectName("groupBox2")

        self.edit = QtWidgets.QTextEdit(self.groupBox2)
        self.edit.setGeometry(QtCore.QRect(10, 30, 330, 385))
        self.edit.setObjectName("textEdit")
        self.edit.setReadOnly(True)
        self.edit.setStyleSheet("QTextEdit {    background-color: #19232D;    color: #F0F0F0;    border: 1px solid #32414B;}")

        self.groupBox3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox3.setGeometry(QtCore.QRect(400, 30, 520, 440))
        self.groupBox3.setObjectName("groupBox3")

        self.left_spacer = QWidget()
        self.left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_spacer = QWidget()
        self.right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.pref = QAction(QIcon('prefix.png'), '&All Prefixes', self)
        self.occur = QAction(QIcon('occurrence.jpg'), '&Find All Occurences', self)
        self.sg = QAction(QIcon('automaton.png'), '&Draw Automaton', self)
        self.sp = QAction(QIcon('plot.png'), '&Draw Plot', self)
        self.zin = QAction(QIcon('zoomin.png'), '&Zoom in', self)
        self.zout = QAction(QIcon('zoomout.png'), '&Zoom out', self)
        self.toolbar = self.addToolBar('toolbar')
        self.toolbar.addWidget(self.left_spacer)
        self.toolbar.addAction(self.pref)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.occur)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.sg)
        self.toolbar.addAction(self.zin)
        self.toolbar.addAction(self.zout)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.sp)
        self.toolbar.addWidget(self.right_spacer)
        

        self.occur.triggered.connect(self.occurrence)
        self.sg.triggered.connect(self.display_image)

        
        self.view = QtWidgets.QGraphicsView(self.groupBox3)
        self.view.setGeometry(QtCore.QRect(10, 20, 500, 405))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.view.setFont(font)
        self.view.setObjectName("graphicsView")
        self.view.setStyleSheet("QTextEdit {    background-color: #19232D;    color: #F0F0F0;    border: 1px solid #32414B;}")
        self.view.setMouseTracking(True)
        self.view.setAutoFillBackground(False)
        self.view.setFrameShadow(QtWidgets.QFrame.Sunken)

        
        
        
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        #-------- appel du methode qui contient les raccourcis clavier et les valeurs des composants de l'application
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        #-------- pour la visualisation de l'application
        self.show()
        return app.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Strings Matching Patterns"))
        self.shortcut = QShortcut(QKeySequence("Esc"), self)
        

        self.groupBox.setTitle(_translate("MainWindow", "Affichage"))
        self.groupBox.setStyleSheet("QGroupBox {font-weight: bold; font: bold; border: 2px solid #32414B; margin-top: 6px ;background-color: #ADFFFA; border-radius: 4px}")

        self.groupBox2.setTitle(_translate("MainWindow", "Texte"))
        self.groupBox2.setStyleSheet("QGroupBox {font-weight: bold; font: bold; border: 2px solid #32414B; margin-top: 6px ;background-color: #ADFFFA; border-radius: 4px}")

        self.groupBox3.setTitle(_translate("MainWindow", "Graphe"))
        self.groupBox3.setStyleSheet("QGroupBox {font-weight: bold; font: bold; border: 2px solid #32414B; margin-top: 6px ;background-color: #ADFFFA; border-radius: 4px}")


        self.occur.setShortcut('ctrl+c')
        self.sg.setShortcut('ctrl+a')
        self.sp.setShortcut('ctrl+p')

    @pyqtSlot()
    def occurrence(self):
        print("pressed tool button ")
        



    @pyqtSlot()
    def display_image(self):
        
        scene = QtWidgets.QGraphicsScene()
        img = QImage('ahocorasick/graph.gv.png')
        item = QtWidgets.QGraphicsPixmapItem(QPixmap(img))
        scene.addItem(item)
        self.view.setScene(scene)
        self.view.fitInView(scene.sceneRect())


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    win = window()
    win.self.show()
    sys.exit(app.exec_())
