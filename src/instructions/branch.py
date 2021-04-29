from identifiers.label import Label
from identifiers.variable import Variable
from state import State
from .instruction import Instruction


class Branch(Instruction):
	def __init__(self, var: Variable, label: Label):
		self.__var = var
		self.__label = label

	def run(self, state: State):
		if state.vars.is_zero(self.__var):
			state.inc_pc()
		else:
			state.go_to(self.__label)