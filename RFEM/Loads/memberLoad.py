from RFEM.initModel import *
from RFEM.enums import MemberLoadType, MemberLoadDistribution, LoadDirectionType
from enum import Enum

class MemberLoad():
    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 members_no: str = '1',
                 load_type = MemberLoadType.LOAD_TYPE_FORCE,
                 load_distribution = MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = LoadDirectionType.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter = None,
                 comment: str = '',
                 params: dict = {}):
        '''
        Params:
            LOAD_DISTRIBUTION_UNIFORM: load_parameter = magnitude
            LOAD_DISTRIBUTION_UNIFORM_TOTAL: load_parameter = magnitude
            LOAD_DISTRIBUTION_CONCENTRATED_1: load_parameter = [magnitude, distance_a_absolute]
            LOAD_DISTRIBUTION_CONCENTRATED_N: load_parameter = [magnitude, count_n, distance_a_absolute, distance_b_absolute]
            LOAD_DISTRIBUTION_CONCENTRATED_2x2: load_parameter = [magnitude, distance_a_absolute, distance_b_absolute, distance_c_absolute]
            LOAD_DISTRIBUTION_CONCENTRATED_2: load_parameter = [magnitude_1, magnitude_2, distance_a_absolute, distance_b_absolute]
            LOAD_DISTRIBUTION_CONCENTRATED_VARYING: load_parameter = [[distance, delta_distance, magnitude], ...]
            LOAD_DISTRIBUTION_TRAPEZOIDAL: load_parameter = [[magnitude_1, magnitude_2, distance_a_absolute, distance_b_absolute], ...]
            LOAD_DISTRIBUTION_TAPERED: load_parameter = [magnitude_1, magnitude_2, distance_a_absolute, distance_b_absolute]
            LOAD_DISTRIBUTION_PARABOLIC: load_parameter = [magnitude_1, magnitude_2, magnitude_3]
            LOAD_DISTRIBUTION_VARYING: load_parameter = [[distance, delta_distance, magnitude], ...]
            LOAD_DISTRIBUTION_VARYING_IN_Z: load_parameter = [[distance, delta_distance, magnitude], ...]
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
        clientObject.load_type = load_type.name

        # Member Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Member Load Direction
        clientObject.load_direction = load_direction.name

        if load_type == MemberLoadType.LOAD_TYPE_FORCE:
            # Load Type Force
            if   load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                clientObject.magnitude = load_parameter
            elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_UNIFORM_TOTAL:
                clientObject.magnitude = load_parameter
            elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1:
                clientObject.magnitude = load_parameter[0]
                clientObject.distance_a_absolute = load_parameter[1]
            elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N:
                clientObject.magnitude = load_parameter[0]
                clientObject.count_n = int(load_parameter[1])
                clientObject.distance_a_absolute = load_parameter[2]
                clientObject.distance_b_absolute = load_parameter[3]
            elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2:
                clientObject.magnitude = load_parameter[0]
                clientObject.distance_a_absolute = load_parameter[1]
                clientObject.distance_b_absolute = load_parameter[2]
                clientObject.distance_c_absolute = load_parameter[3]
            elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2:
                clientObject.magnitude_1 = load_parameter[0]
                clientObject.magnitude_2 = load_parameter[1]
                clientObject.distance_a_absolute = load_parameter[2]
                clientObject.distance_b_absolute = load_parameter[3]
            elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING:
                try:
                    len(load_parameter[0])==3
                except:
                    print("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

                clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_load').varying_load_parameters
                for i in range(len(load_parameter)):
                    mlvlp = clientModel.factory.create('ns0:member_load_varying_load_parameters')
                    mlvlp.no = i+1
                    mlvlp.distance = load_parameter[i][0]
                    mlvlp.delta_distance = load_parameter[i][1]
                    mlvlp.magnitude = load_parameter[i][2]
                    mlvlp.note = None
                    mlvlp.magnitude_t_c = 0.0
                    mlvlp.magnitude_delta_t = 0.0
                    mlvlp.magnitude_t_t = 0.0
                    mlvlp.magnitude_t_b = 0.0

                    clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)
            elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
                clientObject.magnitude_1 = load_parameter[0]
                clientObject.magnitude_2 = load_parameter[1]
                clientObject.distance_a_absolute = load_parameter[2]
                clientObject.distance_b_absolute = load_parameter[3]
            elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
                clientObject.magnitude_1 = load_parameter[0]
                clientObject.magnitude_2 = load_parameter[1]
                clientObject.distance_a_absolute = load_parameter[2]
                clientObject.distance_b_absolute = load_parameter[3]
            elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
                clientObject.magnitude_1 = load_parameter[0]
                clientObject.magnitude_2 = load_parameter[1]
                clientObject.magnitude_3 = load_parameter[2]
            elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING:
                try:
                    len(load_parameter[0])==3
                except:
                    print("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

                clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_load').varying_load_parameters
                for i in range(len(load_parameter)):
                    mlvlp = clientModel.factory.create('ns0:member_load_varying_load_parameters')
                    mlvlp.no = i+1
                    mlvlp.distance = load_parameter[i][0]
                    mlvlp.delta_distance = load_parameter[i][1]
                    mlvlp.magnitude = load_parameter[i][2]
                    mlvlp.note = None
                    mlvlp.magnitude_t_c = 0.0
                    mlvlp.magnitude_delta_t = 0.0
                    mlvlp.magnitude_t_t = 0.0
                    mlvlp.magnitude_t_b = 0.0

                    clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)
            elif load_distribution == MemberLoadDistribution.LOAD_DISTRIBUTION_VARYING_IN_Z:
                try:
                    len(load_parameter[0])==3
                except:
                    print("WARNING: MemberLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

                clientObject.varying_load_parameters = clientModel.factory.create('ns0:member_load').varying_load_parameters
                for i in range(len(load_parameter)):
                    mlvlp = clientModel.factory.create('ns0:member_load_varying_load_parameters')
                    mlvlp.no = i+1
                    mlvlp.distance = load_parameter[i][0]
                    mlvlp.delta_distance = load_parameter[i][1]
                    mlvlp.magnitude = load_parameter[i][2]
                    mlvlp.note = None
                    mlvlp.magnitude_t_c = 0.0
                    mlvlp.magnitude_delta_t = 0.0
                    mlvlp.magnitude_t_t = 0.0
                    mlvlp.magnitude_t_b = 0.0

                    clientObject.varying_load_parameters.member_load_varying_load_parameters.append(mlvlp)
        elif load_type == MemberLoadType.LOAD_TYPE_LOAD_TYPE_MOMENT:
            # Load Type Moment
            pass

        elif load_type == MemberLoadType.E_TYPE_MASS:
            # Load Type Mass
            clientObject.mass_x = load_parameter_1
            clientObject.mass_y = load_parameter_1
            clientObject.mass_z = load_parameter_1

        elif load_type == MemberLoadType.LOAD_TYPE_TEMPERATURE:
            # Load Type Temperature
            pass

        elif load_type == MemberLoadType.LOAD_TYPE_TEMPERATURE_CHANGE:
            # Load Type Temperature Change
            pass

        elif load_type == MemberLoadType.LOAD_TYPE_AXIAL_STRAIN:
            # Load Type Axial Strain
            pass

        elif load_type == MemberLoadType.LOAD_TYPE_AXIAL_DISPLACEMENT:
            # Load Type Axial Displacemenet
            pass

        elif load_type == MemberLoadType.LOAD_TYPE_PRECAMBER:
            # Load Type Precamber
            pass

        elif load_type == MemberLoadType.LOAD_TYPE_INITIAL_PRESTRESS:
            # Load Type Initial Prestress
            pass

        elif load_type == MemberLoadType.LOAD_TYPE_DISPLACEMENT:
            # Load Type Displacement
            pass

        elif load_type == MemberLoadType.LOAD_TYPE_ROTATION:
            # Load Type Rotation
            pass

        elif load_type == MemberLoadType.LOAD_TYPE_PIPE_CONTENT_FULL:
            # Load Type Pipe Content - Full
            pass

        elif load_type == MemberLoadType.LOAD_TYPE_PIPE_CONTENT_PARTIAL:
            # Load Type Pipe Content - Partial
            pass

        elif load_type == MemberLoadType.LOAD_TYPE_PIPE_INTERNAL_PRESSURE:
            # Load Type Pipe Internal Pressure
            pass

        elif load_type == MemberLoadType.LOAD_TYPE_ROTARY_MOTION:
            # Load Type Rotary Motation
            pass

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Load Member Load to client model
        clientModel.service.set_member_load(load_case_no, clientObject)
