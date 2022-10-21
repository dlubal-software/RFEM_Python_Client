import json
import sys

from InstallPyQt5 import installPyQt5
installPyQt5()

from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsItem, QVBoxLayout, QPushButton, QSlider, QHBoxLayout

from MyRFEM import *

# TODO 4: Implement input validation
# TODO 5: Define a dictionary for the calculation model and implement the updates in event handler
# TODO 6: Write a class for the connection to RFEM
# TODO 7: Fill the tab for load input
# TODO 8: Fill the tab for steel design

class MyWindow(QMainWindow):
    # This dictionary stores the data for the graphic that will
    # be drawn with drawGraphic().
    graphic_model = {}

    # All usable materials are defined in this list.
    material_list = []

    # All usable cross sections are defined in this list.
    cross_section_list_1 = []
    cross_section_list_2 = []

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = uic.loadUi("MyApp.ui", self)

        self.readConfig()

        # Fill the comboBoxes with default values
        self.ui.comboBox_Material_o_c.addItems(self.material_list)
        self.ui.comboBox_Material_i_c.addItems(self.material_list)
        self.ui.comboBox_Material_r.addItems(self.material_list)
        self.ui.comboBox_Material_s.addItems(self.material_list)

        self.ui.comboBox_CS_o_c.addItems(self.cross_section_list_1)
        self.ui.comboBox_CS_i_c.addItems(self.cross_section_list_2)
        self.ui.comboBox_CS_r.addItems(self.cross_section_list_1)
        self.ui.comboBox_CS_s.addItems(self.cross_section_list_1)

        self.ui.comboBox_support_1.addItems(self.support_list)
        self.ui.comboBox_support_2.addItems(self.support_list)
        self.ui.comboBox_support_3.addItems(self.support_list)
        self.ui.comboBox_support_4.addItems(self.support_list)

        # Slots for LineEdits
        self.ui.lineEdit_l_1.textChanged.connect(self.onChange_l_1)
        self.ui.lineEdit_l_2.textChanged.connect(self.onChange_l_2)
        self.ui.lineEdit_l_3.textChanged.connect(self.onChange_l_3)

        self.ui.lineEdit_h_1.textChanged.connect(self.onChange_h_1)
        self.ui.lineEdit_h_2.textChanged.connect(self.onChange_h_2)
        self.ui.lineEdit_h_3.textChanged.connect(self.onChange_h_3)

        # Slots for Combo Boxes
        self.ui.comboBox_Material_o_c.currentIndexChanged.connect(self.onCurrentIndexChanged_Material_o_c)
        self.ui.comboBox_Material_i_c.currentIndexChanged.connect(self.onCurrentIndexChanged_Material_i_c)
        self.ui.comboBox_Material_r.currentIndexChanged.connect(self.onCurrentIndexChanged_Material_r)
        self.ui.comboBox_Material_s.currentIndexChanged.connect(self.onCurrentIndexChanged_Material_s)

        self.ui.comboBox_CS_o_c.currentIndexChanged.connect(self.onCurrentIndexChanged_CS_o_c)
        self.ui.comboBox_CS_i_c.currentIndexChanged.connect(self.onCurrentIndexChanged_CS_i_c)
        self.ui.comboBox_CS_r.currentIndexChanged.connect(self.onCurrentIndexChanged_CS_r)
        self.ui.comboBox_CS_s.currentIndexChanged.connect(self.onCurrentIndexChanged_CS_s)

        self.ui.comboBox_support_1.currentIndexChanged.connect(self.onCurrentIndexChanged_support_1)
        self.ui.comboBox_support_2.currentIndexChanged.connect(self.onCurrentIndexChanged_support_2)
        self.ui.comboBox_support_3.currentIndexChanged.connect(self.onCurrentIndexChanged_support_3)
        self.ui.comboBox_support_4.currentIndexChanged.connect(self.onCurrentIndexChanged_support_4)

        # Slots for buttons
        self.ui.buttonCalculate.clicked.connect(self.onCalculate)
        self.ui.buttonCancel.clicked.connect(self.onCancel)

        self.drawGraphic()

    def readConfig(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
        self.material_list = config['material_list']
        self.cross_section_list_1 = config['cross_section_list_1']
        self.cross_section_list_2 = config['cross_section_list_2']
        self.support_list = config['support_list']
        self.graphic_model = config['graphic_model']

    def drawGraphic(self):
        scene = QGraphicsScene()
        self.ui.graphicsView.setScene(scene)

        n_01 = self.graphic_model['node']['01']
        n_02 = self.graphic_model['node']['02']
        n_03 = self.graphic_model['node']['03']
        n_04 = self.graphic_model['node']['04']
        n_05 = self.graphic_model['node']['05']
        n_06 = self.graphic_model['node']['06']
        n_07 = self.graphic_model['node']['07']
        n_08 = self.graphic_model['node']['08']
        n_09 = self.graphic_model['node']['09']
        n_10 = self.graphic_model['node']['10']
        n_11 = self.graphic_model['node']['11']

        factor_x = 400 / n_04[0]
        factor_y = 700 / n_01[1]
        factor = min(factor_x, factor_y)

        # TODO: This does't work. The background of the ellipse is still transparent.
        brush = QBrush()
        brush.setColor(QtCore.Qt.green)
        ###

        # Diameter Circle
        d = 7

        pen = QPen()
        pen.setWidth(2)

        # TODO: The assignment of the colors does not work. It jumps to the correct branch. Nevertheless, everything is black.
        if self.graphic_model['member_color']['01'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['01'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_02[0] * factor, n_02[1] * factor, n_03[0] * factor, n_03[1] * factor, pen)

        if self.graphic_model['member_color']['02'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['02'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_01[0] * factor, n_01[1] * factor, n_02[0] * factor, n_02[1] * factor, pen)

        if self.graphic_model['member_color']['03'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['03'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_01[0] * factor, n_01[1] * factor, n_02[0] * factor, n_02[1] * factor, pen)

        if self.graphic_model['member_color']['04'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['04'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_01[0] * factor, n_01[1] * factor, n_02[0] * factor, n_02[1] * factor, pen)

        if self.graphic_model['member_color']['05'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['05'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_01[0] * factor, n_01[1] * factor, n_02[0] * factor, n_02[1] * factor, pen)

        if self.graphic_model['member_color']['06'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['06'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_05[0] * factor, n_05[1] * factor, n_06[0] * factor, n_06[1] * factor, pen)

        if self.graphic_model['member_color']['07'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['07'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_04[0] * factor, n_04[1] * factor, n_05[0] * factor, n_05[1] * factor, pen)

        if self.graphic_model['member_color']['08'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['08'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_03[0] * factor, n_03[1] * factor, n_07[0] * factor, n_07[1] * factor, pen)

        if self.graphic_model['member_color']['09'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['09'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_07[0] * factor, n_07[1] * factor, n_06[0] * factor, n_06[1] * factor, pen)

        if self.graphic_model['member_color']['10'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['10'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_08[0] * factor, n_08[1] * factor, n_09[0] * factor, n_09[1] * factor, pen)

        if self.graphic_model['member_color']['11'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['11'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_10[0] * factor, n_10[1] * factor, n_11[0] * factor, n_11[1] * factor, pen)

        if self.graphic_model['member_color']['12'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['12'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_02[0] * factor, n_02[1] * factor, n_09[0] * factor, n_09[1] * factor, pen)

        if self.graphic_model['member_color']['13'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['13'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_09[0] * factor, n_09[1] * factor, n_11[0] * factor, n_11[1] * factor, pen)

        if self.graphic_model['member_color']['14'] == 'wrong':
            pen.setBrush(QtCore.Qt.red)
        elif self.graphic_model['member_color']['14'] == 'ok':
            pen.setBrush(QtCore.Qt.green)
        else: pen.setBrush(QtCore.Qt.black)
        scene.addLine(n_11[0] * factor, n_11[1] * factor, n_05[0] * factor, n_05[1] * factor, pen)

        # Supports
        if self.graphic_model['supports']['1'] == 'Hinged':
            scene.addEllipse((n_01[0]* factor) - d/2, n_01[1]* factor, d, d, pen, brush)
            scene.addLine(n_01[0]* factor, (n_01[1]* factor) + d, (n_01[0]* factor) - 10, (n_01[1]* factor) + d + 10, pen)
            scene.addLine(n_01[0]* factor, (n_01[1]* factor) + d, (n_01[0]* factor) + 10, (n_01[1]* factor) + d + 10, pen)
            scene.addLine((n_01[0]* factor) - 10, (n_01[1]* factor) + d + 10, (n_01[0]* factor) + 10, (n_01[1]* factor) + d + 10, pen)
        else:
            scene.addLine((n_01[0]* factor) - 10, (n_01[1]* factor), (n_01[0]* factor) + 10, (n_01[1]* factor), pen)

        if self.graphic_model['supports']['2'] == 'Hinged':
            scene.addEllipse((n_04[0]* factor) - d/2, n_04[1]* factor, d, d, pen)
            scene.addLine(n_04[0]* factor, (n_04[1]* factor) + d, (n_04[0]* factor) - 10, (n_04[1]* factor) + d + 10, pen)
            scene.addLine(n_04[0]* factor, (n_04[1]* factor) + d, (n_04[0]* factor) + 10, (n_04[1]* factor) + d + 10, pen)
            scene.addLine((n_04[0]* factor) - 10, (n_04[1]* factor) + d + 10, (n_04[0]* factor) + 10, (n_04[1]* factor) + d + 10, pen)
        else:
            scene.addLine((n_04[0]* factor) - 10, (n_04[1]* factor), (n_04[0]* factor) + 10, (n_04[1]* factor), pen)

        if self.graphic_model['supports']['3'] == 'Hinged':
            scene.addEllipse((n_08[0]* factor) - d/2, n_08[1]* factor, d, d, pen)
            scene.addLine(n_08[0]* factor, (n_08[1]* factor) + d, (n_08[0]* factor) - 10, (n_08[1]* factor) + d + 10, pen)
            scene.addLine(n_08[0]* factor, (n_08[1]* factor) + d, (n_08[0]* factor) + 10, (n_08[1]* factor) + d + 10, pen)
            scene.addLine((n_08[0]* factor) - 10, (n_08[1]* factor) + d + 10, (n_08[0]* factor) + 10, (n_08[1]* factor) + d + 10, pen)
        else:
            scene.addLine((n_08[0]* factor) - 10, (n_08[1]* factor), (n_08[0]* factor) + 10, (n_08[1]* factor), pen)

        if self.graphic_model['supports']['4'] == 'Hinged':
            scene.addEllipse((n_10[0]* factor) - d/2, n_10[1]* factor, d, d, pen)
            scene.addLine(n_10[0]* factor, (n_10[1]* factor) + d, (n_10[0]* factor) - 10, (n_10[1]* factor) + d + 10, pen)
            scene.addLine(n_10[0]* factor, (n_10[1]* factor) + d, (n_10[0]* factor) + 10, (n_10[1]* factor) + d + 10, pen)
            scene.addLine((n_10[0]* factor) - 10, (n_10[1]* factor) + d + 10, (n_10[0]* factor) + 10, (n_10[1]* factor) + d + 10, pen)
        else:
            scene.addLine((n_10[0]* factor) - 10, (n_10[1]* factor), (n_10[0]* factor) + 10, (n_10[1]* factor), pen)

        # Hinges
        scene.addEllipse((n_02[0]* factor), (n_02[1]* factor) - d/2, d, d, pen)
        scene.addEllipse((n_05[0]* factor) - d, (n_05[1]* factor) - d/2, d, d, pen)

    def onChange_l_1(self):
        # TODO: Überprüfung der Eingabe fehlt
        l_1 = float(self.ui.lineEdit_l_1.text())

        # TODO: Update calculation model

        n_4 = self.graphic_model['node']['04']
        n_5 = self.graphic_model['node']['05']
        n_6 = self.graphic_model['node']['06']
        n_7 = self.graphic_model['node']['07']
        n_8 = self.graphic_model['node']['08']
        n_9 = self.graphic_model['node']['09']
        n_10 = self.graphic_model['node']['10']
        n_11 = self.graphic_model['node']['11']

        delta_x = l_1 - n_8[0]

        n_4[0] = n_4[0] + delta_x
        n_5[0] = n_5[0] + delta_x
        n_6[0] = n_6[0] + delta_x
        n_7[0] = n_7[0] + delta_x / 2
        n_8[0] = n_8[0] + delta_x
        n_9[0] = n_9[0] + delta_x
        n_10[0] = n_10[0] + delta_x
        n_11[0] = n_11[0] + delta_x

        self.graphic_model['node']['04'][0] = n_4[0]
        self.graphic_model['node']['05'][0] = n_5[0]
        self.graphic_model['node']['06'][0] = n_6[0]
        self.graphic_model['node']['07'][0] = n_7[0]
        self.graphic_model['node']['08'][0] = n_8[0]
        self.graphic_model['node']['09'][0] = n_9[0]
        self.graphic_model['node']['10'][0] = n_10[0]
        self.graphic_model['node']['11'][0] = n_11[0]

        # Update graphic
        self.drawGraphic()

    def onChange_l_2(self):
        # TODO: Überprüfung der Eingabe fehlt
        l_2 = float(self.ui.lineEdit_l_2.text())

        # TODO: Update calculation model

        n_4 = self.graphic_model['node']['04']
        n_5 = self.graphic_model['node']['05']
        n_6 = self.graphic_model['node']['06']
        n_7 = self.graphic_model['node']['07']
        n_8 = self.graphic_model['node']['08']
        n_10 = self.graphic_model['node']['10']
        n_11 = self.graphic_model['node']['11']

        delta_x = l_2 - n_10[0] + n_8[0]

        n_4[0] = n_4[0] + delta_x
        n_5[0] = n_5[0] + delta_x
        n_6[0] = n_6[0] + delta_x
        n_7[0] = n_7[0] + delta_x / 2
        n_10[0] = n_10[0] + delta_x
        n_11[0] = n_11[0] + delta_x

        self.graphic_model['node']['04'][0] = n_4[0]
        self.graphic_model['node']['05'][0] = n_5[0]
        self.graphic_model['node']['06'][0] = n_6[0]
        self.graphic_model['node']['07'][0] = n_7[0]
        self.graphic_model['node']['10'][0] = n_10[0]
        self.graphic_model['node']['11'][0] = n_11[0]

        # Update graphic
        self.drawGraphic()

    def onChange_l_3(self):
        # TODO: Überprüfung der Eingabe fehlt
        l_3 = float(self.ui.lineEdit_l_3.text())

        # TODO: Update calculation model

        n_4 = self.graphic_model['node']['04']
        n_5 = self.graphic_model['node']['05']
        n_6 = self.graphic_model['node']['06']
        n_7 = self.graphic_model['node']['07']
        n_8 = self.graphic_model['node']['08']
        n_10 = self.graphic_model['node']['10']

        delta_x = l_3 - n_4[0] + n_10[0]
        print(delta_x)

        n_4[0] = n_4[0] + delta_x
        n_5[0] = n_5[0] + delta_x
        n_6[0] = n_6[0] + delta_x
        n_7[0] = n_7[0] + delta_x / 2

        self.graphic_model['node']['04'][0] = n_4[0]
        self.graphic_model['node']['05'][0] = n_5[0]
        self.graphic_model['node']['06'][0] = n_6[0]
        self.graphic_model['node']['07'][0] = n_7[0]

        # Update graphic
        self.drawGraphic()

    def onChange_h_1(self):
        # TODO: Überprüfung der Eingabe fehlt
        h_1 = float(self.ui.lineEdit_h_1.text())

        # TODO: Update calculation model

        n_1 = self.graphic_model['node']['01']
        n_2 = self.graphic_model['node']['02']
        n_8 = self.graphic_model['node']['08']
        n_4 = self.graphic_model['node']['04']
        n_10 = self.graphic_model['node']['10']

        delta_y = n_2[1] - n_1[1] + h_1

        n_1[1] = n_1[1] + delta_y
        n_4[1] = n_4[1] + delta_y
        n_8[1] = n_8[1] + delta_y
        n_10[1] = n_10[1] + delta_y

        self.graphic_model['node']['01'][1] = n_1[1]
        self.graphic_model['node']['04'][1] = n_4[1]
        self.graphic_model['node']['08'][1] = n_8[1]
        self.graphic_model['node']['10'][1] = n_10[1]

        # Update graphic
        self.drawGraphic()

    def onChange_h_2(self):
        # TODO: Überprüfung der Eingabe fehlt
        h_2 = float(self.ui.lineEdit_h_2.text())

        # TODO: Update calculation model

        n_1 = self.graphic_model['node']['01']
        n_2 = self.graphic_model['node']['02']
        n_3 = self.graphic_model['node']['03']
        n_8 = self.graphic_model['node']['08']
        n_4 = self.graphic_model['node']['04']
        n_5 = self.graphic_model['node']['05']
        n_9 = self.graphic_model['node']['09']
        n_10 = self.graphic_model['node']['10']
        n_11 = self.graphic_model['node']['11']

        delta_y = n_3[1] - n_2[1] + h_2

        n_1[1] = n_1[1] + delta_y
        n_2[1] = n_2[1] + delta_y
        n_4[1] = n_4[1] + delta_y
        n_5[1] = n_5[1] + delta_y
        n_8[1] = n_8[1] + delta_y
        n_9[1] = n_9[1] + delta_y
        n_10[1] = n_10[1] + delta_y
        n_11[1] = n_11[1] + delta_y

        self.graphic_model['node']['01'][1] = n_1[1]
        self.graphic_model['node']['02'][1] = n_2[1]
        self.graphic_model['node']['04'][1] = n_4[1]
        self.graphic_model['node']['05'][1] = n_5[1]
        self.graphic_model['node']['08'][1] = n_8[1]
        self.graphic_model['node']['08'][1] = n_8[1]
        self.graphic_model['node']['10'][1] = n_10[1]
        self.graphic_model['node']['11'][1] = n_11[1]

        # Update graphic
        self.drawGraphic()

    def onChange_h_3(self):
        # TODO: Überprüfung der Eingabe fehlt
        h_3 = float(self.ui.lineEdit_h_3.text())

        # TODO: Update calculation model

        n_1 = self.graphic_model['node']['01']
        n_2 = self.graphic_model['node']['02']
        n_3 = self.graphic_model['node']['03']
        n_6 = self.graphic_model['node']['06']
        n_8 = self.graphic_model['node']['08']
        n_4 = self.graphic_model['node']['04']
        n_5 = self.graphic_model['node']['05']
        n_9 = self.graphic_model['node']['09']
        n_10 = self.graphic_model['node']['10']
        n_11 = self.graphic_model['node']['11']

        delta_y = h_3 - n_3[1]

        n_1[1] = n_1[1] + delta_y
        n_2[1] = n_2[1] + delta_y
        n_3[1] = n_3[1] + delta_y
        n_6[1] = n_6[1] + delta_y
        n_8[1] = n_8[1] + delta_y
        n_4[1] = n_4[1] + delta_y
        n_5[1] = n_5[1] + delta_y
        n_9[1] = n_9[1] + delta_y
        n_10[1] = n_10[1] + delta_y
        n_11[1] = n_11[1] + delta_y

        self.graphic_model['node']['01'][1] = n_1[1]
        self.graphic_model['node']['02'][1] = n_2[1]
        self.graphic_model['node']['03'][1] = n_3[1]
        self.graphic_model['node']['06'][1] = n_6[1]
        self.graphic_model['node']['08'][1] = n_8[1]
        self.graphic_model['node']['04'][1] = n_4[1]
        self.graphic_model['node']['05'][1] = n_5[1]
        self.graphic_model['node']['09'][1] = n_9[1]
        self.graphic_model['node']['10'][1] = n_10[1]
        self.graphic_model['node']['11'][1] = n_11[1]

        # Update graphic
        self.drawGraphic()

    def onCurrentIndexChanged_Material_o_c(self, index):
        print(self.material_list[index])
        # TODO: Update calculation model
        pass

    def onCurrentIndexChanged_Material_i_c(self, index):
        print(self.material_list[index])
        # TODO: Update calculation model
        pass

    def onCurrentIndexChanged_Material_r(self, index):
        print(self.material_list[index])
        # TODO: Update calculation model
        pass

    def onCurrentIndexChanged_Material_s(self, index):
        print(self.material_list[index])
        # TODO: Update calculation model
        pass

    def onCurrentIndexChanged_CS_o_c(self, index):
        print(self.cross_section_list_1[index])
        # TODO: Update calculation model
        pass

    def onCurrentIndexChanged_CS_i_c(self, index):
        print(self.cross_section_list_2[index])
        # TODO: Update calculation model
        pass

    def onCurrentIndexChanged_CS_r(self, index):
        print(self.cross_section_list_1[index])
        # TODO: Update calculation model
        pass

    def onCurrentIndexChanged_CS_s(self, index):
        print(self.cross_section_list_1[index])
        # TODO: Update calculation model
        pass

    def onCurrentIndexChanged_support_1(self, index):
        print(self.support_list[index])
        # TODO: Update calculation model

        # Update graphic model
        self.graphic_model['supports']['1'] = self.support_list[index]
        self.drawGraphic()

    def onCurrentIndexChanged_support_2(self, index):
        print(self.support_list[index])
        # TODO: Update calculation model

        # Update graphic model
        self.graphic_model['supports']['2'] = self.support_list[index]
        self.drawGraphic()

    def onCurrentIndexChanged_support_3(self, index):
        print(self.support_list[index])
        # TODO: Update calculation model

        # Update graphic model
        self.graphic_model['supports']['3'] = self.support_list[index]
        self.drawGraphic()

    def onCurrentIndexChanged_support_4(self, index):
        print(self.support_list[index])
        # TODO: Update calculation model

        # Update graphic model
        self.graphic_model['supports']['4'] = self.support_list[index]
        self.drawGraphic()


    def onCalculate(self):
        print('Calculate')

        # Call the calculate method in MyRFEM class.

    def onCancel(self):
        print('Schluss jetzt!')
        self.close()







def window():
    app = QApplication(sys.argv)
    with open('styles.qss', 'r') as f:
        style = f.read()
        app.setStyleSheet(style)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
	window()