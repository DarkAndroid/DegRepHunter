#coding=utf8


# 20230207: Fix it for work




# Importing of libraries
import time
import timeit
import os
import sqlite3
import sys

try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3



folder = "BATS_REP"

files=os.listdir(folder)
prepath=os.getcwd()+"/" + folder + "/"



# Consistent work with a repeats database for each genome
for f in files:
    print(f)
    # The path to DB
    path = prepath+f
    # Connection to DB
    con = sqlite3.connect(path)
    cur = con.cursor()
    # Receiving of name of species from DB filename 
    fname = f[:-7].split("_")
    lname= fname[1]
    for fn in fname[2:]:
        lname=lname+"_"+fn
    #print(lname)   
    n=0



    cur.execute('SELECT * FROM repeats_gap')
    reps=cur.fetchall()
    len(reps)
    for r in reps:
        #print("%s\r" % r[0]),
        q = ("SELECT * FROM repeats_gap WHERE length<%s AND first_start>=%s AND first_start<=%s AND first_start+length-1>=%s AND first_start+length-1<=%s AND second_start>=%s AND second_start<=%s AND second_start+length-1>=%s AND second_start+length-1<=%s AND id!=%s" % (r[4], r[2], r[2]+r[4], r[2], r[2]+r[4], r[3], r[3]+r[4], r[3], r[3]+r[4],  r[0]))
        cur.execute(q)
        of=cur.fetchall() 
        if len(of)!=0:
            for i in of:
                q = ("DELETE FROM repeats_gap WHERE id=%s" % (i[0]))
                cur.execute(q)
    con.commit()


    con.close()