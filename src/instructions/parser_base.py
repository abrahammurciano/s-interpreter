from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
	from instructions.instruction import Instruction


class ParserBase(ABC):
	@abstractmethod
	def parse(self, input: str) -> Optional[Instruction]:
		pass