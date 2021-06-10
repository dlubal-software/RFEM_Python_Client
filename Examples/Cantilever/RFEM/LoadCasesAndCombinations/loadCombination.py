from RFEM.initModel import *
from RFEM.enums import AnalysisType

class LoadCombination():
	def __init__(self,
				 no: int = 1,
				 name: str = '',
				 analysis_type = AnalysisType.ANALYSIS_TYPE_STATIC,
				 items: dict = {},
				 comment: str = ''):
				 
		# Client model | Load Case
		