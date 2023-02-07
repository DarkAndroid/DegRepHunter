#coding=utf8

import time
import timeit
import os
import sqlite3

#score=[]



# fix1 28.06.2018    XXXXXXXXX    BAD_END



pgen_path = 'MammalsGenomesWithEcology.fasta.txt'

#pgen_path = 'test.fa'


#path2=open("uni.txt",'r')

path3=("lenatgc.csv")
reps = open(path3, "w")




#for n in range(10):

br=3713
while True:

    uname = path2.readline()[:-1]
    print uname

    pgen = open(pgen_path,'r')
    #uname = "Zu_cristatus"    


    pr=1
    while True:
        
        name = pgen.readline()[1:-1]
        genome = pgen.readline()
        length=len(genome)


        #print uname+" "+name

  
        if (uname==name.replace(" ","_")):
            

            a = genome.count("A")
            t = genome.count("T")
            g = genome.count("G")
            c = genome.count("C")
            reps.write("%s %s %s %s %s %s %s %s\n" % (br,uname,pr,name,a,t,g,c))

            break
            




        pr=pr+1

        if pr>3954:
	        break

    br=br+1

    if br>3717:
        break