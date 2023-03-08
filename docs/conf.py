# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from datetime import datetime

# -- Project information -----------------------------------------------------

project = 'DeepWater Exploration'
copyright = f'{datetime.now().year}, DeepWater Exploration Inc.'
author = 'Brandon Stevens'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser', 'sphinx_design', 'sphinxcontrib.youtube'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'

# Disable showing the sourcelink option for each page
html_show_sourcelink = False

html_context = {
    'default_description': 'Resources on DeepWater Exploration Documentation',
}

myst_enable_extensions = [
    'colon_fence'
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

html_css_files = [
    'css/custom.css'
]

html_favicon = 'img/wave.png'

html_title = "DeepWater Exploration docs"

#html_logo = 'dwe_transparent2.png'
html_theme_options = {
    'dark_logo': 'DWELogo_white_WEB.svg',
    'light_logo': 'DWELogo_black_WEB.svg',
    'navigation_with_keys': True,
    'footer_icons': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/DeepwaterExploration/DeepwaterExplorationDocs',
            'html': '''
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>''',
            'class': ''
        },
        {
            'name': 'Globe',
            'url': 'https://exploredeepwater.com',
            'html': '''
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8.50024 1C9.78581 1 11.0425 1.38123 12.1114 2.09546C13.1804 2.80969 14.0135 3.82483 14.5055 5.01257C14.8975 5.95898 15.0589 6.98108 14.9814 7.99524C14.8965 9.10645 14.527 10.1801 13.9048 11.1112C13.1906 12.1802 12.1754 13.0133 10.9877 13.5052C9.79997 13.9972 8.49304 14.126 7.23216 13.8751C5.97128 13.6243 4.81309 13.0052 3.90405 12.0962C2.99501 11.1871 2.37594 10.0289 2.12514 8.76807C1.87434 7.5072 2.00307 6.20032 2.49502 5.01257C2.987 3.82483 3.82011 2.80969 4.88904 2.09546C5.95796 1.38123 7.21467 1 8.50024 1ZM13.3942 5C12.7529 3.75281 11.6615 2.79626 10.3414 2.32373C10.7848 3.16357 11.1062 4.0647 11.2942 5H13.3942ZM13.9768 7.99524C13.9921 7.83081 13.9999 7.66553 14.0002 7.5C13.9992 6.99255 13.9275 6.48767 13.7872 6H11.4452C11.4772 6.33105 11.5002 6.66406 11.5002 7C11.5 7.12598 11.4973 7.25195 11.4923 7.37769C11.492 7.38623 11.4917 7.39417 11.4913 7.40271C11.4837 7.58289 11.4711 7.76331 11.4538 7.94263C11.4195 8.29749 11.3663 8.65039 11.2942 9H13.7872C13.8818 8.67139 13.9452 8.33496 13.9768 7.99524ZM10.4411 7.99524C10.443 7.97815 10.4449 7.96106 10.4468 7.94397C10.4811 7.63074 10.499 7.31567 10.5002 7C10.4936 6.66553 10.4682 6.33167 10.4242 6H6.57625C6.53232 6.33167 6.50694 6.66553 6.50024 7C6.50299 7.67334 6.58114 8.34412 6.73324 9H10.2672C10.3441 8.66833 10.4021 8.33289 10.4411 7.99524ZM10.2492 5C10.1609 4.60352 10.0467 4.21399 9.90622 3.83447C9.67142 3.2019 9.36575 2.59644 8.99425 2.03003C8.83024 2.01599 8.66624 2 8.50024 2C8.39575 2 8.29207 2.00635 8.18867 2.01453C8.12779 2.01929 8.06701 2.02478 8.00624 2.03003L8.00024 2.03918C7.40912 2.94299 6.98598 3.9458 6.75125 5H10.2492ZM5.70625 5C5.89804 4.0647 6.22337 3.16174 6.67224 2.31897C5.34624 2.78979 4.24971 3.74866 3.60625 5H5.70625ZM3.21324 6C3.07294 6.48767 3.00125 6.99255 3.00024 7.5C3.00125 8.00745 3.07294 8.51233 3.21324 9H5.70625C5.57068 8.34192 5.50166 7.67188 5.50024 7C5.50024 6.66406 5.52325 6.33105 5.55525 6H3.21324ZM5.96725 10H3.60725C3.98526 10.7384 4.52496 11.382 5.18619 11.8829C5.84739 12.3838 6.6131 12.729 7.42625 12.8931C6.78622 12.0142 6.29344 11.0371 5.96725 10ZM8.50024 12.644C9.13968 11.8531 9.63951 10.959 9.97824 10H7.02225C7.36099 10.959 7.86082 11.8531 8.50024 12.644ZM11.0332 10C10.707 11.0371 10.2143 12.0142 9.57425 12.8931C10.3874 12.729 11.1531 12.3838 11.8143 11.8829C12.4755 11.382 13.0152 10.7384 13.3932 10H11.0332Z"/>
                </svg>''',
            'class': ''
        }
    ]
}

language = "en"
myst_html_meta = {
    "description": "DeepWater Exploration Documentation Site",
    "keywords": "rov, exploreHD, HDCam, Camera"
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
