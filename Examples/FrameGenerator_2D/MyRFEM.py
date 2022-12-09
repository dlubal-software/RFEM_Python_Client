import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import NodalSupportType, MemberLoadDirection, AnalysisType
from RFEM.initModel import Model, insertSpaces
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.TypesForMembers.memberHinge import MemberHinge
from RFEM.BasicObjects.member import Member
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.dataTypes import inf
class MyRFEM():
    input ={}
    results ={}

    def __init__(self, calculation_model):
        self.input = calculation_model

        Model()
        Model.clientModel.service.begin_modification()

        # Creation the nodes
        x = 0.0
        y = 0.0
        z = 0.0
        Node(1, x, y ,z)

        z = float(self.input['structure']['dimensions'][3]) * -1
        Node(2, x, y ,z)

        z = (float(self.input['structure']['dimensions'][3])
            + float(self.input['structure']['dimensions'][4])) * -1
        Node(3, x, y ,z)

        x = (float(self.input['structure']['dimensions'][0])
            + float(self.input['structure']['dimensions'][1])
            + float(self.input['structure']['dimensions'][2]))
        z = 0.0
        Node(4, x, y ,z)

        z = float(self.input['structure']['dimensions'][3]) * -1
        Node(5, x, y, z)

        z = (float(self.input['structure']['dimensions'][3])
            + float(self.input['structure']['dimensions'][4])) * -1
        Node(6, x, y, z)

        x = x/2
        z = (float(self.input['structure']['dimensions'][3])
            + float(self.input['structure']['dimensions'][4])
            + float(self.input['structure']['dimensions'][5])) * -1
        Node(7, x, y, z)

        x = float(self.input['structure']['dimensions'][0])
        z = 0.0
        Node(8, x, y, z)

        z = float(self.input['structure']['dimensions'][3]) * -1
        Node(9, x, y, z)

        x = (float(self.input['structure']['dimensions'][0])
            + float(self.input['structure']['dimensions'][1]))
        z = 0.0
        Node(10, x, y, z)

        z = float(self.input['structure']['dimensions'][3]) * -1
        Node(11, x, y, z)

        # Create materials
        Material(1, self.input['structure']['material'][0])
        Material(2, self.input['structure']['material'][1])
        Material(3, self.input['structure']['material'][2])
        Material(4, self.input['structure']['material'][3])

        # Create cross-sections
        Section(1, self.input['structure']['cs'][0], 1)
        Section(2, self.input['structure']['cs'][1], 2)
        Section(3, self.input['structure']['cs'][2], 3)
        Section(4, self.input['structure']['cs'][3], 4)

        # Create a hinge
        MemberHinge(1)

        # Create the members
        Member(1, 1, 2, 0.0, 1, 1)
        Member(2, 2, 3, 0.0, 1, 1)
        Member(3, 4, 5, 0.0, 1, 1)
        Member(4, 5, 6, 0.0, 1, 1)

        Member(5, 8, 9, 0.0, 2, 2, 0, 1)
        Member(6, 10, 11, 0.0, 2, 2, 0, 1)

        Member(7, 3, 7, 0.0, 3, 3)
        Member(8, 7, 6, 0.0, 3, 3)

        Member(9, 2, 9, 0.0, 4, 4, 1, 0)
        Member(10, 9, 11, 0.0, 4, 4)
        Member(11, 11, 5, 0.0, 4, 4, 0, 1)

        # Create supports
        if self.input['structure']['supports'][0] == 'Fixed':
            support = NodalSupportType.FIXED
        else:
            support = NodalSupportType.HINGED

        NodalSupport(1, '1', support)

        if self.input['structure']['supports'][1] == 'Fixed':
            support = NodalSupportType.FIXED
        else:
            support = NodalSupportType.HINGED

        NodalSupport(2, '4', support)

        if self.input['structure']['supports'][2] == 'Fixed':
            support = NodalSupportType.FIXED
        else:
            support = NodalSupportType.HINGED

        NodalSupport(3, '8', support)

        if self.input['structure']['supports'][3] == 'Fixed':
            support = NodalSupportType.FIXED
        else:
            support = NodalSupportType.HINGED

        NodalSupport(4, '10', support)

        NodalSupport(5, '3, 6', [0, inf, 0, 0, 0, 0])

        # Create load cases and load combinations
        # TODO: Set the right Action Category
        StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
        StaticAnalysisSettings.SecondOrderPDelta(2, "SecondOrder")

        LoadCase(1, 'Self-Weight', [True, 0.0, 0.0, 1.0])
        LoadCase(2, 'Snow', [False])
        LoadCase(3, 'Slab', [False])

        # Create the loads
        magnitude = self.input['loads']['self-weight'][0] * 1000 # convert in SI unit N/m
        MemberLoad(1, 1, '7,8', MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, magnitude)

        magnitude = self.input['loads']['self-weight'][1] * 1000
        MemberLoad(2, 1, '1-4', MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, magnitude)

        magnitude = self.input['loads']['self-weight'][2] * 1000
        MemberLoad(3, 1, '9-11', MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, magnitude)

        magnitude = self.input['loads']['snow'][0] * 1000
        MemberLoad(1, 2, '7,8', MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, magnitude)

        magnitude = self.input['loads']['slab'][0] * 1000
        MemberLoad(1, 3, '9-11', MemberLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_PROJECTED, magnitude)

        # Create load combinations
        LoadCombination(1, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1.35, 1, 1, False]])
        LoadCombination(2, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1.35, 1, 1, False], [1.5, 2, 2, True]])
        LoadCombination(3, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1.35, 1, 1, False], [1.5, 2, 2, True], [1.05, 3, 3, False]])
        LoadCombination(4, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1.35, 1, 1, False], [1.5, 3, 3, True]])
        LoadCombination(5, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1.35, 1, 1, False], [0.75, 2, 2, False], [1.5, 3, 3, True]])
        LoadCombination(6, AnalysisType.ANALYSIS_TYPE_STATIC, 2, '', 2, False, False, False, True, [[1.0, 1, 1, False]])
        LoadCombination(7, AnalysisType.ANALYSIS_TYPE_STATIC, 2, '', 2, False, False, False, True, [[1.0, 1, 1, False], [1.0, 2, 2, True]])
        LoadCombination(8, AnalysisType.ANALYSIS_TYPE_STATIC, 2, '', 2, False, False, False, True, [[1.0, 1, 1, False], [1.0, 2, 2, True], [0.7, 3, 3, False]])
        LoadCombination(8, AnalysisType.ANALYSIS_TYPE_STATIC, 2, '', 2, False, False, False, True, [[1.0, 1, 1, False], [1.0, 2, 2, True], [0.7, 3, 3, False]])
        LoadCombination(9, AnalysisType.ANALYSIS_TYPE_STATIC, 2, '', 2, False, False, False, True, [[1.0, 1, 1, False], [1.0, 3, 3, True]])
        LoadCombination(10, AnalysisType.ANALYSIS_TYPE_STATIC, 2, '', 2, False, False, False, True, [[1.0, 1, 1, False], [0.5, 2, 2, False], [1.0, 3, 3, True]])
        LoadCombination(11, AnalysisType.ANALYSIS_TYPE_STATIC, 3, '', 2, False, False, False, True, [[1.0, 1, 1, False]])
        LoadCombination(12, AnalysisType.ANALYSIS_TYPE_STATIC, 3, '', 2, False, False, False, True, [[1.0, 1, 1, False], [0.2, 2, 2, True]])
        LoadCombination(13, AnalysisType.ANALYSIS_TYPE_STATIC, 3, '', 2, False, False, False, True, [[1.0, 1, 1, False], [0.2, 2, 2, True], [0.3, 3, 3, False]])
        LoadCombination(14, AnalysisType.ANALYSIS_TYPE_STATIC, 3, '', 2, False, False, False, True, [[1.0, 1, 1, False], [0.3, 3, 3, True]])
        LoadCombination(15, AnalysisType.ANALYSIS_TYPE_STATIC, 4, '', 2, False, False, False, True, [[1.0, 1, 1, False]])
        LoadCombination(16, AnalysisType.ANALYSIS_TYPE_STATIC, 4, '', 2, False, False, False, True, [[1.0, 1, 1, False], [0.3, 3, 3, True]])

        Model.clientModel.service.finish_modification()



    def calculate(self):
        return self.results

    def done(self):
        # This method close the model and close the connection to RFEM server.
        pass



if __name__ == "__main__":
    # ist ein Argument vorhanden?
    # Wenn ja, dann die JSON-Datei einlesen und die Methode calculate() aufrufen.
    pass
