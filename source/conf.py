# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "May.la"
html_title = "May.la"
copyright = "2023, Philip May"
author = "Philip May"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # "myst_parser",  # not needed when myst_nb is active
    "myst_nb",
    "sphinx_design",  # https://sphinx-design.readthedocs.io/
    "sphinx_copybutton",  # https://github.com/executablebooks/sphinx-copybutton
    "ablog",  # https://ablog.readthedocs.io/
]

templates_path = ['_templates']
exclude_patterns = []

# implicit link header targets
# https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html#implicit-targets
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# https://github.com/executablebooks/sphinx-book-theme
# https://sphinx-book-theme.readthedocs.io/
html_theme = 'sphinx_book_theme'

html_theme_options = {
    # "home_page_in_toc": True,
    # "github_url": "https://github.com/PhilipMay/may-la-myst",
    "repository_url": "https://github.com/PhilipMay/may-la-myst",
    "repository_branch": "main",
    "path_to_docs": "source",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    # "announcement": "<b>v2.0.0</b> is now out! See the Changelog for details",
}

html_static_path = ['_static']

html_extra_path = ['_extra']

# https://myst-nb.readthedocs.io/en/latest/computation/execute.html
nb_execution_mode = "off"

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    # "amsmath",
    "colon_fence",
    # "deflist",
    # "dollarmath",
    # "fieldlist",
    # "html_admonition",
    # "html_image",
    # "linkify",
    # "replacements",
    # "smartquotes",
    # "strikethrough",
    # "substitution",
    # "tasklist",
]

# Blog config https://ablog.readthedocs.io/en/stable/manual/ablog-configuration-options.html
blog_authors = {
    'PhilipMay': ('Philip May', 'http://may.la'),
}

blog_default_author='PhilipMay'
