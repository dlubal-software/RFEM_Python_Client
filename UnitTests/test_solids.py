import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.enums import SetType
from RFEM.initModel import Model
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.solid import Solid
from RFEM.TypesForSolids.solidGas import SolidGas
from RFEM.TypesForSolids.solidContact import SolidContact
from RFEM.BasicObjects.solidSet import SolidSet

if Model.clientModel is None:
    Model()

def test_solids_and_solid_sets():

    # Testing solids
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Material(2, 'Sand')

    # Solid 1
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10.0, 0.0, 0.0)
    Node(3, 10.0, 10.0, 0.0)
    Node(4, 0.0, 10.0, 0.0)

    Node(5, 0.0, 0.0, -5.0)
    Node(6, 10.0, 0.0, -5.0)
    Node(7, 10.0, 10.0, -5.0)
    Node(8, 0.0, 10.0, -5.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Line(5, '5 6')
    Line(6, '6 7')
    Line(7, '7 8')
    Line(8, '8 5')

    Line(9, '1 5')
    Line(10, '2 6')
    Line(11, '3 7')
    Line(12, '4 8')

    Thickness(1, 'My Test Thickness', 1, 0.05)

    Surface(1, '1-4', 1)
    Surface(2, '5-8', 1)
    Surface(3, '1 9 5 10', 1)
    Surface(4, '2 10 6 11', 1)
    Surface(5, '3 11 7 12', 1)
    Surface(6, '4 12 8 9', 1)

    Solid.Soil(1, '1-6', 2)

    solid = Model.clientModel.service.get_solid(1)
    assert round(solid.volume, 1) == 500
    assert solid.type == 'TYPE_SOIL'

    # Solid 2
    Node(9, 0.0, 20.0, 0.0)
    Node(10, 10.0, 20.0, 0.0)
    Node(11, 10.0, 30.0, 0.0)
    Node(12, 0.0, 30.0, 0.0)

    Node(13, 0.0, 20.0, -5.0)
    Node(14, 10.0, 20.0, -5.0)
    Node(15, 10.0, 30.0, -5.0)
    Node(16, 0.0, 30.0, -5.0)

    Line(13, '9 10')
    Line(14, '10 11')
    Line(15, '11 12')
    Line(16, '12 9')

    Line(17, '13 14')
    Line(18, '14 15')
    Line(19, '15 16')
    Line(20, '16 13')

    Line(21, '9 13')
    Line(22, '10 14')
    Line(23, '11 15')
    Line(24, '12 16')

    Surface(7, '13-16', 1)
    Surface(8, '17-20', 1)
    Surface(9, '13 22 17 21', 1)
    Surface(10, '15 23 19 24', 1)
    Surface(11, '16 21 20 24', 1)
    Surface(12, '14 22 18 23', 1)

    Material(3, 'S275')
    Solid.Standard(2, '7-12', 3)

    solid = Model.clientModel.service.get_solid(2)
    assert round(solid.volume, 1) == 500
    assert solid.type == 'TYPE_STANDARD'

    # Solid 3
    Node(17, 20.0, 20.0, 0.0)
    Node(18, 20.0, 30.0, 0.0)
    Node(19, 20.0, 20.0, -5.0)
    Node(20, 20.0, 30.0, -5.0)

    Line(25, '10 17')
    Line(26, '17 18')
    Line(27, '18 11')
    Line(28, '14 19')
    Line(29, '19 20')
    Line(30, '20 15')
    Line(31, '17 19')
    Line(32, '18 20')

    Surface(13, '25 26 27 14', 1)
    Surface(14, '28 29 30 18', 1)
    Surface(15, '25 31 28 22', 1)
    Surface(16, '27 32 30 23', 1)
    Surface(17, '26 31 29 32', 1)

    SolidContact()
    Solid.Contact(3, '13-17,12', 1, params={'solid_contact': 1,
                 'solid_contact_first_surface':12})

    solid = Model.clientModel.service.get_solid(3)
    assert solid.type == 'TYPE_CONTACT'
    assert solid.solid_contact_first_surface == 12
    assert solid.solid_contact_second_surface == 17

    # Solid 4
    Node(21, 11.0, 0.0, 0.0)
    Node(22, 21.0, 0.0, 0.0)
    Node(23, 11.0, 10.0, 0.0)
    Node(24, 21.0, 10.0, 0.0)

    Node(25, 11.0, 0.0, -10.0)
    Node(26, 21.0, 0.0, -10.0)
    Node(27, 11.0, 10.0, -10.0)
    Node(28, 21.0, 10.0, -10.0)

    Line(33, '21 22')
    Line(34, '22 24')
    Line(35, '24 23')
    Line(36, '23 21')

    Line(37, '25 26')
    Line(38, '26 28')
    Line(39, '27 28')
    Line(40, '25 27')

    Line(41, '21 25')
    Line(42, '22 26')
    Line(43, '24 28')
    Line(44, '23 27')

    Surface(18, '33-36', 1)
    Surface(19, '37-40', 1)
    Surface(20, '33 42 37 41', 1)
    Surface(21, '34 43 38 42', 1)
    Surface(22, '35 44 39 43', 1)
    Surface(23, '36 41 40 44', 1)

    Material(4, 'Krypton')
    SolidGas(1,params={'pressure':21000000, 'temperature':293.1})
    Solid.Gas(4, '18-23', 4,params={'gas':1})
    SolidSet(1,'2 3')
    SolidSet.ContinuousSolids(2, '2 3')
    SolidSet.GroupOfSolids(3, '1 4')

    Model.clientModel.service.finish_modification()

    solid = Model.clientModel.service.get_solid(4)
    assert round(solid.volume, 1) == 1000
    assert solid.type == 'TYPE_GAS'

    gas = Model.clientModel.service.get_solid_gas(1)
    assert round(gas.pressure, 1) == 21000000.0 # 210 bar
    assert round(gas.temperature, 1) == 293.1 # 20°C

    solidSet = Model.clientModel.service.get_solid_set(1)
    assert solidSet.set_type == SetType.SET_TYPE_GROUP.name
    assert solidSet.solids == '2 3'

    solidSet = Model.clientModel.service.get_solid_set(2)
    assert solidSet.set_type == SetType.SET_TYPE_CONTINUOUS.name
    assert solidSet.solids == '2 3'

    solidSet = Model.clientModel.service.get_solid_set(3)
    assert solidSet.set_type == SetType.SET_TYPE_GROUP.name
    assert solidSet.solids == '1 4'

def test_solid_delete():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'S235')
    Material(2, 'Sand')

    # Solid 1
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 10.0, 0.0, 0.0)
    Node(3, 10.0, 10.0, 0.0)
    Node(4, 0.0, 10.0, 0.0)

    Node(5, 0.0, 0.0, -5.0)
    Node(6, 10.0, 0.0, -5.0)
    Node(7, 10.0, 10.0, -5.0)
    Node(8, 0.0, 10.0, -5.0)

    Line(1, '1 2')
    Line(2, '2 3')
    Line(3, '3 4')
    Line(4, '4 1')

    Line(5, '5 6')
    Line(6, '6 7')
    Line(7, '7 8')
    Line(8, '8 5')

    Line(9, '1 5')
    Line(10, '2 6')
    Line(11, '3 7')
    Line(12, '4 8')

    Thickness(1, 'My Test Thickness', 1, 0.05)

    Surface(1, '1-4', 1)
    Surface(2, '5-8', 1)
    Surface(3, '1 9 5 10', 1)
    Surface(4, '2 10 6 11', 1)
    Surface(5, '3 11 7 12', 1)
    Surface(6, '4 12 8 9', 1)

    Solid.Soil(1, '1-6', 2)

    solid = Model.clientModel.service.get_solid(1)
    assert round(solid.volume, 1) == 500
    assert solid.type == 'TYPE_SOIL'

    # Solid 2
    Node(9, 0.0, 20.0, 0.0)
    Node(10, 10.0, 20.0, 0.0)
    Node(11, 10.0, 30.0, 0.0)
    Node(12, 0.0, 30.0, 0.0)

    Node(13, 0.0, 20.0, -5.0)
    Node(14, 10.0, 20.0, -5.0)
    Node(15, 10.0, 30.0, -5.0)
    Node(16, 0.0, 30.0, -5.0)

    Line(13, '9 10')
    Line(14, '10 11')
    Line(15, '11 12')
    Line(16, '12 9')

    Line(17, '13 14')
    Line(18, '14 15')
    Line(19, '15 16')
    Line(20, '16 13')

    Line(21, '9 13')
    Line(22, '10 14')
    Line(23, '11 15')
    Line(24, '12 16')

    Surface(7, '13-16', 1)
    Surface(8, '17-20', 1)
    Surface(9, '13 22 17 21', 1)
    Surface(10, '15 23 19 24', 1)
    Surface(11, '16 21 20 24', 1)
    Surface(12, '14 22 18 23', 1)

    Material(3, 'S275')
    Solid.Standard(2, '7-12', 3)

    Solid.DeleteSolid('1')

    Model.clientModel.service.finish_modification()

    modelInfo = Model.clientModel.service.get_model_info()

    assert modelInfo.property_solid_count == 1
