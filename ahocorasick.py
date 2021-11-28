from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap, QIcon, QColor
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
import sys
import matplotlib.pyplot as plt
from datetime import datetime
from graphviz import Digraph, Source, nohtml
from os import *
from sys import *
from time import *
import pyqtgraph as pg
import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from threading import Thread


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
        self.groupBox2.setGeometry(QtCore.QRect(20, 25, 360, 450))
        self.groupBox2.setObjectName("groupBox2")

        self.edit = QtWidgets.QTextEdit(self.groupBox2)
        self.edit.setGeometry(QtCore.QRect(10, 30, 340, 395))
        self.edit.setObjectName("textEdit")
        self.edit.setReadOnly(True)
        self.edit.setStyleSheet("QTextEdit {    background-color: #19232D;    color: #F0F0F0;    border: 1px solid #32414B;}")

        self.groupBox3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox3.setGeometry(QtCore.QRect(400, 25, 530, 450))
        self.groupBox3.setObjectName("groupBox3")

        self.left_spacer = QWidget()
        self.left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_spacer = QWidget()
        self.right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.pref = QAction(QIcon('prefix.png'), '&All Prefixes', self)
        self.occur = QAction(QIcon('occurrence.jpg'), '&Find All Occurences', self)
        self.sg = QAction(QIcon('automaton.png'), '&Draw Automaton', self)
        self.sp = QAction(QIcon('plot.png'), '&Draw Plot', self)
        self.zoom = QAction(QIcon('zoom.png'), '&Zoom', self)
        self.clear = QAction(QIcon('clear.png'), '&Clear Data', self)
        self.zoomg = QAction(QIcon('zoom.png'), '&Zoom', self)
        self.toolbar = self.addToolBar('toolbar')


        self.toolbar.addWidget(self.left_spacer)
        self.toolbar.addAction(self.pref)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.occur)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.sg)
        self.toolbar.addAction(self.zoom)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.sp)
        self.toolbar.addAction(self.zoomg)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.clear)
        self.toolbar.addWidget(self.right_spacer)
        

        self.pref.triggered.connect(self.prefixe)
        self.occur.triggered.connect(self.occurrence)
        self.sg.triggered.connect(self.display_image)
        self.sp.triggered.connect(self.display_plot)
        self.zoom.triggered.connect(self.zooom)
        self.zoomg.triggered.connect(self.zooomg)
        self.clear.triggered.connect(self.clear_data)
        
        self.scene = QtWidgets.QGraphicsScene()
        self.view = QtWidgets.QGraphicsView()
        self.scene2 = QtWidgets.QGraphicsScene()
        self.view2 = QtWidgets.QGraphicsView()
        
        self.layout = QVBoxLayout()
        self.groupBox3.setLayout(self.layout)
        
        
        
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
        self.groupBox2.setStyleSheet("QGroupBox {font-weight: bold; font: bold; border: 2px solid #32414B; margin-top: 6px ;background-color: #FFFFBA; border-radius: 4px}")

        self.groupBox3.setTitle(_translate("MainWindow", "Graphe"))
        self.groupBox3.setStyleSheet("QGroupBox {font-weight: bold; font: bold; border: 2px solid #32414B; margin-top: 6px ;background-color: #FFFFBA; border-radius: 4px}")


        self.occur.setShortcut('ctrl+c')
        self.sg.setShortcut('ctrl+a')
        self.sp.setShortcut('ctrl+p')

    
    @pyqtSlot()
    def prefixe(self):
        
        global msg
        global s
        global patterns
        global pref
        a = ""
        self.edit.setText("#############################")
        self.edit.append("######### AHO-CORASCIK #########")
        self.edit.append("############################# \n\n")
        self.edit.append(">>>>>>> Touts les prefixes du motif <<<<<<< \n")
        self.edit.append("->  Motif : "+str(patterns))
        print("========================= ", pref)
        for i in pref:
            a += "   "+i
        self.edit.append("->  Prefixes : "+a)

    @pyqtSlot()
    def occurrence(self):
        global s1, pat1
        
        global msg
        global s
        global patterns
        global tmp5
        self.edit.setText("#############################")
        self.edit.append("######### AHO-CORASCIK #########")
        self.edit.append("############################# \n\n")
        self.edit.append(">>>>>>> Touts les occurrences <<<<<<< \n")
        self.edit.append("\tTexte : "+s)
        self.edit.append("  Motif : "+str(patterns)+"\n")
        self.edit.append(msg+"\n")
        self.edit.append(">>> Le temps d'execution : "+str(tmp5)+" S")
        

    @pyqtSlot()
    def display_image(self):
        global b1
        global b2
        b1 = True
        
        if(b2 == True):
            self.view2.setParent(None)
            b2 = False
            self.layout.addWidget(self.view)
        else:
            self.layout.addWidget(self.view)

        self.view.setGeometry(QtCore.QRect(10, 20, 500, 405))
        self.view.setObjectName("graphicsView")
        self.view.setStyleSheet("QTextEdit {    background-color: #19232D;    color: #F0F0F0;    border: 1px solid #32414B;}")
        self.view.setMouseTracking(True)
        self.view.setAutoFillBackground(False)
        self.view.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.view.setScene(self.scene)
        
        img = QImage('graph.gv.png')
        item = QtWidgets.QGraphicsPixmapItem(QPixmap(img))
        self.scene.addItem(item)
        
        self.view.fitInView(self.scene.sceneRect())
        
        

    @pyqtSlot()
    def display_plot(self):     
        
        global b2
        global b1
        global stat
        b2 = True 
        
        if(b1 == True):
            self.view.setParent(None)
            b1 = False
            self.layout.addWidget(self.view2)
        else:
            self.layout.addWidget(self.view2)
        
        self.view2.setGeometry(QtCore.QRect(10, 20, 500, 405))
        self.view2.setObjectName("graphicsView")
        self.view2.setStyleSheet("QTextEdit {    background-color: #19232D;    color: #F0F0F0;    border: 1px solid #32414B;}")
        self.view2.setMouseTracking(True)
        self.view2.setAutoFillBackground(False)
        self.view2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.view2.setScene(self.scene2)

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)   
        self.scene2.addWidget(self.canvas)
        
        
        ax = self.fig.add_subplot(111)
        global x

        ax.plot(x, stat[0],'', color='blue', label='Rech-Naïve')
        ax.plot(x, stat[1],'', color='red', label='MP-Algo')
        ax.plot(x, stat[2],'', color='green', label='KMP-Algo')
        ax.plot(x, stat[3],'', color='yellow', label='Rabin-Karp')
        ax.plot(x, stat[4],'', color='gray', label='Aho-Corasick')
        ax.legend()
        
        ax.set_ylabel('Y', color='black', fontsize='large', weight='bold')
        ax.set_xlabel('X', color='black', fontsize='large', weight='bold')

        ax.set_title("My plot", fontsize='large', weight='bold')
        
        
        for tick in ax.xaxis.get_ticklabels():
            tick.set_fontsize('large')
            tick.set_fontname('Times New Roman')
            tick.set_color('Black')
            tick.set_weight('bold')

        for tick in ax.yaxis.get_ticklabels():
            tick.set_fontsize('large')
            tick.set_fontname('Times New Roman')
            tick.set_color('black')
            tick.set_weight('bold')
        
        #self.canvas.draw() 
        self.fig.canvas.draw()
        self.view2.fitInView(self.scene2.sceneRect())
        

    @pyqtSlot()
    def zooom(self):
        source.view()

    @pyqtSlot()
    def zooomg(self):
        global stat
        ax = plt.axes(facecolor='w')
        ax.set_axisbelow(True)
        plt.grid(color='#E7E6E6', linestyle='solid')
        ax.yaxis.tick_left()
        global x
        
        plt.plot(x,stat[0],color='blue', label="Rech-Naïve")
        plt.plot(x,stat[1],color='red', label="MP-Algo")
        plt.plot(x,stat[2],color='green', label="KMP-Algo")
        plt.plot(x,stat[3],color='yellow', label="Rabin-Karp")
        plt.plot(x,stat[4],color='gray', label="Aho-Corasick")
        plt.gca().get_xaxis().set_ticks(x)
        #plt.gca().get_yaxis().set_ticks(stat)
        ax.xaxis.set_label_coords(1.05, -0.025)
        ax.yaxis.set_label_coords(-0.025,1.025)
        h = plt.ylabel('y')
        h.set_rotation(0)
        plt.title("Pattern Matching Algorithm")
        plt.xlabel("Iteration")
        plt.ylabel("Time (S)")
        plt.legend()
        plt.show()
    
    @pyqtSlot()
    def clear_data(self):
        self.scene.clear()
        self.view.fitInView(self.scene.sceneRect())
        self.scene2.clear()
        self.view2.fitInView(self.scene.sceneRect())
        self.edit.setText("")


