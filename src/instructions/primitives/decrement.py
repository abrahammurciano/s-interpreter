import re
from typing import Optional
from identifiers.variable import Variable
from state import State
from instructions.instruction import Instruction
from instructions.parser_base import ParserBase


class Decrement(Instruction):
	def __init__(self, var: Variable):
		self.__var = var

	def run(self, state: State):
		state.vars.dec(self.__var)
		state.inc_pc()

	class Parser(ParserBase):
		__regex = re.compile(rf"^({Variable.regex})<-\1\-1$")

		def parse(self, instruction: str) -> Optional["Decrement"]:
			match = self.__regex.match(instruction)
			return Decrement(Variable(match[1])) if match else None

	@classmethod
	@property
	def parser(cls) -> "Decrement.Parser":
		return cls.Parser()