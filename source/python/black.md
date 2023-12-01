# Black

## Links
- [Black Doc](https://black.readthedocs.io/)

## Configuration
Black can be configured in `pyproject.toml`
(see [Usage and Configuration - The basics](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html)). 

Example config:

:::{code} python
:filename: pyproject.toml
[tool.black]
line-length = 99
target-version = ["py310"]
:::
