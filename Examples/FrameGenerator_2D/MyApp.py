import json
import sys

from InstallPyQt5 import installPyQt5
installPyQt5()

from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPainter, QPen, QColor, QFont, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsItem, QVBoxLayout, QPushButton, QSlider, QHBoxLayout, QMessageBox

from MyRFEM import *

# TODO 19: Draw the loads
# TODO 18: Read the date from load tab into the graphic_model
# TODO 33: Add buttons for switch on and switch of the load in graphic
# TODO 32: Generate the report and display it an the tab
# TODO 11: Make path specification better
# TODO 12: Uniform use of ' or " in open()
# TODO 13: Correct tab order of the dimensions
# TODO 14: Make path specification better
# TODO 16: Write the done() method in class MyRFEM
# TODO 23: Implement a "Wait" dialog. It should display after click of [Calculate] and
#          should disappear when the calculation is finished (in done() method).
# TODO 15: Add spin buttons on edit lines (?)
# TODO 30: delete test_DesignSituations.py
# TODO 36:
# TODO 37:

class MyWindow(QMainWindow):
    # This dictionary stores the data for the graphic that will
    # be drawn with drawGraphic().
    graphic_model = {}

    # This dictionary contains all calculation relevant information.
    calculation_model = {}

    results = {}

    # All usable materials are defined in this list.
    material_list = []

    # All usable cross sections are defined in this list.
    cross_section_list_1 = []
    cross_section_list_2 = []

    # Presets for UI
    # The data is loaded from config.json.
    presets = {}

    def __init__(self):
        super(MyWindow, self).__init__()
        # TODO: Make path specification better
        self.ui = uic.loadUi("./Examples/FrameGenerator_2D/MyApp.ui", self)

        self.readConfig()

        # Fill the check boxes with the values form config
        if self.presets['check_load'] == 1:
            self.ui.checkBox_loads.setChecked(True)
            self.ui.groupBox_SW.setEnabled(True)
            self.ui.groupBox_Snow.setEnabled(True)
            self.ui.groupBox_Slab.setEnabled(True)
            self.ui.checkBox_steel_design.setEnabled(True)
        else:
            self.ui.checkBox_loads.setChecked(False)
            self.ui.groupBox_SW.setEnabled(False)
            self.ui.groupBox_Snow.setEnabled(False)
            self.ui.groupBox_Slab.setEnabled(False)
            self.ui.checkBox_steel_design.setEnabled(False)

        if self.presets['check_steel_design'] == 1:
            self.ui.checkBox_steel_design.setChecked(True)
        else:
            self.ui.checkBox_steel_design.setChecked(False)

        # Fill the LineEdits for structure with the values form config
        self.ui.lineEdit_l_1.setText(self.presets['dimensions'][0])
        self.ui.lineEdit_l_2.setText(self.presets['dimensions'][1])
        self.ui.lineEdit_l_3.setText(self.presets['dimensions'][2])
        self.ui.lineEdit_h_1.setText(self.presets['dimensions'][3])
        self.ui.lineEdit_h_2.setText(self.presets['dimensions'][4])
        self.ui.lineEdit_h_3.setText(self.presets['dimensions'][5])

        # Fill the comboBoxes with default values form config
        self.ui.comboBox_Material_o_c.addItems(self.material_list)
        index = self.presets['material'][0]
        self.ui.comboBox_Material_o_c.setCurrentText(self.material_list[index])

        self.ui.comboBox_Material_i_c.addItems(self.material_list)
        index = self.presets['material'][1]
        self.ui.comboBox_Material_i_c.setCurrentText(self.material_list[index])

        self.ui.comboBox_Material_r.addItems(self.material_list)
        index = self.presets['material'][2]
        self.ui.comboBox_Material_r.setCurrentText(self.material_list[index])

        self.ui.comboBox_Material_s.addItems(self.material_list)
        index = self.presets['material'][3]
        self.ui.comboBox_Material_s.setCurrentText(self.material_list[index])

        self.ui.comboBox_CS_o_c.addItems(self.cross_section_list_1)
        index = self.presets['cross_section'][0]
        self.ui.comboBox_CS_o_c.setCurrentText(self.cross_section_list_1[index])

        self.ui.comboBox_CS_i_c.addItems(self.cross_section_list_2)
        index = self.presets['cross_section'][1]
        self.ui.comboBox_CS_i_c.setCurrentText(self.cross_section_list_2[index])

        self.ui.comboBox_CS_r.addItems(self.cross_section_list_1)
        index = self.presets['cross_section'][2]
        self.ui.comboBox_CS_r.setCurrentText(self.cross_section_list_1[index])

        self.ui.comboBox_CS_s.addItems(self.cross_section_list_1)
        index = self.presets['cross_section'][3]
        self.ui.comboBox_CS_s.setCurrentText(self.cross_section_list_1[index])

        self.ui.comboBox_support_1.addItems(self.support_list)
        index = self.presets['supports'][0]
        self.ui.comboBox_support_1.setCurrentText(self.support_list[index])

        self.ui.comboBox_support_2.addItems(self.support_list)
        index = self.presets['supports'][1]
        self.ui.comboBox_support_2.setCurrentText(self.support_list[index])

        self.ui.comboBox_support_3.addItems(self.support_list)
        index = self.presets['supports'][2]
        self.ui.comboBox_support_3.setCurrentText(self.support_list[index])

        self.ui.comboBox_support_4.addItems(self.support_list)
        index = self.presets['supports'][3]
        self.ui.comboBox_support_4.setCurrentText(self.support_list[index])

        # Fill the LineEdits for loads with the values form config
        self.ui.lineEdit_g_r.setText(self.presets['loads']['self-weight'][0])
        self.ui.lineEdit_g_s.setText(self.presets['loads']['self-weight'][1])
        self.ui.lineEdit_g_w.setText(self.presets['loads']['self-weight'][2])
        self.ui.lineEdit_s_r.setText(self.presets['loads']['snow'][0])
        self.ui.lineEdit_p_s.setText(self.presets['loads']['slab'][0])

        # Slots for CheckBox
        self.ui.checkBox_loads.stateChanged.connect(self.onChange_checkBox_loads)
        self.ui.checkBox_steel_design.stateChanged.connect(self.onChange_checkBox_steel_design)

        # Slots for LineEdits
        self.ui.lineEdit_l_1.textChanged.connect(self.onChange_l_1)
        self.ui.lineEdit_l_2.textChanged.connect(self.onChange_l_2)
        self.ui.lineEdit_l_3.textChanged.connect(self.onChange_l_3)

        self.ui.lineEdit_h_1.textChanged.connect(self.onChange_h_1)
        self.ui.lineEdit_h_2.textChanged.connect(self.onChange_h_2)
        self.ui.lineEdit_h_3.textChanged.connect(self.onChange_h_3)

        self.ui.lineEdit_g_r.textChanged.connect(self.onChange_g_r)
        self.ui.lineEdit_g_s.textChanged.connect(self.onChange_g_s)
        self.ui.lineEdit_g_w.textChanged.connect(self.onChange_g_w)
        self.ui.lineEdit_s_r.textChanged.connect(self.onChange_s_r)
        self.ui.lineEdit_p_s.textChanged.connect(self.onChange_p_s)

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
        # TODO: Make path specification better
        with open('./Examples/FrameGenerator_2D/config.json', 'r') as f:
            config = json.load(f)
        self.material_list = config['material_list']
        self.cross_section_list_1 = config['cross_section_list_1']
        self.cross_section_list_2 = config['cross_section_list_2']
        self.support_list = config['support_list']
        self.graphic_model = config['graphic_model']
        self.presets = config['presets']
        self.calculation_model = config['calculation_model']

    def writeConfig(self):
        config = {}
        config['material_list'] = self.material_list
        config['cross_section_list_1'] = self.cross_section_list_1
        config['cross_section_list_2'] = self.cross_section_list_2
        config['support_list'] = self.support_list
        config['graphic_model'] = self.graphic_model
        config['presets'] = self.presets
        config['calculation_model'] = self.calculation_model
        # TODO: Make path specification better
        with open('./Examples/FrameGenerator_2D/config.json', 'w') as f:
            json.dump(config, f)

    def drawGraphic(self):
        scene = QGraphicsScene()
        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.ui.graphicsView.setBackgroundBrush(QColor(253, 250, 250, 255))

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

        # Distance dimension lines from static model
        dim_spacing = 100
        load_spacing = 20
        load_high = 30
        dim_length = 20

        factor_x = (400 - dim_spacing) / n_04[0]
        factor_y = (700 - dim_spacing - load_spacing) / n_01[1]
        factor = min(factor_x, factor_y)

        # TODO: This does't work. The background of the ellipse is still transparent.
        brush = QBrush()
        brush.setColor(Qt.green)
        ###

        # Diameter Circle
        d = 7

        pen = QPen()
        pen.setStyle(Qt.SolidLine)
        pen.setWidth(2)
        pen.setBrush(Qt.black)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)

        scene.addLine(n_02[0] * factor, n_02[1] * factor, n_03[0] * factor, n_03[1] * factor, pen)
        scene.addLine(n_01[0] * factor, n_01[1] * factor, n_02[0] * factor, n_02[1] * factor, pen)
        scene.addLine(n_01[0] * factor, n_01[1] * factor, n_02[0] * factor, n_02[1] * factor, pen)
        scene.addLine(n_01[0] * factor, n_01[1] * factor, n_02[0] * factor, n_02[1] * factor, pen)
        scene.addLine(n_01[0] * factor, n_01[1] * factor, n_02[0] * factor, n_02[1] * factor, pen)
        scene.addLine(n_05[0] * factor, n_05[1] * factor, n_06[0] * factor, n_06[1] * factor, pen)
        scene.addLine(n_04[0] * factor, n_04[1] * factor, n_05[0] * factor, n_05[1] * factor, pen)
        scene.addLine(n_03[0] * factor, n_03[1] * factor, n_07[0] * factor, n_07[1] * factor, pen)
        scene.addLine(n_07[0] * factor, n_07[1] * factor, n_06[0] * factor, n_06[1] * factor, pen)
        scene.addLine(n_08[0] * factor, n_08[1] * factor, n_09[0] * factor, n_09[1] * factor, pen)
        scene.addLine(n_10[0] * factor, n_10[1] * factor, n_11[0] * factor, n_11[1] * factor, pen)
        scene.addLine(n_02[0] * factor, n_02[1] * factor, n_09[0] * factor, n_09[1] * factor, pen)
        scene.addLine(n_09[0] * factor, n_09[1] * factor, n_11[0] * factor, n_11[1] * factor, pen)
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
        scene.addEllipse((n_02[0]* factor), (n_02[1]* factor) - d/2, d, d, pen, brush)
        scene.addEllipse((n_05[0]* factor) - d, (n_05[1]* factor) - d/2, d, d, pen)

        # Dimensions
        dim_pen = QPen()
        dim_pen.setStyle(Qt.SolidLine)
        dim_pen.setWidth(1)
        dim_pen.setBrush(Qt.blue)
        dim_pen.setCapStyle(Qt.RoundCap)
        dim_pen.setJoinStyle(Qt.RoundJoin)

        dim_font = QFont()

        # Horizontal dimensions
        scene.addLine(n_01[0] * factor, n_01[1] * factor + dim_spacing, n_08[0] * factor, n_08[1] * factor + dim_spacing, dim_pen)
        scene.addLine(n_08[0] * factor, n_08[1] * factor + dim_spacing, n_10[0] * factor, n_10[1] * factor + dim_spacing, dim_pen)
        scene.addLine(n_10[0] * factor, n_10[1] * factor + dim_spacing, n_04[0] * factor, n_04[1] * factor + dim_spacing, dim_pen)

        scene.addLine(n_01[0] * factor, n_01[1] * factor + dim_spacing - dim_length / 2, n_01[0] * factor, n_01[1] * factor + dim_spacing + dim_length / 2, dim_pen)
        scene.addLine(n_08[0] * factor, n_08[1] * factor + dim_spacing - dim_length / 2, n_08[0] * factor, n_08[1] * factor + dim_spacing + dim_length / 2, dim_pen)
        scene.addLine(n_10[0] * factor, n_10[1] * factor + dim_spacing - dim_length / 2, n_10[0] * factor, n_10[1] * factor + dim_spacing + dim_length / 2, dim_pen)
        scene.addLine(n_04[0] * factor, n_04[1] * factor + dim_spacing - dim_length / 2, n_04[0] * factor, n_04[1] * factor + dim_spacing + dim_length / 2, dim_pen)

        scene.addText('l 1', dim_font).setPos((n_01[0] + n_08[0])/2 * factor, n_01[1] * factor + dim_spacing - dim_length)
        scene.addText('l 2', dim_font).setPos((n_08[0] + n_10[0])/2 * factor, n_08[1] * factor + dim_spacing - dim_length)
        scene.addText('l 3', dim_font).setPos((n_10[0] + n_04[0])/2 * factor, n_10[1] * factor + dim_spacing - dim_length)

        # Vertical dimensions
        scene.addLine(n_01[0] * factor - dim_spacing, n_01[1] * factor, n_02[0] * factor - dim_spacing, n_02[1] * factor, dim_pen)
        scene.addLine(n_02[0] * factor - dim_spacing, n_02[1] * factor, n_03[0] * factor - dim_spacing, n_03[1] * factor, dim_pen)
        scene.addLine(n_03[0] * factor - dim_spacing, n_03[1] * factor, n_03[0] * factor - dim_spacing, n_07[1] * factor, dim_pen)

        scene.addLine(n_01[0] * factor - dim_spacing - dim_length / 2, n_01[1] * factor, n_01[0] * factor - dim_spacing + dim_length / 2, n_01[1] * factor, dim_pen)
        scene.addLine(n_02[0] * factor - dim_spacing - dim_length / 2, n_02[1] * factor, n_02[0] * factor - dim_spacing + dim_length / 2, n_02[1] * factor, dim_pen)
        scene.addLine(n_03[0] * factor - dim_spacing - dim_length / 2, n_03[1] * factor, n_03[0] * factor - dim_spacing + dim_length / 2, n_03[1] * factor, dim_pen)
        scene.addLine(n_03[0] * factor - dim_spacing - dim_length / 2, n_07[1] * factor, n_03[0] * factor - dim_spacing + dim_length / 2, n_07[1] * factor, dim_pen)

        scene.addText('h 1', dim_font).setPos(n_01[0] * factor - dim_spacing + dim_length / 2, (n_01[1] + n_02[1]) / 2 * factor - dim_length / 2)
        scene.addText('h 2', dim_font).setPos(n_01[0] * factor - dim_spacing + dim_length / 2, (n_02[1] + n_03[1]) / 2 * factor - dim_length / 2)
        scene.addText('h 3', dim_font).setPos(n_01[0] * factor - dim_spacing + dim_length / 2, (n_03[1] + n_07[1]) / 2 * factor - dim_length / 2)

        # Loads
        load_pen = QPen()
        load_pen.setStyle(Qt.SolidLine)
        load_pen.setWidth(1)
        #load_pen.setBrush(Qt.green)
        load_pen.setBrush(QColor(0, 120, 120, 127))
        load_pen.setCapStyle(Qt.RoundCap)
        load_pen.setJoinStyle(Qt.RoundJoin)

        scene.addLine(n_03[0] * factor, n_03[1] * factor - load_spacing, n_07[0] * factor, n_07[1] * factor - load_spacing, load_pen)
        scene.addLine(n_03[0] * factor, n_03[1] * factor - load_spacing - load_high, n_07[0] * factor, n_07[1] * factor - load_spacing - load_high, load_pen)
        scene.addLine(n_07[0] * factor, n_07[1] * factor - load_spacing, n_06[0] * factor, n_06[1] * factor - load_spacing, load_pen)
        scene.addLine(n_07[0] * factor, n_07[1] * factor - load_spacing - load_high, n_06[0] * factor, n_06[1] * factor - load_spacing - load_high, load_pen)

        scene.addLine(n_03[0] * factor, n_03[1] * factor - load_spacing, n_03[0] * factor, n_03[1] * factor - load_spacing - load_high, load_pen)
        scene.addLine(n_07[0] * factor, n_07[1] * factor - load_spacing, n_07[0] * factor, n_07[1] * factor - load_spacing - load_high, load_pen)
        scene.addLine(n_06[0] * factor, n_06[1] * factor - load_spacing, n_06[0] * factor, n_06[1] * factor - load_spacing - load_high, load_pen)

        scene.addLine(n_03[0] * factor, n_07[1] * factor - (load_spacing * 2 + load_high), n_06[0] * factor, n_07[1] * factor - (load_spacing * 2 + load_high), load_pen)
        scene.addLine(n_03[0] * factor, n_07[1] * factor - (load_spacing * 2 + load_high *2), n_06[0] * factor, n_07[1] * factor - (load_spacing * 2 + load_high * 2), load_pen)

        scene.addLine(n_03[0] * factor, n_07[1] * factor - (load_spacing * 2 + load_high), n_03[0] * factor, n_07[1] * factor - (load_spacing * 2 + load_high *2), load_pen)
        scene.addLine(n_07[0] * factor, n_07[1] * factor - (load_spacing * 2 + load_high), n_07[0] * factor, n_07[1] * factor - (load_spacing * 2 + load_high *2), load_pen)
        scene.addLine(n_06[0] * factor, n_07[1] * factor - (load_spacing * 2 + load_high), n_06[0] * factor, n_07[1] * factor - (load_spacing * 2 + load_high *2), load_pen)

        scene.addLine(n_02[0] * factor, n_02[1] * factor - load_spacing, n_05[0] * factor, n_05[1] * factor - load_spacing, load_pen)
        scene.addLine(n_02[0] * factor, n_02[1] * factor - (load_spacing + load_high), n_05[0] * factor, n_05[1] * factor - (load_spacing + load_high), load_pen)

        scene.addLine(n_02[0] * factor, n_02[1] * factor - load_spacing, n_02[0] * factor, n_02[1] * factor - (load_spacing + load_high), load_pen)
        scene.addLine(n_07[0] * factor, n_02[1] * factor - load_spacing, n_07[0] * factor, n_02[1] * factor - (load_spacing + load_high), load_pen)
        scene.addLine(n_05[0] * factor, n_05[1] * factor - load_spacing, n_05[0] * factor, n_05[1] * factor - (load_spacing + load_high), load_pen)

        #Beschriftung der Lasten


    def validate(self, s):
        # Replace comma with dot
        s = s.replace(',', '.')

        # Replace empty string with '0'
        if s == '':
            s = '0'

        # Remove spaces
        s = s.rstrip()

        try:
            f = float(s)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Error')
            msg.setText('Please enter a number.')
            msg.exec_()
            s = '0'

        if f <= 0.0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Error')
            msg.setText('Please enter a positive number.')
            msg.exec_()
            s = '0'

        return s

    def onChange_checkBox_loads(self):
        if self.ui.checkBox_loads.checkState():
            # save it in config
            self.presets['check_load'] = 1

            # save it in calculation model
            self.calculation_model['check_load'] = 1

            # enable GroupBoxes
            self.ui.groupBox_SW.setEnabled(True)
            self.ui.groupBox_Snow.setEnabled(True)
            self.ui.groupBox_Slab.setEnabled(True)
            self.ui.checkBox_steel_design.setEnabled(True)
        else:
            self.presets['check_load'] = 0
            self.calculation_model['check_load'] = 0

            # disable GroupBoxes
            self.ui.groupBox_SW.setEnabled(False)
            self.ui.groupBox_Snow.setEnabled(False)
            self.ui.groupBox_Slab.setEnabled(False)
            self.ui.checkBox_steel_design.setEnabled(False)

    def onChange_checkBox_steel_design(self):
        if self.ui.checkBox_steel_design.checkState():
            self.presets['check_steel_design'] = 1
            self.calculation_model['check_steel_design'] = 1
        else:
            self.presets['check_steel_design'] = 0
            self.calculation_model['check_steel_design'] = 0

    def onChange_l_1(self):
        s = self.ui.lineEdit_l_1.text()
        s = self.validate(s)
        self.presets['dimensions'][0] = s
        l_1 = float(s)

        # Update calculation model
        self.calculation_model['structure']['dimensions'][0] = l_1

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
        s = self.ui.lineEdit_l_2.text()
        s = self.validate(s)
        self.presets['dimensions'][1] = s
        l_2 = float(s)

        # Update calculation model
        self.calculation_model['structure']['dimensions'][1] = l_2

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
        s = self.ui.lineEdit_l_3.text()
        s = self.validate(s)
        self.presets['dimensions'][2] = s
        l_3 = float(s)

        # Update calculation model
        self.calculation_model['structure']['dimensions'][2] = l_3

        n_4 = self.graphic_model['node']['04']
        n_5 = self.graphic_model['node']['05']
        n_6 = self.graphic_model['node']['06']
        n_7 = self.graphic_model['node']['07']
        n_8 = self.graphic_model['node']['08']
        n_10 = self.graphic_model['node']['10']

        delta_x = l_3 - n_4[0] + n_10[0]

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
        s = self.ui.lineEdit_h_1.text()
        s = self.validate(s)
        self.presets['dimensions'][3] = s
        h_1 = float(s)

        # Update calculation model
        self.calculation_model['structure']['dimensions'][3] = h_1

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
        s = self.ui.lineEdit_h_2.text()
        s = self.validate(s)
        self.presets['dimensions'][4] = s
        h_2 = float(s)

        # Update calculation model
        self.calculation_model['structure']['dimensions'][4] = h_2

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
        s = self.ui.lineEdit_h_3.text()
        s = self.validate(s)
        self.presets['dimensions'][5] = s
        h_3 = float(s)

        # Update calculation model
        self.calculation_model['structure']['dimensions'][5] = h_3

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

    def onChange_g_r(self):
        s = self.ui.lineEdit_g_r.text()
        s = self.validate(s)
        self.presets['loads']['self-weight'][0] = s
        g_r = float(s)

        # Update calculation model
        self.calculation_model['loads']['self-weight'][0] = g_r
        pass

    def onChange_g_s(self):
        s = self.ui.lineEdit_g_s.text()
        s = self.validate(s)
        self.presets['loads']['self-weight'][1] = s
        g_s = float(s)

        # Update calculation model
        self.calculation_model['loads']['self-weight'][1] = g_s
        pass

    def onChange_g_w(self):
        s = self.ui.lineEdit_g_w.text()
        s = self.validate(s)
        self.presets['loads']['self-weight'][2] = s
        g_w = float(s)

        # Update calculation model
        self.calculation_model['loads']['self-weight'][2] = g_w
        pass

    def onChange_s_r(self):
        s = self.ui.lineEdit_s_r.text()
        s = self.validate(s)
        self.presets['loads']['snow'][0] = s
        s_r = float(s)

        # Update calculation model
        self.calculation_model['loads']['snow'][0] = s_r
        pass

    def onChange_p_s(self):
        s = self.ui.lineEdit_p_s.text()
        s = self.validate(s)
        self.presets['loads']['slab'][0] = s
        p_s = float(s)

        # Update calculation model
        self.calculation_model['loads']['slab'][0] = p_s
        pass

    def onCurrentIndexChanged_Material_o_c(self, index):
        self.presets['material'][0] = index

        # Update calculation model
        self.calculation_model['structure']['material'][0] = self.material_list[index]

    def onCurrentIndexChanged_Material_i_c(self, index):
        self.presets['material'][1] = index

        # Update calculation model
        self.calculation_model['structure']['material'][1] = self.material_list[index]

    def onCurrentIndexChanged_Material_r(self, index):
        self.presets['material'][2] = index

        # Update calculation model
        self.calculation_model['structure']['material'][2] = self.material_list[index]

    def onCurrentIndexChanged_Material_s(self, index):
        self.presets['material'][3] = index

        # Update calculation model
        self.calculation_model['structure']['material'][3] = self.material_list[index]

    def onCurrentIndexChanged_CS_o_c(self, index):
        self.presets['cross_section'][0] = index

        # Update calculation model
        self.calculation_model['structure']['cs'][0] = self.cross_section_list_1[index]

    def onCurrentIndexChanged_CS_i_c(self, index):
        self.presets['cross_section'][1] = index

        # Update calculation model
        self.calculation_model['structure']['cs'][1] = self.cross_section_list_2[index]

    def onCurrentIndexChanged_CS_r(self, index):
        self.presets['cross_section'][2] = index

        # Update calculation model
        self.calculation_model['structure']['cs'][2] = self.cross_section_list_1[index]

    def onCurrentIndexChanged_CS_s(self, index):
        self.presets['cross_section'][3] = index

        # Update calculation model
        self.calculation_model['structure']['cs'][3] = self.cross_section_list_1[index]

    def onCurrentIndexChanged_support_1(self, index):
        self.presets['supports'][0] = index

        # Update calculation model
        self.calculation_model['structure']['supports'][0] = self.support_list[index]

        # Update graphic model
        self.graphic_model['supports']['1'] = self.support_list[index]
        self.drawGraphic()

    def onCurrentIndexChanged_support_2(self, index):
        self.presets['supports'][1] = index

        # Update calculation model
        self.calculation_model['structure']['supports'][1] = self.support_list[index]

        # Update graphic model
        self.graphic_model['supports']['2'] = self.support_list[index]
        self.drawGraphic()

    def onCurrentIndexChanged_support_3(self, index):
        self.presets['supports'][2] = index

        # Update calculation model
        self.calculation_model['structure']['supports'][2] = self.support_list[index]

        # Update graphic model
        self.graphic_model['supports']['3'] = self.support_list[index]
        self.drawGraphic()

    def onCurrentIndexChanged_support_4(self, index):
        self.presets['supports'][3] = index

        # Update calculation model
        self.calculation_model['structure']['supports'][3] = self.support_list[index]

        # Update graphic model
        self.graphic_model['supports']['4'] = self.support_list[index]
        self.drawGraphic()


    def onCalculate(self):
        # Save data in dialog
        self.writeConfig()

        # Make an instance of class MyRFEM and init it
        my_rfem = MyRFEM(self.calculation_model)

        # Call the calculation method in the class and store the results in a dictionary
        self.results = my_rfem.calculate()

        # This method close the model and close the connection to RFEM server.
        my_rfem.done()

    def onCancel(self):
        print('Schluss jetzt!')
        self.close()


def window():
    app = QApplication(sys.argv)
    # TODO: Make path specification better
    with open('./Examples/FrameGenerator_2D/styles.qss', 'r') as f:
        style = f.read()
        app.setStyleSheet(style)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
	window()