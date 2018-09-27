#! /usr/bin/env python

#----------------------------------------------------------------------
# Markdown Extensions
# Author: Ricky Dall'Armellina
# Date: 09/4/2018
#
# Description: Adds support for <del> and <ins> to the python
#              markdown to html converter
# Reference: https://github.com/aleray/mdx_del_ins/blob/master/mdx_del_ins.py
#----------------------------------------------------------------------

import markdown
from markdown.inlinepatterns import SimpleTagPattern

DEL_RE = r"(\~\~)(.+?)(\~\~)"
INS_RE = r"(\+\+)(.+?)(\+\+)"

class DelInsExtension(markdown.extensions.Extension):
    #adds del ins to the markdown class
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('del', SimpleTagPattern(DEL_RE, 'del'), '<not_strong')
        md.inlinePatterns.add('ins', SimpleTagPattern(INS_RE, 'ins'), '<not_strong')

def makeExtension(configs={}):
    return DelInsExtension(configs=dict(configs))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
