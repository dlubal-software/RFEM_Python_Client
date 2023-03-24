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
from RFEM.TypesForMembers.memberShearPanel import MemberShearPanel
from RFEM.TypesForMembers.memberRotationalRestraint import MemberRotationalRestraint
from RFEM.TypesForMembers.memberSupport import MemberSupport

if __name__ == '__main__':


    Model()
    Model.clientModel.service.begin_modification()

    MemberShearPanel()
    MemberRotationalRestraint()

    Model.clientModel.service.finish_modification()

