## 3.1 Import der Bibliotheken
from RFEM.enums import *
from RFEM.initModel import *
from RFEM.BasicObjects.material import Material                                                 #Material
from RFEM.BasicObjects.node import Node                                                         #Knoten
from RFEM.BasicObjects.line import Line                                                         #Linien
from RFEM.BasicObjects.thickness import Thickness                                               #Dicke
from RFEM.BasicObjects.surface import Surface                                                   #Fläche
from RFEM.TypesForNodes.nodalSupport import NodalSupport                                        #Lagerung
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings         #Sttatikanalys-Einstellung (z.B. I.Ordnung)
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase                                     #Lastfall
from RFEM.BasicObjects.lineSet import LineSet                                                   #Liniensatz
from RFEM.Loads.linesetLoad import LineSetLoad                                                  #Liniensatzlasten

# Modell in
Model(True, 'Test_2')
Model.clientModel.service.delete_all()
Model.clientModel.service.begin_modification('new')

# Material
Material(1, 'S355J2')

# Dicke
Thickness(1,'Blechdicke', 1, 50/1000)

# Knoten
Node(1, 0, 0, 0)
Node(2, 0, 8, 0)
Node(3, 25, 0, 0)
Node(4, 25, 8, 0)
Node(5, 50, 8, 0)
Node(6, 50, 16, 0)
Node(7, 0, 2, 0)
Node(8, 0, 6, 0)
Node(9, 25, 2, 0)
Node(10, 25, 6, 0)
Node(11, 50, 10, 0)
Node(12, 50, 14, 0)

# Linie
Line(1, '1 3')
Line(2, '2 4')
Line(3, '3 5')
Line(4, '4 6')
Line(5, '1 2')
Line(6, '3 4')
Line(7, '5 6')
Line(8, '7 9')
Line(9, '8 10')
Line(10, '9 11')
Line(11, '10 12')

# Fläche
Surface(1, '1 2 3 4 5 7',1)

# Lagerung
NodalSupport(1,'1', NodalSupportType.HINGED)
NodalSupport(2,'2', NodalSupportType.HINGED)
NodalSupport(3,'3', NodalSupportType.HINGED)
NodalSupport(4,'4', NodalSupportType.HINGED)
NodalSupport(5,'5', NodalSupportType.HINGED)
NodalSupport(6,'6', NodalSupportType.HINGED)

# Statikanalyse-Einstellung
StaticAnalysisSettings.GeometricallyLinear(1, "Linear")

# Lastfälle
LoadCase.StaticAnalysis(1,'Ermüdung',analysis_settings_no=1,self_weight=[True, 0.0, 0.0, 1.0])

# Liniensätze
LineSet(1, '8 10')
LineSet(2, '9 11')

# Liniensatzlast
vu = 20 #KN
af0 = 1756/1000 #mm
af1 = 2*2845/1000 #mm
af2 = 2*1756/1000 #mm
arv = 1730/1000 #mm
arho = 2410/1000 #mm
arhu = 2754/1000

m = 0
# version 1
#LineSetLoad.Force(1, 1, '1 2', LineSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, LineSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [[m+0,vu],[m+arv,vu],[m+af1,vu],[m+af1+arv,vu],[m+af1+af2,vu],[m+af1+arv+arv,vu],[m+af1+af2+af1,vu],[m+af1+af2+af1+arv,vu]] )
LineSetLoad.Force(1, 1, '1 2', LineSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, LineSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [[0,20000]])
# version 2
# LineSetLoad.Force(1, m+1, '1 2', LineSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, LineSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [m+0,vu,m+arv,vu,m+af1,vu] ) # like GitHub docu

# version 3
# LineSetLoad.Force(1, m+1, '1 2', LineSetLoadDistribution.LOAD_DISTRIBUTION_CONCENTRATED_VARYING, LineSetLoadDirection.LOAD_DIRECTION_LOCAL_Z, [[1,0,vu],[2,0,vu]] )   # like GUI




Model.clientModel.service.finish_modification()