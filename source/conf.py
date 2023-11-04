# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'May.la'
copyright = '2023, Philip May'
author = 'Philip May'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # "myst_parser",  # not needed when myst_nb is active
    "myst_nb",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# https://github.com/executablebooks/sphinx-book-theme
# https://sphinx-book-theme.readthedocs.io/
html_theme = 'sphinx_book_theme'

html_static_path = ['_static']

# https://myst-nb.readthedocs.io/en/latest/computation/execute.html
nb_execution_mode = "off"
