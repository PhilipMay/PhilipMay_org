# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "PhilipMay.org"
html_title = "PhilipMay.org"
copyright = "2020-2024 Philip May"
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

templates_path = ["_templates"]
exclude_patterns = []

# implicit link header targets
# https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html#implicit-targets
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# https://pydata-sphinx-theme.readthedocs.io/
html_theme = "pydata_sphinx_theme"

html_sidebars = {
    "index": ["sidebar-nav-bs"],
    "blog": [
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/archives.html",
    ],
    "blog/**": [
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/archives.html",
    ],
}

#
html_theme_options = {
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/header-links.html#navigation-bar-dropdown-links
    "header_links_before_dropdown": 6,
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/layout.html#hide-the-previous-and-next-buttons
    "show_prev_next": False,
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/search.html#configure-the-search-bar-text
    "search_bar_text": "Search this site...",
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/source-buttons.html#add-an-edit-button
    "use_edit_page_button": True,
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/layout.html#footer
    "footer_start": ["copyright"],
    "footer_end": [],
}

# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/source-buttons.html#view-source-link
html_show_sourcelink = False

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_copy_source
html_copy_source = False

html_static_path = ["_static"]

html_extra_path = ["_extra"]

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
    "PhilipMay": ("Philip May", "http://may.la"),
}

# https://ablog.readthedocs.io/en/stable/manual/ablog-configuration-options.html#confval-blog_default_author
blog_default_author = "PhilipMay"

# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/source-buttons.html#github
html_context = {
    "github_user": "PhilipMay",
    "github_repo": "may-la-myst",
    "github_version": "main",
    "doc_path": "source",
}
