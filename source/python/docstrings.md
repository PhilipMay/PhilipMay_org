# Docstrings

## Description

Python docstrings can be written in many different formats. An overview
of different methods can be found in the following Stack Overflow entry:
[What is the standard Python docstring
format?](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)

It seems to be clever to use the docstring format of scipy and numpy
since these packages are very popular. A guide to the numpy docstring
format is here: [numpydoc docstring
guide](https://numpydoc.readthedocs.io/en/latest/) and here is a
[Restructured Text (reST) syntax CheatSheet for
Sphinx](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html).

## Links

- PEP 8: <https://www.python.org/dev/peps/pep-0008/>
- PEP 257: <https://www.python.org/dev/peps/pep-0257/>
- PEP 287 - reStructuredText Docstring Format:
  <https://www.python.org/dev/peps/pep-0287/>
- Google Python Style Guide:
  <https://github.com/google/styleguide/blob/gh-pages/pyguide.md>
- Example Google Style Python Docstrings: https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html

## Napoleon and Sphinx

### Cross-referencing Python objects

- function: ``:func:`module_name.function_name` ``
- class: ``:class:`module_name.ClassName` ``
- meth: ``:meth:`module_name.ClassName.method_name` ``
- [Cross-referencing Python objects](https://www.sphinx-doc.org/en/master/usage/domains/python.html#cross-referencing-python-objects)

### Docstring Sections

The most comment docstring sections are:

- `Args:`
- `Returns:`
- `Raises:`
- `Yields:`
- `See Also:`
- more see: [Docstring Sections](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#docstring-sections)
