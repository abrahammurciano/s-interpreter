from identifiers import normalize
from instructions.instruction import Instruction
from state import State
from typing import Dict, List, Sequence
import re


class Interpreter:
	def __init__(self, code: List[str], args: Sequence[int]):
		self.__code = code
		labels = self.__extract_labels()
		self.__state = State(args, labels)

	__label_regex = re.compile(r"\[[A-E]\d*\]")

	def __extract_labels(self) -> Dict[str, int]:
		labels: Dict[str, int] = {}
		for i in range(len(self.__code)):
			instruction = self.__code[i]
			match = self.__label_regex.match(instruction)
			if match:
				label = normalize(match[1])
				labels[label] = i
				self.__code[i] = instruction[len(match[0]) :]
		return labels

	def run(self) -> int:
		"Runs the program and returns the integer result."
		while self.__state.pc is not None:
			instruction = Instruction.parse(self.__code[self.__state.pc])
			instruction.run(self.__state)
		return self.__state.return_value
