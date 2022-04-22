#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/../..')

from RFEM.initModel import Model
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.member import Member
from RFEM.TypesForMembers.memberDefinableStiffness import MemberDefinableStiffness

if __name__ == '__main__':

    Model(True, "Demo2")
    Model.clientModel.service.begin_modification()

    Node(1, 0,0,0)
    Node(2, 5,2,3)

    MemberDefinableStiffness()

    Member.DefinableStiffness(1, 1, 2, definable_stiffness=1)

    Model.clientModel.service.finish_modification()


