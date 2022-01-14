from RFEM.initModel import *
from RFEM.enums import *
from RFEM.BasicObjects.node import *
from RFEM.BasicObjects.line import *

Model(False)
Model.clientModel.service.begin_modification('new')

Node(1, 0, 0, 0)
Node(2, 0, -5, 0)
Node(3, 0, 5, 0)
Node(4, 5, 0, 0)

Line.Circle(1, 1, '2', [0,0,0], 5)
Line.Circle(1, 2, '3', [0,10,0], 5, [0,1,0])
Line.Circle(1, 3, '1', [0,10,0], 10)

Model.clientModel.service.finish_modification()