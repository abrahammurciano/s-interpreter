from abc import ABC, abstractmethod
from instructions.parser_base import ParserBase
from state import State


class Instruction(ABC):
	@abstractmethod
	def run(self, state: State):
		pass

	@classmethod
	@property
	@abstractmethod
	def parser(cls) -> ParserBase:
		pass