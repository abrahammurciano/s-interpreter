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

-   `[{label}]{instruction}`
-   `{instruction}`

Each `{instruction}` must be in one of the following four forms:

-   `{var}<-{var}`: This is a no-op. This instruction does nothing.
-   `{var}<-{var}+1`: This instruction increments `{var}` by one.
-   `{var}<-{var}-1`: This instruction decrements `{var}` by one, with a lower limit of zero.
-   `IF {var}!=0 GOTO {label}`: This instruction jumps to the first instruction starting with `[{label}]` only if the value of `{var}` is not zero.

`{label}` can be any string starting with an uppercase letter or underscore and containing only uppercase letters, underscores, and digits. Labels point to the end of the program by default. Note, variables `A`, `B`, `C`, `D`, and `E` are aliases for `A1`, `B1`, `C1`, `D1`, and `E1` respectively.

`{var}` can be any string starting with an uppercase letter or underscore and containing only uppercase letters, underscores, and digits. Variables' values are zero by default. `X1`, `X2`, etc. are set to the input values. Note, variables `X` and `Z` are aliases for `X1` and `Z1` respectively. Variable `Y` is the returned variable.
