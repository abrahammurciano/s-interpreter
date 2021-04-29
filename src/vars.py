from collections import defaultdict
from typing import DefaultDict, Sequence
from identifiers.variable import Variable


class Vars:
	def __init__(self, args: Sequence[int]):
		self.__vars: DefaultDict[Variable, int] = defaultdict(int)
		for i in range(len(args)):
			self.__vars[f"X{i+1}"] = args[i]
		self.__return_var = Variable("Y")

	def inc(self, var: Variable):
		"Increments the value of the variable `var` by one."
		self.__vars[var] += 1

	def dec(self, var: Variable):
		"Decrements the value of the variable `var` by one."
		if self.__vars[var] > 0:
			self.__vars[var] -= 1

	def is_zero(self, var: Variable) -> bool:
		return self.__vars[var] == 0

	@property
	def return_value(self):
		return self.__vars[self.__return_var]
