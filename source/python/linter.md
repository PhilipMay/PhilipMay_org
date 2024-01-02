# Linter

## Black

- see <https://black.readthedocs.io/>
- ignore formatting in one line: `# fmt: skip` - <https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#code-style>

## Ruff

- see <https://docs.astral.sh/ruff/>
- ignore lint error in one line: `# noqa: ERROR_ID` - <https://docs.astral.sh/ruff/tutorial/#ignoring-errors>

## mypy

- see <https://mypy.readthedocs.io/en/stable/>
- ignore typing
    - ignore all typing in one line: `# type: ignore`
    - ignore specific error in one line: `# type: ignore[error-code]`
    - <https://mypy.readthedocs.io/en/stable/common_issues.html#spurious-errors-and-locally-silencing-the-checker>
