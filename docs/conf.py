import os
import sys
sys.path.insert(0, os.path.abspath('..')) # docs 바로 위가 루트이므로 '..'

project = 'HealthHabitHelper'
copyright = '2025, Lee Seung Ryul'
author = 'Lee Seung Ryul'
release = 'v0.0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

autodoc_mock_imports = ["flask", "Flask"]