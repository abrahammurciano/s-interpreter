from typing import Callable
import inspect


def normalize_arg(arg_name: str) -> Callable:
	"""
	Wrapper which normalizes the argument named `arg_name` so that the value of the variable whose name is the value of `arg_name` ends in a number.
	For example, "X" becomes "X1", but "Z2" remains "Z2".
	"""

	def decorator(func: Callable) -> Callable:
		arg_names = inspect.getfullargspec(func)[0]
		index = arg_names.index(arg_name)

		def wrapper(*args, **kwargs):
			var = args[index]
			var = normalize(var)
			return func(*args[:index], var, *args[index + 1 :], **kwargs)

		return wrapper

	return decorator


def normalize(var_name: str) -> str:
	return var_name + "" if var_name[-1].isdigit() else "1"