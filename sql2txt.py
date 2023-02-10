import os
import sqlite3

fol = "FOUND3"

files=os.listdir(fol)
prepath=os.getcwd()+"/"+fol+"/"


outfol = fol + "_TXT" 


for f in files:
	print(f)
	path3 = outfol + '/' + f.replace(".sqlite",".csv")
	reps3 = open(path3, "w")
	reps3.write("first_start;second_start;length;id_type;first_seq;second_seq;alt_second_seq;errs\n")

	
	path = prepath+f
	con = sqlite3.connect(path)
	cur = con.cursor()
	cur.execute('SELECT * FROM repeats_gap')
	reps=cur.fetchall()
	
	for r in reps:
		#print(r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9])
		reps3.write("%s;%s;%s;%s;%s;%s;%s;%s\n" % (r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9]))
