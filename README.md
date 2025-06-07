# [Everybody Codes](https://everybody.codes) ![status](https://github.com/pmareke/everybody-codes/actions/workflows/app.yml/badge.svg)

## Requirements

- You only need to have [uv](https://docs.astral.sh/uv) installed.

## Folder structure

- There is a `tests` folder with the tests files.
  - In order to add new tests please follow the [pytest](https://docs.pytest.org/en/7.1.x/getting-started.html) recommendations.
- The production code goes inside the `src` folder.
- Inside the `scripts` folder you can find the git hooks files.

## Project commands

The project uses [Makefiles](https://www.gnu.org/software/make/manual/html_node/Introduction.html) to run the most common tasks:

- `add-package package=XXX`: Installs the package XXX in the app, ex: `make install package=requests`.
- `build`: Builds the app.
- `check-format`: Checks the code format.
- `check-lint`: Checks the code style.
- `check-typing`: Runs a static analyzer over the code in order to find issues.
- `format`: Formats the code.
- `lint`: Lints the code.
- `help` : Shows this help.
- `install`: Installs the app packages.
- `local-setup`: Sets up the local environment (e.g. install git hooks).
- `run`: Runs the app.
- `test`: Run all the tests.
- `update`: Updates the app packages.
- `watch`: Run all the tests in watch mode.

**Important: Please run the `make local-setup` command before starting with the code.**

_In order to create a commit you have to pass the pre-commit phase which runs the check and test commands._

## Packages

This project uses [uv](https://docs.astral.sh/uv) as the package manager.

### Testing

- [pytest](https://docs.pytest.org/en/7.1.x/contents.html): Testing runner.
- [expects](https://expects.readthedocs.io/en/stable/): An expressive and extensible TDD/BDD assertion library for Python..

### Code style

- [ty](https://github.com/astral-sh/ty): A static type checker.
- [ruff](https://github.com/astral-sh/ruff): An extremely fast Python linter, written in Rust..
