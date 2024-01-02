# Docstrings

## Description

- overview different docstring methods: [What is the standard Python docstring format?](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)

## Links

- PEP 8: <https://www.python.org/dev/peps/pep-0008/>
- PEP 257: <https://www.python.org/dev/peps/pep-0257/>
- PEP 287 - reStructuredText Docstring Format:
  <https://www.python.org/dev/peps/pep-0287/>
- Google Python Style Guide:
  <https://github.com/google/styleguide/blob/gh-pages/pyguide.md>
- Example Google Style Python Docstrings: <https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html>

## Napoleon and Sphinx

### Cross-referencing Python objects

- function: ``:func:`module_name.function_name` ``
- class: ``:class:`module_name.ClassName` ``
- meth: ``:meth:`module_name.ClassName.method_name` ``
- prefix `~`: link text will only be the last component of the target
- also see: [Cross-referencing syntax](https://www.sphinx-doc.org/en/master/usage/domains/index.html#cross-referencing-syntax)
- also see: [Cross-referencing Python objects](https://www.sphinx-doc.org/en/master/usage/domains/python.html#cross-referencing-python-objects)

### Docstring Sections

The most comment docstring sections are:

- `Args:`
- `Returns:`
- `Raises:`
- `Yields:`
- `See Also:`
- also see: [Docstring Sections](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#docstring-sections)
