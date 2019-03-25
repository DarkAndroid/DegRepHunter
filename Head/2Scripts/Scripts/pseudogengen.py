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



  

outpath=("pseudogenomes.fa")
out = open(outpath, "w")



    

for n in range(0,432,48): # 400, 30

    genome = ""
    genome = genome + "A"*  (1600+(16*n)) #(1000+(16*n))
    genome = genome + "T"*  (4800-(16*n/3)) #(3000-(16*n/3))
    genome = genome + "G"*  (4800-(16*n/3)) #(3000-(16*n/3))
    genome = genome + "C"*  (4800-(16*n/3)) #(3000-(16*n/3))

    for q in range(100):
        out.write(">pseudo_%s_%s\n" % (n,q))
        


        for x in range(100):
            l=list(genome)
            random.shuffle(l)
            genone = ""
            genome = ''.join(l)

        


        out.write("%s\n" % genome)

        a = genome.count("A")
        t = genome.count("T")
        g = genome.count("G")
        c = genome.count("C")

    
        summ=a+t+g+c
        afr=float(float(a)/float(summ))
        tfr=float(float(t)/float(summ))
        gfr=float(float(g)/float(summ))
        cfr=float(float(c)/float(summ))
        print ("%s %s %s %s  %s %s %s %s  %s" % (a,t,g,c, afr,tfr,gfr,cfr,a+t+g+c))           



    #print ("\n")














