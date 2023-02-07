#coding=utf8

import time
import timeit
import os
import sqlite3

#score=[]



from random import choice
import random






def weightedchoice(items): # this doesn't require the numbers to add up to 100
    return choice("".join(x * y for x, y in items))


def String(length,ap,tp,gp,cp):
   DNA=""
   for count in range(length):
      DNA+=weightedchoice([("A", ap), ("T", tp), ("G", gp), ("C", cp)])
   return DNA




# Return random CGTA sequences, set minimum = maximum to get a specified length.
def random_length_dnasequence(minimum=25, maximum=10000, actg_distribution=None):
    if (minimum == maximum):
        length = minimum
    else:
        length = random.randint(minimum, maximum)
    if (actg_distribution == None):
        actg_distribution = ''.join(random.choice('ATGC') for _x in xrange(7))

    return ''.join(random.choice(actg_distribution) for _x in xrange(length))


def random_dnasequence(length, actg_distribution=None):
    return random_length_dnasequence(length, length, actg_distribution)

















# fix1 28.06.2018    XXXXXXXXX    BAD_END



pgen_path = 'MammalsGenomesWithEcology.fasta.txt'

#pgen_path = 'test.fa'


# path2=open("uni.txt",'r')

# path3=("lenatgc.txt")
# reps = open(path3, "w")






pgen = open(pgen_path,'r')
    #uname = "Zu_cristatus"    

outpath=("pseudogenomes.fa")
out = open(outpath, "w")



pr=1
while True:
        
    name = pgen.readline()[1:-1]
    genome = pgen.readline()[:-1]
    length=len(genome)


        #print uname+" "+name


    a = genome.count("A")
    t = genome.count("T")
    g = genome.count("G")
    c = genome.count("C")

    
    summ=a+t+g+c
    afr=float(float(a)/float(summ))
    tfr=float(float(t)/float(summ))
    gfr=float(float(g)/float(summ))
    cfr=float(float(c)/float(summ))
    print ("%s %s  %s %s %s %s" % (pr,name, a,t,g,c))    



    DNA=""



    for q in range(100):
        out.write(">pseudo_%s_%s\n" % (name,q))
        

        # In %
        # mtdna=String(16000,a,t,g,c)
        # print ("A%s T%s G%s C%s" % (mtdna.count('A'),mtdna.count('T'),mtdna.count('G'),mtdna.count('C')))
        # out.write("%s\n" % mtdna)


        l=list(genome)
        random.shuffle(l)
        result = ''.join(l)
        out.write("%s\n" % result)

        a = result.count("A")
        t = result.count("T")
        g = result.count("G")
        c = result.count("C")

    
        summ=a+t+g+c
        afr=float(float(a)/float(summ))
        tfr=float(float(t)/float(summ))
        gfr=float(float(g)/float(summ))
        cfr=float(float(c)/float(summ))
        #print ("* %s %s %s %s" % (a,t,g,c))           



    #print ("\n")






    pr=pr+1

    if pr>705:
        break







