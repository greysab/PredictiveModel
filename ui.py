# # Copyright (C) 2016-2017 {Sabrina Amrouche} <{as_amrouche@esi.dz}>
#
# Created by: PyQt4 UI code generator 4.11.4 for GUI
#
# Requires:
#   PyQt4
#   Apscheduler
#   Scikit-learn

from time import gmtime, strftime
from PyQt4 import QtCore, QtGui
import sys
import webbrowser
import glob
from sklearn.externals import joblib
import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from matplotlib.figure import Figure
from datetime import datetime, date
from NN_pred import live_prediction, set_stop, get_stop, readR
from datetime import datetime
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)


        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #Accuracy chart
        self.dpi = 100
        self.fig = Figure((3.0, 2.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.centralwidget)
        self.axes = self.fig.add_subplot(111)
        y=[100,80,79,69,79,78,75]
        self.axes.get_xaxis().set_visible(False)
        self.axes.set_axis_bgcolor('black')
        self.fig.suptitle('Accuracy chart', fontsize=15)
        self.canvas.setGeometry(QtCore.QRect(0, 300, 350, 250))


        self.textEdit_live = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_live.setGeometry(QtCore.QRect(230, 20, 220, 31))
        self.textEdit_live.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_live.setText('C:\Users\Administrator\Desktop\Check NN\LV1.txt')


        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 70, 220, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setText('/home/learning/')
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 191, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_live = QtGui.QLabel(self.centralwidget)
        self.label_live.setGeometry(QtCore.QRect(20, 30, 191, 16))
        self.label_live.setObjectName(_fromUtf8("label_live"))


        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 211, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 120, 220, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_2.setText('C:\Users\Administrator\Desktop\Check NN\B6.txt')
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 211, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.textEdit_3 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(230, 170, 220, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_3.setText("C:\Users\Administrator\Desktop\dist\datafiles")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 211, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.label_log = QtGui.QLabel(self.centralwidget)
        self.label_log.setGeometry(QtCore.QRect(20, 270, 211, 16))
        self.label_log.setObjectName(_fromUtf8("label_log"))

        self.timeEdit = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(230, 220, 118, 27))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.timeEdit.setTime(QtCore.QTime(23, 00, 00)) 


        self.timeLog = QtGui.QTextEdit(self.centralwidget)
        self.timeLog.setGeometry(QtCore.QRect(230, 270, 118, 27))
        self.timeLog.setObjectName(_fromUtf8("timeLog"))
        self.timeLog.setText("24") 

        self.trainButton = QtGui.QPushButton(self.centralwidget)
        self.trainButton.setGeometry(QtCore.QRect(370, 220, 50, 30))

        self.okButton = QtGui.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(480, 110, 50, 30))

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 226, 121, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 255, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(82, 228, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 101, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 135, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 228, 146))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 255, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(82, 228, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 101, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 135, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 228, 146))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 101, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 255, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(82, 228, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 101, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 135, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 101, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 101, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 128, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 202, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton.setPalette(palette)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)

        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(400, 410, 350, 121))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))


        self.okButton.setStyleSheet(_fromUtf8("background-color: grey;"))
        self.okButton.setObjectName(_fromUtf8("pushButton"))
        self.okButton.clicked.connect(self.updateLog)
        self.okButton.setStatusTip('OK')


        self.trainButton.setStyleSheet(_fromUtf8("background-color: grey;"))
        self.trainButton.setObjectName(_fromUtf8("pushButton"))
        self.trainButton.clicked.connect(self.train_model)
        self.trainButton.setStatusTip('Train model')

        self.pushButton.setStyleSheet(_fromUtf8("background-color: green;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textBrowser.setText('Logs window')

        self.pushButton.clicked.connect(self.live_predictions)
        self.pushButton.setStatusTip('Start model')


        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 300, 121, 51))
        self.pushButton_2.clicked.connect(self.stop_model)
        self.pushButton_2.setStatusTip('Stop model')
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 255, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(82, 228, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 101, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 135, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 228, 146))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 255, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(82, 228, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 101, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 135, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 228, 146))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 101, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 255, 96))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(82, 228, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 101, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 135, 25))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 101, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(27, 101, 19))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(54, 202, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.pushButton_2.setPalette(palette)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: red;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 380, 211, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))

      
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))

        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()

        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        
        self.actionHelp.triggered.connect(self.openReport)

        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())


        curent_t = self.timeEdit.time().toPyTime()
  
        duration =datetime.combine(date.min,curent_t)- datetime.combine(date.min,QTime.currentTime().toPyTime()) 
        print duration.total_seconds()
        self.timer = QTimer(self)
        self.timer.start(1000*duration.total_seconds())
        self.timer.timeout.connect(self.train_model)
        self.timer.setSingleShot(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openReport(self):

        webbrowser.open_new(r'report.pdf')

    def live_predictions(self):
        gui_log(self,'Starting live prediction',strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        QtGui.QApplication.processEvents()
        live_prediction(self,self.textEdit_live.toPlainText(),self.textEdit_2.toPlainText(),get_stop,QtGui.QApplication)
        
    #offline test    
    def start_model(self):       
        gui_log(self,'Building predictive model',strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        QtGui.QApplication.processEvents()
        features=np.load('features.npy')
        y=np.load('target.npy')[:10000]
        X=features[:10000]
        gui_log(self,'Data loaded',strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        QtGui.QApplication.processEvents()
        clf = joblib.load('model/SVM/SVM_model.pkl')
        s=int(len(X)*0.7)
        X_test = X[s:]
        y_test = y[s:]
        prediction = clf.predict(X_test)
        accuracy = np.mean((prediction > .5) == y_test)
        gui_log(self,'model buit with accuracy '+str(100*round(accuracy,2))+' %',strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        
   
    def train_model(self):

        accu=[]
        gui_log(self,'Training model',strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        QtGui.QApplication.processEvents()
        
        rfiles= glob.glob(str(self.textEdit_3.toPlainText())+"\*.txt")
        
        fea=[]
        t=[]
        for f,s in zip(rfiles,range(len(rfiles))):
            print f
            features,target=readR(f)
            
            if len(features)>1 and 1 in target: 
                gui_log(self,'Evening data loaded',strftime("%Y-%m-%d %H:%M:%S", gmtime()))
                QtGui.QApplication.processEvents()
                fea.append(features)
                t.append(target)
                accuracy=learnSVM(features,target,save=False)
                print "retrained for file "+str(s+1)+" of "+str(len(rfiles))
            gui_log(self,'Model retrained with accuracy  '+str(100*round(accuracy,2))+' %',strftime("%Y-%m-%d %H:%M:%S", gmtime()))          
            QtGui.QApplication.processEvents()
            accu.append(100*round(accuracy,2))
            self.axes.plot(accu,'r--')
            self.canvas.draw()
        gui_log(self,'Training finished ',strftime("%Y-%m-%d %H:%M:%S", gmtime()))          
        QtGui.QApplication.processEvents()
        self.timer.stop()
        
        curent_t = self.timeEdit.time().toPyTime()
        duration =datetime.combine(date.min,curent_t)- datetime.combine(date.min,QTime.currentTime().toPyTime())
        print duration
        self.timer.start(1000*duration.seconds)#(3600*duration.hour+duration.minute*60+duration.seconds))
        gui_log(self,'Training again in '+str(duration.seconds//3600)+"H"+str(duration.seconds%3600/60.0)+"mn",strftime("%Y-%m-%d %H:%M:%S", gmtime()))          
        QtGui.QApplication.processEvents()
         

    def stop_model(self):
        gui_log(self,'Model stopped',strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        set_stop()
    def over(self):
        gui_log(self,'All predictions written',strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        QtGui.QApplication.processEvents()
    def updateLog(self):

        logs = [line.rstrip('\n') for line in open("logs.txt")]
        t1=logs[0][1:20]
        t2=logs[-1][1:20]
        diff= datetime.strptime(t2,"%Y-%m-%d %H:%M:%S")-datetime.strptime(t1,"%Y-%m-%d %H:%M:%S")
        if int(diff.total_seconds()/3600) >= int(self.timeLog.toPlainText()):
            with open("logs.txt", 'w') as b:
                b.write('['+str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))+'] '+"cleared"+"\n")
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_live.setText(_translate("MainWindow", "Live file", None))
        self.label.setText(_translate("MainWindow", "Learning workbooks", None))
        self.label_2.setText(_translate("MainWindow", "Prediction file", None))
        self.label_3.setText(_translate("MainWindow", "Training files", None))
        self.label_4.setText(_translate("MainWindow", "Learning time", None))
        self.label_log.setText(_translate("MainWindow", "Log clearing", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        self.trainButton.setText(_translate("MainWindow", "Train", None))
        self.okButton.setText(_translate("MainWindow", "OK", None))


        self.pushButton_2.setText(_translate("MainWindow", "Stop", None))
        self.label_5.setText(_translate("MainWindow", "Log screen", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))

        self.actionClose.setText(_translate("MainWindow", "Close", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))

def gui_log(self,text,timestamp=''):
    self.textBrowser.append('['+timestamp+'] '+text)
    with open("logs.txt", 'a') as b:
            b.write('['+str(timestamp)+'] '+str(text)+"\n")

def split_set(x,y,pourcentage=0.7):
    D=int(len(x)*pourcentage)
    return x[:D],x[D:],y[:D],y[D:]
def learnSVM(x,y,save=False):

    x_train,x_test,y_train,y_test=split_set(x,y)

    clf=joblib.load('model/SVM/SVM_model.pkl')
    print "model loaded"
    clf.fit(x_train, y_train)
    print "retrained"
    y_predicted = clf.predict(x_test)
    accuracy= np.mean((y_predicted > .5) == y_test)
    #Persist
    if save==True:
        joblib.dump(clf, 'model/SVM/SVM_model.pkl')
    return accuracy 


class MyWindow(QtGui.QMainWindow):
    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self,
                                            "Confirm Exit",
                                            "Are you sure you want to exit ?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        event.ignore()

        if result == QtGui.QMessageBox.Yes:
            event.accept()


if __name__ == "__main__":

        app = QtGui.QApplication(sys.argv)
        MainWindow = MyWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)


        
        MainWindow.setWindowTitle('Predictive model 1.0')
        MainWindow.show()
        sys.exit(app.exec_())
