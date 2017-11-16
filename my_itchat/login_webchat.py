import itchat
import time
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

graphviz = GraphvizOutput()
graphviz.output_file = ('out2.png')

with PyCallGraph(output=graphviz):
    itchat.auto_login()
    time.sleep(3)
    itchat.logout()

# todo: why out.png and out2.png cannot show the itchat module.