#===============================================================================================
#============| Naïve / Morris-Pratt / Knuth-Morris-Pratt / Rabin-Karp Algorithms |==============
#===============================================================================================

#============== Algorithme de Recherche Naive =============
def recherche_naive(texte, mot):
    n = len(texte)
    m = len(mot)
    mot.append('')
    
    i = 0
    result = []

    while (i < (n-m)):
        j = 0
        while (j < m) & (texte[i + j] == mot[j]):
            j = j+1
        if(j==m):
            result.append(i)
        i = i+1

    mot.pop(len(mot)-1)
    return result


#============= Table de bords / Knuth-Morris-Pratt ==============
def mp_table_bords(mot):
    m = len(mot)
    bords = [-1]
    bords.extend([0]*m)
    mot.append('')
    i = -1

    for j in range(m):
        while ((i >= 0) & (mot[i] != mot[j])):
            i = bords[i]

        i = i+1

        if((i == (m-1)) | (mot[j+1] != mot[i])):
            bords[j+1] = i
        else:
            bords[j+1] = bords[i]

    print(">>>>> Bords : " , bords)
    mot.pop(len(mot)-1)
    return bords

#============== Table de bords / Knuth-Morris-Pratt =====================
def kmp_table_bords(mot, m, bords): 
	j = 0

	bords[0]
	i = 1

	while i < m: 
		if mot[i]== mot[j]: 
			j += 1
			bords[i] = j
			i += 1
		else: 
			if j != 0: 
				j = bords[j-1] 
				
			else: 
				bords[i] = 0
				i += 1


