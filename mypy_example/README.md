# MyPy
* linter
* based on PEP 484
* docs: [link](https://mypy.readthedocs.io/en/stable/)
* github: [link](https://github.com/python/mypy)
* `disallow-untyped-defs`

## Usage
* `mypy main.py` after commenting / uncommenting desired lines
* `mypy main.py --strict` for more strict checks
* `mypy main.py --disallow-untyped-defs` to disallow untyped defs
* both strict mode and disallow-untyped-defs can be combined causes error regardles, because of `greetings` definition
* most of the time, it's better to use config file, file `mypy.ini`
