from .identifier import Identifier


class Label(Identifier):
	def __init__(self, name: str):
		super().__init__(name + ("1" if name in {"A", "B", "C", "D", "E"} else ""))