#!/usr/bin/env python3

import sys
from interpreter import Interpreter


def main():
	code = open(sys.argv[1]).readlines()
	args = [int(arg) for arg in sys.argv[2:]]
	interpreter = Interpreter(code, args)
	print(interpreter.run())


if __name__ == "__main__":
	main()