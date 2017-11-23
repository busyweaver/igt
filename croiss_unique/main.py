import cfu
import sys
import string
import prm
import trans
N=int(sys.argv[1])
recur = [0,1]
recurint=[
    [0],
    [1]
    ]


def main():

    tab=[]
    res2=[]
    res=prm.perm_contr(N,1,2)
    
    for e in res:
        print e 
        trans.permtoarb(e,tab)
        print 'allee'
        print tab
        print 'retour'
        trans.arbtoperm(tab,res2)
        print res2
        print ''
        res2=[]
        tab=[]
    print 'fin'
    cfu.recurrence(N,recur,recurint)
    cfu.iterateur(int(sys.argv[1]),recur,recurint)
    
    #print "%s" % str(recurint)
    #print "%s" % str(recur)
    
    #arbrefor=cfu.un_arbre(int(sys.argv[1]),recur,recurint)
    
    #arbre=cfu.recon_arbre(arbrefor)
#    gene_dot(arbre)

# if(sys.argv[2]=='0'):
#     cal_coeff()
#     sauv_coeff()

# elif(sys.argv[2]=='1'):
#     cal_coeff()
#     print 'kf %s' % str(kf)
#     moy=recursive_generator(int(sys.argv[1]))
# #    print 'res %s' % str(moy[0])
    
# else:
    
#    if(int(sys.argv[3])>int(sys.argv[1])):
#        print 'taille arbre demande plus grande que possible'
#    else:
#        print 'good'
#        cal_coeff()
#        print 'Co %s' % str(CON[5])
#        coq=un_arbre(int(sys.argv[3]))
#        # for e in coq:
#        #     print '\n'
#        #     for i in e :
#        #         if not(i==None):
#        #             print '%d,' % i
#        #         else:
#        #             print '*,'
#        print 'coq %s' % str(coq)
#        noeuds2=recon_arbre(coq)
#        taille=height(noeuds2)
#        print 'taille %d' % taille
#        print 'arbre %s' % str(noeuds2)
#        gene_dot(noeuds2)

main()


    
