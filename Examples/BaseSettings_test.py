import sys
sys.path.append(".")
from RFEM.Loads.surfaceLoad import SurfaceLoad
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.Loads.nodalLoad import NodalLoad
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.TypesForMembers.memberHinge import MemberHinge
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.BasicObjects.solidSet import SolidSet
from RFEM.BasicObjects.surfaceSet import SurfaceSet
from RFEM.BasicObjects.memberSet import MemberSet
from RFEM.BasicObjects.lineSet import LineSet
from RFEM.BasicObjects.opening import Opening
from RFEM.BasicObjects.solid import Solid
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.thickness import Thickness 
from RFEM.BasicObjects.section import Section
from RFEM.BasicObjects.material import Material
from RFEM.initModel import *
from RFEM.enums import *
from RFEM.baseSettings import BaseSettings

if __name__ == '__main__':

    clientModel.service.begin_modification()

    # Set Base Settings
    BaseSettings(12, GlobalAxesOrientationType.E_GLOBAL_AXES_ORIENTATION_ZUP, LocalAxesOrientationType.E_LOCAL_AXES_ORIENTATION_ZUP, [0.001, 0.002, 0.003, 0.004])

    print('Ready!')

    clientModel.service.finish_modification()

