import re
from typing import Optional
from identifiers.variable import Variable
from state import State
from instructions.instruction import Instruction
from instructions.parser_base import ParserBase


class Increment(Instruction):
	def __init__(self, var: Variable):
		self.__var = var

	def run(self, state: State):
		state.vars.inc(self.__var)
		state.inc_pc()

	class Parser(ParserBase):
		__regex = re.compile(rf"^({Variable.regex})<-\1\+1$")

		def parse(self, instruction: str) -> Optional["Increment"]:
			match = self.__regex.match(instruction)
			return Increment(Variable(match[1])) if match else None

	@classmethod
	@property
	def parser(cls) -> "Increment.Parser":
		return cls.Parser()