from os import name
from RFEM.initModel import *
from RFEM.enums import *
from enum import *

class ConcreteEffectiveLength():

    def __init__(self,
                no: int = 1, 
                name: str = "EL 1",
                members_no: str = "1",
                member_sets_no: str = "1",
                flexural_buckling_about_y = [True, ConcreteEffectiveLengthAxisY.STRUCTURE_TYPE_UNBRACED],
                flexural_buckling_about_z = [True, ConcreteEffectiveLengthsAxisZ.STRUCTURE_TYPE_UNBRACED],
                nodal_supports = [[0, EffectiveLengthSupportType.SUPPORT_TYPE_FIXED_ALL,
                    True, EffectiveLengthEccentricityType.eccentricity_type, 0, 0, 0, 0, 
                    SupportStatus.SUPPORT_STATUS_YES, RestraintTypeAboutX.SUPPORT_STATUS_NO, 
                    RestraintTypeAboutZ.SUPPORT_STATUS_NO, RestraintTypeWarping.SUPPORT_STATUS_NO, "2"], 
                    [0, EffectiveLengthSupportType.SUPPORT_TYPE_FIXED_ALL,
                    True, EffectiveLengthEccentricityType.eccentricity_type, 0, 0, 0, 0, 
                    SupportStatus.SUPPORT_STATUS_YES, RestraintTypeAboutX.SUPPORT_STATUS_NO, 
                    RestraintTypeAboutZ.SUPPORT_STATUS_NO, RestraintTypeWarping.SUPPORT_STATUS_NO, "2"]],
                factors = [[1, 1, 1]],
                comment: str = '', 
                params: dict = {}):
        
        # Client model | Concrete Durabilities
        clientObject = clientModel.factory.create('ns0:concrete_effective_lengths')

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

        if type(flexural_buckling_about_y[0]) == bool:
            pass
        else:
            raise Exception('WARNING: The type of the first parameter should be bool. Kindly check list inputs for completeness and correctness.')

        clientObject.flexural_buckling_about_z = flexural_buckling_about_z[0]
        clientObject.structure_type_about_axis_z = flexural_buckling_about_z[1]

        if type(flexural_buckling_about_z[0]) == bool:
            pass
        else:
            raise Exception('WARNING: The type of the first parameter should be bool. Kindly check list inputs for completeness and correctness.')

        # Factors
        clientObject.concrete_effective_lengths_factors = factors
        
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Global Parameter to client model          
        clientModel.service.set_concrete_effective_lengths(clientObject)





        
        

