from collections import defaultdict
from typing import DefaultDict, Sequence
from identifiers import normalize_arg


class Vars:
	def __init__(self, args: Sequence[int]):
		self.__vars: DefaultDict[str, int] = defaultdict(int)
		for i in range(len(args)):
			self.__vars[f"X{i+1}"] = args[i]

	@normalize_arg("var")
	def inc(self, var: str):
		"Increments the value of the variable `var` by one."
		self.__vars[var] += 1

	@normalize_arg("var")
	def dec(self, var: str):
		"Decrements the value of the variable `var` by one."
		if self.__vars[var] > 0:
			self.__vars[var] -= 1

	@normalize_arg("var")
	def is_zero(self, var: str) -> bool:
		return self.__vars[var] == 0

	@property
	def return_value(self):
		return self.__vars["Y1"]