#============== Morris-Pratt Algorithms ===================
#>>>>>>>> Algorithme de recherche
def Knuth_morris_pratt_algorithm(texte, mot):
    i = 0
    j = 0
    m = len(mot)
    n = len(texte)
    result = []
    bords = [0]*m
    kmp_table_bords(mot, m, bords)

    while i < n:
        if mot[j] == texte[i]:
            i += 1
            j += 1

        if j == m:
            result.append(i-j)
            j = bords[j-1] 

        elif i < n and mot[j] != texte[i]: 
            if j != 0:
                j = bords[j-1]
            else:
                i += 1

    return result

#============= Knuth-Morris-Pratt Algorithm ==================
def morris_pratt_algorithm(texte, mot):
    i = 0
    j = 0
    m = len(mot)
    n = len(texte)
    result = []
    bords = mp_table_bords(mot)

    while i < n:
        if mot[j] == texte[i]:
            i += 1
            j += 1

        if j == m:
            result.append(i-j)
            j = bords[j-1] 

        elif i < n and mot[j] != texte[i]: 
            if j != 0:
                j = bords[j-1]
            else:
                i += 1

    return result

#=============== Fonction de hashage =================
def myhash(t):
    motif = {'a':1, 'b':2, 'c':3, 'd': 4, 'e':5, 'f':6, 'g':7, 'h': 8,
             'i':9, 'j':10, 'k':11, 'l': 12, 'm':13, 'n':14, 'o':15, 'p': 16,
             'q':17, 'r':18, 's':19, 't': 20, 'u':21, 'v':22, 'w':23, 'x': 24,
             'y':25, 'z':26}
    key = 0
    for i in range(len(t)):
        c = t[i]
        p = int(motif[c]) * 26**(len(t)-1-i)
        key = key + p

    return key

#============== Rabin-Karp algorithm ==================
def Rabin_Karp_Generale(texte, mot):
    n = len(texte)
    m = len(mot)
    hm = myhash(mot)
    ht = myhash(texte[0:m])
    result = []

    for i in range(n - m + 1):
        if (hm == ht):
            if (mot[0:m] == texte[i :i + m]):
                result.append(i)
        if (i+1 < (n - m + 1)):
            ht = myhash(texte[i+1: i + m+1])
    
    return result

#-----------------------------------------------------------------------------
#########################################
#   Recherche naive
def fct1(texte, mot):
    dic = {}
    lst = []
    
    for i in mot:
        l = []
        for j in range(len(i)):
            l.append(i[j])
        print("----- * * * ---- ", type(l))
        lst = recherche_naive(texte, list(l))
        if(lst != []):
            dic[i] = lst
    return dic
