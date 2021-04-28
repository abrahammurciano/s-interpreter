from exceptions.parse_error import ParseError
from instructions.branch import Branch
from instructions.decrement import Decrement
from instructions.increment import Increment
from instructions.instruction import Instruction
from instructions.no_op import NoOp
import re

__no_op_regex = re.compile(r"^([XYZ]\d*)<-\1$")
__inc_regex = re.compile(r"^([XYZ]\d*)<-\1\+1$")
__dec_regex = re.compile(r"^([XYZ]\d*)<-\1-1$")
__branch_regex = re.compile(r"IF ([XYZ]\d*)!=0 GOTO ([A-E]\d*)")


def parse(instruction: str) -> Instruction:
	if __no_op_regex.match(instruction):
		return NoOp()

	match = __inc_regex.match(instruction)
	if match:
		return Increment(match[1])

	match = __dec_regex.match(instruction)
	if match:
		return Decrement(match[1])

	match = __branch_regex.match(instruction)
	if match:
		return Branch(match[1], match[2])

	raise ParseError(f'Invalid instruction "{instruction}".')