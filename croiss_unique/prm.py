import math
import random
import sys
import string
import itertools
import sys

x=list(itertools.permutations([1,2,3,4]))

def permutation(n):
    tab=[i for i in range(1,n+1)]
    res=list(itertools.permutations(tab))
    return res

def perm_contr(n,x,y):
    tab = permutation(n)
    res=[]
    for i in range(0,len(tab)):
        if(indice(x,tab[i])<indice(y,tab[i])):
            res.append(tab[i])
    return res



def indice(x,tab):
    for i in range(0,len(tab)):
        if(tab[i]==x):
            return i
    print "erreur non indice"
    sys.exit(-1)

