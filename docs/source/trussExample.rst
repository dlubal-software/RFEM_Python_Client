2D Truss Generator Example
==============================

.. image:: pics/trussEx.png
    :width: 750px
    :align: center
    :height: 400px
    :alt: alternate text

This examples shows, how to create a GUI which user can configure a 2 dimensional Truss::

   import os

   import sys
   
   try:
       from PyQt5 import QtCore, QtGui, QtWidgets
   except:
       print('PyQt5 library is not installed in your Python env.')
       instPyQt5 = input('Do you want to install it (y/n)? ')
       instPyQt5 = instPyQt5.lower()
       if instPyQt5 == 'y':
           import subprocess
           try:
               subprocess.call('python -m pip install PyQt5 --user')
           except:
               print('WARNING: Installation of PyQt5 library failed!')
               print('Please use command "pip install PyQt5 --user" in your Command Prompt.')
               input('Press Enter to exit...')
               sys.exit()
       else:
           input('Press Enter to exit...')
           sys.exit()
   
   try:
       import qdarkstyle
   except:
       print('qdarkstyle library is not installed in your Python env.')
       instqdark = input('Do you want to install it (y/n)? ')
       instqdark = instPyQt5.lower()
       if instqdark == 'y':
           import subprocess
           try:
               subprocess.call('python -m pip install qdarkstyle')
           except:
               print('WARNING: Installation of qdarkstyle library failed!')
               print('Please use command "pip install qdarkstyle" in your Command Prompt.')
               input('Press Enter to exit...')
               sys.exit()
       else:
           input('Press Enter to exit...')
           sys.exit()
   
   try:
       import numpy as np
   except:
       print('numpy library is not installed in your Python env.')
       instqdark = input('Do you want to install it (y/n)? ')
       instqdark = instPyQt5.lower()
       if instqdark == 'y':
           import subprocess
           try:
               subprocess.call('python -m pip install numpy')
           except:
               print('WARNING: Installation of numpy library failed!')
               print('Please use command "pip install numpy" in your Command Prompt.')
               input('Press Enter to exit...')
               sys.exit()
       else:
           input('Press Enter to exit...')
           sys.exit()
   
   baseName = os.path.basename(__file__)
   dirName = os.path.dirname(__file__)
   print('basename:    ', baseName)
   print('dirname:     ', dirName)
   sys.path.append(dirName + r'/../..')
   from RFEM.enums import *
   from RFEM.window import *
   from RFEM.dataTypes import *
   from RFEM.initModel import *
   from RFEM.BasicObjects.material import *
   from RFEM.BasicObjects.section import *
   from RFEM.BasicObjects.thickness import *
   from RFEM.BasicObjects.node import *
   from RFEM.BasicObjects.line import *
   from RFEM.BasicObjects.member import *
   from RFEM.BasicObjects.surface import *
   from RFEM.BasicObjects.solid import *
   from RFEM.BasicObjects.opening import *
   from RFEM.BasicObjects.lineSet import *
   from RFEM.BasicObjects.memberSet import *
   from RFEM.BasicObjects.surfaceSet import *
   from RFEM.BasicObjects.solidSet import *
   from RFEM.TypesForNodes.nodalSupport import *
   from RFEM.TypesForMembers.memberHinge import *
   from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
   from RFEM.LoadCasesAndCombinations.loadCase import *
   from RFEM.Loads.nodalLoad import *
   from RFEM.Loads.memberLoad import *
   from RFEM.Loads.surfaceLoad import *
   
   class Ui_MainWindow(object):
       def setupUi(self, MainWindow):
           MainWindow.setObjectName("MainWindow")
           MainWindow.resize(858, 407)
           palette = QtGui.QPalette()
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
           brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
           brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
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
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
           brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
           brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
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
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
           brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
           brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
           brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
           brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
           brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
           brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
           brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
           brush.setStyle(QtCore.Qt.SolidPattern)
           palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
           MainWindow.setPalette(palette)
           font = QtGui.QFont()
           font.setFamily("Segoe UI")
           font.setPointSize(9)
           MainWindow.setFont(font)
           icon = QtGui.QIcon()
           icon.addPixmap(QtGui.QPixmap(dirName+"/sources/logo_round.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           MainWindow.setWindowIcon(icon)
           MainWindow.setWindowOpacity(1.0)
           MainWindow.setAutoFillBackground(False)
           MainWindow.setStyleSheet("foreground\": \"#eff0f1;\n"
   "background\": \"#31363b")
           MainWindow.setDocumentMode(False)
           self.centralwidget = QtWidgets.QWidget(MainWindow)
           self.centralwidget.setObjectName("centralwidget")
           self.frame = QtWidgets.QFrame(self.centralwidget)
           self.frame.setGeometry(QtCore.QRect(20, 10, 191, 341))
           self.frame.setFrameShape(QtWidgets.QFrame.Box)
           self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.frame.setLineWidth(2)
           self.frame.setObjectName("frame")
           self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
           self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 171, 321))
           self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
           self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
           self.verticalLayout.setContentsMargins(0, 0, 0, 0)
           self.verticalLayout.setObjectName("verticalLayout")
           self.truss_1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
           self.truss_1.setText("")
           icon1 = QtGui.QIcon()
           icon1.addPixmap(QtGui.QPixmap(dirName+"/sources/truss_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.truss_1.setIcon(icon1)
           self.truss_1.setIconSize(QtCore.QSize(150, 32))
           self.truss_1.setObjectName("truss_1")
           self.verticalLayout.addWidget(self.truss_1)
           self.truss_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
           self.truss_2.setText("")
           icon2 = QtGui.QIcon()
           icon2.addPixmap(QtGui.QPixmap(dirName+"/sources/truss_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.truss_2.setIcon(icon2)
           self.truss_2.setIconSize(QtCore.QSize(150, 32))
           self.truss_2.setObjectName("truss_2")
           self.verticalLayout.addWidget(self.truss_2)
           self.truss_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
           self.truss_3.setText("")
           icon3 = QtGui.QIcon()
           icon3.addPixmap(QtGui.QPixmap(dirName+"/sources/truss_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.truss_3.setIcon(icon3)
           self.truss_3.setIconSize(QtCore.QSize(150, 32))
           self.truss_3.setObjectName("truss_3")
           self.verticalLayout.addWidget(self.truss_3)
           self.truss_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
           self.truss_4.setText("")
           icon4 = QtGui.QIcon()
           icon4.addPixmap(QtGui.QPixmap(dirName+"/sources/truss_4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.truss_4.setIcon(icon4)
           self.truss_4.setIconSize(QtCore.QSize(250, 40))
           self.truss_4.setObjectName("truss_4")
           self.verticalLayout.addWidget(self.truss_4)
           self.truss_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
           self.truss_5.setText("")
           icon5 = QtGui.QIcon()
           icon5.addPixmap(QtGui.QPixmap(dirName+"/sources/truss_5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.truss_5.setIcon(icon5)
           self.truss_5.setIconSize(QtCore.QSize(250, 50))
           self.truss_5.setObjectName("truss_5")
           self.verticalLayout.addWidget(self.truss_5)
           self.frame_2 = QtWidgets.QFrame(self.centralwidget)
           self.frame_2.setGeometry(QtCore.QRect(220, 10, 631, 131))
           self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
           self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.frame_2.setLineWidth(2)
           self.frame_2.setObjectName("frame_2")
           self.gridLayoutWidget = QtWidgets.QWidget(self.frame_2)
           self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 108))
           self.gridLayoutWidget.setObjectName("gridLayoutWidget")
           self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
           self.gridLayout.setContentsMargins(0, 0, 0, 0)
           self.gridLayout.setObjectName("gridLayout")
           self.diag_5 = QtWidgets.QRadioButton(self.gridLayoutWidget)
           self.diag_5.setMinimumSize(QtCore.QSize(150, 50))
           self.diag_5.setMaximumSize(QtCore.QSize(130, 50))
           self.diag_5.setText("")
           icon6 = QtGui.QIcon()
           icon6.addPixmap(QtGui.QPixmap(dirName+"/sources/diag_5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.diag_5.setIcon(icon6)
           self.diag_5.setIconSize(QtCore.QSize(120, 32))
           self.diag_5.setObjectName("diag_5")
           self.gridLayout.addWidget(self.diag_5, 0, 2, 1, 1)
           self.diag_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
           self.diag_2.setMinimumSize(QtCore.QSize(150, 50))
           self.diag_2.setMaximumSize(QtCore.QSize(130, 50))
           self.diag_2.setText("")
           icon7 = QtGui.QIcon()
           icon7.addPixmap(QtGui.QPixmap(dirName+"/sources/diag_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.diag_2.setIcon(icon7)
           self.diag_2.setIconSize(QtCore.QSize(120, 32))
           self.diag_2.setObjectName("diag_2")
           self.gridLayout.addWidget(self.diag_2, 1, 0, 1, 1)
           self.diag_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
           self.diag_4.setMinimumSize(QtCore.QSize(150, 50))
           self.diag_4.setMaximumSize(QtCore.QSize(130, 50))
           self.diag_4.setText("")
           icon8 = QtGui.QIcon()
           icon8.addPixmap(QtGui.QPixmap(dirName+"/sources/diag_4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.diag_4.setIcon(icon8)
           self.diag_4.setIconSize(QtCore.QSize(120, 32))
           self.diag_4.setObjectName("diag_4")
           self.gridLayout.addWidget(self.diag_4, 1, 1, 1, 1)
           self.diag_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
           self.diag_3.setMinimumSize(QtCore.QSize(150, 50))
           self.diag_3.setMaximumSize(QtCore.QSize(130, 50))
           self.diag_3.setText("")
           icon9 = QtGui.QIcon()
           icon9.addPixmap(QtGui.QPixmap(dirName+"/sources/diag_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.diag_3.setIcon(icon9)
           self.diag_3.setIconSize(QtCore.QSize(120, 32))
           self.diag_3.setObjectName("diag_3")
           self.gridLayout.addWidget(self.diag_3, 0, 1, 1, 1)
           self.diag_6 = QtWidgets.QRadioButton(self.gridLayoutWidget)
           self.diag_6.setMinimumSize(QtCore.QSize(150, 50))
           self.diag_6.setMaximumSize(QtCore.QSize(130, 50))
           self.diag_6.setText("")
           icon10 = QtGui.QIcon()
           icon10.addPixmap(QtGui.QPixmap(dirName+"/sources/diag_6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.diag_6.setIcon(icon10)
           self.diag_6.setIconSize(QtCore.QSize(120, 32))
           self.diag_6.setObjectName("diag_6")
           self.gridLayout.addWidget(self.diag_6, 1, 2, 1, 1)
           self.diag_1 = QtWidgets.QRadioButton(self.gridLayoutWidget)
           self.diag_1.setMinimumSize(QtCore.QSize(150, 50))
           self.diag_1.setMaximumSize(QtCore.QSize(130, 50))
           self.diag_1.setText("")
           icon11 = QtGui.QIcon()
           icon11.addPixmap(QtGui.QPixmap(dirName+"/sources/diag_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.diag_1.setIcon(icon11)
           self.diag_1.setIconSize(QtCore.QSize(120, 32))
           self.diag_1.setObjectName("diag_1")
           self.gridLayout.addWidget(self.diag_1, 0, 0, 1, 1)
           self.diag_7 = QtWidgets.QRadioButton(self.gridLayoutWidget)
           self.diag_7.setMinimumSize(QtCore.QSize(150, 50))
           self.diag_7.setMaximumSize(QtCore.QSize(130, 50))
           self.diag_7.setText("")
           icon12 = QtGui.QIcon()
           icon12.addPixmap(QtGui.QPixmap(dirName+"/sources/diag_7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
           self.diag_7.setIcon(icon12)
           self.diag_7.setIconSize(QtCore.QSize(120, 32))
           self.diag_7.setObjectName("diag_7")
           self.gridLayout.addWidget(self.diag_7, 0, 3, 1, 1)
           self.diag_8 = QtWidgets.QRadioButton(self.gridLayoutWidget)
           self.diag_8.setMinimumSize(QtCore.QSize(150, 50))
           self.diag_8.setMaximumSize(QtCore.QSize(130, 50))
           font = QtGui.QFont()
           font.setFamily("Verdana")
           font.setPointSize(8)
           self.diag_8.setFont(font)
           self.diag_8.setText("No Diagonals")
           self.diag_8.setIconSize(QtCore.QSize(120, 32))
           self.diag_8.setObjectName("diag_8")
           self.gridLayout.addWidget(self.diag_8, 1, 3, 1, 1)
           self.frame_3 = QtWidgets.QFrame(self.centralwidget)
           self.frame_3.setGeometry(QtCore.QRect(220, 150, 281, 201))
           self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
           self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.frame_3.setLineWidth(2)
           self.frame_3.setMidLineWidth(0)
           self.frame_3.setObjectName("frame_3")
           self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
           self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 241, 171))
           self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
           self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
           self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
           self.verticalLayout_2.setObjectName("verticalLayout_2")
           self.horizontalLayout = QtWidgets.QHBoxLayout()
           self.horizontalLayout.setObjectName("horizontalLayout")
           self.bay_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
           font = QtGui.QFont()
           font.setFamily("Verdana")
           font.setPointSize(8)
           self.bay_label.setFont(font)
           self.bay_label.setObjectName("bay_label")
           self.horizontalLayout.addWidget(self.bay_label)
           self.bay_input = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
           self.bay_input.setObjectName("bay_input")
           self.horizontalLayout.addWidget(self.bay_input)
           self.verticalLayout_2.addLayout(self.horizontalLayout)
           self.line_17 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
           self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
           self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_17.setObjectName("line_17")
           self.verticalLayout_2.addWidget(self.line_17)
           self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
           self.horizontalLayout_2.setObjectName("horizontalLayout_2")
           self.length_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
           font = QtGui.QFont()
           font.setFamily("Verdana")
           self.length_label.setFont(font)
           self.length_label.setObjectName("length_label")
           self.horizontalLayout_2.addWidget(self.length_label)
           self.length_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
           self.length_input.setObjectName("length_input")
           self.horizontalLayout_2.addWidget(self.length_input)
           self.verticalLayout_2.addLayout(self.horizontalLayout_2)
           self.line_18 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
           self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
           self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_18.setObjectName("line_18")
           self.verticalLayout_2.addWidget(self.line_18)
           self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
           self.horizontalLayout_3.setObjectName("horizontalLayout_3")
           self.height_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
           font = QtGui.QFont()
           font.setFamily("Verdana")
           self.height_label.setFont(font)
           self.height_label.setObjectName("height_label")
           self.horizontalLayout_3.addWidget(self.height_label)
           self.height_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
           self.height_input.setObjectName("height_input")
           self.horizontalLayout_3.addWidget(self.height_input)
           self.verticalLayout_2.addLayout(self.horizontalLayout_3)
           self.line_20 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
           self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
           self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_20.setObjectName("line_20")
           self.verticalLayout_2.addWidget(self.line_20)
           self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
           self.horizontalLayout_4.setObjectName("horizontalLayout_4")
           self.height_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
           font = QtGui.QFont()
           font.setFamily("Verdana")
           self.height_label_2.setFont(font)
           self.height_label_2.setObjectName("height_label_2")
           self.horizontalLayout_4.addWidget(self.height_label_2)
           self.firstspan_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
           self.firstspan_input.setObjectName("firstspan_input")
           self.horizontalLayout_4.addWidget(self.firstspan_input)
           self.verticalLayout_2.addLayout(self.horizontalLayout_4)
           self.line_19 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
           self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
           self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_19.setObjectName("line_19")
           self.verticalLayout_2.addWidget(self.line_19)
           self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
           self.horizontalLayout_5.setObjectName("horizontalLayout_5")
           self.sideheight_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
           font = QtGui.QFont()
           font.setFamily("Verdana")
           self.sideheight_label.setFont(font)
           self.sideheight_label.setObjectName("sideheight_label")
           self.horizontalLayout_5.addWidget(self.sideheight_label)
           self.sideheight_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
           self.sideheight_input.setObjectName("sideheight_input")
           self.horizontalLayout_5.addWidget(self.sideheight_input)
           self.verticalLayout_2.addLayout(self.horizontalLayout_5)
           self.frame_4 = QtWidgets.QFrame(self.centralwidget)
           self.frame_4.setGeometry(QtCore.QRect(520, 150, 331, 201))
           self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
           self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.frame_4.setLineWidth(2)
           self.frame_4.setObjectName("frame_4")
           self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame_4)
           self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 291, 173))
           self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
           self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
           self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
           self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
           self.gridLayout_2.setObjectName("gridLayout_2")
           self.line_12 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
           self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_12.setObjectName("line_12")
           self.gridLayout_2.addWidget(self.line_12, 6, 1, 1, 1)
           self.upperchord_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
           font = QtGui.QFont()
           font.setFamily("Verdana")
           self.upperchord_label.setFont(font)
           self.upperchord_label.setObjectName("upperchord_label")
           self.gridLayout_2.addWidget(self.upperchord_label, 6, 0, 1, 1)
           self.verticals_mat = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
           self.verticals_mat.setObjectName("verticals_mat")
           self.gridLayout_2.addWidget(self.verticals_mat, 10, 4, 1, 1)
           self.diagonals_mat = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
           self.diagonals_mat.setObjectName("diagonals_mat")
           self.gridLayout_2.addWidget(self.diagonals_mat, 8, 4, 1, 1)
           self.verticals_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
           font = QtGui.QFont()
           font.setFamily("Verdana")
           self.verticals_label.setFont(font)
           self.verticals_label.setObjectName("verticals_label")
           self.gridLayout_2.addWidget(self.verticals_label, 10, 0, 1, 1)
           self.lowerchord_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
           font = QtGui.QFont()
           font.setFamily("Verdana")
           self.lowerchord_label.setFont(font)
           self.lowerchord_label.setObjectName("lowerchord_label")
           self.gridLayout_2.addWidget(self.lowerchord_label, 4, 0, 1, 1)
           self.line_7 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
           self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_7.setObjectName("line_7")
           self.gridLayout_2.addWidget(self.line_7, 4, 3, 1, 1)
           self.line_8 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
           self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_8.setObjectName("line_8")
           self.gridLayout_2.addWidget(self.line_8, 6, 3, 1, 1)
           self.upperchord_section = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
           self.upperchord_section.setObjectName("upperchord_section")
           self.gridLayout_2.addWidget(self.upperchord_section, 6, 2, 1, 1)
           self.line_6 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
           self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_6.setObjectName("line_6")
           self.gridLayout_2.addWidget(self.line_6, 0, 0, 1, 5)
           self.line_10 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
           self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_10.setObjectName("line_10")
           self.gridLayout_2.addWidget(self.line_10, 10, 3, 1, 1)
           self.diagonals_section = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
           self.diagonals_section.setObjectName("diagonals_section")
           self.gridLayout_2.addWidget(self.diagonals_section, 8, 2, 1, 1)
           self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
           self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_4.setObjectName("line_4")
           self.gridLayout_2.addWidget(self.line_4, 9, 0, 1, 5)
           self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
           font = QtGui.QFont()
           font.setFamily("Verdana")
           font.setPointSize(8)
           font.setBold(False)
           font.setWeight(50)
           self.label_5.setFont(font)
           self.label_5.setObjectName("label_5")
           self.gridLayout_2.addWidget(self.label_5, 1, 2, 1, 1)
           self.line = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line.setFrameShape(QtWidgets.QFrame.HLine)
           self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line.setObjectName("line")
           self.gridLayout_2.addWidget(self.line, 2, 0, 1, 5)
           self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
           font = QtGui.QFont()
           font.setFamily("Verdana")
           font.setPointSize(8)
           font.setBold(False)
           font.setWeight(50)
           self.label_7.setFont(font)
           self.label_7.setObjectName("label_7")
           self.gridLayout_2.addWidget(self.label_7, 1, 4, 1, 1)
           self.lowerchord_section = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
           self.lowerchord_section.setObjectName("lowerchord_section")
           self.gridLayout_2.addWidget(self.lowerchord_section, 4, 2, 1, 1)
           self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
           self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_2.setObjectName("line_2")
           self.gridLayout_2.addWidget(self.line_2, 5, 0, 1, 5)
           self.line_14 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
           self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_14.setObjectName("line_14")
           self.gridLayout_2.addWidget(self.line_14, 10, 1, 1, 1)
           self.line_11 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
           self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_11.setObjectName("line_11")
           self.gridLayout_2.addWidget(self.line_11, 1, 3, 1, 1)
           self.line_15 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
           self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_15.setObjectName("line_15")
           self.gridLayout_2.addWidget(self.line_15, 4, 1, 1, 1)
           self.line_9 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
           self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_9.setObjectName("line_9")
           self.gridLayout_2.addWidget(self.line_9, 8, 3, 1, 1)
           self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
           self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_3.setObjectName("line_3")
           self.gridLayout_2.addWidget(self.line_3, 7, 0, 1, 5)
           self.line_16 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
           self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_16.setObjectName("line_16")
           self.gridLayout_2.addWidget(self.line_16, 1, 1, 1, 1)
           self.diagonals_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
           font = QtGui.QFont()
           font.setFamily("Verdana")
           self.diagonals_label.setFont(font)
           self.diagonals_label.setObjectName("diagonals_label")
           self.gridLayout_2.addWidget(self.diagonals_label, 8, 0, 1, 1)
           self.verticals_section = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
           self.verticals_section.setObjectName("verticals_section")
           self.gridLayout_2.addWidget(self.verticals_section, 10, 2, 1, 1)
           self.lowerchord_mat = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
           self.lowerchord_mat.setObjectName("lowerchord_mat")
           self.gridLayout_2.addWidget(self.lowerchord_mat, 4, 4, 1, 1)
           self.upperchord_mat = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
           self.upperchord_mat.setObjectName("upperchord_mat")
           self.gridLayout_2.addWidget(self.upperchord_mat, 6, 4, 1, 1)
           self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
           self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_5.setObjectName("line_5")
           self.gridLayout_2.addWidget(self.line_5, 11, 0, 1, 5)
           self.line_13 = QtWidgets.QFrame(self.gridLayoutWidget_2)
           self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
           self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
           self.line_13.setObjectName("line_13")
           self.gridLayout_2.addWidget(self.line_13, 8, 1, 1, 1)
           self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
           self.horizontalLayoutWidget.setGeometry(QtCore.QRect(690, 360, 160, 25))
           self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
           self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
           self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
           self.horizontalLayout_10.setObjectName("horizontalLayout_10")
           self.create_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
           self.create_button.setObjectName("create_button")
           self.horizontalLayout_10.addWidget(self.create_button)
           self.done_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
           self.done_button.setObjectName("done_button")
           self.horizontalLayout_10.addWidget(self.done_button)
           MainWindow.setCentralWidget(self.centralwidget)
           self.statusbar = QtWidgets.QStatusBar(MainWindow)
           self.statusbar.setObjectName("statusbar")
   
           # Tab Order
           MainWindow.setStatusBar(self.statusbar)
           MainWindow.setTabOrder(self.sideheight_input, self.lowerchord_section)
           MainWindow.setTabOrder(self.lowerchord_section, self.upperchord_section)
           MainWindow.setTabOrder(self.upperchord_section, self.diagonals_section)
           MainWindow.setTabOrder(self.diagonals_section, self.verticals_section)
           MainWindow.setTabOrder(self.verticals_section, self.lowerchord_mat)
           MainWindow.setTabOrder(self.lowerchord_mat, self.upperchord_mat)
           MainWindow.setTabOrder(self.upperchord_mat, self.diagonals_mat)
           MainWindow.setTabOrder(self.diagonals_mat, self.verticals_mat)
   
           # Default Values
           self.truss_1.setChecked(True)
           self.diag_1.setChecked(True)
           self.bay_input.setValue(4)
           self.length_input.setText("24")
           self.height_input.setText("6")
           self.sideheight_input.setText("3")
           self.firstspan_input.setText("4")
   
           self.lowerchord_section.setText("IPE 200")
           self.upperchord_section.setText("IPE 140")
           self.diagonals_section.setText("CHS 76.1x3")
           self.verticals_section.setText("CHS 88.9x4")
   
           self.lowerchord_mat.setText("S235")
           self.upperchord_mat.setText("S235")
           self.diagonals_mat.setText("S235")
           self.verticals_mat.setText("S235")
   
           self.create_button.clicked.connect(self.click)
           self.done_button.clicked.connect(self.close)
   
           self.retranslateUi(MainWindow)
           QtCore.QMetaObject.connectSlotsByName(MainWindow)
   
       def retranslateUi(self, MainWindow):
           _translate = QtCore.QCoreApplication.translate
           MainWindow.setWindowTitle(_translate("MainWindow", "2D Truss Generator"))
           self.bay_label.setText(_translate("MainWindow", "Number of Bays:\t"))
           self.length_label.setText(_translate("MainWindow", "Total Length (m):\t"))
           self.height_label.setText(_translate("MainWindow", "Total Height (m):\t"))
           self.height_label_2.setText(_translate("MainWindow", "First Span (m):\t"))
           self.sideheight_label.setText(_translate("MainWindow", "Side Height (m):\t"))
           self.upperchord_label.setText(_translate("MainWindow", "Upper Chord"))
           self.verticals_label.setText(_translate("MainWindow", "Verticals      "))
           self.lowerchord_label.setText(_translate("MainWindow", "Lower Chord"))
           self.label_5.setText(_translate("MainWindow", " Cross Section"))
           self.label_7.setText(_translate("MainWindow", "  Material"))
           self.diagonals_label.setText(_translate("MainWindow", "Diagonals    "))
           self.create_button.setText(_translate("MainWindow", "Create Model"))
           self.done_button.setText(_translate("MainWindow", "Close"))
   
       def click(self):
   
           upper_chord_material = self.upperchord_mat.text()
           lower_chord_material = self.lowerchord_mat.text()
           diagonal_material = self.diagonals_mat.text()
           vertical_material = self.verticals_mat.text()
           upper_chord_section = self.upperchord_section.text()
           lower_chord_section = self.lowerchord_section.text()
           diagonal_section = self.diagonals_section.text()
           vertical_section = self.verticals_section.text()
           number_of_bays = int(self.bay_input.text())
           total_length = float(self.length_input.text())
           total_height = float(self.height_input.text())
           first_span = float(self.firstspan_input.text())
           side_height = float(self.sideheight_input.text())
   
           allGood = True
   
           if Model.clientModel is None:
               Model(True, "MyTruss")
   
           Model.clientModel.service.delete_all()
           Model.clientModel.service.begin_modification()
           # Create Materials
           try:
               Material(1, upper_chord_material)
               Material(2, lower_chord_material)
               Material(3, diagonal_material)
               Material(4, vertical_material)
               # Create Sections
               try:
                   Section(1, upper_chord_section, 1)
                   Section(2, lower_chord_section, 2)
                   Section(3, diagonal_section, 3)
                   Section(4, vertical_section, 4)
               except:
                   allGood = False
                   msg = QtWidgets.QMessageBox()
                   msg.setIcon(QtWidgets.QMessageBox.Critical)
                   msg.setText("WARNING")
                   msg.setInformativeText("WARNING: Please enter valid section values.")
                   msg.setWindowTitle("WARNING")
                   msg.exec_()
   
           except:
               allGood = False
               msg = QtWidgets.QMessageBox()
               msg.setIcon(QtWidgets.QMessageBox.Critical)
               msg.setText("WARNING")
               msg.setInformativeText("WARNING: Please enter valid material values.")
               msg.setWindowTitle("WARNING")
               msg.exec_()
   
           Model.clientModel.service.finish_modification()
   
           if allGood:
               if self.truss_1.isChecked():
                   Model.clientModel.service.begin_modification()
   
                   # Create Nodes
                   x_nodes = np.repeat(np.arange(0, total_length + total_length/number_of_bays -0.1, total_length/number_of_bays), 2)
                   z_nodes = (0, (-total_height))*int((len(x_nodes)/2))
                   tag_nodes = np.arange(1, len(x_nodes)+1, 1)
   
                   for tag,x,z in zip(tag_nodes, x_nodes, z_nodes):
                       Node(tag, x, 0, z)
   
                   # Create Lower Chord
                   Member(1, 1, tag_nodes[-2], 0, 2, 2)
   
                   # Create Upper Chord
                   Member(2, 2, tag_nodes[-1], 0, 1, 1)
   
                   # Create Verticals
                   i = 1
                   j = 1
                   while j<len(tag_nodes) and i<len(tag_nodes):
                       Member.Truss(0, j+2, i, i+1, section_no=4)
                       i += 2
                       j += 1
   
                   # Create Diagonals
                   if self.diag_1.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1):
                           Member.Truss(0, j, i, i+3, section_no=3)
                           i +=2
                           j +=1
   
                   elif self.diag_2.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 2):
                           Member.Truss(0, j, i+1, i+2, section_no=3)
                           i +=2
                           j +=1
   
                   elif self.diag_3.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       k = 1
   
                       while i < len(tag_nodes) -1 and j < diagonal_tag[-1] +2  and k < len(tag_nodes) :
                           Member.Truss(0, j, i, i+3, section_no=3)
                           j += 1
                           Member.Truss(0, j, k+3, k+4, section_no=3)
                           i += 4
                           k += 4
                           j += 1
   
                   elif self.diag_4.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       k = 1
   
                       while i < len(tag_nodes) -1 and j < diagonal_tag[-1] +1  and k < len(tag_nodes) :
                           Member.Truss(0, j, i+2, i+5, section_no=3)
                           j += 1
                           Member.Truss(0, j, k+1, k+2, section_no=3)
                           i += 4
                           k += 4
                           j += 1
   
                   elif self.diag_5.isChecked():
                       if (number_of_bays % 2) == 0:
                           diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < ((tag_nodes[-1]/2) + 1) and j <diagonal_tag[-1] +1:
                               Member.Truss(0, j, i, i+3, section_no=3)
                               i += 2
                               j += 1
                           i = int(len(tag_nodes)/2) + 1
                           j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                           while i < tag_nodes[-1] and j <diagonal_tag[-1] +1:
                               Member.Truss(0, j, i, i+1, section_no=3)
                               i += 2
                               j += 1
                       else:
                           msg = QtWidgets.QMessageBox()
                           msg.setIcon(QtWidgets.QMessageBox.Critical)
                           msg.setText("WARNING")
                           msg.setInformativeText("WARNING: Please enter an even number of spans for a symmetrical net.")
                           msg.setWindowTitle("WARNING")
                           msg.exec_()
   
                   elif self.diag_6.isChecked():
                       if (number_of_bays % 2) == 0:
                           diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1] +1:
                               Member.Truss(0, j, i+1, i+2, section_no=3)
                               i += 2
                               j += 1
                           i = int(len(tag_nodes)/2)
                           j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                           while i < tag_nodes[-1] and j <diagonal_tag[-1] +1:
                               Member.Truss(0, j, i, i+3, section_no=3)
                               i += 2
                               j += 1
                       else:
                           msg = QtWidgets.QMessageBox()
                           msg.setIcon(QtWidgets.QMessageBox.Critical)
                           msg.setText("WARNING")
                           msg.setInformativeText("WARNING: Please enter an even number of spans for a symmetrical net.")
                           msg.setWindowTitle("WARNING")
                           msg.exec_()
   
                   elif self.diag_7.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1)*2:
                           Member.Truss(0, j, i, i+3, section_no=3)
                           j +=1
                           Member.Truss(0, j, i+1, i+2, section_no=3)
                           i +=2
                           j +=1
   
                   #elif self.diag_8.isChecked():
                   #    pass
   
                   Model.clientModel.service.finish_modification()
   
               elif self.truss_2.isChecked():
   
                   Model.clientModel.service.begin_modification()
   
                   # Create Nodes
                   x_nodes = np.repeat(np.arange(0, total_length + total_length/number_of_bays -0.1, total_length/number_of_bays), 2)
                   z_nodes = (0, (-total_height))*int((len(x_nodes)/2))
                   tag_nodes = np.arange(1, len(x_nodes)+1, 1)
   
                   for tag,x,z in zip(tag_nodes, x_nodes, z_nodes):
                       Node(tag, x, 0, z)
   
                   # Create Lower Chord
                   Member(1, 1, tag_nodes[-2], 0, 2, 2)
   
                   # Create Upper Chord
                   Member(2, 2, tag_nodes[-1], 0, 1, 1)
   
                   # Create Verticals
                   i = 1
                   j = 1
                   while j<len(tag_nodes) and i<len(tag_nodes):
                       Member.Truss(0, j+2, i, i+1, section_no=4)
                       i += 2
                       j += 1
   
                   # Create Diagonals
                   if self.diag_1.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       while i < len(tag_nodes) +2 and j < int(diagonal_tag[-1] + 2):
                           Member.Truss(0, j, i, i+3, section_no=3)
                           i +=2
                           j +=1
                       #Add first span
                       Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
                       Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)
   
                       Member((int(diagonal_tag[-1])+1), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
                       Member((int(diagonal_tag[-1])+2), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)
   
                       Member.Truss(0, (int(diagonal_tag[-1])+3), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
                       Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)
   
                   elif self.diag_2.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 2):
                           Member.Truss(0, j, i+1, i+2, section_no=3)
                           i +=2
                           j +=1
   
                       #Add first span
                       Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
                       Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)
   
                       Member((int(diagonal_tag[-1])+1), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
                       Member((int(diagonal_tag[-1])+2), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)
   
                       Member.Truss(0, (int(diagonal_tag[-1])+3), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
                       Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)
   
                   elif self.diag_3.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       k = 1
   
                       while i < len(tag_nodes) -1 and j < diagonal_tag[-1] +2  and k < len(tag_nodes) :
                           Member.Truss(0, j, i, i+3, section_no=3)
                           j += 1
                           Member.Truss(0, j, k+3, k+4, section_no=3)
                           i += 4
                           k += 4
                           j += 1
   
                       #Add first span
                       Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
                       Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)
   
                       Member((int(diagonal_tag[-1])+1), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
                       Member((int(diagonal_tag[-1])+2), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)
   
                       Member.Truss(0, (int(diagonal_tag[-1])+3), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
                       Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)
   
                   elif self.diag_4.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       k = 1
   
                       while i < len(tag_nodes) -1 and j < diagonal_tag[-1]+1  and k < len(tag_nodes) :
                           Member.Truss(0, j, i+2, i+5, section_no=3)
                           j += 1
                           Member.Truss(0, j, k+1, k+2, section_no=3)
                           i += 4
                           k += 4
                           j += 1
   
                       #Add first span
                       Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
                       Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)
   
                       Member((int(diagonal_tag[-1])+2), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
                       Member((int(diagonal_tag[-1])+3), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)
   
                       Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
                       Member.Truss(0, (int(diagonal_tag[-1])+5), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)
   
                   elif self.diag_5.isChecked():
                       if (number_of_bays % 2) == 0:
                           diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < ((tag_nodes[-1]/2) + 1) and j <diagonal_tag[-1] +1:
                               Member.Truss(0, j, i, i+3, section_no=3)
                               i += 2
                               j += 1
                           i = int(len(tag_nodes)/2) + 1
                           j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                           while i < tag_nodes[-1] and j <diagonal_tag[-1] +1:
                               Member.Truss(0, j, i, i+1, section_no=3)
                               i += 2
                               j += 1
                           #Add first span
                           Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
                           Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)
   
                           Member((int(diagonal_tag[-1])+2), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
                           Member((int(diagonal_tag[-1])+3), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)
   
                           Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
                           Member.Truss(0, (int(diagonal_tag[-1])+5), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)
                       else:
                           msg = QtWidgets.QMessageBox()
                           msg.setIcon(QtWidgets.QMessageBox.Critical)
                           msg.setText("WARNING")
                           msg.setInformativeText("WARNING: Please enter an even number of spans for a symmetrical net.")
                           msg.setWindowTitle("WARNING")
                           msg.exec_()
   
                   elif self.diag_6.isChecked():
                       if (number_of_bays % 2) == 0:
                           diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1] +1:
                               Member.Truss(0, j, i+1, i+2, section_no=3)
                               i += 2
                               j += 1
                           i = int(len(tag_nodes)/2)
                           j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                           while i < tag_nodes[-1] and j <diagonal_tag[-1] +1:
                               Member.Truss(0, j, i, i+3, section_no=3)
                               i += 2
                               j += 1
                           #Add first span
                           Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
                           Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)
   
                           Member((int(diagonal_tag[-1])+2), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
                           Member((int(diagonal_tag[-1])+3), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)
   
                           Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
                           Member.Truss(0, (int(diagonal_tag[-1])+5), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)
   
                       else:
                           msg = QtWidgets.QMessageBox()
                           msg.setIcon(QtWidgets.QMessageBox.Critical)
                           msg.setText("WARNING")
                           msg.setInformativeText("WARNING: Please enter an even number of spans for a symmetrical net.")
                           msg.setWindowTitle("WARNING")
                           msg.exec_()
   
                   elif self.diag_7.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1)*2:
                           Member.Truss(0, j, i, i+3, section_no=3)
                           j +=1
                           Member.Truss(0, j, i+1, i+2, section_no=3)
                           i +=2
                           j +=1
                       #Add first span
                       Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
                       Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)
   
                       Member((int(diagonal_tag[-1])*2+1), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
                       Member((int(diagonal_tag[-1])*2+2), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)
   
                       Member.Truss(0, (int(diagonal_tag[-1])*2+3), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
                       Member.Truss(0, (int(diagonal_tag[-1])*2+4), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)
   
                   elif self.diag_8.isChecked():
                       #Add first span
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays + 3, 1)
                       Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
                       Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)
   
                       Member((int(diagonal_tag[1])), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
                       Member((int(diagonal_tag[2])), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)
   
                       Member.Truss(0, (int(diagonal_tag[3])), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
                       Member.Truss(0, (int(diagonal_tag[3]) + 1), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)
   
                   Model.clientModel.service.finish_modification()
   
               elif self.truss_3.isChecked():
   
                   Model.clientModel.service.begin_modification()
   
                   # Create Nodes
                   x_nodes = np.repeat(np.arange(0, total_length + total_length/number_of_bays -0.1, total_length/number_of_bays), 2)
                   z_nodes = (0, (-total_height))*int((len(x_nodes)/2))
                   tag_nodes = np.arange(1, len(x_nodes)+1, 1)
   
                   for tag,x,z in zip(tag_nodes, x_nodes, z_nodes):
                       Node(tag, x, 0, z)
   
                   # Create Lower Chord
                   Member(1, 1, tag_nodes[-2], 0, 2, 2)
   
                   # Create Upper Chord
                   Member(2, 2, tag_nodes[-1], 0, 1, 1)
   
                   # Create Verticals
                   i = 1
                   j = 1
                   while j<len(tag_nodes) and i<len(tag_nodes):
                       Member.Truss(0, j+2, i, i+1, section_no=4)
                       i += 2
                       j += 1
   
                   # Create Diagonals
                   if self.diag_1.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1):
                           Member.Truss(0, j, i, i+3, section_no=3)
                           i +=2
                           j +=1
                       #Add first span
                       Node(tag_nodes[-1]+1, (-first_span), 0, 0)
                       Node(tag_nodes[-1]+2, (total_length+first_span), 0, 0)
   
                       Member((int(diagonal_tag[-1])+1), tag_nodes[0], tag_nodes[-1]+1, 0, 1, 1, 0, 0)
                       Member((int(diagonal_tag[-1])+2), tag_nodes[-2], tag_nodes[-1]+2, 0, 2, 2, 0, 0)
   
                       Member.Truss(0, (int(diagonal_tag[-1])+3), tag_nodes[-1]+1, tag_nodes[1], section_no=3)
                       Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-1]+2, tag_nodes[-1], section_no=3)
   
                   elif self.diag_2.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 2):
                           Member.Truss(0, j, i+1, i+2, section_no=3)
                           i +=2
                           j +=1
                       #Add first span
                       Node(tag_nodes[-1]+1, (-first_span), 0, 0)
                       Node(tag_nodes[-1]+2, (total_length+first_span), 0, 0)
   
                       Member((int(diagonal_tag[-1])+1), tag_nodes[0], tag_nodes[-1]+1, 0, 1, 1, 0, 0)
                       Member((int(diagonal_tag[-1])+2), tag_nodes[-2], tag_nodes[-1]+2, 0, 2, 2, 0, 0)
   
                       Member.Truss(0, (int(diagonal_tag[-1])+3), tag_nodes[-1]+1, tag_nodes[1], section_no=3)
                       Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-1]+2, tag_nodes[-1], section_no=3)
   
                   elif self.diag_3.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       k = 1
   
                       while i < len(tag_nodes) -1 and j < diagonal_tag[-1] +2  and k < len(tag_nodes) :
                           Member.Truss(0, j, i, i+3, section_no=3)
                           j += 1
                           Member.Truss(0, j, k+3, k+4, section_no=3)
                           i += 4
                           k += 4
                           j += 1
                       #Add first span
                       Node(tag_nodes[-1]+1, (-first_span), 0, 0)
                       Node(tag_nodes[-1]+2, (total_length+first_span), 0, 0)
   
                       Member((int(diagonal_tag[-1])+1), tag_nodes[0], tag_nodes[-1]+1, 0, 1, 1, 0, 0)
                       Member((int(diagonal_tag[-1])+2), tag_nodes[-2], tag_nodes[-1]+2, 0, 2, 2, 0, 0)
   
                       Member.Truss(0, (int(diagonal_tag[-1])+3), tag_nodes[-1]+1, tag_nodes[1], section_no=3)
                       Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-1]+2, tag_nodes[-1], section_no=3)
   
                   elif self.diag_4.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       k = 1
   
                       while i < len(tag_nodes) -1 and j < diagonal_tag[-1]+1  and k < len(tag_nodes) :
                           Member.Truss(0, j, i+2, i+5, section_no=3)
                           j += 1
                           Member.Truss(0, j, k+1, k+2, section_no=3)
                           i += 4
                           k += 4
                           j += 1
                       #Add first span
                       Node(tag_nodes[-1]+1, (-first_span), 0, 0)
                       Node(tag_nodes[-1]+2, (total_length+first_span), 0, 0)
   
                       Member((int(diagonal_tag[-1])+2), tag_nodes[0], tag_nodes[-1]+1, 0, 1, 1, 0, 0)
                       Member((int(diagonal_tag[-1])+3), tag_nodes[-2], tag_nodes[-1]+2, 0, 2, 2, 0, 0)
   
                       Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-1]+1, tag_nodes[1], section_no=3)
                       Member.Truss(0, (int(diagonal_tag[-1])+5), tag_nodes[-1]+2, tag_nodes[-1], section_no=3)
   
                   elif self.diag_5.isChecked():
                       if (number_of_bays % 2) == 0:
                           diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < ((tag_nodes[-1]/2) + 1) and j <diagonal_tag[-1] +1:
                               Member.Truss(0, j, i, i+3, section_no=3)
                               i += 2
                               j += 1
                           i = int(len(tag_nodes)/2) + 1
                           j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                           while i < tag_nodes[-1] and j <diagonal_tag[-1] +1:
                               Member.Truss(0, j, i, i+1, section_no=3)
                               i += 2
                               j += 1
                           #Add first span
                           Node(tag_nodes[-1]+1, (-first_span), 0, 0)
                           Node(tag_nodes[-1]+2, (total_length+first_span), 0, 0)
   
                           Member((int(diagonal_tag[-1])+2), tag_nodes[0], tag_nodes[-1]+1, 0, 1, 1, 0, 0)
                           Member((int(diagonal_tag[-1])+3), tag_nodes[-2], tag_nodes[-1]+2, 0, 2, 2, 0, 0)
   
                           Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-1]+1, tag_nodes[1], section_no=3)
                           Member.Truss(0, (int(diagonal_tag[-1])+5), tag_nodes[-1]+2, tag_nodes[-1], section_no=3)
                       else:
                           msg = QtWidgets.QMessageBox()
                           msg.setIcon(QtWidgets.QMessageBox.Critical)
                           msg.setText("WARNING")
                           msg.setInformativeText("WARNING: Please enter an even number of spans for a symmetrical net.")
                           msg.setWindowTitle("WARNING")
                           msg.exec_()
   
                   elif self.diag_6.isChecked():
                       if (number_of_bays % 2) == 0:
                           diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1] +1:
                               Member.Truss(0, j, i+1, i+2, section_no=3)
                               i += 2
                               j += 1
                           i = int(len(tag_nodes)/2)
                           j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                           while i < tag_nodes[-1] and j <diagonal_tag[-1] +1:
                               Member.Truss(0, j, i, i+3, section_no=3)
                               i += 2
                               j += 1
                           #Add first span
                           Node(tag_nodes[-1]+1, (-first_span), 0, 0)
                           Node(tag_nodes[-1]+2, (total_length+first_span), 0, 0)
   
                           Member((int(diagonal_tag[-1])+2), tag_nodes[0], tag_nodes[-1]+1, 0, 1, 1, 0, 0)
                           Member((int(diagonal_tag[-1])+3), tag_nodes[-2], tag_nodes[-1]+2, 0, 2, 2, 0, 0)
   
                           Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-1]+1, tag_nodes[1], section_no=3)
                           Member.Truss(0, (int(diagonal_tag[-1])+5), tag_nodes[-1]+2, tag_nodes[-1], section_no=3)
   
                       else:
                           msg = QtWidgets.QMessageBox()
                           msg.setIcon(QtWidgets.QMessageBox.Critical)
                           msg.setText("WARNING")
                           msg.setInformativeText("WARNING: Please enter an even number of spans for a symmetrical net.")
                           msg.setWindowTitle("WARNING")
                           msg.exec_()
   
                   elif self.diag_7.isChecked():
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       i = 1
                       j = int(diagonal_tag[0])
                       while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1)*2:
                           Member.Truss(0, j, i, i+3, section_no=3)
                           j +=1
                           Member.Truss(0, j, i+1, i+2, section_no=3)
                           i +=2
                           j +=1
                       #Add first span
                       Node(tag_nodes[-1]+3, (-first_span), 0, 0)
                       Node(tag_nodes[-1]+4, (total_length+first_span), 0, 0)
   
                       Member((int(diagonal_tag[-1])*2+1), tag_nodes[-1]+3, tag_nodes[0], 0, 1, 1, 0, 0)
                       Member((int(diagonal_tag[-1])*2+2), tag_nodes[-1]+4, tag_nodes[-2], 0, 2, 2, 0, 0)
   
                       Member.Truss(0, (int(diagonal_tag[-1])*2+3), tag_nodes[-1]+3, tag_nodes[1], section_no=3)
                       Member.Truss(0, (int(diagonal_tag[-1])*2+4), tag_nodes[-1], tag_nodes[-1]+4, section_no=3)
   
                   elif self.diag_8.isChecked():
                       #Add first span
                       diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                       Node(tag_nodes[-1]+3, (-first_span), 0, 0)
                       Node(tag_nodes[-1]+4, (total_length+first_span), 0, 0)
   
                       Member((int(diagonal_tag[-1])*2+1), tag_nodes[-1]+3, tag_nodes[0], 0, 1, 1, 0, 0)
                       Member((int(diagonal_tag[-1])*2+2), tag_nodes[-1]+4, tag_nodes[-2], 0, 2, 2, 0, 0)
   
                       Member.Truss(0, (int(diagonal_tag[-1])*2+3), tag_nodes[-1]+3, tag_nodes[1], section_no=3)
                       Member.Truss(0, (int(diagonal_tag[-1])*2+4), tag_nodes[-1], tag_nodes[-1]+4, section_no=3)
   
                   Model.clientModel.service.finish_modification()
   
               elif self.truss_4.isChecked():
   
                   if (number_of_bays % 2) == 0:
                       Model.clientModel.service.begin_modification()
   
                       # Create Nodes
                       x_nodes = [0]
                       for i in np.arange(total_length/number_of_bays, total_length - 0.1, total_length/number_of_bays):
                           x_nodes.append(i)
                           x_nodes.append(i)
                       x_nodes.append(total_length)
   
                       z_nodes = [0]
                       for i in np.arange(((total_length/number_of_bays) * total_height)/(total_length/2), total_height + 0.1, ((total_length/number_of_bays) * total_height)/(total_length/2)):
                           z_nodes.append(0)
                           z_nodes.append(-i)
                       for i in z_nodes[::-1][1:-1]:
                           z_nodes.append(i)
   
                       tag_nodes = np.arange(1, len(x_nodes)+1, 1)
   
                       for tag,x,z in zip(tag_nodes, x_nodes, z_nodes):
                           Node(tag, x, 0, z)
   
                       # Create Lower Chord
                       Member(1, 1, tag_nodes[-1], 0, 2, 2)
   
                       # Create Upper Chord
                       Member(2, 1, int(sum(tag_nodes) / len(tag_nodes) + 0.5), 0, 1, 1)
                       Member(3, int(sum(tag_nodes) / len(tag_nodes) + 0.5), tag_nodes[-1], 0, 1, 1)
   
                       # Create Verticals
                       i = 1
                       j = 1
                       while j<len(tag_nodes)-1 and i<len(tag_nodes):
                           Member.Truss(0, j+3, i+1, i+2, section_no=4)
                           i += 2
                           j += 1
   
                       #Create Diagonals
                       if self.diag_1.isChecked():
                           diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < len(tag_nodes)-1 and j < int(diagonal_tag[-1]):
                               Member.Truss(0, j, i+1, i+4, section_no=3)
                               i +=2
                               j +=1
   
                       elif self.diag_2.isChecked():
                           diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1):
                               Member.Truss(0, j, i+2, i+3, section_no=3)
                               i +=2
                               j +=1
   
                       elif self.diag_3.isChecked():
                           diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           k = 1
                           while i < len(tag_nodes) -2 and j < diagonal_tag[-1]  and k < len(tag_nodes) :
                               Member.Truss(0, j, i+1, i+4, section_no=3)
                               j += 1
                               Member.Truss(0, j,  k+4, k+5, section_no=3)
                               i += 4
                               k += 4
                               j += 1
   
                       elif self.diag_4.isChecked():
                           diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           k = 1
                           while i < len(tag_nodes) -2 and j < diagonal_tag[-1]  and k < len(tag_nodes) :
                               Member.Truss(0, j, i+2, i+3, section_no=3)
                               j += 1
                               Member.Truss(0, j, k+3, k+6, section_no=3)
                               i += 4
                               k += 4
                               j += 1
   
                       elif self.diag_5.isChecked():
                           diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1]:
                               Member.Truss(0, j, i+1, i+4, section_no=3)
                               i += 2
                               j += 1
                           i = int(len(tag_nodes)/2)
                           j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                           while i < tag_nodes[-1] and j <diagonal_tag[-1]:
                               Member.Truss(0, j, i+1, i+2, section_no=3)
                               i += 2
                               j += 1
   
                       elif self.diag_6.isChecked():
                           diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1]:
                               Member.Truss(0, j, i+2, i+3, section_no=3)
                               i += 2
                               j += 1
                           i = int(len(tag_nodes)/2)
                           j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                           while i < tag_nodes[-1] and j <diagonal_tag[-1]:
                               Member.Truss(0, j, i, i+3, section_no=3)
                               i += 2
                               j += 1
   
                       elif self.diag_7.isChecked():
                           diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1)*2:
                               Member.Truss(0, j, i+2, i+3, section_no=3)
                               j +=1
                               Member.Truss(0, j, i+1, i+4, section_no=3)
                               i +=2
                               j +=1
   
                       #elif self.diag_8.isChecked():
                       #    pass
   
                       Model.clientModel.service.finish_modification()
   
                   else:
                       msg = QtWidgets.QMessageBox()
                       msg.setIcon(QtWidgets.QMessageBox.Critical)
                       msg.setText("WARNING")
                       msg.setInformativeText("WARNING: Please enter an even number of spans for a symmetrical net.")
                       msg.setWindowTitle("WARNING")
                       msg.exec_()
   
               elif self.truss_5.isChecked():
   
                   if (number_of_bays % 2) == 0:
                       Model.clientModel.service.begin_modification()
   
                       # Create Nodes
                       x_nodes = [0, 0]
                       for i in np.arange(total_length/number_of_bays, total_length - 0.1, total_length/number_of_bays):
                           x_nodes.append(i)
                           x_nodes.append(i)
                       x_nodes.append(total_length)
                       x_nodes.append(total_length)
   
                       z_nodes = []
                       for i in np.arange(side_height, total_height +0.1, (total_height-side_height)/(number_of_bays/2)):
                           z_nodes.append(0)
                           z_nodes.append(-i)
                       for i in z_nodes[::-1][1:-1]:
                           z_nodes.append(i)
   
                       tag_nodes = np.arange(1, len(x_nodes)+1, 1)
   
                       for tag,x,z in zip(tag_nodes, x_nodes, z_nodes):
                           Node(tag, x, 0, z)
   
                       # Create Lower Chord
                       Member(1, 1, tag_nodes[-2], 0, 2, 2)
   
                       # Create Upper Chord
                       Member(2, 2, int(sum(tag_nodes) / len(tag_nodes) + 0.5), 0, 1, 1)
                       Member(3, int(sum(tag_nodes) / len(tag_nodes) + 0.5), tag_nodes[-1], 0, 1, 1)
   
                       # Create Verticals
                       i = 1
                       j = 1
                       while j<len(tag_nodes)-1 and i<len(tag_nodes):
                           Member.Truss(0, j+3, i, i+1, section_no=4)
                           i += 2
                           j += 1
   
                       #Create Diagonals
                       if self.diag_1.isChecked():
                           diagonal_tag = np.arange(number_of_bays+5, 2*number_of_bays+4, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 2):
                               Member.Truss(0, j, i, i+3, section_no=3)
                               i +=2
                               j +=1
   
                       elif self.diag_2.isChecked():
                           diagonal_tag = np.arange(number_of_bays+5, 2*number_of_bays+4, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < len(tag_nodes)-1 and j < int(diagonal_tag[-1] + 2):
                               Member.Truss(0, j, i+1, i+2, section_no=3)
                               i +=2
                               j +=1
   
                       elif self.diag_3.isChecked():
                           diagonal_tag = np.arange(number_of_bays+5, 2*number_of_bays+4, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           k = 1
                           while i < len(tag_nodes) +2 and j < diagonal_tag[-1] + 2  and k < len(tag_nodes) :
                               Member.Truss(0, j, i, i+3, section_no=3)
                               j += 1
                               Member.Truss(0, j, k+3, k+4, section_no=3)
                               i += 4
                               k += 4
                               j += 1
   
                       elif self.diag_4.isChecked():
                           diagonal_tag = np.arange(number_of_bays+5, 2*number_of_bays+4, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           k = 1
                           while i < len(tag_nodes) +2  and j < diagonal_tag[-1] + 2  and k < len(tag_nodes) :
                               Member.Truss(0, j, i+1, i+2, section_no=3)
                               j += 1
                               Member.Truss(0, j, k+2, k+5, section_no=3)
                               i += 4
                               k += 4
                               j += 1
   
                       elif self.diag_5.isChecked():
                           diagonal_tag = np.arange(number_of_bays+5, 2*number_of_bays+4, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1] + 10:
                               Member.Truss(0, j, i, i+3, section_no=3)
                               i += 2
                               j += 1
                           i = int(len(tag_nodes)/2)
                           j = int(diagonal_tag[int(len(diagonal_tag)/2)]) +1
                           while i < tag_nodes[-1] + 2 and j <diagonal_tag[-1] + 2:
                               Member.Truss(0, j, i+1, i+2, section_no=3)
                               i += 2
                               j += 1
   
                       elif self.diag_6.isChecked():
                           diagonal_tag = np.arange(number_of_bays+5, 2*number_of_bays+4, 1)
                           i = 1
                           j = int(diagonal_tag[0])
                           while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1] + 10:
                               Member.Truss(0, j, i+1, i+2, section_no=3)
                               i += 2
                               j += 1
                           i = int(len(tag_nodes)/2)
                           j = int(diagonal_tag[int(len(diagonal_tag)/2)]) +1
                           while i < tag_nodes[-1] + 2 and j <diagonal_tag[-1] + 2:
                               Member.Truss(0, j, i, i+3, section_no=3)
                               i += 2
                               j += 1
   
                       elif self.diag_7.isChecked():
                           diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
                           i = 1
                           j = int(diagonal_tag[0]) +2
                           while i < len(tag_nodes) and j < int(diagonal_tag[-1])*2:
                               Member.Truss(0, j, i+1, i+2, section_no=3)
                               j +=1
                               Member.Truss(0, j, i, i+3, section_no=3)
                               i +=2
                               j +=1
   
                       #elif self.diag_8.isChecked():
                       #    pass
   
                       Model.clientModel.service.finish_modification()
                   else:
                       msg = QtWidgets.QMessageBox()
                       msg.setIcon(QtWidgets.QMessageBox.Critical)
                       msg.setText("WARNING")
                       msg.setInformativeText("WARNING: Please enter an even number of spans for a symmetrical net.")
                       msg.setWindowTitle("WARNING")
                       msg.exec_()
   
           session.close()
   
       def close(self):
           sys.exit(app.exec_())
   
   if __name__ == "__main__":
       app = QtWidgets.QApplication(sys.argv)
       app.setStyleSheet(qdarkstyle.load_stylesheet())
       MainWindow = QtWidgets.QMainWindow()
       ui = Ui_MainWindow()
       ui.setupUi(MainWindow)
       MainWindow.show()
       sys.exit(app.exec_())