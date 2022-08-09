from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import *

class ConcreteEffectiveLength():
    def __init__(self,
                no: int = 1,
                name: str = "EL 1",
                members_no: str = "1",
                member_sets_no: str = "1",
                flexural_buckling_about_y: list = [True, ConcreteEffectiveLengthAxisY.STRUCTURE_TYPE_UNBRACED],
                flexural_buckling_about_z: list = [True, ConcreteEffectiveLengthsAxisZ.STRUCTURE_TYPE_UNBRACED],
                nodal_supports: list = [[EffectiveLengthSupportType.SUPPORT_TYPE_FIXED_ALL,
                    True, 0, EffectiveLengthEccentricityType.ECCENTRICITY_TYPE_NONE, 0, 0, 0, 0,
                    SupportStatus.SUPPORT_STATUS_YES, RestraintTypeAboutX.SUPPORT_STATUS_NO,
                    RestraintTypeAboutZ.SUPPORT_STATUS_NO, RestraintTypeWarping.SUPPORT_STATUS_NO, "1"],
                    [EffectiveLengthSupportType.SUPPORT_TYPE_FIXED_ALL,
                    True, 0, EffectiveLengthEccentricityType.ECCENTRICITY_TYPE_NONE, 0, 0, 0, 0,
                    SupportStatus.SUPPORT_STATUS_YES, RestraintTypeAboutX.SUPPORT_STATUS_NO,
                    RestraintTypeAboutZ.SUPPORT_STATUS_NO, RestraintTypeWarping.SUPPORT_STATUS_NO, "2"]],
                factors: list = [[1, 1]],
                comment: str = '',
                params: dict = None,
                model = Model):
        """
        Args:
            no (int): Concrete Effective Length Tag
            name (str): User Defined Name
            members_no (str): Assigned Members
            member_sets_no (str): Assigned Member Sets
            flexural_buckling_about_y (list): Flexural Buckling About Y Option
            flexural_buckling_about_z (list): Flexural Buckling About Z Option
            nodal_supports (list of lists): Nodal Support Table
                nodal_supports = [[support_type, support_in_z, support_spring_in_y, eccentricity_type,
                                   eccentricity_ez, restraint_spring_about_x,
                                   restraint_spring_about_z, restraint_spring_warping, support_in_y_type,
                                   restraint_about_x_type, restraint_about_z_type, restraint_warping_type, nodes], ...]
            factors (list of lists): Factors Table
                factors = [[flexural_buckling_y, flexural_buckling_z]]
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client model | Concrete Durabilities
        clientObject = model.clientModel.factory.create('ns0:concrete_effective_lengths')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Concrete Durability No.
        clientObject.no = no

        # User Defined Name
        clientObject.user_defined_name_enabled = True
        clientObject.name = name

        # Assigned Members
        clientObject.members = ConvertToDlString(members_no)

        # Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets_no)

        # Flexural Buckling
        clientObject.flexural_buckling_about_y = flexural_buckling_about_y[0]
        clientObject.structure_type_about_axis_y = flexural_buckling_about_y[1]

        if not isinstance(flexural_buckling_about_y[0], bool):
            raise Exception('WARNING: The type of the first parameter should be bool. Kindly check list inputs for completeness and correctness.')

        clientObject.flexural_buckling_about_y = flexural_buckling_about_y[0]
        clientObject.structure_type_about_axis_y = flexural_buckling_about_y[1].name

        if not isinstance(flexural_buckling_about_z[0], bool):
            raise Exception('WARNING: The type of the first parameter should be bool. Kindly check list inputs for completeness and correctness.')

        clientObject.flexural_buckling_about_z = flexural_buckling_about_z[0]
        clientObject.structure_type_about_axis_z = flexural_buckling_about_z[1].name

        # Factors
        clientObject.factors = model.clientModel.factory.create('ns0:concrete_effective_lengths.factors')
        for i in range(len(factors)):
            mlvlp = model.clientModel.factory.create('ns0:concrete_effective_lengths_factors')
            mlvlp.no = i+1
            mlvlp.flexural_buckling_y = factors[i][0]
            mlvlp.flexural_buckling_z = factors[i][1]
            clientObject.factors.concrete_effective_lengths_factors.append(mlvlp)

        # Nodal Supports
        clientObject.nodal_supports = model.clientModel.factory.create('ns0:concrete_effective_lengths.nodal_supports')
        for i in range(len(nodal_supports)):
            mlvlp = model.clientModel.factory.create('ns0:concrete_effective_lengths_nodal_supports')
            mlvlp.no = i+1
            mlvlp.support_type = nodal_supports[i][0].name
            mlvlp.support_in_z = nodal_supports[i][1]
            mlvlp.support_spring_in_y = nodal_supports[i][2]
            mlvlp.eccentricity_type = nodal_supports[i][3].name
            mlvlp.eccentricity_ez = nodal_supports[i][4]
            mlvlp.restraint_spring_about_x = nodal_supports[i][5]
            mlvlp.restraint_spring_about_z = nodal_supports[i][6]
            mlvlp.restraint_warping_type = nodal_supports[i][7]
            mlvlp.support_in_y_type = nodal_supports[i][8].name
            mlvlp.restraint_about_x_type = nodal_supports[i][9].name
            mlvlp.restraint_about_z_type = nodal_supports[i][10].name
            mlvlp.restraint_warping_type = nodal_supports[i][11].name
            mlvlp.nodes = nodal_supports[i][12]
            clientObject.nodal_supports.concrete_effective_lengths_nodal_supports.append(mlvlp)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Global Parameter to client model
        model.clientModel.service.set_concrete_effective_lengths(clientObject)