#########################################
#   Morris-Pratt 
def fct2(texte, mot):
    dic = {}
    lst = []
    for i in mot:
        lst = morris_pratt_algorithm(texte, list(i))
        print("/////////////////////////////////")
        if(lst != []):
            dic[i] = lst
    return dic
#########################################
#   Knuth-Morris-Pratt 
def fct3(texte, mot):
    dic = {}
    lst = []
    for i in mot:
        lst = Knuth_morris_pratt_algorithm(texte, list(i))
        if(lst != []):
            dic[i] = lst
    return dic
#########################################
#   Rabin-Karp 
def fct4(texte, mot):
    dic = {}
    lst = []
    for i in mot:
        lst = Rabin_Karp_Generale(texte, list(i))
        if(lst != []):
            dic[i] = lst
    return dic
#-----------------------------------------------------------------------------

#===============================================================================================
#=====================================| Aho-Corasick |==========================================
#===============================================================================================

"""
La structure Node est un nouveau type composé de 3 champs:
    1.  goto: dictionnaire pour les transitions (les arretes)
    2.  out:  liste qui contient les elements du motif 
    3.  fail: un pointeur (on l'utilise pour construire les ε-transitions)
"""
class Node:
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None

"""
La fonction prefixe retourne touts les prefixes de touts les elements
 de motif à rechercher
"""
def prefixe(root, pref=[], ch = ""):
    
    for key in root.goto:
        ch += key
        for k in root.goto[key].goto:
            if root.goto[key].goto:
                if ch not in pref:
                    pref.append(ch)
        prefixe(root.goto[key], pref, ch)
        ch = ""
        
    return pref

      
"""
La fonction display permet d'afficher tout les noeuds (sommets) de l'arbre construite 
à partir de la liste de motifs (Parcour profondeur)
"""
def display(root):
    if(root.fail != None):
        print("---  ", root.out, "  --- ", root.fail.out, " --- ", root.fail.goto.keys())
    for key in root.goto:
        display(root.goto[key])
    

"""
La fonction arbre permet de créer l'arbre
"""
def arbre(patterns):
    root = Node()
 
    for path in patterns:
        node = root
        for symbol in path:
            node = node.goto.setdefault(symbol, Node())
        node.out.append(path)
        
    return root
 
"""
La fonction automate prend en parametres la liste de motif (patterns), en construisant
l'arbre et ajouter les ε-transitions.
C'est le cas de chauvechement (exp : abc, bc), afin d'optimiser la reherche et le parcour.
"""
def automate(patterns):
    root = arbre(patterns)
    queue = []    
    
    dot = Digraph(comment='The Round Table')
    dot = Digraph('structs', node_attr={'shape': 'record'})
    dot.node(nohtml('<f0> '+str(root.goto.keys())+'|<f1> '+str(root.out)+'|<f2>.'), nohtml('<f0> '+str(root.goto.keys())+'|<f1> '+str(root.out)+'|<f2>.'))

    for k, node in root.goto.items():
        queue.append(node)
        node.fail = root
        dot.node(nohtml('<f0> '+str(node.goto.keys())+'|<f1> '+str(node.out)+'|<f2>.'), nohtml('<f0> '+str(node.goto.keys())+'|<f1> '+str(node.out)+'|<f2>.'))
        dot.edge(nohtml('<f0> '+str(root.goto.keys())+'|<f1> '+str(root.out)+'|<f2>.') ,nohtml('<f0> '+str(node.goto.keys())+'|<f1> '+str(node.out)+'|<f2>.'), label=k)
        dot.edge(nohtml('<f0> '+str(node.goto.keys())+'|<f1> '+str(node.out)+'|<f2>.'), nohtml('<f0> '+str(root.goto.keys())+'|<f1> '+str(root.out)+'|<f2>.'), label="ε")

    while len(queue) > 0:
        rnode = queue.pop(0)
        dot.node(nohtml('<f0> '+str(rnode.goto.keys())+'|<f1> '+str(rnode.out)+'|<f2>.'), nohtml('<f0> '+str(rnode.goto.keys())+'|<f1> '+str(rnode.out)+'|<f2>.'))
        
        for key, unode in rnode.goto.items():    
            queue.append(unode)
            fnode = rnode.fail
            
            while fnode != None and not key in fnode.goto:
                fnode = fnode.fail
            
            
            unode.fail = fnode.goto[key] if fnode else root
            """
            Pareil que : 
            if fnode:
                unode.fail = fnode.goto[key]
                
            else:
                unode.fail = root.goto[key]
            """    
            unode.out += unode.fail.out
            dot.edge(nohtml('<f0> '+str(rnode.goto.keys())+'|<f1> '+str(rnode.out)+'|<f2>.'), nohtml('<f0> '+str(unode.goto.keys())+'|<f1> '+str(unode.out)+'|<f2>.'), label=str(key))
            dot.edge(nohtml('<f0> '+str(unode.goto.keys())+'|<f1> '+str(unode.out)+'|<f2>.'), nohtml('<f0> '+str(unode.fail.goto.keys())+'|<f1> '+str(unode.fail.out)+'|<f2>.'), label="ε")

    global source    
    source = Source(dot.source, filename="graph.gv", format="png")
    
    
    return root
 

