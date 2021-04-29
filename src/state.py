from typing import Dict, Optional, Sequence
from identifiers.label import Label
from vars import Vars


class State:
	def __init__(self, args: Sequence[int], labels: Dict[Label, int]):
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

	def go_to(self, label: Label):
		"Set the program counter to the given label, or None if the label is not defined."
		self.__pc = self.__labels.get(label, None)

	def inc_pc(self):
		if self.__pc is not None:
			self.__pc += 1