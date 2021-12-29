import sys
import numpy as np
sys.path.append(r'.')
from RFEM.enums import *
from RFEM.window import *
from RFEM.dataTypes import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import *
from RFEM.BasicObjects.section import *
from RFEM.BasicObjects.thickness import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.line import *
from RFEM.BasicObjects.member import *
from RFEM.BasicObjects.surface import *
from RFEM.BasicObjects.solid import *
from RFEM.BasicObjects.opening import *
from RFEM.BasicObjects.lineSet import *
from RFEM.BasicObjects.memberSet import *
from RFEM.BasicObjects.surfaceSet import *
from RFEM.BasicObjects.solidSet import *
from RFEM.TypesForNodes.nodalSupport import *
from RFEM.TypesForMembers.memberHinge import *
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import *
from RFEM.LoadCasesAndCombinations.loadCase import *
from RFEM.Loads.nodalLoad import *
from RFEM.Loads.memberLoad import *
from RFEM.Loads.surfaceLoad import *

def truss_1(diagonal_type,
            number_of_bays,
            total_length,
            total_height,
            upper_chord_material,
            upper_chord_section,
            lower_chord_material,
            lower_chord_section,
            diagonal_material,
            diagonal_section,
            vertical_material,
            vertical_section):

    if __name__ == '__main__':

        Model(False)
        Model.clientModel.service.reset()
        Model.clientModel.service.begin_modification('new')

        # Create Materials
        Material(1, upper_chord_material)
        Material(2, lower_chord_material)
        Material(3, diagonal_material)
        Material(4, vertical_material)

        # Create Sections
        Section(1, upper_chord_section, 1)
        Section(2, lower_chord_section, 2)
        Section(3, diagonal_section, 3)
        Section(4, vertical_section, 4)

        # Create Nodes
        x_nodes = np.repeat(np.arange(0, total_length + total_length/number_of_bays, total_length/number_of_bays), 2)
        z_nodes = (0, (-total_height))*int((len(x_nodes)/2))
        tag_nodes = np.arange(1, len(x_nodes)+1, 1)

        for tag,x,z in zip(tag_nodes, x_nodes, z_nodes):
            Node(tag, x, 0, z)

        # Create Lower Chord
        Member(1, 1, tag_nodes[-2], 0, 2, 2)

        # Create Upper Chord
        Member(2, 2, tag_nodes[-1], 0, 1, 1)

        # Create Verticals
        i = 1
        j = 1
        while j<len(tag_nodes) and i<len(tag_nodes):
            Member.Truss(0, j+2, i, i+1, section_no=4)
            i += 2
            j += 1

        # Create Diagonals
        if diagonal_type == 1:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1):
                Member.Truss(0, j, i, i+3, section_no=3)
                i +=2
                j +=1
        elif diagonal_type == 2:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 2):
                Member.Truss(0, j, i+1, i+2, section_no=3)
                i +=2
                j +=1
        elif diagonal_type == 3:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            k = 1

            while i < len(tag_nodes) -1 and j < diagonal_tag[-1] +2  and k < len(tag_nodes) :
                Member.Truss(0, j, i, i+3, section_no=3)
                j += 1
                Member.Truss(0, j, k+3, k+4, section_no=3)
                i += 4
                k += 4
                j += 1
        elif diagonal_type == 4:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            k = 1

            while i < len(tag_nodes) -1 and j < diagonal_tag[-1] +1  and k < len(tag_nodes) :
                Member.Truss(0, j, i+2, i+5, section_no=3)
                j += 1
                Member.Truss(0, j, k+1, k+2, section_no=3)
                i += 4
                k += 4
                j += 1
        elif diagonal_type == 5:
            if (number_of_bays % 2) == 0:
                diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                i = 1
                j = int(diagonal_tag[0])
                while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1] +1:
                    Member.Truss(0, j, i+1, i+2, section_no=3)
                    i += 2
                    j += 1
                i = int(len(tag_nodes)/2)
                j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                while i < tag_nodes[-1] and j <diagonal_tag[-1] +1:
                    Member.Truss(0, j, i, i+3, section_no=3)
                    i += 2
                    j += 1
            else:
                print("WARNING: Please enter an even number of spans for a symmetrical net.")

        elif diagonal_type == 6:
            if (number_of_bays % 2) == 0:
                diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                i = 1
                j = int(diagonal_tag[0])
                while i < ((tag_nodes[-1]/2) + 1) and j <diagonal_tag[-1] +1:
                    Member.Truss(0, j, i, i+3, section_no=3)
                    i += 2
                    j += 1
                i = int(len(tag_nodes)/2) + 1
                j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                while i < tag_nodes[-1] and j <diagonal_tag[-1] +1:
                    Member.Truss(0, j, i, i+1, section_no=3)
                    i += 2
                    j += 1
            else:
                print("WARNING: Please enter an even number of spans for a symmetrical net.")

        elif diagonal_type == 7:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1)*2:
                Member.Truss(0, j, i, i+3, section_no=3)
                j +=1
                Member.Truss(0, j, i+1, i+2, section_no=3)
                i +=2
                j +=1

        elif diagonal_type == 8:
            pass

        Model.clientModel.service.finish_modification()

