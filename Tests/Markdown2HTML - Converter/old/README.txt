#!README

Markdown to HTML Translator README File
Author: Ricky Dall'Armellina
Date: 09/4/2018

Description:
    Accepts a Markdown file as an input, converts it to an HTML file
    and returns that file as an output

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
    import markdown2html as Converter
    [output_file] = Converter.markdown2html( [file_to_convert] )

