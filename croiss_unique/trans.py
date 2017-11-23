import cfu
import sys
import string
import prm

def permtoarb(p,res):
    if(len(p)==1):
        return res
    if(len(p)==2):
        #normalement cest forcement 2,1 au debut
        return res.append([1,2])
        

    orig=origtaille(p)
   # print orig
    comp_orig=orig+1
   # print comp_orig
   # print [indice(comp_orig,p),len(p)-orig+1]
    if(orig==1):
        res.append([1,len(p)-orig+1])
    else:
        res.append([indice(comp_orig,p)+1,len(p)-orig+1])



    
    y=supprimer_traite(p,orig)
   # print y
    permtoarb(y,res)
    

def origtaille(p):
    orig=len(p)-1
    pos=len(p)
    while(pos==p[pos-1] and orig>=2):
        pos=pos-1
        orig=orig-1
    return orig


def indice(x,tab):
    #print x
    #print tab
    for i in range(0,len(tab)):
        if(tab[i]==x):
            return i
    print "erreur non indice"
    sys.exit(-1)

def supprimer_traite(p,x):
    np = []
    for i in range(0,len(p)):
        if(p[i]<=x):
            np.append(p[i])
    return np


def arbtoperm(arb,res):
    x = arb[len(arb)-1]
    for i in range(1,x[1]+1):
        res.append(i)
    
    del arb[len(arb)-1]
    
    while(len(arb)!=0):
        x = arb[len(arb)-1]
        if(x[1]>2):
            #ajouter a la perm x[1] - 2 elem a la fin
            va = x[1]-2
            garde = len(res)+1
          #  print res
            while(va>0):
                res.insert(len(res),len(res)+2)
                va=va-1
          #  print res
            res.insert(x[0]-1,garde)
        else:
            res.insert(x[0]-1,len(res)+1)
        del arb[len(arb)-1]
