from abc import ABC, abstractmethod


class Identifier(ABC):
	def __init__(self, name: str):
		self.__name = name

	@staticmethod
	@property
	def regex(self) -> str:
		"A string containing a regex which matches the identifier. This can be used within other regexes."
		return r"[A-Z_][A-Z0-9_]*"

	@property
	def name(self) -> str:
		return self.__name

	def __eq__(self, other):
		return type(self) == type(other) and self.name == other.name