



import os 
import sqlite3
from StringIO import StringIO
import sys




outpath=("OutOriginal.csv")
out = open(outpath, "w")


out.write("Animal;TLOfADRR1;TLOfADRR2;TLOfADRR3;TLOfADRR4;TLOfADRR5;TLOfADRR6;TLOfADRR7;TLOfADRR8;TLOfADRR9;TLOfADRR10;TLOfADRR11;TLOfADRR12;TLOfADRR13;TLOfADRR14;TLOfADRR15;TLOfADRR16;TLOfADRR17;TLOfADRR18;TLOfADRR19;TLOfADRR20;TLOfADRR21;TLOfADRR22;TLOfADRR23;TLOfADRR24;TLOfADRR25;TLOfADRR26;TLOfADRR27;TLOfADRR28;TLOfADRR29;TLOfADRR30;TLOfADRR31;TLOfADRR32;TLOfADRR33;TLOfADRR34;TLOfADRR35;TLOfADRR36;TLOfADRR37;TLOfADRR38;TLOfADRR39;TLOfADRR40;TLOfADRR41;TLOfADRR42;TLOfADRR43;TLOfADRR44;TLOfADRR45;TLOfADRR46;TLOfADRR47;TLOfADRR48;TLOfADRR49;TLOfADRR50;TLOfADRR51;TLOfADRR52;TLOfADRR53;TLOfADRR54;TLOfADRR55;TLOfADRR56;TLOfADRR57;TLOfADRR58;TLOfADRR59;TLOfADRR60;TLOfADRR61;TLOfADRR62;TLOfADRR63;TLOfADRR64;TLOfADRR65;TLOfADRR66;TLOfADRR67;TLOfADRR68;TLOfADRR69;TLOfADRR70;TLOfADRR71;TLOfADRR72;TLOfADRR73;TLOfADRR74;TLOfADRR75;TLOfADRR76;TLOfADRR77;TLOfADRR78;TLOfADRR79;TLOfADRR80;TLOfADRR81;TLOfADRR82;TLOfADRR83;TLOfADRR84;TLOfADRR85;TLOfADRR86;TLOfADRR87;TLOfADRR88;TLOfADRR89;TLOfADRR90;TLOfADRR91;TLOfADRR92;TLOfADRR93;TLOfADRR94;TLOfADRR95;TLOfADRR96;TLOfADRR97;TLOfADRR98;TLOfADRR99;TLOfADRR100\n")



files=os.listdir("Repeats")




arr=""
cou=0

for f in files:
     
    if f[-1:] != "E":
        
    
        file = open("Repeats\\"+f,'r')

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

            #print (string)
        

            if strarr[6] == "Direct_repeat":
                #print (strarr)
            
                sumlen+=int(strarr[2])

            #print (sumlen)

        arr=arr+str(sumlen)+";"
        cou+=1
        if cou == 100:
        
            out.write("%s;%s\n" % (f[:-14],arr))
            arr=""
            cou=0
