import os
import sys
sys.path.insert(0, os.path.abspath('..\RFEM'))


# -- Project information -----------------------------------------------------

project = 'RFEM/RSTAB Webservices'
copyright = '2022, Dlubal Software'
author = 'Dlubal Software'

# The full version, including alpha/beta/rc tags
release = '1.0.2'

# Sphinx Extensions
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx_autodoc_typehints']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 20,
    'includehidden': False,
    'titles_only': False
}

html_logo = "pics/logo.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

# Add any paths that contain custom static files
html_static_path = ['_static']

import mock

MOCK_MODULES = ['RFEM.initModel', 'RFEM.enums', 'math']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()

autodoc_dumb_docstring = True
autodoc_preserve_defaults = True
autodoc_process_signature = True

autodoc_typehints = "none"
autoclass_content = 'both'