def truss_2(diagonal_type,
            number_of_bays,
            total_length,
            total_height,
            first_span,
            upper_chord_material,
            upper_chord_section,
            lower_chord_material,
            lower_chord_section,
            diagonal_material,
            diagonal_section,
            vertical_material,
            vertical_section):

    if __name__ == '__main__':

        Model(False)
        Model.clientModel.service.reset()
        Model.clientModel.service.begin_modification('new')

        # Create Materials
        Material(1, upper_chord_material)
        Material(2, lower_chord_material)
        Material(3, diagonal_material)
        Material(4, vertical_material)

        # Create Sections
        Section(1, upper_chord_section, 1)
        Section(2, lower_chord_section, 2)
        Section(3, diagonal_section, 3)
        Section(4, vertical_section, 4)

        # Create Nodes
        x_nodes = np.repeat(np.arange(0, total_length + total_length/number_of_bays, total_length/number_of_bays), 2)
        z_nodes = (0, (-total_height))*int((len(x_nodes)/2))
        tag_nodes = np.arange(1, len(x_nodes)+1, 1)

        for tag,x,z in zip(tag_nodes, x_nodes, z_nodes):
            Node(tag, x, 0, z)

        # Create Lower Chord
        Member(1, 1, tag_nodes[-2], 0, 2, 2)

        # Create Upper Chord
        Member(2, 2, tag_nodes[-1], 0, 1, 1)

        # Create Verticals
        i = 1
        j = 1
        while j<len(tag_nodes) and i<len(tag_nodes):
            Member.Truss(0, j+2, i, i+1, section_no=4)
            i += 2
            j += 1

        # Create Diagonals
        if diagonal_type == 1:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1):
                Member.Truss(0, j, i, i+3, section_no=3)
                i +=2
                j +=1
            #Add first span
            Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
            Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)

            Member((int(diagonal_tag[-1])+1), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
            Member((int(diagonal_tag[-1])+2), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)

            Member.Truss(0, (int(diagonal_tag[-1])+3), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
            Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)

        elif diagonal_type == 2:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 2):
                Member.Truss(0, j, i+1, i+2, section_no=3)
                i +=2
                j +=1

            #Add first span
            Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
            Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)

            Member((int(diagonal_tag[-1])+1), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
            Member((int(diagonal_tag[-1])+2), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)

            Member.Truss(0, (int(diagonal_tag[-1])+3), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
            Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)

        elif diagonal_type == 3:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            k = 1

            while i < len(tag_nodes) -1 and j < diagonal_tag[-1] +2  and k < len(tag_nodes) :
                Member.Truss(0, j, i, i+3, section_no=3)
                j += 1
                Member.Truss(0, j, k+3, k+4, section_no=3)
                i += 4
                k += 4
                j += 1

            #Add first span
            Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
            Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)

            Member((int(diagonal_tag[-1])+1), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
            Member((int(diagonal_tag[-1])+2), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)

            Member.Truss(0, (int(diagonal_tag[-1])+3), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
            Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)

        elif diagonal_type == 4:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            k = 1

            while i < len(tag_nodes) -1 and j < diagonal_tag[-1]+1  and k < len(tag_nodes) :
                Member.Truss(0, j, i+2, i+5, section_no=3)
                j += 1
                Member.Truss(0, j, k+1, k+2, section_no=3)
                i += 4
                k += 4
                j += 1

            #Add first span
            Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
            Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)

            Member((int(diagonal_tag[-1])+2), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
            Member((int(diagonal_tag[-1])+3), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)

            Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
            Member.Truss(0, (int(diagonal_tag[-1])+5), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)

        elif diagonal_type == 5:
            if (number_of_bays % 2) == 0:
                diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                i = 1
                j = int(diagonal_tag[0])
                while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1] +1:
                    Member.Truss(0, j, i+1, i+2, section_no=3)
                    i += 2
                    j += 1
                i = int(len(tag_nodes)/2)
                j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                while i < tag_nodes[-1] and j <diagonal_tag[-1] +1:
                    Member.Truss(0, j, i, i+3, section_no=3)
                    i += 2
                    j += 1
                #Add first span
                Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
                Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)

                Member((int(diagonal_tag[-1])+2), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
                Member((int(diagonal_tag[-1])+3), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)

                Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
                Member.Truss(0, (int(diagonal_tag[-1])+5), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)

            else:
                print("WARNING: Please enter an even number of spans for a symmetrical net.")

        elif diagonal_type == 6:
            if (number_of_bays % 2) == 0:
                diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                i = 1
                j = int(diagonal_tag[0])
                while i < ((tag_nodes[-1]/2) + 1) and j <diagonal_tag[-1] +1:
                    Member.Truss(0, j, i, i+3, section_no=3)
                    i += 2
                    j += 1
                i = int(len(tag_nodes)/2) + 1
                j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                while i < tag_nodes[-1] and j <diagonal_tag[-1] +1:
                    Member.Truss(0, j, MemberType.TYPE_TRUSS, i, i+1, section_no=3)
                    i += 2
                    j += 1
                #Add first span
                Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
                Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)

                Member((int(diagonal_tag[-1])+2), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
                Member((int(diagonal_tag[-1])+3), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)

                Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
                Member.Truss(0, (int(diagonal_tag[-1])+5), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)
            else:
                print("WARNING: Please enter an even number of spans for a symmetrical net.")

        elif diagonal_type == 7:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1)*2:
                Member.Truss(0, j, i, i+3, section_no=3)
                j +=1
                Member.Truss(0, j, i+1, i+2, section_no=3)
                i +=2
                j +=1
            #Add first span
            Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
            Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)

            Member((int(diagonal_tag[-1])*2+1), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
            Member((int(diagonal_tag[-1])*2+2), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)

            Member.Truss(0, (int(diagonal_tag[-1])*2+3), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
            Member.Truss(0, (int(diagonal_tag[-1])*2+4), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)

        elif diagonal_type == 8:
            #Add first span
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            Node(tag_nodes[-1]+1, (-first_span), 0, -total_height)
            Node(tag_nodes[-1]+2, (total_length+first_span), 0, -total_height)

            Member((int(diagonal_tag[1])), tag_nodes[-1]+1, tag_nodes[1], 0, 1, 1, 0, 0)
            Member((int(diagonal_tag[2])), tag_nodes[-1]+2, tag_nodes[-1], 0, 2, 2, 0, 0)

            Member.Truss(0, (int(diagonal_tag[3])), tag_nodes[0], tag_nodes[-1]+1, section_no=3)
            Member.Truss(0, (int(diagonal_tag[4])), tag_nodes[-2], tag_nodes[-1]+2, section_no=3)

        Model.clientModel.service.finish_modification()

def truss_3(diagonal_type,
            number_of_bays,
            total_length,
            total_height,
            first_span,
            upper_chord_material,
            upper_chord_section,
            lower_chord_material,
            lower_chord_section,
            diagonal_material,
            diagonal_section,
            vertical_material,
            vertical_section):

    if __name__ == '__main__':

        Model(False)
        Model.clientModel.service.reset()
        Model.clientModel.service.begin_modification('new')

        # Create Materials
        Material(1, upper_chord_material)
        Material(2, lower_chord_material)
        Material(3, diagonal_material)
        Material(4, vertical_material)

        # Create Sections
        Section(1, upper_chord_section, 1)
        Section(2, lower_chord_section, 2)
        Section(3, diagonal_section, 3)
        Section(4, vertical_section, 4)

        # Create Nodes
        x_nodes = np.repeat(np.arange(0, total_length + total_length/number_of_bays, total_length/number_of_bays), 2)
        z_nodes = (0, (-total_height))*int((len(x_nodes)/2))
        tag_nodes = np.arange(1, len(x_nodes)+1, 1)

        for tag,x,z in zip(tag_nodes, x_nodes, z_nodes):
            Node(tag, x, 0, z)

        # Create Lower Chord
        Member(1, MemberType.TYPE_BEAM, 1, tag_nodes[-2], 0, 2, 2)

        # Create Upper Chord
        Member(2, MemberType.TYPE_BEAM, 2, tag_nodes[-1], 0, 1, 1)

        # Create Verticals
        i = 1
        j = 1
        while j<len(tag_nodes) and i<len(tag_nodes):
            Member.Truss(0, j+2, i, i+1, section_no=4)
            i += 2
            j += 1

        # Create Diagonals
        if diagonal_type == 1:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1):
                Member.Truss(0, j, i, i+3, section_no=3)
                i +=2
                j +=1
            #Add first span
            Node(tag_nodes[-1]+1, (-first_span), 0, 0)
            Node(tag_nodes[-1]+2, (total_length+first_span), 0, 0)

            Member((int(diagonal_tag[-1])+1), tag_nodes[0], tag_nodes[-1]+1, 0, 1, 1, 0, 0)
            Member((int(diagonal_tag[-1])+2), tag_nodes[-2], tag_nodes[-1]+2, 0, 2, 2, 0, 0)

            Member.Truss(0, (int(diagonal_tag[-1])+3), tag_nodes[-1]+1, tag_nodes[1], section_no=3)
            Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-1]+2, tag_nodes[-1], section_no=3)
        elif diagonal_type == 2:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 2):
                Member.Truss(0, j, i+1, i+2, section_no=3)
                i +=2
                j +=1
            #Add first span
            Node(tag_nodes[-1]+1, (-first_span), 0, 0)
            Node(tag_nodes[-1]+2, (total_length+first_span), 0, 0)

            Member((int(diagonal_tag[-1])+1), tag_nodes[0], tag_nodes[-1]+1, 0, 1, 1, 0, 0)
            Member((int(diagonal_tag[-1])+2), tag_nodes[-2], tag_nodes[-1]+2, 0, 2, 2, 0, 0)

            Member.Truss(0, (int(diagonal_tag[-1])+3), tag_nodes[-1]+1, tag_nodes[1], section_no=3)
            Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-1]+2, tag_nodes[-1], section_no=3)
        elif diagonal_type == 3:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            k = 1

            while i < len(tag_nodes) -1 and j < diagonal_tag[-1] +2  and k < len(tag_nodes) :
                Member.Truss(0, j, i, i+3, section_no=3)
                j += 1
                Member.Truss(0, j, k+3, k+4, section_no=3)
                i += 4
                k += 4
                j += 1
            #Add first span
            Node(tag_nodes[-1]+1, (-first_span), 0, 0)
            Node(tag_nodes[-1]+2, (total_length+first_span), 0, 0)

            Member((int(diagonal_tag[-1])+1), tag_nodes[0], tag_nodes[-1]+1, 0, 1, 1, 0, 0)
            Member((int(diagonal_tag[-1])+2), tag_nodes[-2], tag_nodes[-1]+2, 0, 2, 2, 0, 0)

            Member.Truss(0, (int(diagonal_tag[-1])+3), tag_nodes[-1]+1, tag_nodes[1], section_no=3)
            Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-1]+2, tag_nodes[-1], section_no=3)
        elif diagonal_type == 4:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            k = 1

            while i < len(tag_nodes) -1 and j < diagonal_tag[-1]+1  and k < len(tag_nodes) :
                Member.Truss(0, j, i+2, i+5, section_no=3)
                j += 1
                Member.Truss(0, j, k+1, k+2, section_no=3)
                i += 4
                k += 4
                j += 1
            #Add first span
            Node(tag_nodes[-1]+1, (-first_span), 0, 0)
            Node(tag_nodes[-1]+2, (total_length+first_span), 0, 0)

            Member((int(diagonal_tag[-1])+2), tag_nodes[0], tag_nodes[-1]+1, 0, 1, 1, 0, 0)
            Member((int(diagonal_tag[-1])+3), tag_nodes[-2], tag_nodes[-1]+2, 0, 2, 2, 0, 0)

            Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-1]+1, tag_nodes[1], section_no=3)
            Member.Truss(0, (int(diagonal_tag[-1])+5), tag_nodes[-1]+2, tag_nodes[-1], section_no=3)
        elif diagonal_type == 5:
            if (number_of_bays % 2) == 0:
                diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                i = 1
                j = int(diagonal_tag[0])
                while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1] +1:
                    Member.Truss(0, j, i+1, i+2, section_no=3)
                    i += 2
                    j += 1
                i = int(len(tag_nodes)/2)
                j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                while i < tag_nodes[-1] and j <diagonal_tag[-1] +1:
                    Member.Truss(0, j, i, i+3, section_no=3)
                    i += 2
                    j += 1
                #Add first span
                Node(tag_nodes[-1]+1, (-first_span), 0, 0)
                Node(tag_nodes[-1]+2, (total_length+first_span), 0, 0)

                Member((int(diagonal_tag[-1])+2), tag_nodes[0], tag_nodes[-1]+1, 0, 1, 1, 0, 0)
                Member((int(diagonal_tag[-1])+3), tag_nodes[-2], tag_nodes[-1]+2, 0, 2, 2, 0, 0)

                Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-1]+1, tag_nodes[1], section_no=3)
                Member.Truss(0, (int(diagonal_tag[-1])+5), tag_nodes[-1]+2, tag_nodes[-1], section_no=3)

            else:
                print("WARNING: Please enter an even number of spans for a symmetrical net.")

        elif diagonal_type == 6:
            if (number_of_bays % 2) == 0:
                diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
                i = 1
                j = int(diagonal_tag[0])
                while i < ((tag_nodes[-1]/2) + 1) and j <diagonal_tag[-1] +1:
                    Member.Truss(0, j, i, i+3, section_no=3)
                    i += 2
                    j += 1
                i = int(len(tag_nodes)/2) + 1
                j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                while i < tag_nodes[-1] and j <diagonal_tag[-1] +1:
                    Member.Truss(0, j, i, i+1, section_no=3)
                    i += 2
                    j += 1
                #Add first span
                Node(tag_nodes[-1]+1, (-first_span), 0, 0)
                Node(tag_nodes[-1]+2, (total_length+first_span), 0, 0)

                Member((int(diagonal_tag[-1])+2), tag_nodes[0], tag_nodes[-1]+1, 0, 1, 1, 0, 0)
                Member((int(diagonal_tag[-1])+3), tag_nodes[-2], tag_nodes[-1]+2, 0, 2, 2, 0, 0)

                Member.Truss(0, (int(diagonal_tag[-1])+4), tag_nodes[-1]+1, tag_nodes[1], section_no=3)
                Member.Truss(0, (int(diagonal_tag[-1])+5), tag_nodes[-1]+2, tag_nodes[-1], section_no=3)
            else:
                print("WARNING: Please enter an even number of spans for a symmetrical net.")

        elif diagonal_type == 7:
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1)*2:
                Member.Truss(0, j, i, i+3, section_no=3)
                j +=1
                Member.Truss(0, j, i+1, i+2, section_no=3)
                i +=2
                j +=1
            #Add first span
            Node(tag_nodes[-1]+3, (-first_span), 0, 0)
            Node(tag_nodes[-1]+4, (total_length+first_span), 0, 0)

            Member((int(diagonal_tag[-1])*2+1), tag_nodes[-1]+3, tag_nodes[0], 0, 1, 1, 0, 0)
            Member((int(diagonal_tag[-1])*2+2), tag_nodes[-1]+4, tag_nodes[-2], 0, 2, 2, 0, 0)

            Member.Truss(0, (int(diagonal_tag[-1])*2+3), tag_nodes[-1]+3, tag_nodes[1], section_no=3)
            Member.Truss(0, (int(diagonal_tag[-1])*2+4), tag_nodes[-1], tag_nodes[-1]+4, section_no=3)

        elif diagonal_type == 8:
            #Add first span
            diagonal_tag = np.arange((len(tag_nodes)/2 + 3), (len(tag_nodes)/2 + 3) + number_of_bays, 1)
            Node(tag_nodes[-1]+3, (-first_span), 0, 0)
            Node(tag_nodes[-1]+4, (total_length+first_span), 0, 0)

            Member((int(diagonal_tag[-1])*2+1), tag_nodes[-1]+3, tag_nodes[0], 0, 1, 1, 0, 0)
            Member((int(diagonal_tag[-1])*2+2), tag_nodes[-1]+4, tag_nodes[-2], 0, 2, 2, 0, 0)

            Member.Truss(0, (int(diagonal_tag[-1])*2+3), tag_nodes[-1]+3, tag_nodes[1], section_no=3)
            Member.Truss(0, (int(diagonal_tag[-1])*2+4), tag_nodes[-1], tag_nodes[-1]+4, section_no=3)

        Model.clientModel.service.finish_modification()

