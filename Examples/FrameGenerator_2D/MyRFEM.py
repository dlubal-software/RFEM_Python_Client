import os
import sys
import tempfile
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.enums import NodalSupportType, MemberLoadDirection, AnalysisType, ActionCategoryType, AddOn, SetType, SteelBoundaryConditionsSupportType, SteelBoundaryConditionsEccentricityTypeZ
from RFEM.initModel import Model, Calculate_all, SetAddonStatus
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.section import Section
from RFEM.TypesForMembers.memberHinge import MemberHinge
from RFEM.BasicObjects.member import Member
from RFEM.BasicObjects.memberSet import MemberSet
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.LoadCasesAndCombinations.designSituation import DesignSituation, DesignSituationType
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.loadCombination import LoadCombination
from RFEM.Loads.memberLoad import MemberLoad
from RFEM.dataTypes import inf
from RFEM.TypesForSteelDesign.steelEffectiveLengths import SteelEffectiveLengths
from RFEM.TypesForSteelDesign.steelBoundaryConditions import SteelBoundaryConditions
from RFEM.SteelDesign.steelServiceabilityConfiguration import SteelDesignServiceabilityConfigurations
from RFEM.SteelDesign.steelUltimateConfigurations import SteelDesignUltimateConfigurations
from RFEM.Reports.html import ExportResultTablesToHtml
class MyRFEM():
    input = {}
    results = False

    def __init__(self, calculation_model):
        self.input = calculation_model

        Model(True, 'Frame')
        Model.clientModel.service.begin_modification()

        # Activate add on Steel Design
        if self.input['check_steel_design'] == 1:
            SetAddonStatus(Model.clientModel, AddOn.steel_design_active, True)
        else:
            SetAddonStatus(Model.clientModel, AddOn.steel_design_active, False)

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

        MemberSet(1, '9-11', SetType.SET_TYPE_CONTINUOUS)
        MemberSet(2, '1-2', SetType.SET_TYPE_CONTINUOUS)
        MemberSet(3, '3-4', SetType.SET_TYPE_CONTINUOUS)

        if self.input['check_steel_design'] == 1:
            # Design Configurations
            SteelDesignUltimateConfigurations(1, members_no='5-8', member_sets_no='1-3')
            SteelDesignServiceabilityConfigurations(1, members_no='5-8', member_sets_no='1-3')

            p = {
                    "member_steel_design_uls_configuration": 1,
                    "member_steel_design_sls_configuration": 1
            }
            MemberSet(1, '9-11', SetType.SET_TYPE_CONTINUOUS, params=p)
            MemberSet(2, '1-2', SetType.SET_TYPE_CONTINUOUS, params=p)
            MemberSet(3, '3-4', SetType.SET_TYPE_CONTINUOUS, params=p)

            # Columns
            SteelEffectiveLengths(1, '5, 6', factors=[[1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])

            # Slap beam
            # The design properties of members 9, 10, 11 are defined in
            # member set No. 1 and not in member properties.
            p = {
                "design_properties_via_parent_member_set": True,
                "design_properties_parent_member_set": 1
            }

            Member(9, 2, 9, 0.0, 4, 4, 1, 0, params=p)
            Member(10, 9, 11, 0.0, 4, 4, params=p)
            Member(11, 11, 5, 0.0, 4, 4, 0, 1, params=p)

            l = [
                    [0, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, "2"],
                    [1, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, "9"],
                    [2, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, "11"],
                    [3, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, "5"]
                ]

            SteelBoundaryConditions(1, member_sets='1', intermediate_nodes=True, nodal_supports=l)

            # Frame Columns
            p = {
                "design_properties_via_parent_member_set": True,
                "design_properties_parent_member_set": 2
            }

            Member(1, 1, 2, 0.0, 1, 1, params=p)
            Member(2, 2, 3, 0.0, 1, 1, params=p)

            l = [
                    [0, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, "1"],
                    [1, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, "2"],
                    [2, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, "3"]
                ]

            SteelBoundaryConditions(2, member_sets='2', intermediate_nodes=True, nodal_supports=l)

            p = {
                "design_properties_via_parent_member_set": True,
                "design_properties_parent_member_set": 3
            }

            Member(3, 4, 5, 0.0, 1, 1, params=p)
            Member(4, 5, 6, 0.0, 1, 1, params=p)

            l = [
                    [0, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, "4"],
                    [1, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, "5"],
                    [2, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, "6"]
                ]

            SteelBoundaryConditions(3, member_sets='3', intermediate_nodes=True, nodal_supports=l)

            # Roof
            l = [
                    [0, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, ""],
                    [1, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, ""]
                ]
            SteelBoundaryConditions(4, members='7, 8', intermediate_nodes=True, nodal_supports=l)

            p = {
                    "member_steel_design_uls_configuration": 1,
                    "member_steel_design_sls_configuration": 1
            }
            Member(7, 3, 7, 0.0, 3, 3, params=p)
            Member(8, 7, 6, 0.0, 3, 3, params=p)

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

        NodalSupport(5, '2, 3, 5, 6, 7, 9, 11', [0, inf, 0, 0, 0, 0])

        # Create load cases and load combinations
        # TODO: Set the right Action Category


        StaticAnalysisSettings.GeometricallyLinear(1, "Linear")
        StaticAnalysisSettings.SecondOrderPDelta(2, "SecondOrder")

        # Create Design situations
        DesignSituation(1, DesignSituationType.DESIGN_SITUATION_TYPE_STR_PERMANENT_AND_TRANSIENT_6_10)
        DesignSituation(2, DesignSituationType.DESIGN_SITUATION_TYPE_SLS_CHARACTERISTIC)
        DesignSituation(3, DesignSituationType.DESIGN_SITUATION_TYPE_SLS_FREQUENT)
        DesignSituation(4, DesignSituationType.DESIGN_SITUATION_TYPE_SLS_QUASI_PERMANENT)

        LoadCase(1, 'Self-Weight', [True, 0.0, 0.0, 1.0], ActionCategoryType.ACTION_CATEGORY_PERMANENT_G)
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
        #LoadCombination(1, combination_items=[[1.35, 1, 1, False]])
        #LoadCombination(2, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1.35, 1, 1, False], [1.5, 2, 2, True]])
        #LoadCombination(3, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1.35, 1, 1, False], [1.5, 2, 2, True], [1.05, 3, 3, False]])
        #LoadCombination(4, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1.35, 1, 1, False], [1.5, 3, 3, True]])
        #LoadCombination(5, AnalysisType.ANALYSIS_TYPE_STATIC, 1, '', 2, False, False, False, True, [[1.35, 1, 1, False], [0.75, 2, 2, False], [1.5, 3, 3, True]])
        #LoadCombination(6, AnalysisType.ANALYSIS_TYPE_STATIC, 2, '', 2, False, False, False, True, [[1.0, 1, 1, False]])
        #LoadCombination(7, AnalysisType.ANALYSIS_TYPE_STATIC, 2, '', 2, False, False, False, True, [[1.0, 1, 1, False], [1.0, 2, 2, True]])
        #LoadCombination(8, AnalysisType.ANALYSIS_TYPE_STATIC, 2, '', 2, False, False, False, True, [[1.0, 1, 1, False], [1.0, 2, 2, True], [0.7, 3, 3, False]])
        #LoadCombination(8, AnalysisType.ANALYSIS_TYPE_STATIC, 2, '', 2, False, False, False, True, [[1.0, 1, 1, False], [1.0, 2, 2, True], [0.7, 3, 3, False]])
        #LoadCombination(9, AnalysisType.ANALYSIS_TYPE_STATIC, 2, '', 2, False, False, False, True, [[1.0, 1, 1, False], [1.0, 3, 3, True]])
        #LoadCombination(10, AnalysisType.ANALYSIS_TYPE_STATIC, 2, '', 2, False, False, False, True, [[1.0, 1, 1, False], [0.5, 2, 2, False], [1.0, 3, 3, True]])
        #LoadCombination(11, AnalysisType.ANALYSIS_TYPE_STATIC, 3, '', 2, False, False, False, True, [[1.0, 1, 1, False]])
        #LoadCombination(12, AnalysisType.ANALYSIS_TYPE_STATIC, 3, '', 2, False, False, False, True, [[1.0, 1, 1, False], [0.2, 2, 2, True]])
        #LoadCombination(13, AnalysisType.ANALYSIS_TYPE_STATIC, 3, '', 2, False, False, False, True, [[1.0, 1, 1, False], [0.2, 2, 2, True], [0.3, 3, 3, False]])
        #LoadCombination(14, AnalysisType.ANALYSIS_TYPE_STATIC, 3, '', 2, False, False, False, True, [[1.0, 1, 1, False], [0.3, 3, 3, True]])
        #LoadCombination(15, AnalysisType.ANALYSIS_TYPE_STATIC, 4, '', 2, False, False, False, True, [[1.0, 1, 1, False]])
        #LoadCombination(16, AnalysisType.ANALYSIS_TYPE_STATIC, 4, '', 2, False, False, False, True, [[1.0, 1, 1, False], [0.3, 3, 3, True]])

        # TODO Create imperfection cases


        Model.clientModel.service.finish_modification()



    def calculate(self):
        Calculate_all()
        # Was the calculation successful?
        self.results = True
        return self.results

    def get_report(self):
        report_dir = tempfile.gettempdir() + '\\PyExample\\'
        report_dir = report_dir.replace('\\', '/')
        ExportResultTablesToHtml(report_dir, OpenBrowser=False)
        return report_dir + 'index.html'

    def done(self):
        # This method Close the connection to RFEM server.
        Model.clientModel.service.close_connection()

if __name__ == "__main__":
    # ist ein Argument vorhanden?
    # TODO Wenn ja, dann die JSON-Datei einlesen und die Methode calculate() aufrufen.
    pass
