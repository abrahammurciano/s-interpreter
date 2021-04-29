from identifiers.label import Label
from instructions.parser_registry import ParserRegistry
from instructions.instruction import Instruction
from instructions.primitives.no_op import NoOp
from instructions.primitives.increment import Increment
from instructions.primitives.decrement import Decrement
from instructions.primitives.branch import Branch
from state import State
from typing import Dict, List, Sequence, Tuple
import re


class Interpreter:
	def __init__(self, code: Sequence[str], args: Sequence[int]):
		code, labels = self.__extract_labels(code)
		parser_registry = ParserRegistry()
		self.__register_parsers(parser_registry)
		self.__code: List[Instruction] = [
			parser_registry.parse(instruction) for instruction in code
		]
		self.__state = State(args, labels)

	__label_regex = re.compile(rf"\[({Label.regex})\]")

	def __extract_labels(
		self, code: Sequence[str]
	) -> Tuple[Sequence[str], Dict[Label, int]]:
		code_copy = list(code)
		labels: Dict[Label, int] = {}
		for i in range(len(code)):
			instruction = code[i]
			match = self.__label_regex.match(instruction)
			if match:
				label = Label(match[1])
				if label not in labels:
					labels[label] = i
				code_copy[i] = instruction[len(match[0]) :]
		return code_copy, labels

	def __register_parsers(self, registry: ParserRegistry):
		registry.register(NoOp.parser)
		registry.register(Increment.parser)
		registry.register(Decrement.parser)
		registry.register(Branch.parser)

	def run(self) -> int:
		"Runs the program and returns the integer result."
		while self.__state.pc is not None:
			try:
				instruction = self.__code[self.__state.pc]
				instruction.run(self.__state)
			except IndexError:
				break
		return self.__state.return_value
