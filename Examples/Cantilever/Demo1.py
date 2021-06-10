#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import der Bibliotheken
from RFEM.enums import *
#from RFEM.window import *
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

if __name__ == '__main__':
	# Eingabe der Parameter auf der Kommandozeile
	l = float(input('Length of the cantilever in m: '))
	f = float(input('Force in kN: '))
	
	# Sperren der Benutzeroberfläche von RFEM 
	clientModel.service.begin_modification('new')
	
	# Das Material Nr. 1 wird erzeugt. Die Materialbezeichnung wird als String geschrieben. RFEM holt sich die Daten automatisch aus der Materialbibliothek. 
	Material(1, 'S235')
	
	# Der Querschnitt Nr. 1 wird erzeugt. Die Bezeichnung wird wie beim Material als Sting geschrieben.
	Section(1, 'IPE 200')
	
	# Der Knoten Nr. 1 wird an der Stelle (0.0, 0.0, 0.0), also im Ursprung, erzeugt.
	Node(1, 0.0, 0.0, 0.0)
	
	# Der Knoten Nr. 2 wird 3 m in X-Richtung erzeugt.
	Node(2, l, 0.0, 0.0)
	
	# Der Stab Nr. 1 wird erzeugt.
	# Der Stabtyp ist Balken.
	# Er beginnt am Knoten 1 und endet am Knoten 2.
	# Die Querschnittsdrehung ist 0.0.
	# Der Anfangs- und Endquerschnitt ist der Querschnittstyp 1.
	Member(1, MemberType.TYPE_BEAM, 1, 2, 0.0, 1, 1)
	
	# Es wird das Knotenauflager 1 erzeugt.
	# Es soll sich am Knoten 1 befinden. Die Knotennummer wird als String übergeben.
	# Das Auflager ist vom vordefinierten Typ "Fest".
	NodalSupport(1, '1', NodalSupportType.FIXED)
	
	# Das Analyse-Setting 1 wird angelegt.
	# Der Name wird als Sting übergeben.
	# Es wird der vordefinierte Typ "geometrisch linear" verwendet.
	StaticAnalysisSettings(1, '1. Ordnung', StaticAnalysisType.GEOMETRICALLY_LINEAR)
	
	# Es wird der Lastfall 1 mit dem Namen "Eigengewicht" angelegt.
	# Dabei handelt es sich um eine statische Analyse.
	# Es wird das Analyse-Setting Nr. 1 verwendet.
	# Er hat die Action-Kategorie 1.
	# Das Eigengewicht soll berücksichtigt werden, deshalb True. Sonst muss da False stehen.
	# Das Eigengewicht soll in Z-Richtung mit dem Faktor 1.0 berücksichtigt werden.
	LoadCase(1 , 'Eigengewicht', AnalysisType.ANALYSIS_TYPE_STATIC, 1,  1, True, 0.0, 0.0, 1.0)
	
	# Es wird die Knotenlast Nr. 1 erzeugt. Sie wird dem Lastfall Nr. 1 zugewiesen.
	# Die Last wirkt am Knoten 2. Die Knotennummer  wird als Sting übergeben.
	# Die Last soll in die vordefinierte Richtung Z wirken.
	# Die Last ist 2000.0 N groß. 
	# Achtung! Es werden immer die SI-Grundeinheiten verwendet.
	NodalLoad(1, 1, '2', LoadDirectionType.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W, f*1000)
	
	# Die Berechnung wird gestartet.
	Calculate_all()
	print('Ready!')
	
	# Freigeben der Benutzeroberfläche von RFEM
	clientModel.service.finish_modification()
	
