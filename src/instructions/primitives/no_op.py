import re
from typing import Optional
from instructions.instruction import Instruction
from instructions.parser_base import ParserBase
from state import State
from identifiers.variable import Variable


class NoOp(Instruction):
	def run(self, state: State):
		state.inc_pc()

	class Parser(ParserBase):
		__regex = re.compile(rf"^({Variable.regex})<-\1$")

		def parse(self, instruction: str) -> Optional["NoOp"]:
			return NoOp() if self.__regex.match(instruction) else None

	@classmethod
	@property
	def parser(cls) -> "NoOp.Parser":
		return cls.Parser()