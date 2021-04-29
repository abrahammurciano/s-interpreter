from typing import Set
from exceptions.parse_error import ParseError
from instructions.parser_base import ParserBase
from instructions.instruction import Instruction


class ParserRegistry:
	def __init__(self):
		self.__parsers: Set[ParserBase] = set()

	def register(self, parser: ParserBase):
		self.__parsers.add(parser)

	def parse(self, input: str) -> Instruction:
		for parser in self.__parsers:
			instruction = parser.parse(input)
			if instruction:
				return instruction
		raise ParseError(f'Invalid instruction "{input}".')