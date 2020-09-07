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
        if not isinstance(code, str):
            import inspect
            code = inspect.getsource(code)
            language = 'python'
        if language:
            self._latex_name = 'lstlisting'
            self.packages.append(Package('listings'))
            self.packages.append(Command('lstset', arguments={'language':language}))
        self.append(pl.NoEscape(code))

class Column(Environment):
    def __init__(self, width=.5):
        self.width = pl.NoEscape(str(width)) + pl.NoEscape(r'\textwidth')
        super().__init__(arguments=self.width)
        
class Columns(Environment):
    def __init__(self, ncols=2):
        super().__init__()
        self.cols = [
            Column(width=round(1/ncols, ndigits=2))
            for i in range(ncols)
        ]
        for col in self.cols:
            self.append(col)
        
class Frame(Environment):
    def __init__(self, title, subtitle='', ncols=0):
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
        if ncols:
            self.add_columns(ncols = ncols)

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

    def add_columns(self, ncols):
        self.columns = Columns(ncols = ncols)
        self.append(self.columns)
