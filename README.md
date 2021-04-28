# S Iinterpreter

An interpreter for the S language written in python. The S language is a minimal turing complete language created for educational purposes.

# Usage

Run `s.py` with the first argument being the name of the file containing the S code and the rest of the arguments (none to infinitely many) being the arguments to pass to the S program. All arguments after the first must be positive integers.

Example run:
```
$ ./s.py /path/to/multiply.s 10 5
50
```

# Syntax

Each line of the S program must be in one of the following formats:

- `[{label}]{instruction}`
- `{instruction}`

Each `{instruction}` must be in one of the following four forms:

- `{var}<-{var}`: This is a no-op. This instruction does nothing.
- `{var}<-{var}+1`: This instruction increments `{var}` by one.
- `{var}<-{var}-1`: This instruction decrements `{var}` by one, with a lower limit of zero.
- `IF {var}!=0 GOTO {label}`: This instruction jumps to the first instruction starting with `[{label}]` only if the value of `{var}` is not zero.

`{label}` must be a single uppercase letter between `A` and `E` inclusive, optionally followed by a positive integer. In the case of a label appearing at the start of more than one line, only the first one is used.

`{var}` must be a single uppercase `X` or `Z` followed by a number, or alternatively simply a `Y`. If a `{var}` appears in an instruction, a different one may not appear in that same instruction.