def truss_4(diagonal_type,
            number_of_bays,
            total_length,
            total_height,
            upper_chord_material,
            upper_chord_section,
            lower_chord_material,
            lower_chord_section,
            diagonal_material,
            diagonal_section,
            vertical_material,
            vertical_section):

    if __name__ == '__main__':

        Model(False)
        Model.clientModel.service.reset()
        Model.clientModel.service.begin_modification('new')

        # Create Materials
        Material(1, upper_chord_material)
        Material(2, lower_chord_material)
        Material(3, diagonal_material)
        Material(4, vertical_material)

        # Create Sections
        Section(1, upper_chord_section, 1)
        Section(2, lower_chord_section, 2)
        Section(3, diagonal_section, 3)
        Section(4, vertical_section, 4)

        # Create Nodes
        x_nodes = [0]
        for i in np.arange(total_length/number_of_bays, total_length, total_length/number_of_bays):
            x_nodes.append(i)
            x_nodes.append(i)
        x_nodes.append(total_length)

        z_nodes = [0]
        for i in np.arange(((total_length/number_of_bays) * total_height)/(total_length/2), total_height + 0.1, ((total_length/number_of_bays) * total_height)/(total_length/2)):
            z_nodes.append(0)
            z_nodes.append(-i)
        for i in z_nodes[::-1][1:-1]:
            z_nodes.append(i)

        tag_nodes = np.arange(1, len(x_nodes)+1, 1)

        for tag,x,z in zip(tag_nodes, x_nodes, z_nodes):
            Node(tag, x, 0, z)

        # Create Lower Chord
        Member(1, MemberType.TYPE_BEAM, 1, tag_nodes[-1], 0, 2, 2)

        # Create Upper Chord
        Member(2, 1, int(sum(tag_nodes) / len(tag_nodes) + 0.5), 0, 1, 1)
        Member(3, int(sum(tag_nodes) / len(tag_nodes) + 0.5), tag_nodes[-1], 0, 1, 1)

        # Create Verticals
        i = 1
        j = 1
        while j<len(tag_nodes)-1 and i<len(tag_nodes):
            Member.Truss(0, j+3, i+1, i+2, section_no=4)
            i += 2
            j += 1

        #Create Diagonals
        if diagonal_type == 1:
            diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1):
                Member.Truss(0, j, i+2, i+3, section_no=3)
                i +=2
                j +=1

        elif diagonal_type == 2:
            diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes)-1 and j < int(diagonal_tag[-1]):
                Member.Truss(0, j, i+1, i+4, section_no=3)
                i +=2
                j +=1

        elif diagonal_type == 3:
            diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
            i = 1
            j = int(diagonal_tag[0])
            k = 1
            while i < len(tag_nodes) -2 and j < diagonal_tag[-1]  and k < len(tag_nodes) :
                Member.Truss(0, j, i+1, i+4, section_no=3)
                j += 1
                Member.Truss(0, j,  k+4, k+5, section_no=3)
                i += 4
                k += 4
                j += 1

        elif diagonal_type == 4:
            diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
            i = 1
            j = int(diagonal_tag[0])
            k = 1
            while i < len(tag_nodes) -2 and j < diagonal_tag[-1]  and k < len(tag_nodes) :
                Member.Truss(0, j, i+2, i+3, section_no=3)
                j += 1
                Member.Truss(0, j, k+3, k+6, section_no=3)
                i += 4
                k += 4
                j += 1

        elif diagonal_type == 5:
            if (number_of_bays % 2) == 0:
                diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
                i = 1
                j = int(diagonal_tag[0])
                while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1]:
                    Member.Truss(0, j, i+2, i+3, section_no=3)
                    i += 2
                    j += 1
                i = int(len(tag_nodes)/2)
                j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                while i < tag_nodes[-1] and j <diagonal_tag[-1]:
                    Member.Truss(0, j, i, i+3, section_no=3)
                    i += 2
                    j += 1
            else:
                print("WARNING: Please enter an even number of spans for a symmetrical net.")

        elif diagonal_type == 6:
            if (number_of_bays % 2) == 0:
                diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
                i = 1
                j = int(diagonal_tag[0])
                while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1]:
                    Member.Truss(0, j, i+1, i+4, section_no=3)
                    i += 2
                    j += 1
                i = int(len(tag_nodes)/2)
                j = int(diagonal_tag[int(len(diagonal_tag)/2)])
                while i < tag_nodes[-1] and j <diagonal_tag[-1]:
                    Member.Truss(0, j, i+1, i+2, section_no=3)
                    i += 2
                    j += 1
            else:
                print("WARNING: Please enter an even number of spans for a symmetrical net.")

        elif diagonal_type == 7:
            diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 1)*2:
                Member.Truss(0, j, i+2, i+3, section_no=3)
                j +=1
                Member.Truss(0, j, i+1, i+4, section_no=3)
                i +=2
                j +=1

        elif diagonal_type == 8:
            pass

        Model.clientModel.service.finish_modification()

