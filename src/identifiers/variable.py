from .identifier import Identifier


class Variable(Identifier):
	def __init__(self, name: str):
		super().__init__(name + ("1" if name in {"X", "Z"} else ""))