from .instruction import Instruction
from state import State


class NoOp(Instruction):
	def run(self, state: State):
		state.inc_pc()