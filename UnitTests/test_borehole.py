import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, SetAddonStatus
from RFEM.enums import AddOn, MaterialModel
from RFEM.BasicObjects.material import Material
from RFEM.SpecialObjects.borehole import Borehole

if Model.clientModel is None:
    Model()

def test_borehole():

    SetAddonStatus(Model.clientModel, AddOn.geotechnical_analysis_active, True)
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'Sand, closely graded (fine sand) | --')
    Material(2, 'Clay, medium plastic | --')
    Material(3, 'Gravel, well-graded (GW) | DIN 18196:2011-05')
    Material(4, 'Peat (Pt) | DIN 18196:2011-05')
    Material(5, 'Silt, inorganic, medium to high plasticity (MH) | DIN 18196:2011-05')

    Borehole(1, [0,0,0], None, [[1, 2.5], [3, 4.5], [2, 7]])
    Borehole(2, [10,10,-2], 5, [[2, 3.5], [4, 7.5], [5, 9]], 'Borehole 2')

    Model.clientModel.service.finish_modification()

    bore1 = Model.clientModel.service.get_borehole(1)
    bore2 = Model.clientModel.service.get_borehole(2)

    assert bore1.no == 1
    assert bore1.groundwater == False
    print(bore1.layers_table[0][1].row)
    assert bore1.layers_table[0][1].row['depth'] == 4.5

    assert bore2.no == 2
    assert bore2.groundwater == True
    assert bore2.coordinate_2 == -2
    assert bore2.layers_table[0][0].row['depth'] == 3.5
    assert bore2.name == 'Borehole 2'

def test_getBorehole():

    SetAddonStatus(Model.clientModel, AddOn.geotechnical_analysis_active, True)
    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    Material(1, 'Sand, closely graded (fine sand) | --')
    Material(2, 'Clay, medium plastic | --')
    Material(3, 'Gravel, well-graded (GW) | DIN 18196:2011-05')

    Borehole(1, [0,0,0], None, [[1, 2.5], [3, 4.5], [2, 7]], name = 'Borehole')

    borehole = Borehole.GetBorehole(1)

    Model.clientModel.service.finish_modification()

    assert borehole['no'] == 1
    assert borehole['coordinate_2'] == 0
    assert borehole['name'] == 'Borehole'
