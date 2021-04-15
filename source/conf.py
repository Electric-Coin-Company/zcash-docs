# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
import sphinx_fontawesome
import sphinx_sitemap
#sys.path.insert(0, os.path.abspath('extensions'))

# -- Project information -----------------------------------------------------

project = u'Zcash Documentation'
copyright = u'2019, Electric Coin Company'
author = u'ECC'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u'4.4.0'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# TODO research sphinxcontrib.osexample
extensions = ['sphinx.ext.intersphinx', 'sphinx_fontawesome','recommonmark','sphinx_sitemap','sphinx_copybutton']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['ntemplates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
#locale_dirs = ['locale/']   # path is example but recommended.
#gettext_compact = False     # optional.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
#exclude_patterns = []
html_extra_path = ['robots.txt']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['nstatic']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_extra_path = ['_extra']

#local_dirs = ['locale/']
#gettext_compact = False


# -- Options for displaying GitLab content -------------------------------------------------

html_context = {
    "display_gitlab": True, # Integrate Gitlab
    "gitlab_user": "zcash-docs", # Username
    "gitlab_repo": "zcash-docs", # Repo name
    "gitlab_version": "master", # Version
    "conf_py_path": "/source/" # Path in the checkout to the docs root
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ZCashDocumentationdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ZCashDocumentation.tex', u'Zcash Documentation',
     u'Paige Peterson \\& Marshall Gaucher', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'zcashdocumentation', u'Zcash Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ZCashDocumentation', u'Zcash Documentation',
     author, 'ZCashDocumentation', 'One line description of project.',
     'Miscellaneous'),
]

# Set the value of html_baseurl for sphinx_sitemap
html_baseurl = 'https://zcash.readthedocs.io/en/latest/'

# Add additional JS files
def setup(app):
    app.add_javascript('//cdn.transifex.com/live.js')
    app.add_javascript('js/transifex-api.js')
    app.add_javascript('js/zcash-docs.js')
    app.add_stylesheet('css/custom.css')
