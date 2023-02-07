#coding=utf8

import os 
import sqlite3


files = os.listdir("F:\\DegRepsHunter\\190316\\FOUND")
prepath="F:\\DegRepsHunter\\190316\\FOUND\\"

path3="RepsCount.txt"
reps3 = open(path3, "w")




for f in files:
    

    
    path = prepath+f

    print path

    con = sqlite3.connect(path)
   
    cur = con.cursor()


    q = ("SELECT * FROM repeats_gap WHERE length = (SELECT max(length) from repeats_gap)")
    cur.execute(q)
    of=cur.fetchall()
    maxlen=of[0][4]

    reps3.write ("%s;" % f)

    for rlen in range(10,maxlen+1):

        q = ("SELECT * FROM repeats_gap WHERE id_type=1 and length=%s" % rlen)
        cur.execute(q)
        of=cur.fetchall()
        dirc=len(of)
        reps3.write ("%s;%s;" % (rlen,dirc))


    reps3.write ("\n")

    con.close()