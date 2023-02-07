#coding=utf8

import time
import timeit
import os
import sqlite3



# Зверь A T G C GenomeLength GenerationLength TotalLengthOfAllDirectRepeatsReal TotalLengthOfAllDirectRepeatsPseudo001 TotalLengthOfAllDirectRepeatsPseudo002 ... TotalLengthOfAllDirectRepeatsPseudo100



pgen_path = 'Raw\\MammalsGenomesEcology.txt'
pgen = open(pgen_path, "r")

# Species           Sequence    GenerationLength_d  REP.DirRepLength    GenomeLength    A        T       G   C
# Acinonyx_jubatus   genome            2190              3403              17047      5642    4693    2315    4397


path3=("eco.csv")
reps = open(path3, "w")






string = pgen.readline()

#pr=1
while True:
        
    string = pgen.readline().strip()

    if string == "":
        break
    strarr= string.split("	")
    name = strarr[0] 
    genome = strarr[1] 
    generlen= strarr[2] 
    dirreplrn=  strarr[3]      
    genomelen= strarr[4] 
    a= strarr[5] 
    t= strarr[6] 
    g= strarr[7] 
    c= strarr[8] 
    print (name,c)
    reps.write("%s;%s;%s;%s;%s;%s;%s\n" % (name,a,t,g,c,genomelen,generlen))

    #pr=pr+1