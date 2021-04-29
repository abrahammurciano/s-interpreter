import re
from typing import Optional
from identifiers.label import Label
from identifiers.variable import Variable
from state import State
from instructions.instruction import Instruction
from instructions.parser_base import ParserBase


class Branch(Instruction):
	def __init__(self, var: Variable, label: Label):
		self.__var = var
		self.__label = label

	def run(self, state: State):
		if state.vars.is_zero(self.__var):
			state.inc_pc()
		else:
			state.go_to(self.__label)

	class Parser(ParserBase):
		__regex = re.compile(rf"IF ({Variable.regex})!=0 GOTO ({Label.regex})")

		def parse(self, instruction: str) -> Optional["Branch"]:
			match = self.__regex.match(instruction)
			return Branch(Variable(match[1]), Label(match[2])) if match else None

	@classmethod
	@property
	def parser(cls) -> "Branch.Parser":
		return cls.Parser()