def toutes_occurrences(s, root, callback):
    node = root
 
    for i in range(len(s)):
        while node != None and not s[i] in node.goto:
            node = node.fail
        if node == None:
            node = root
            continue
        node = node.goto[s[i]]
        for pattern in node.out:
            callback(i - len(pattern) + 1, pattern)
 

def occurence(pos, patterns):
    print ("Le %s est touvé à la position %s" % (patterns, pos))
    global msg
    msg += ">   Le \'"+str(patterns)+"\' est touvé à la position "+str(pos)+" \n"
 

def ahocorasick(s, patterns):
    global tmp5, tmp3, tmp4
    
    tmp1 = clock()
    root = automate(patterns)
    tmp2 = clock()
    
    tmp3 = clock()
    toutes_occurrences(s, root, occurence)
    tmp4 = clock()
    tmp5 = tmp4-tmp3+tmp2-tmp1
    """
    print("1.   %s" % (tmp2-tmp1))
    print("2.   %s" % (tmp4-tmp3))
    print("3.   %s" % (tmp5))
    """

def graphe():
    
    global s, patt1, patt2, patt3,patt4, patt5, patt
    global stat
    
    
    lst1, lst2, lst3, lst4, lst5 = [], [], [], [], []
    
    for i in range(len(patt)):
        
        t1 = clock()
        d1 = fct1(s,patt[i])
        t1 = clock() - t1
        t2 = clock()
        #d2 = fct2(s,patt[i])
        t2 = clock() - t2
        t3 = clock()
        d3 = fct3(s,patt[i])
        t3 = clock() - t3
        t4 = clock() 
        #d4 = fct4(s,patt[i])
        t4 = clock() - t4
        t5 = clock()
        ahocorasick(s,patt[i])
        t5 = clock() - t5 

        lst1.append(t1)
        lst2.append(t2)
        lst3.append(t3)
        lst4.append(t4)
        lst5.append(tmp4-tmp3)
    stat = [lst1, lst2, lst3, lst4, lst5]
    print("######    ",len(stat))


if __name__ == "__main__":

    b1, b2 = False, False
    msg = ""
    pref = []
    stat = []
    

    pat1 = ['a', 'ab', 'abc', 'bc', 'c', 'cba']
    pat2 = ['ac', 'a', 'acb', 'ba']
    pat3 = ['a', 'ab', 'abc', 'bc', 'c', 'cba', 'cb','ba']

    patt1 = ['at', 'ct']
    patt2 = ['agt', 'ctcc', 'acct']
    patt3 = ['agtc', 'gtg', 'tgac', 'ccgt', 'tccg']
    patt4 = ['agg', 'ccta', 'ta', 'gt', 'tca', 'gacct']
    patt5 = ['gctccgt', 'tccgtac', 'gacct', 'gtgacct', 'acct', 'gccgt', 'gct']
    

    s1 = "abcba"
    s2 = "bacbac"
    s3 = "agctccgtgacct"
    #s = "agcgtcctgct"
    s = s3
    patterns = pat3
    patt = [patt1 , patt2, patt3, patt4, patt5]
    x = [1,2,3,4,5]
    #patt = [pat1 , pat2, pat3]
    #x = [1,2,3]
    r = arbre(patterns)
    pref = prefixe(r)

    ahocorasick(s2, pat2)
    
    graphe()

    app = QApplication(sys.argv)
    win = window()
    win.self.show()
    sys.exit(app.exec_())
    
