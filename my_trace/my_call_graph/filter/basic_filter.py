# -*- coding: utf-8 -*-
import time


class Banana:

    def __init__(self):
        pass

    def eat(self):
        self.secret_function()
        self.chew()
        self.swallow()

    def secret_function(self):
        time.sleep(0.2)

    def chew(self):
        pass

    def swallow(self):
        pass

# No Filter
#!/usr/bin/env python

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

graphviz = GraphvizOutput(output_file='filter_none.png')

with PyCallGraph(output=graphviz):
    banana = Banana()
    banana.eat()


# Hide the secret
from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput

config = Config()
config.trace_filter = GlobbingFilter(exclude=[
    'pycallgraph.*',
    '*.secret_function',
])

graphviz = GraphvizOutput(output_file='filter_exclude.png')

with PyCallGraph(output=graphviz, config=config):
    banana = Banana()
    banana.eat()

# Maximum Depth
#!/usr/bin/env python

from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph.output import GraphvizOutput


config = Config(max_depth=1)
graphviz = GraphvizOutput(output_file='filter_max_depth.png')

with PyCallGraph(output=graphviz, config=config):
    banana = Banana()
    banana.eat()