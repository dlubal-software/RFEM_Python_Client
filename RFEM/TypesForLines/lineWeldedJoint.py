from RFEM.initModel import Model, clearAtributes, ConvertStrToListOfInt
from RFEM.enums import LineWeldedJointType, WeldType, WeldLongitudalArrangement

class LineWeldedJoint():
    def __init__(self,
                 no: int = 1,
                 lines: str = '5',
                 surfaces: str = '1 2',
                 joint_type = LineWeldedJointType.BUTT_JOINT,
                 weld_type = WeldType.WELD_SINGLE_V,
                 weld_size_a1: int = 0.005,
                 longitudinal_arrangement = WeldLongitudalArrangement.CONTINUOUS,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        # Client model | Line Welded Joint
        clientObject = model.clientModel.factory.create('ns0:line_welded_joint')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line Welded Joint No.
        clientObject.no = no

        # Line Welded Joint Type
        clientObject.joint_type = joint_type.name

        # Weld Type
        clientObject.weld_type = weld_type.name

        # Weld Longitudal Arrangement
        clientObject.longitudinal_arrangement = longitudinal_arrangement.name

        # Weld Size a1
        clientObject.weld_size_a1 = weld_size_a1

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Line welded joint to client model
        model.clientModel.service.set_line_welded_joint(clientObject)

        iLines = ConvertStrToListOfInt(lines)
        iSurfaces = ConvertStrToListOfInt(surfaces)

        for i in iLines:
            line = model.clientModel.service.get_line(i)
            line.has_line_welds = True
            clientWeld = model.clientModel.factory.create('ns0:line_line_weld_assignment_row')
            clientWeld.no = i
            clientWeld.row.weld = no
            clientWeld.row.surface1 = iSurfaces[0]
            clientWeld.row.surface2 = iSurfaces[1]
            if len(iSurfaces) == 3:
                clientWeld.surface3 = iSurfaces[2]
            line.line_weld_assignment = model.clientModel.factory.create('ns0:array_of_line_line_weld_assignment')
            line.line_weld_assignment.line_line_weld_assignment.append(clientWeld)
            model.clientModel.service.set_line(line)