def truss_5(diagonal_type,
            number_of_bays,
            total_length,
            total_height,
            side_height,
            upper_chord_material,
            upper_chord_section,
            lower_chord_material,
            lower_chord_section,
            diagonal_material,
            diagonal_section,
            vertical_material,
            vertical_section):

    if __name__ == '__main__':

        Model(False)
        Model.clientModel.service.reset()
        Model.clientModel.service.begin_modification('new')

        # Create Materials
        Material(1, upper_chord_material)
        Material(2, lower_chord_material)
        Material(3, diagonal_material)
        Material(4, vertical_material)

        # Create Sections
        Section(1, upper_chord_section, 1)
        Section(2, lower_chord_section, 2)
        Section(3, diagonal_section, 3)
        Section(4, vertical_section, 4)

        # Create Nodes
        x_nodes = [0, 0]
        for i in np.arange(total_length/number_of_bays, total_length, total_length/number_of_bays):
            x_nodes.append(i)
            x_nodes.append(i)
        x_nodes.append(total_length)
        x_nodes.append(total_length)

        z_nodes = []
        for i in np.arange(side_height, total_height +0.1, (total_height-side_height)/(number_of_bays/2)):
            z_nodes.append(0)
            z_nodes.append(-i)
        for i in z_nodes[::-1][1:-1]:
            z_nodes.append(i)

        tag_nodes = np.arange(1, len(x_nodes)+1, 1)

        for tag,x,z in zip(tag_nodes, x_nodes, z_nodes):
            Node(tag, x, 0, z)

        # Create Lower Chord
        Member(1, 1, tag_nodes[-2], 0, 2, 2)

        # Create Upper Chord
        Member(2, 2, int(sum(tag_nodes) / len(tag_nodes) + 0.5), 0, 1, 1)
        Member(3, int(sum(tag_nodes) / len(tag_nodes) + 0.5), tag_nodes[-1], 0, 1, 1)

        # Create Verticals
        i = 1
        j = 1
        while j<len(tag_nodes)-1 and i<len(tag_nodes):
            Member.Truss(0, j+3, i, i+1, section_no=4)
            i += 2
            j += 1

        #Create Diagonals
        if diagonal_type == 1:
            diagonal_tag = np.arange(number_of_bays+5, 2*number_of_bays+4, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes) and j < int(diagonal_tag[-1] + 2):
                Member.Truss(0, j, i, i+3, section_no=3)
                i +=2
                j +=1

        elif diagonal_type == 2:
            diagonal_tag = np.arange(number_of_bays+5, 2*number_of_bays+4, 1)
            i = 1
            j = int(diagonal_tag[0])
            while i < len(tag_nodes)-1 and j < int(diagonal_tag[-1] + 2):
                Member.Truss(0, j, i+1, i+2, section_no=3)
                i +=2
                j +=1

        elif diagonal_type == 3:
            diagonal_tag = np.arange(number_of_bays+5, 2*number_of_bays+4, 1)
            i = 1
            j = int(diagonal_tag[0])
            k = 1
            while i < len(tag_nodes) +2  and j < diagonal_tag[-1] + 2  and k < len(tag_nodes) :
                Member.Truss(0, j, i+1, i+2, section_no=3)
                j += 1
                Member.Truss(0, j, k+2, k+5, section_no=3)
                i += 4
                k += 4
                j += 1

        elif diagonal_type == 4:
            diagonal_tag = np.arange(number_of_bays+5, 2*number_of_bays+4, 1)
            i = 1
            j = int(diagonal_tag[0])
            k = 1
            while i < len(tag_nodes) +2 and j < diagonal_tag[-1] + 2  and k < len(tag_nodes) :
                Member.Truss(0, j, MemberType.TYPE_TRUSS, i, i+3, section_no=3)
                j += 1
                Member.Truss(0, j, k+3, k+4, section_no=3)
                i += 4
                k += 4
                j += 1

        elif diagonal_type == 5:
            if (number_of_bays % 2) == 0:
                diagonal_tag = np.arange(number_of_bays+5, 2*number_of_bays+4, 1)
                i = 1
                j = int(diagonal_tag[0])
                while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1] + 10:
                    Member.Truss(0, j, i+1, i+2, section_no=3)
                    i += 2
                    j += 1

                i = int(len(tag_nodes)/2)
                j = int(diagonal_tag[int(len(diagonal_tag)/2)]) +1
                while i < tag_nodes[-1] + 2 and j <diagonal_tag[-1] + 2:
                    Member.Truss(0, j, MemberType.TYPE_TRUSS, i, i+3, section_no=3)
                    i += 2
                    j += 1
            else:
                print("WARNING: Please enter an even number of spans for a symmetrical net.")

        elif diagonal_type == 6:
            if (number_of_bays % 2) == 0:
                diagonal_tag = np.arange(number_of_bays+5, 2*number_of_bays+4, 1)
                i = 1
                j = int(diagonal_tag[0])
                while i < (tag_nodes[-1]/2) and j <diagonal_tag[-1] + 10:
                    Member.Truss(0, j, i, i+3, section_no=3)
                    i += 2
                    j += 1

                i = int(len(tag_nodes)/2)
                print(i)
                j = int(diagonal_tag[int(len(diagonal_tag)/2)]) +1
                while i < tag_nodes[-1] + 2 and j <diagonal_tag[-1] + 2:
                    Member.Truss(0, j, i+1, i+2, section_no=3)
                    i += 2
                    j += 1
            else:
                print("WARNING: Please enter an even number of spans for a symmetrical net.")

        elif diagonal_type == 7:
            diagonal_tag = np.arange(number_of_bays+3, 2*number_of_bays+2, 1)
            i = 1
            j = int(diagonal_tag[0]) +2
            while i < len(tag_nodes) and j < int(diagonal_tag[-1])*2:
                Member.Truss(0, j, i+1, i+2, section_no=3)
                j +=1
                Member.Truss(0, j, i, i+3, section_no=3)
                i +=2
                j +=1

        elif diagonal_type == 8:
            pass

        Model.clientModel.service.finish_modification()

truss_5(7, 14, 68.4, 12.2, 4.3, 'S235', 'IPE 200', 'S235', 'IPE 160', 'S235', 'IPE 120', 'S235', 'IPE 80')
