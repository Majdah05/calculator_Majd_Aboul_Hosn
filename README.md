# Lab 6 calculator

This project implements the graded PyBuilder exercise. The optional Makefile
exercise is not included.

## Setup and commands

From this project directory in PowerShell, create an environment and install
PyBuilder (Python 3.11 was used for verification):

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\pyb.exe --no-venvs run_unit_tests
.\.venv\Scripts\pyb.exe --no-venvs publish
```

`--no-venvs` reuses the environment containing PyBuilder. It avoids creating
additional nested environments, whose paths can exceed Windows' path limit
in a deeply nested OneDrive directory. From a short project path, the usual
`pyb run_unit_tests` and `pyb publish` commands can be used after activation.
The first build needs internet access to install PyBuilder's dependencies.

Run the tests independently from the project root:

```powershell
python -m unittest -v tests.unittest.calculator_Majd_Aboul_Hosn.test_calculator_Majd_Aboul_Hosn
```

## How it works

The calculator package in `src/main/python` contains seven functions. Addition,
subtraction, multiplication, division, modulus, and power use Python operators.
Square root uses `math.sqrt`. Division and modulus reject a zero divisor with
`ValueError`; square root rejects negative inputs with `ValueError`. Power
follows Python's `**` behavior, including `0 ** 0 == 1` and `ZeroDivisionError`
for zero raised to a negative exponent.

The test module contains seven tests, one for each calculator operation.
Division, modulus, and square root also check invalid inputs within their tests. The empty `__init__.py`
files in the test folders let Python import the tests using the handout's
dotted module command.

`build.py` sets the project name and version and loads the core, unittest, and
distutils plugins. It explicitly sets the test directory and the `test_*`
filename pattern so PyBuilder actually discovers the tests. `publish` runs
the build tasks, including tests, and creates a source archive and wheel in
`target/dist/dist/`. Running PyBuilder without a
task also selects `publish`.

## Submission

In the current Lab6 workspace, the environment is already installed in the
parent directory. From `calculator_Majd_Aboul_Hosn`, run this for the screenshot:

```powershell
..\.venv\Scripts\pyb.exe --no-venvs run_unit_tests
```

Submit the project ZIP and a genuine terminal screenshot. Keep the successful
test count, `BUILD SUCCESSFUL`, base directory containing
`calculator_Majd_Aboul_Hosn`, `Build finished`, and `Build took` visible.
Generated environments, caches, and the `target` directory are not needed in
the source ZIP; PyBuilder recreates them.
