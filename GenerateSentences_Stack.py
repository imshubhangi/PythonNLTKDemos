'''
Created on 20-Jan-2020

@author: shubhangiP
'''


from nltk import CFG, ChartParser, Nonterminal
from random import choice
from tokenize import tokenize
from nltk import grammar
import nltk
from Carbon.Aliases import false
from queue import LifoQueue 


ListofSentnces = ["" for x in range(100)]
globalmaxindex=0
indexestoProcess = []

stack = LifoQueue()

def is_terminal(item):
    """
    Return True if the item is a terminal, which currently is
    if it is hashable and not a ``Nonterminal``.
    :rtype: bool
    """
    return hasattr(item, '__hash__') and not isinstance(item, Nonterminal)

def replace(loop,old,new):
    out=[]
    prevdone=False
    for i in range(len(loop)):
        if loop[i]==old:
            out.append(new)
        else:
            out.append(loop[i])
        
    #print(out)
    return out

def produceStk(grammar):
    while (True):
        if(stack.empty()):
            break
        prodrule=stack.get()
        flag=True
        for prod in prodrule.rhs():
            if(is_terminal(prod)):
                continue
            else:
                flag=False
                prodsagain = grammar.productions(lhs = prod)
                for prodagain in prodsagain:
                    prodrulenew= nltk.grammar.Production(prodrule.lhs(),replace(prodrule.rhs(),prod,prodagain.rhs()))
                    stack.put(prodrulenew)
                break
        if(flag):
            print "one of the sentence :",prodrule
    return

grammar = CFG.fromstring('''
S -> A OP B
OP -> '+'| '-' | '*' | '/' | '%'
B -> '1'|'2'
A -> '3' | '4' 
''')
parser = ChartParser(grammar)
gr = parser.grammar()
print "GR:",gr
print "gr.start():",gr.start()
globalmaxindex=0
print "gr.start() : "
print gr.start()
productions = grammar.productions(lhs = gr.start())
for production in productions:
    stack.put(production)
produceStk(gr)
print "+++++++++++++++++"

