from RFEM.initModel import *
from RFEM.enums import LineLoadType, LineLoadDistribution, LoadDirectionType
from enum import Enum

class LineLoad():
    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 lines_no: str = '1',
                 load_type = LineLoadType.LOAD_TYPE_FORCE,
                 load_distribution = LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM,
                 load_direction = LoadDirectionType.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter = None,
                 comment: str = ''):

        # Client model | Line Load
        clientObject = clientModel.factory.create('ns0:line_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Line No. (e.g. '5 6 7 12')
        clientObject.lines = lines_no

        # Line Load Type
        clientObject.load_type = load_type.name

        # Line Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Line Load Direction
        clientObject.load_direction = load_direction.name

        if load_type == LineLoadType.LOAD_TYPE_FORCE:
            # Load Type Force
            if   load_distribution == LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM:
                clientObject.magnitude = load_parameter
            elif load_distribution == LineLoadDistribution.LOAD_DISTRIBUTION_UNIFORM_TOTAL:
                clientObject.magnitude = load_parameter
            elif load_distribution == LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_1:
                clientObject.magnitude = load_parameter[0]
                clientObject.distance_a_absolute = load_parameter[1]
            elif load_distribution == LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_N:
                clientObject.magnitude = load_parameter[0]
                clientObject.count_n = int(load_parameter[1])
                clientObject.distance_a_absolute = load_parameter[2]
                clientObject.distance_b_absolute = load_parameter[3]
            elif load_distribution == LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2x2:
                clientObject.magnitude = load_parameter[0]
                clientObject.distance_a_absolute = load_parameter[1]
                clientObject.distance_b_absolute = load_parameter[2]
                clientObject.distance_c_absolute = load_parameter[3]
            elif load_distribution == LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_2:
                clientObject.magnitude_1 = load_parameter[0]
                clientObject.magnitude_2 = load_parameter[1]
                clientObject.distance_a_absolute = load_parameter[2]
                clientObject.distance_b_absolute = load_parameter[3]
            elif load_distribution == LineLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING:
                #pass
                try:
                    len(load_parameter[0])==3
                except:
                    print("WARNING: LineLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

                clientObject.varying_load_parameters = clientModel.factory.create('ns0:line_load').varying_load_parameters
                for i in range(len(load_parameter)):
                    llvlp = clientModel.factory.create('ns0:line_load_varying_load_parameters')
                    llvlp.no = i+1
                    llvlp.distance = load_parameter[i][0]
                    llvlp.delta_distance = load_parameter[i][1]
                    llvlp.magnitude = load_parameter[i][2]
                    llvlp.note = None
                    llvlp.magnitude_t_c = 0.0
                    llvlp.magnitude_delta_t = 0.0
                    llvlp.magnitude_t_t = 0.0
                    llvlp.magnitude_t_b = 0.0

                    clientObject.varying_load_parameters.line_load_varying_load_parameters.append(llvlp)
            elif load_distribution == LineLoadDistribution.LOAD_DISTRIBUTION_TRAPEZOIDAL:
                clientObject.magnitude_1 = load_parameter[0]
                clientObject.magnitude_2 = load_parameter[1]
                clientObject.distance_a_absolute = load_parameter[2]
                clientObject.distance_b_absolute = load_parameter[3]
            elif load_distribution == LineLoadDistribution.LOAD_DISTRIBUTION_TAPERED:
                clientObject.magnitude_1 = load_parameter[0]
                clientObject.magnitude_2 = load_parameter[1]
                clientObject.distance_a_absolute = load_parameter[2]
                clientObject.distance_b_absolute = load_parameter[3]
            elif load_distribution == LineLoadDistribution.LOAD_DISTRIBUTION_PARABOLIC:
                clientObject.magnitude_1 = load_parameter[0]
                clientObject.magnitude_2 = load_parameter[1]
                clientObject.magnitude_3 = load_parameter[2]
            elif load_distribution == LineLoadDistribution.LOAD_DISTRIBUTION_VARYING:
                try:
                    len(load_parameter[0])==3
                except:
                    print("WARNING: LineLoad no: %x, load case: %x - Wrong data input." % (no, load_case_no))

                clientObject.varying_load_parameters = clientModel.factory.create('ns0:line_load').varying_load_parameters
                for i in range(len(load_parameter)):
                    llvlp = clientModel.factory.create('ns0:line_load_varying_load_parameters')
                    llvlp.no = i+1
                    llvlp.distance = load_parameter[i][0]
                    llvlp.delta_distance = load_parameter[i][1]
                    llvlp.magnitude = load_parameter[i][2]
                    llvlp.note = None
                    llvlp.magnitude_t_c = 0.0
                    llvlp.magnitude_delta_t = 0.0
                    llvlp.magnitude_t_t = 0.0
                    llvlp.magnitude_t_b = 0.0
            
                    clientObject.varying_load_parameters.line_load_varying_load_parameters.append(llvlp)
            
        elif load_type == LineLoadType.LOAD_TYPE_LOAD_TYPE_MOMENT:
            # Load Type Moment
            pass

        elif load_type == LineLoadType.E_TYPE_MASS:
            # Load Type Mass
            clientObject.mass_x = load_parameter_1
            clientObject.mass_y = load_parameter_1
            clientObject.mass_z = load_parameter_1

        # Comment
        clientObject.comment = comment

        # Add Load Line Load to client model
        clientModel.service.set_line_load(load_case_no, clientObject)
