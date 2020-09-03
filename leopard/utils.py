# -*- coding: utf-8 -*-
"""Leopard utility functions and classes
"""

import pandas as pd, re
from collections import OrderedDict

def makeFigFromFile(filename,*args,**kwargs):
    """
    Renders an image in a matplotlib figure, so it can be added to reports 
    args and kwargs are passed to plt.subplots
    """
    import matplotlib.pyplot as plt
    img = plt.imread(filename)
    fig,ax = plt.subplots(*args,**kwargs)
    ax.axis('off')
    ax.imshow(img)
    return fig

def pdSeriesToFrame(pdseries,colname='value'):
    "Returns a series as a pd dataframe"
    return pd.DataFrame(pdseries,columns=[colname])

def renewliner(text):
    newline = re.compile(r'(\w)\n(\w)')
    return newline.subn(r'\g<1> \g<2>',text)[0]

class LeopardDict(OrderedDict):
    """Leopard Dictionary

    Ordered dictionary that only allows string keys.
    Integers can be used to query the dict instead of the string key.
    """
    def __setitem__(self, key, item, **kwargs):
        if not isinstance(key, str):
            raise KeyError("Only string keys are allowed in LeopardDict")
        super().__setitem__(key,item,**kwargs)

    def __getitem__(self, key):
        if isinstance(key, str):
            return super().__getitem__(key)
        elif isinstance(key, int):
            return super().__getitem__(list(self.keys())[key])
        else:
            raise KeyError("LeopardDict item retrieval is only possible with str or int")

class FigureDict(LeopardDict):
    """
    Connects the report section to the dict
    Currently not used!
    """
    def __init__(self, *args, section=None, **kwds):
        super().__init__(*args, **kwds)
        self._section = section 
        
    def __setitem__(self, key, figure, **kwargs):
        super().__setitem__(key,figure,**kwargs)

def print2report(report):
    """Redirecting print to report
    Original print function saved as builtins._print
    """
    import builtins
    if not '_print' in vars(builtins):
        builtins._print = builtins.print
    builtins._print('Redirecting print to print method', report)
    builtins.print = report.print

def open_file(filename):
    import os, sys, subprocess
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
