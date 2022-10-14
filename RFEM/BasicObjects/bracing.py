# from RFEM.initModel import Model, clearAttributes, ConvertToDlString
# from RFEM.enums import BracingType

# class Bracing():
#  def __init__(self,
#                  no: int = 1,
#                  member_type = BracingType.TYPE_HORIZONTAL,
#                  start_node_no: int = 1,
#                  end_node_no: int = 2,
#                  rotation_angle: float = 0.0,
#                  start_section_no: int = 1,
#                  end_section_no: int = 1,
#                  comment: str = '',
#                  params: dict = None, model = Model):

#        '''
#        Args:
#            no (int): Bracing Tag
#            member_type (enum): Bracing Type Enumeration
#            start_node_no (int): Start Node
#            end_node_no (int): End Node
#            rotation_angle (float): Rotation Angle
#            start_section_no (int): Tag of Start Section
#            end_section_no (int): End of End Section
#            comment (str, optional): Comment
#            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
#        '''

#         # Client model | Bracing
#         clientObject = model.clientModel.factory.create('ns0:bracing')

#         # Clears object atributes | Sets all atributes to None
#         clearAttributes(clientObject)

#         # Bracing No.
#         clientObject.no = no

#         # Bracing Type
#         clientObject.type = bracing_type.name

#         # Start Node No.
#         clientObject.node_start = start_node_no

#         # End Node No.
#         clientObject.node_end = end_node_no

#         # Bracing Rotation Angle beta
#         clientObject.rotation_angle = rotation_angle

#         # Start Section No.
#         clientObject.section_start = start_section_no

#         # End Section No.
#         clientObject.section_end = end_section_no

#         # Start Bracing Hinge No.
#         clientObject.bracing_hinge_start = start_bracing_hinge_no

#         # End Bracing Hinge No.
#         clientObject.bracing_hinge_end = end_bracing_hinge_no

#         # Comment
#         clientObject.comment = comment

#         # Adding optional parameters via dictionary
#         for key in params:
#             clientObject[key] = params[key]

#         # Add Member to client model
#         model.clientModel.service.set_bracing(clientObject)

#       def Horizontal(self,
#             no: int = 1,
#             bracing_type = BracingType.TYPE_HORIZONTAL,
#             start_node_no: int = 1,
#             end_node_no: int = 2,
#             rotation_angle: float = 0.0,
#             start_section_no: int = 1,
#             end_section_no: int = 1,
#             start_bracing_hinge_no: int = 0,
#             end_bracing_hinge_no: int = 0,
#             comment: str = '',
#             params: dict = None, model = Model):

#             '''
#            Args:
#                no (int): Bracing Tag
#                bracing_type (enum): Bracing Type Enumeration
#                start_node_no (int): Start Node
#                end_node_no (int): End Node
#                rotation_angle (float): Rotation Angle
#                start_section_no (int): Tag of Start Section
#                end_section_no (int): End of End Section
#                start_bracing_hinge_no (int): Hinge at Bracing Start
#                end_bracing_hinge_no (int): Hinge at Bracing End
#                comment (str, optional): Comment
#                params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
#             '''

#         # Client model | Bracing
#         clientObject = model.clientModel.factory.create('ns0:bracing')

#         # Clears object atributes | Sets all atributes to None
#         clearAttributes(clientObject)

#         # Bracing No.
#         clientObject.no = no

#         # Bracing Type
#         clientObject.type = bracing_type.name

#         # Start Node No.
#         clientObject.node_start = start_node_no

#         # End Node No.
#         clientObject.node_end = end_node_no

#         # Bracing Rotation Angle beta
#         clientObject.rotation_angle = rotation_angle

#         # Start Section No.
#         clientObject.section_start = start_section_no

#         # End Section No.
#         clientObject.section_end = end_section_no

#         # Start Bracing Hinge No.
#         clientObject.bracing_hinge_start = start_bracing_hinge_no

#         # End Bracing Hinge No.
#         clientObject.bracing_hinge_end = end_bracing_hinge_no

#         # Comment
#         clientObject.comment = comment

#         # Adding optional parameters via dictionary
#         for key in params:
#             clientObject[key] = params[key]

#         # Add Bracing to client model
#         model.clientModel.service.set_bracing(clientObject)

#         def Vertical(self,
#             no: int = 1,
#             bracing_type = BracingType.TYPE_VERTICAL,
#             start_node_no: int = 1,
#             end_node_no: int = 2,
#             rotation_angle: float = 0.0,
#             start_section_no: int = 1,
#             end_section_no: int = 1,
#             start_bracing_hinge_no: int = 0,
#             end_bracing_hinge_no: int = 0,
#             comment: str = '',
#             params: dict = None, model = Model):

#            '''
#            Args:
#                no (int): Bracing Tag
#                bracing_type (enum): Bracing Type Enumeration
#                start_node_no (int): Start Node
#                end_node_no (int): End Node
#                rotation_angle (float): Rotation Angle
#                start_section_no (int): Tag of Start Section
#                end_section_no (int): End of End Section
#                start_bracing_hinge_no (int): Hinge at Bracing Start
#                end_bracing_hinge_no (int): Hinge at Bracing End
#                comment (str, optional): Comment
#                params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
#            '''

#         # Client model | Bracing
#         clientObject = model.clientModel.factory.create('ns0:bracing')

#         # Clears object atributes | Sets all atributes to None
#         clearAttributes(clientObject)

#         # Bracing No.
#         clientObject.no = no

#         # Bracing Type
#         clientObject.type = bracing_type.name

#         # Start Node No.
#         clientObject.node_start = start_node_no

#         # End Node No.
#         clientObject.node_end = end_node_no

#         # Bracing Rotation Angle beta
#         clientObject.rotation_angle = rotation_angle

#         # Start Section No.
#         clientObject.section_start = start_section_no

#         # End Section No.
#         clientObject.section_end = end_section_no

#         # Start Bracing Hinge No.
#         clientObject.bracing_hinge_start = start_bracing_hinge_no

#         # End Bracing Hinge No.
#         clientObject.bracing_hinge_end = end_bracing_hinge_no

#         # Comment
#         clientObject.comment = comment

#         # Adding optional parameters via dictionary
#         for key in params:
#             clientObject[key] = params[key]

#         # Add Bracing to client model
#         model.clientModel.service.set_bracing(clientObject)

