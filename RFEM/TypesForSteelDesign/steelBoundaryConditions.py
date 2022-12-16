from RFEM.initModel import Model, clearAttributes, ConvertToDlString, deleteEmptyAttributes
from RFEM.enums import *

class SteelBoundaryConditions():
    def __init__(self,
                no: int = 1,
                name: str = '',
                members: str = '',
                member_sets : str = '',
                intermediate_nodes : bool = False,
                different_properties_supports: bool = True,
                different_properties_hinges: bool = True,
                nodal_supports: list = [
                    [None, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, ""],
                    [None, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, ""]
                                        ],
                member_hinges: list = [
                    ["Start", False, False, False, False, False, False, False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ""],
                    ["End", False, False, False, False, False, False, False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ""]
                                      ],
                comment: str = '',
                params: dict = None,
                model = Model):

        """
        Args:
            no (int): Boundary Conditions Tag
            name (str): User Defined Boundary Conditions Name
            members (str): Assigned Members
            member_sets (str): Assigned Member Sets
            intermediate_nodes (bool): Enable/Disable Intermediate Nodes Option
            different_properties_supports (bool): Different Properties Option for Supports
            different_properties_hinges (bool): Different Properties Option for Hinges
            nodal_supports (list of lists): Nodal Supports Table Definition
                nodal_supports[i][0] (int)= Node Sequence No.
                nodal_supports[i][1] (enum)= Support Type Enumeration
                nodal_supports[i][2] (bool)= Support in X Direction Option
                nodal_supports[i][3] (bool)= Support in Y Direction Option
                nodal_supports[i][4] (bool)= Support in Z Direction Option
                nodal_supports[i][5] (bool)= Restraint About X Option
                nodal_supports[i][6] (bool)= Restraint About Y Option
                nodal_supports[i][7] (bool)= Restraint About Z Option
                nodal_supports[i][8] (bool)= Restraint Warping Option
                nodal_supports[i][9] (float)= Rotation Magnitude
                nodal_supports[i][10] (float)= Rotation About X Magnitude
                nodal_supports[i][11] (float)= Rotation About Y Magnitude
                nodal_supports[i][12] (float)= Rotation About Z Magnitude
                nodal_supports[i][13] (float)= Support Spring X
                nodal_supports[i][14] (float)= Support Spring Y
                nodal_supports[i][15] (float)= Support Spring Z
                nodal_supports[i][16] (float)= Restraint Spring About X Magnitude
                nodal_supports[i][17] (float)= Restraint Spring About Y Magnitude
                nodal_supports[i][18] (float)= Restraint Spring About Z Magnitude
                nodal_supports[i][19] (float)= Restraint Spring Warping Magnitude
                nodal_supports[i][20] (enum)= Eccentricity Type in Z Enumeration
                nodal_supports[i][21] (float)= Eccentricity in X Magnitude
                nodal_supports[i][22] (float)= Eccentricity in Y Magnitude
                nodal_supports[i][23] (float)= Eccentricity in Z Magnitude
                nodal_supports[i][24] (str)= Assigned Nodes
            member_hinges (list of lists): Member Hinges Table Definition
                member_hinges[i][0] = Node Sequence No.
                member_hinges[i][1] = Release in X Option
                member_hinges[i][2] = Release in Y Option
                member_hinges[i][3] = Release in Z Option
                member_hinges[i][4] = Release About X Option
                member_hinges[i][5] = Release About Y Option
                member_hinges[i][6] = Release About Z Option
                member_hinges[i][7] = Release Warping Option
                member_hinges[i][8] = Release Spring in X Magnitude
                member_hinges[i][9] = Release Spring in Y Magnitude
                member_hinges[i][10] = Release Spring in Z Magnitude
                member_hinges[i][11] = Release Spring About X Magnitude
                member_hinges[i][12] = Release Spring About Y Magnitude
                member_hinges[i][13] = Release Spring About Z Magnitude
                member_hinges[i][14] = Release Spring Warping Magnitude
                member_hinges[i][15] = Assigned Nodes
            comment (str, optional): Comment
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RFEM Class, optional): Model to be edited
        """

        # Client Model | Types For Steel Design Boundary Conditions
        clientObject = model.clientModel.factory.create('ns0:steel_boundary_conditions')

        # Clears object atributes | Sets all atributes to None
        clearAttributes(clientObject)

        # Boundary Conditions No.
        clientObject.no = no

        # Boundary Conditions User Defined Name
        if name:
            clientObject.user_defined_name_enabled = True
            clientObject.name = name

        # Intermediate Nodes Option
        clientObject.intermediate_nodes = intermediate_nodes

        # Boundary Conditions Assigned Members
        clientObject.members = ConvertToDlString(members)

        # Boundary Conditions Assigned Member Sets
        clientObject.member_sets = ConvertToDlString(member_sets)

        # Boundary Conditions Nodal Supports
        clientObject.nodal_supports = model.clientModel.factory.create('ns0:steel_boundary_conditions.nodal_supports')

        for i,j in enumerate(nodal_supports):
            mlvlp = model.clientModel.factory.create('ns0:steel_boundary_conditions_nodal_supports_row')
            mlvlp.no = i+1
            mlvlp.row.node_seq_no = nodal_supports[i][0]
            mlvlp.row.support_type = nodal_supports[i][1].name
            mlvlp.row.support_in_x = nodal_supports[i][2]
            mlvlp.row.support_in_y = nodal_supports[i][3]
            mlvlp.row.support_in_z = nodal_supports[i][4]
            mlvlp.row.restraint_about_x = nodal_supports[i][5]
            mlvlp.row.restraint_about_y = nodal_supports[i][6]
            mlvlp.row.restraint_about_z = nodal_supports[i][7]
            mlvlp.row.restraint_warping = nodal_supports[i][8]
            mlvlp.row.rotation = nodal_supports[i][9]
            mlvlp.row.rotation_about_x = nodal_supports[i][10]
            mlvlp.row.rotation_about_y = nodal_supports[i][11]
            mlvlp.row.rotation_about_z = nodal_supports[i][12]
            mlvlp.row.support_spring_in_x = nodal_supports[i][13]
            mlvlp.row.support_spring_in_y = nodal_supports[i][14]
            mlvlp.row.support_spring_in_z = nodal_supports[i][15]
            mlvlp.row.restraint_spring_about_x = nodal_supports[i][16]
            mlvlp.row.restraint_spring_about_y = nodal_supports[i][17]
            mlvlp.row.restraint_spring_about_z = nodal_supports[i][18]
            mlvlp.row.restraint_spring_warping = nodal_supports[i][19]
            mlvlp.row.eccentricity_type_z_type = nodal_supports[i][20].name
            mlvlp.row.eccentricity_x = nodal_supports[i][21]
            mlvlp.row.eccentricity_y = nodal_supports[i][22]
            mlvlp.row.eccentricity_z = nodal_supports[i][23]
            mlvlp.row.nodes = nodal_supports[i][24]

            clientObject.nodal_supports.steel_boundary_conditions_nodal_supports.append(mlvlp)

        # Boundary Conditions Member Hinges
        clientObject.member_hinges = model.clientModel.factory.create('ns0:steel_boundary_conditions.member_hinges')

        for i,j in enumerate(member_hinges):
            mlvlp = model.clientModel.factory.create('ns0:steel_boundary_conditions_member_hinges_row')
            mlvlp.no = i+1
            mlvlp.row.node_seq_no = member_hinges[i][0]
            mlvlp.row.release_in_x = member_hinges[i][1]
            mlvlp.row.release_in_y = member_hinges[i][2]
            mlvlp.row.release_in_z = member_hinges[i][3]
            mlvlp.row.release_about_x = member_hinges[i][4]
            mlvlp.row.release_about_y = member_hinges[i][5]
            mlvlp.row.release_about_z = member_hinges[i][6]
            mlvlp.row.release_warping = member_hinges[i][7]
            mlvlp.row.release_spring_in_x = member_hinges[i][8]
            mlvlp.row.release_spring_in_y = member_hinges[i][9]
            mlvlp.row.release_spring_in_z = member_hinges[i][10]
            mlvlp.row.release_spring_about_x = member_hinges[i][11]
            mlvlp.row.release_spring_about_y = member_hinges[i][12]
            mlvlp.row.release_spring_about_z = member_hinges[i][13]
            mlvlp.row.release_spring_warping = member_hinges[i][14]
            mlvlp.row.nodes = member_hinges[i][15]

            clientObject.member_hinges.steel_boundary_conditions_member_hinges.append(mlvlp)

        # Boundary Conditions Different Properties Supports
        clientObject.different_properties_supports = different_properties_supports

        # Boundary Conditions Different Properties Hinges
        clientObject.different_properties_hinges = different_properties_hinges

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Delete None attributes for improved performance
        deleteEmptyAttributes(clientObject)

        # Add Steel Boundary Conditions to client model
        model.clientModel.service.set_steel_boundary_conditions(clientObject)
