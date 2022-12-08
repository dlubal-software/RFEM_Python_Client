from RFEM.initModel import Model, clearAttributes, deleteEmptyAttributes, ConvertToDlString
from RFEM.enums import TimberEffectiveLengthsSupportType, TimberEffectiveLengthsEccentricityType, TimberEffectiveLengthsSupportTypeInY, \
    TimberEffectiveLengthsRestraintTypeAboutX, TimberEffectiveLengthsDeterminationType

class TimberEffectiveLengths():
    def __init__(self,
                 no: int = 1,
                 members: str = '1',
                 member_sets: str = '',
                 flexural_buckling_about_y: bool = True,
                 flexural_buckling_about_z: bool = True,
                 lateral_torsional_buckling: bool = True,
                 name: str = 'SEL1',
                 nodal_supports: list = [
                     [TimberEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION, True, TimberEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, \
                      TimberEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, TimberEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, "1"],
                     [TimberEffectiveLengthsSupportType.SUPPORT_TYPE_FIXED_IN_Z_Y_AND_TORSION, True, TimberEffectiveLengthsEccentricityType.ECCENTRICITY_TYPE_NONE, \
                      TimberEffectiveLengthsSupportTypeInY.SUPPORT_STATUS_YES, TimberEffectiveLengthsRestraintTypeAboutX.SUPPORT_STATUS_YES, "2"],
                                        ],
                 factors: list = [
                     [1.0, 1.0, 1.0]
                                 ],
                 intermediate_nodes: bool = False,
                 different_properties: bool = True,
                 factors_definition_absolute: bool = False,
                 fire_design_different_buckling_factors: bool = False,
                 import_from_stability_analysis_enabled: bool = False,
                 determination_type = TimberEffectiveLengthsDeterminationType.DETERMINATION_EIGENVALUE_SOLVER,
                 comment: str = '',
                 params: dict = None,
                 model = Model):
        """
        Args:
            no (int): Timber Effective Length Tag
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            flexural_buckling_about_y (bool): Flexural Buckling About Y Option
            flexural_buckling_about_z (bool): Flexural Buckling About Z Option
            lateral_torsional_buckling (bool): Lateral Torsional Buckling Option
            name (str): User Defined Effective Length Name
            nodal_supports (lst): Nodal Support Table Definition
                nodal_supports[i][0] (enum): Support Type Enumeration
                nodal_supports[i][1] (bool): Support in Z Option
                nodal_supports[i][2] (enum): Eccentricity Type Enumeration
                nodal_supports[i][3] (enum): Support Type in Y Enumeration
                nodal_supports[i][4] (enum): Restraint Type in X Enumeration
                nodal_supports[i][5] (str): Assigned Nodes
            factors (list of lists): Effective Length Factors
                factors[i][0] (float): Flexural Buckling in U Coefficient
                factors[i][1] (float): Flexural Buckling in V Coefficient
                factors[i][2] (float): Critical Moment
            intermediate_nodes (bool): Intermediate Nodes Option
            different_properties (bool): Different Properties Option
            factors_definition_absolute (bool): Absolute Factors Definition Option
            fire_design_different_buckling_factors (bool): Different Fire Design Buckling Factors
            import_from_stability_analysis_enabled (bool): Import From Stability Analysis Option
            determination_type (enum): Timber Effective Lengths Determination Type
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client Model | Types For Timber Design Effective Lengths
        clientObject = model.clientModel.factory.create('ns0:timber_effective_lengths')

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

        # Effective Lengths Lateral Torsional Buckling
        clientObject.lateral_torsional_buckling = lateral_torsional_buckling

        # Effective Lengths Intermediate Points
        clientObject.intermediate_nodes = intermediate_nodes

        # Effective Lengths Different Properties
        clientObject.different_properties = different_properties

        # Effective Lengths Factors Definition Absolute
        clientObject.factors_definition_absolute = factors_definition_absolute

        # Effective Lengths User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Effective Lengths Nodal Supports
        clientObject.nodal_supports = model.clientModel.factory.create('ns0:array_of_timber_effective_lengths_nodal_supports')

        for i,j in enumerate(nodal_supports):
            mlvlp = model.clientModel.factory.create('ns0:timber_effective_lengths_nodal_supports_row')
            mlvlp.no = i+1
            mlvlp.row.support_type = nodal_supports[i][0].name
            mlvlp.row.support_in_z = nodal_supports[i][1]
            mlvlp.row.eccentricity_type = nodal_supports[i][2].name
            mlvlp.row.support_in_y_type = nodal_supports[i][3].name
            mlvlp.row.restraint_about_x_type = nodal_supports[i][4].name
            mlvlp.row.nodes = ConvertToDlString(nodal_supports[i][5])

            clientObject.nodal_supports.timber_effective_lengths_nodal_supports.append(mlvlp)

        # Effective Lengths Factors
        clientObject.factors = model.clientModel.factory.create('ns0:array_of_timber_effective_lengths_factors')

        for i,j in enumerate(factors):
            mlvlp_f = model.clientModel.factory.create('ns0:timber_effective_lengths_factors_row')
            mlvlp_f.no = i+1
            mlvlp_f.row.flexural_buckling_u = factors[i][0]
            mlvlp_f.row.flexural_buckling_v = factors[i][1]
            mlvlp_f.row.lateral_torsional_buckling = factors[i][2]

            clientObject.factors.timber_effective_lengths_factors.append(mlvlp_f)

        # Effective Lengths Fire Design
        clientObject.fire_design_different_buckling_factors = fire_design_different_buckling_factors

        # Effective Lengths Import From Stability Analysis Enabled
        clientObject.import_from_stability_analysis_enabled = import_from_stability_analysis_enabled

        # Effective Lengths Determination Type
        clientObject.determination_type = determination_type.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Timber Effective Lengths to client model
        model.clientModel.service.set_timber_effective_lengths(clientObject)
