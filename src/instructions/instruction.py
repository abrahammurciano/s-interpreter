from abc import ABC
from state import State


class Instruction(ABC):
	def run(self, state: State):
		state.inc_pc()
