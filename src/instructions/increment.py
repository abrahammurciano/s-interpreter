from state import State
from .instruction import Instruction


class Increment(Instruction):
	def __init__(self, var: str):
		self.__var = var

	def run(self, state: State):
		state.vars.inc(self.__var)
		state.inc_pc()