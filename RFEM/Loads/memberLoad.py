from RFEM.initModel import *
from RFEM.enums import *
from enum import Enum

class MemberLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_direction = LoadDirectionType.LOAD_DIRECTION_LOCAL_Z,
                 magnitude: float = 0,
                 comment: str = '',
                 params: dict = {}):
        '''
        Assigns member load without any further options. 
        Load type is Force by default.
        Load distrubition is Uniform by default.
        '''

        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        # Member Load Distribution
        load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        clientObject.magnitude = magnitude

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_load(load_case_no, clientObject)


    def Force(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = LoadDirectionType.LOAD_DIRECTION_LOCAL_Z,
                 magnitude : float = 0,
                 force_eccentricity : bool = False,
                 list_reference : bool = False,
                 load_parameter = [],
                 comment: str = '',
                 params: dict = {}):
        '''
        Assigns member load type Force.

        '''

        # Client model | Member Load
        clientObject = clientModel.factory.create('ns0:member_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Member Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Members No. (e.g. '5 6 7 12')
        clientObject.members = ConvertToDlString(members_no)

        # Member Load Type
        load_type = MemberLoadType.LOAD_TYPE_FORCE
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        #Load Magnitude
        clientObject.magnitude = magnitude

        #Reference to List of Members
        clientObject.reference_to_list_of_members = list_reference

        #Force Eccentiricity
        clientObject.has_force_eccentricity = force_eccentricity

        if force_eccentricity == True:

            if load_parameter[0] == False:

                clientObject.is_eccentricity_at_end_different_from_start = False
                clientObject.eccentricity_horizontal_alignment = load_parameter[1]
                clientObject.eccentricity_vertical_alignment = load_parameter[2]
                clientObject.eccentricity_section_middle = load_parameter[3]
                clientObject.eccentricity_y_at_end = load_parameter[4]
                clientObject.eccentricity_y_at_start = load_parameter[4]
                clientObject.eccentricity_z_at_end = load_parameter[5]
                clientObject.eccentricity_z_at_start = load_parameter[5]

            elif load_parameter[0] == True:

                clientObject.is_eccentricity_at_end_different_from_start = True
                clientObject.eccentricity_horizontal_alignment = load_parameter[1]
                clientObject.eccentricity_vertical_alignment = load_parameter[2]
                clientObject.eccentricity_section_middle = load_parameter[3]
                clientObject.eccentricity_y_at_end = load_parameter[4]
                clientObject.eccentricity_y_at_start = load_parameter[5]
                clientObject.eccentricity_z_at_end = load_parameter[6]
                clientObject.eccentricity_z_at_start = load_parameter[7]


        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_load(load_case_no, clientObject)


