# from RFEM.initModel import Model, clearAttributes, ConvertToDlString

# class Frame():
#     def __init__(self,
#                  number_of_frames: int = 1,
#                  span_l: int = 2,
#                  height_h: int = 1,
#                  column_cross_section: 1,
#                  column_member_type = MemberType.TYPE_BEAM,
#                  girder_cross_section: 2,
#                  girder_member_type = MemberType.TYPE_BEAM,
#                  support_type = NodalSupportType.HINGED,
#                  insertion_point_x: int = 3,
#                  insertion_point_y: int = 4,
#                  insertion_point_z: int = 3,
#                  comment: str = '',
#                  params: dict = None, model = Model):

#        '''
#        Args:
#            number_of_frames (int): Number of Frames
#            span_l (int): Span Length
#            height_h (int): Frame Height
#            column_cross_section (int): Tag of Column Section
#            column_member_type (enum): Column Member Type Enumeration
#            girder_cross_section (int): Tag of Girder Section
#            girder_member_type (enum): Girder Member Type Enumeration
#            support_type (enum): Column to Girder Connection Type Enumeration
#            insertion_point_x (int): Insertion Point x
#            insertion_point_y (int): Insertion Point y
#            insertion_point_z (int): Insertion Point z
#            comment (str, optional): Comment
#            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
#        '''

#         # Client model | Frame
#         clientObject = clientModel.factory.create('ns0:member')

#         # Clears object atributes | Sets all atributes to None
#         clearAttributes(clientObject)

#  -------------------------------------------------------------------------
#         # Number of frames: da soll man eine Funktion zu clientModel. herstellen... oder?

#         i = 1
#         while i <= n:
#          j = (i-1) * 5
#          Node(j+1, 0.0, -(i-1)*d, 0.0)
#          Node(j+2, 0.0, -(i-1)*d, -h)
#          Node(j+3, l/2, -(i-1)*d, -h)
#          Node(j+4, l, -(i-1)*d, -h)
#          Node(j+5, l, -(i-1)*d, 0.0)
#          i += 1

#        # Nodal Supports
#        i = 1
#        nodes_no = ""
#        while i <= n:
#         j = (i-1) * 5
#         nodes_no += str(j+1) + " "
#         nodes_no += str(j+5) + " "
#         i += 1
#         nodes_no = nodes_no.rstrip(nodes_no[-1])
#         NodalSupport(1, nodes_no, NodalSupportType.HINGED, "Hinged support")

#        #members: what's about the sections? maybe an input field where the user gives the materials
#        Material (1 , 'S235')
#        Material (2, 'C25/30')

#        Section (1, 'HEM 700',1)
#        Section (2, 'IPE 500',1)

#       #members x direction
#         i = 1
#         while i <= n:
#          j = (i-1) * 5
#          k = (i-1) * 4
#          Member(k+1, MemberType.TYPE_BEAM, j+1, j+2, 0.0,  1, 1)
#          Member(k+2, MemberType.TYPE_BEAM, j+2, j+3, 0.0,  2, 2)
#          Member(k+3, MemberType.TYPE_BEAM, j+3, j+4, 0.0,  2, 2)
#          Member(k+4, MemberType.TYPE_BEAM, j+4, j+5, 0.0,  1, 1)
#          i += 1
#         print(k+1,k+2,k+3,k+4)

#       #members y direction
#        i = 1
#        while i <= n-1:
#         j = (i-1) * 5
#         print(k+4+2*(i-1)+1, k+4+2*(i-1)+2)
#         Member(int(k+4+2*(i-1)+1), MemberType.TYPE_BEAM, j+2, j+7, 0.0, 2, 2)
#         Member(int(k+4+2*(i-1)+2), MemberType.TYPE_BEAM, j+4, j+9, 0.0, 2, 2)
#         i += 1

#     -------------------------------------------------------------------------

#       clientObject. = NodeType.TYPE_BETWEEN_TWO_NODES.name
#                     = column_cross_section

#          #column cross section
#            clientobject. =  columnn_cross_section.name

#          #column member type
#           clientObject.type = column_member_type.name

#         #girder cross section
#           clientobject. =  girder_cross_section.name

#         #girder member type
#          clientObject.type = girder_member_type.name

#        # Nodal Support

#           clientObject.       =    support_type.name

#        # Comment
#         clientObject.comment = comment

#         # Adding optional parameters via dictionary
#         for key in params:
#             clientObject[key] = params[key]

#         # Add Member to client model
#         clientModel.service.set_frame(clientObject)
