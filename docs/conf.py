# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'earthquake_CNN'
copyright = '2025, Paolo Bonfini'
author = 'Paolo Bonfini'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = "Earthquake CNN Documentation"
html_logo = "_static/logo.png"   # If you want a custom logo
html_theme_options = {
    "sidebar_hide_name": False,
}

# Convert GIFs
def setup(app):
    from docutils import nodes

    def replace_gif_with_png(app, doctree, fromdocname):
        if app.builder.name == 'latex':
            for node in doctree.traverse(nodes.image):
                if node['uri'].endswith('.gif'):
                    node['uri'] = node['uri'][:-4] + '.png'

    app.connect('doctree-resolved', replace_gif_with_png)

