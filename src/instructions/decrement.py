from state import State
from .instruction import Instruction


class Decrement(Instruction):
	def __init__(self, var: str):
		self.__var = var

	def run(self, state: State):
		state.vars.dec(self.__var)