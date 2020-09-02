"""Pylatex extensions for leopard.

Different environments to use in reports and presentations
that have a pdf output
"""
import pylatex as pl
from pylatex.base_classes import Environment
from pylatex.base_classes.command import Command
from pylatex.package import Package

class Verbatim(Environment):
    def __init__(self, code, language=None):
        super().__init__()
        self.content_separator = '\n'
        if language:
            self._latex_name = 'lstlisting'
            self.packages.append(Package('listings'))
            self.packages.append(Command('lstset', arguments={'language':language}))
        self.append(pl.NoEscape(code))
        
class Frame(Environment):
    def __init__(self, title, subtitle=''):
        super().__init__()
        self.content_separator = '\n'
        self.append(
            pl.NoEscape(r'\frametitle{')+
            pl.escape_latex(title)+
            pl.NoEscape('}')
        )
        if subtitle:
            self.append(
                pl.NoEscape(r'\framesubtitle{')+
                pl.escape_latex(title)+
                pl.NoEscape('}')
            )

    def add_enumeration(self, enumeration, ordered=False):
        e = Environment()
        e._latex_name = 'enumerate' if ordered else 'itemize'
        for item in enumeration:
            e.append(
                pl.NoEscape(r'\item ') + pl.escape_latex(item)
            )
        self.append(e)

    def add_code(self, code, language=None):
        if self.options:
            raise Exception('Not expecting options already set')
        self.options = ['fragile'] # for verbatim in frame has to be fragile
        self.append(
            Verbatim(code, language)
        )
