from typing import Dict, Optional, Sequence
from identifiers import normalize_arg
from vars import Vars


class State:
	def __init__(self, args: Sequence[int], labels: Dict[str, int]):
		self.__vars = Vars(args)
		self.__labels = labels
		self.__pc: Optional[int] = 0

	@property
	def vars(self) -> Vars:
		"The variable state of ths S program."
		return self.__vars

	@property
	def pc(self) -> Optional[int]:
		"The program counter."
		return self.__pc

	@property
	def return_value(self) -> int:
		return self.vars.return_value

	@normalize_arg("label")
	def go_to(self, label: str):
		"Set the program counter to the given label, or None if the label is not defined."
		self.__pc = self.__labels[label]