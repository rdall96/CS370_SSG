#!README

Markdown to HTML Translator README File
Author: Ricky Dall'Armellina
Date: 09/24/2018

Description:
    Translates a text file written in Markdown to a working HTML document and saves it with the same name.
    Takes the full path of a markdown file and creates an HTML file in the same location.
    Returns TRUE when successful and FALSE when not.

Required Libraries:
    Python-Markdown
    https://python-markdown.github.io

    Installation:
        "pip install markdown"
        "pip install git+https://github.com/Python-Markdown/markdown.git"

Files to copy in your program folder:
    - markdown2html.py
    - markdown_extensions.py
    - html_head.txt

Usage in code:
    >> import markdown2html as Converter
    >> [bool] = Converter.markdown2html( [abspath_of_file_to_convert] )

