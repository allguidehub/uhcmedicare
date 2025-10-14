# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information -----------------------------------------------------

project = 'UHC Medicare Account Setup'
copyright = '2025, UnitedHealthcare'
author = 'UHC Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (leave blank or add as needed)
extensions = []

# Allow reStructuredText raw HTML
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# html_theme = 'sphinx_rtd_theme'

html_title = "How to Register and Log In to Your UHC Medicare Account"
html_short_title = "UHC Medicare Guide"
html_favicon = 'favicon.ico'

html_show_sourcelink = False
html_allow_unsafe = True

html_theme_options = {
    'show_powered_by': False,
}

# html_static_path = ['_static']
