"""Sphinx configuration."""
project = "Contacts"
author = "Derek Vlek McCammond"
copyright = "2024, Derek Vlek McCammond"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
