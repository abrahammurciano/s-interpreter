from abc import ABC, abstractmethod
from state import State


class Instruction(ABC):
	@abstractmethod
	def run(self, state: State):
		pass
