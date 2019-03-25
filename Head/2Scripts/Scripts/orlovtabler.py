



import os 
import sqlite3
from StringIO import StringIO
import sys




outpath=("OutOriginal.csv")
out = open(outpath, "w")


out.write("Animal;TLOfADRR0\n")



files=os.listdir("Original")


for f in files:

    file = open("Original\\"+f,'r')

    print (f)


    while True:
        
        string = file.readline().strip()

        if string[0:14] == "------ Repeats":
            break
 

    sumlen = 0


    while True:
        
        string = file.readline().strip()

        if string == "":
        	break

        # 16545	7373	10	4	ataagacata	ataagacata	Invert_repeat

        strarr = string.split("	")
        
        #print strarr


        

        if strarr[6] == "Direct_repeat":
            #print (strarr)
            
            sumlen+=int(strarr[2])

            #print (sumlen)

    

    out.write("%s;%s\n" % (f[:-14],sumlen))