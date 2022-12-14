from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import *

class SteelEffectiveLengths():
    def __init__(self,
                 no: int = 1,
                 members: str = '1',
                 member_sets: str = '',
                 flexural_buckling_about_y: bool = True,
                 flexural_buckling_about_z: bool = True,
                 torsional_buckling: bool = True,
                 lateral_torsional_buckling: bool = True,
                 principal_section_axes: bool = True,
                 geometric_section_axes: bool = True,
                 name: str = 'SEL1',
                 nodal_supports: list = [
                     [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, \
                      0.0, 0.0, 0.0, 0.0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, \
                      SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, "1"],
                     [SteelEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION, True, 0.0, SteelEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, \
                      0.0, 0.0, 0.0, 0.0, SteelEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, SteelEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, \
                      SteelEffectiveLengthsRestraintTypeAboutZ.SUPPORT_STATUS_NO, SteelEffectiveLengthsRestraintTypeWarping.SUPPORT_STATUS_NO, "2"]
                                        ],
                 factors: list = [
                     [1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                                 ],
                 intermediate_nodes: bool = False,
                 different_properties: bool = True,
                 factors_definition_absolute: bool = False,
                 import_from_stability_analysis_enabled: bool = False,
                 determination_of_mcr = SteelEffectiveLengthsDeterminationMcrEurope.DETERMINATION_EUROPE_EIGENVALUE,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Steel Effective Length Tag
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            flexural_buckling_about_y (bool): Flexural Buckling About Y Option
            flexural_buckling_about_z (bool): Flexural Buckling About Z Option
            torsional_buckling (bool): Torsional Buckling Option
            lateral_torsional_buckling (bool): Lateral Torsional Buckling Option
            principal_section_axes (bool): Principal Section Axes Option
            geometric_section_axes (bool): Geometric Section Axes Option
            name (str): User Defined Effective Length Name
            nodal_supports (lst): Nodal Support Table Definition
                nodal_supports[i][0] (enum): Support Type Enumeration Type
                nodal_supports[i][1] (bool): Support in Z Option
                nodal_supports[i][2] (float): Support Spring in Y Coefficient
                nodal_supports[i][3] (enum): Eccentricity Type Enumeration Type
                nodal_supports[i][4] (float): Eccentricity in Z Direction
                nodal_supports[i][5] (float): Restraint Spring About X Coefficient
                nodal_supports[i][6] (float): Restraint Spring About Z Coefficient
                nodal_supports[i][7] (float): Restraint Spring Warping Coefficient
                nodal_supports[i][8] (enum): Support Type in Y Enumeration Type
                nodal_supports[i][9] (enum): Restraint Type in X Enumeration Type
                nodal_supports[i][10] (enum): Restraint Type in Z Enumeration Type
                nodal_supports[i][11] (enum): Restraint Type Warping Enumeration Type
                nodal_supports[i][12] (str): Assigned Nodes
            factors (list of lists): Effective Length Factors
                factors[i][0] (float): Flexural Buckling in U Coefficient
                factors[i][1] (float): Flexural Buckling in V Coefficient
                factors[i][2] (float): Flexural Buckling in Y Coefficient
                factors[i][3] (float): Flexural Buckling in Z Coefficient
                factors[i][4] (float): Torsional Buckling Coefficient
                factors[i][5] (float): Lateral Torsional Buckling Coefficient
                factors[i][6] (float): Lateral Torsional Buckling Top Coefficient
                factors[i][7] (float): Lateral Torsional Buckling Bottom Coefficient
                factors[i][8] (float): Twist Restraint Coefficient
                factors[i][9] (float): Lateral Torsional Restraint Coefficient
                factors[i][10] (float): Critical Moment
            intermediate_nodes (bool): Intermediate Nodes Option
            different_properties (bool): Different Properties Option
            factors_definition_absolute (bool): Absolute Factors Definition Option
            import_from_stability_analysis_enabled (bool): Import From Stability Analysis Option
            determination_of_mcr (enum): Steel Effective Lengths Determination Mcr Europe Enumeration Item
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client Model | Types For Steel Design Effective Lengths
        clientObject = model.clientModel.factory.create('ns0:steel_effective_lengths')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Effective Lengths No.
        clientObject.no = no

        # Effective Lengths Assigned Members
        clientObject.members = ConvertToDlString(members)

        # Effective Lengths Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Effective Lengths Flexural Buckling About Y
        clientObject.flexural_buckling_about_y = flexural_buckling_about_y

        # Effective Lengths Flexural Buckling About Z
        clientObject.flexural_buckling_about_z = flexural_buckling_about_z

        # Effective Lengths Torsional Buckling
        clientObject.torsional_buckling = torsional_buckling

        # Effective Lengths Lateral Torsional Buckling
        clientObject.lateral_torsional_buckling = lateral_torsional_buckling

        # Effective Lengths Principal Section Axes
        clientObject.principal_section_axes = principal_section_axes

        # Effective Lengths Geometric Section Axes
        clientObject.geometric_section_axes = geometric_section_axes

        # Effective Lengths User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Effective Lengths Nodal Supports
        clientObject.nodal_supports = model.clientModel.factory.create('ns0:array_of_steel_effective_lengths_nodal_supports')

        for i,j in enumerate(nodal_supports):
            mlvlp = model.clientModel.factory.create('ns0:steel_effective_lengths_nodal_supports_row')
            mlvlp.no = i+1
            mlvlp.row.support_type = nodal_supports[i][0].name
            mlvlp.row.support_in_z = nodal_supports[i][1]
            mlvlp.row.support_spring_in_y = nodal_supports[i][2]
            mlvlp.row.eccentricity_type = nodal_supports[i][3].name
            mlvlp.row.eccentricity_ez = nodal_supports[i][4]
            mlvlp.row.restraint_spring_about_x = nodal_supports[i][5]
            mlvlp.row.restraint_spring_about_z = nodal_supports[i][6]
            mlvlp.row.restraint_spring_warping = nodal_supports[i][7]
            mlvlp.row.support_in_y_type = nodal_supports[i][8].name
            mlvlp.row.restraint_about_x_type = nodal_supports[i][9].name
            mlvlp.row.restraint_about_z_type = nodal_supports[i][10].name
            mlvlp.row.restraint_warping_type = nodal_supports[i][11].name
            mlvlp.row.nodes = ConvertToDlString(nodal_supports[i][12])

            clientObject.nodal_supports.steel_effective_lengths_nodal_supports.append(mlvlp)

        # Effective Lengths Factors
        clientObject.factors = model.clientModel.factory.create('ns0:array_of_steel_effective_lengths_factors')

        for i,j in enumerate(factors):
            mlvlp_f = model.clientModel.factory.create('ns0:steel_effective_lengths_factors_row')
            mlvlp_f.no = i+1
            mlvlp_f.row.flexural_buckling_u = factors[i][0]
            mlvlp_f.row.flexural_buckling_v = factors[i][1]
            mlvlp_f.row.flexural_buckling_y = factors[i][2]
            mlvlp_f.row.flexural_buckling_z = factors[i][3]
            mlvlp_f.row.torsional_buckling = factors[i][4]
            mlvlp_f.row.lateral_torsional_buckling = factors[i][5]
            mlvlp_f.row.lateral_torsional_buckling_top = factors[i][6]
            mlvlp_f.row.lateral_torsional_buckling_bottom = factors[i][7]
            mlvlp_f.row.twist_restraint = factors[i][8]
            mlvlp_f.row.lateral_torsional_restraint = factors[i][9]
            mlvlp_f.row.critical_moment = factors[i][10]

            clientObject.factors.steel_effective_lengths_factors.append(mlvlp_f)

        # Effective Lengths Intermediate Points
        clientObject.intermediate_nodes = intermediate_nodes

        # Effective Lengths Different Properties
        clientObject.different_properties = different_properties

        # Effective Lengths Factors Definition Absolute
        clientObject.factors_definition_absolute = factors_definition_absolute

        # Effective Lengths Import From Stability Analysis Enabled
        clientObject.import_from_stability_analysis_enabled = import_from_stability_analysis_enabled

        # Effective Lengths Determination MCR Europe
        clientObject.determination_mcr_europe = determination_of_mcr.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Steel Effective Lengths to client model
        model.clientModel.service.set_steel_effective_lengths(clientObject)
