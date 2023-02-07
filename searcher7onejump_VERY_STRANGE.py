# BRANCH_UPDATE

#coding=utf8

import time
import timeit
import os
import sqlite3

pgen_path = 'genomes.fa'
pgen = open(pgen_path,'r')
nucAlphabet = {'a', 't', 'g', 'c', 'x'}


def zeros(shape):
    retval = []
    for x in range(shape[0]):
        retval.append([])
        for y in range(shape[1]):
            retval[-1].append(0)
    return retval


def extractWordsTen(s, alphabet):
    arr = []
    n=10
    for i in range(len(s)-n+1):
        arr.append(''.join(s[i:i+n]))
    return arr


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
         
    def __exit__(self, type, value, traceback):
        print "Elapsed time: {:.3f} sec".format(time.time() - self._startTime)



def twbethamaster(rtype, betha):
    if rtype==1:
        twbetha=betha
    elif rtype==2:
        twbetha=compmaster(betha)  
    elif rtype==3:
        twbetha=polimaster(betha)
    elif rtype==4:
        twbetha=invertmaster(betha)
    return twbetha




def lev(s, t):
    if s == t: return 0
    elif len(s) == 0: return len(t)
    elif len(t) == 0: return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]
    return v1[len(t)]



















def  match_check (words,invert,score,oi,oj,i,j,e,reptype,origlen):
    lengthj=len(score[oi])
    lengthi=len(score)
    match=1
    dmatch=e
    #for k in range(1, 10-dmatch):
    itera=0
    bitera=0
    while True:
        #if oi==3 and (oj==5992 or oj==14883):
        #    print itera
        #if oi==0:
        #    print "LOOP"
        #    print genome[oi:oi+itera+1]
            

        ci=i+itera
        cj=j+itera  
        
        if i+itera >= j:
            if bitera!=0:
                for d in range(0,bitera):
                    score[i+d][j+d]=5     
                q = "INSERT INTO repeats (id,first_start, second_start, length, id_type, first_seq, second_seq, alt_second_seq, errs, degen) VALUES(NULL,?,?,?,?,?,?,?,?,?)"
                cur.execute(q,(boi,bpoint,blength,breptype,balpha,bbetha, btwbetha, berrs, bdegen))
                return 1

            else:
                return 0

        if invert:  # VVVVVVVVVVVVvVVV
            point=lengthj-oj-11  # VVVVVVVVVVVVvVVV
        else:  # VVVVVVVVVVVVvVVV
            point=oj  # VVVVVVVVVVVVvVVV
        if point>origlen-1:  # VVVVVVVVVVVVvVVV
            point=point-origlen   # VVVVVVVVVVVVvVVV
        if oi>origlen-1:   # VVVVVVVVVVVVvVVV
            oi=oi-origlen  # VVVVVVVVVVVVvVVV

        if ((ci>(lengthi-1)) or (cj>(lengthj-1))):          
                return 0



        if score[ci][cj]==10:   
            match=match+1  # VVVVVVVVVVVVvVVV

            
            #if oi==0:
                #print genome[ci]
                #print genome[cj]

                #print oi 
                #print point
                #print match
                #print "Match"  +genome[ci]+genome[cj]



        elif itera>9:
            #if oi==3 and (oj==5992 or oj==14883):   
            #    print "DisMatch 888"     
            alpha=genome[oi:oi+itera]
            betha=genome[point:point+itera]

            twbetha=twbethamaster(reptype,betha)     
            errs=lev(alpha,twbetha)
            length=len(alpha)
            degen = float ( float(errs) / float(length) )
            #if oi==3 and (oj==5992 or oj==14883):
            #if oi==0: 
            #    print oi 
            #    print point
            #    print itera
            #    print alpha
            #    print twbetha
            #    print betha
            #    print degen   
            #    input("stop")         
            if degen>0.4:
                #if oi==3 and (oj==5992 or oj==14883):
                #    print "OVER"
                #    print bitera
                if bitera!=0:
                    for d in range(0,bitera):
                        score[i+d][j+d]=5
                    #if oi==3 and (oj==5992 or oj==14883):
                    #    print "INSERTs"     
                    q = "INSERT INTO repeats (id,first_start, second_start, length, id_type, first_seq, second_seq, alt_second_seq, errs, degen) VALUES(NULL,?,?,?,?,?,?,?,?,?)"
                    cur.execute(q,(boi,bpoint,blength,breptype,balpha,bbetha, btwbetha, berrs, bdegen))
                    return 1

                else:
                    return 0

            elif degen<=0.2:
            	#if oi==3 and (oj==5992 or oj==14883):
            	#	print "GOOD"
        
                bitera=itera
                boi=oi
                bpoint=point
                blength=length
                breptype=reptype
                balpha=alpha
                bbetha=betha
                btwbetha=twbetha
                berrs=errs
                bdegen=degen

        else:         
            #if oi==3 and (oj==5992 or oj==14883):
            dmatch=dmatch+1

            #if oi==0:
                #print genome[ci]
                #print genome[cj]

                #print oi 
                #print point
                #print dmatch
                #print "DisMatch"    +genome[ci]+genome[cj]      

            if (dmatch>3) :   
                #if oi==0:
                #    print "RETURN"         
                return 0
        itera+=1
        #if oi==3 and (oj==5992 or oj==14883):
        #	input()
    


    '''   WTF ?????????????????????????
    if (match>8): #######################################
        if invert:
            point=lengthj-oj-11
        else:
            point=oj
        if point>origlen-1:
            point=point-origlen   
        if oi>origlen-1:
            oi=oi-origlen
        q = "INSERT INTO repeats (first_start, second_start, length, id_type, first_seq, second_seq) VALUES(?,?,?,?,?,?)"
        cur.execute(q,(oi,point,10,reptype,words[oi],words[point]))
        return 1
    else:
    	return 0
    '''




def master (seq1, seq2, invert,reptype,origlen):
    seq2=seq2.replace("X","N")  
    m, n = len(seq1), len(seq2)
    words=extractWordsTen(seq1, nucAlphabet)
    score = zeros((m+1, n+1))   
    if invert:
        print "matching invert"
        for i in range(0, m):       
            print("%s\r" % i),
            for j in range(0, m-i+10 +1):
                if j<m:
                    if seq1[i] == seq2[j]:
                        score[i][j]=10
        print "checking invert"
        lengthj=len(score[i])
        lengthi=len(score)
        for i in range(0, m):
            print("%s\r" % i),
            for j in range(1, m-i-9):
                if j<m:
                    if score[i][j]==10: 
                        match_check(words,invert,score,i,j,i,j,0,reptype,origlen)        
                    #elif score[i+1][j+1]==10:
                        #match_check(words,invert,score,i,j,i+1,j+1,1,reptype,origlen)

    else:             
        print "matching"
        for i in range(0, m):       
            print("%s\r" % i),
            for j in range(i+10, n):
                if seq1[i] == seq2[j]:
                    score[i][j]=10   
        print "checking"
        lengthj=len(score[i])
        lengthi=len(score)
        for i in range(0, m-10  +1):
            print("%s\r" % i),
            for j in range(i+10, n-10):
                if score[i][j]==10: 
                    match_check(words,invert,score,i,j,i,j,0,reptype,origlen)
                #elif score[i+1][j+1]==10:
                    #match_check(words,invert,score,i,j,i+1,j+1,1,reptype,origlen)  

    






def compmaster (seq1):     
    arr1=[]
    s2=""
    for char in seq1:
        if char=='A':
            arr1.append('T')
        elif char=='T':
            arr1.append('A')
        elif char=='G':
            arr1.append('C')
        elif char=='C':
            arr1.append('G')
        else:
            arr1.append('N')
    s2=(''.join(arr1))
    return s2

# Receiving of sequense that mirror to given one
def polimaster (seq1):
    arr2=[]
    s3=""
    for char in seq1:
        arr2.append(char)
    s3=(''.join(reversed(arr2)))
    return s3

# Receiving of sequense that inverted to given one
def invertmaster (seq1):  
    arr1=[]
    s2=""
    for char in seq1:   
        if char=='A':
            arr1.append('T')
        elif char=='T':
            arr1.append('A')
        elif char=='G':
            arr1.append('C')
        elif char=='C':
            arr1.append('G')
        else:
            arr1.append('N')
    arr3=reversed(arr1)
    s4=""
    s4=(''.join(arr3))
    return s4

    



def mastercomp (seq1, seq2,origlen):

    reptype=2
        
    print "\nCompliment:"

    arr1=[]
    s2=""

    for char in seq1:
        
        if char=='A':
            arr1.append('T') 
        elif char=='T':
            arr1.append('A')
        elif char=='G':
            arr1.append('C')
        elif char=='C':
            arr1.append('G')
        else:
            arr1.append('N')

    s2=(''.join(arr1))


    master (seq1, s2,False,reptype,origlen)

def masterpoli (seq1, seq2,origlen):

    reptype=3
        
    print "\nPolindrom:"

    arr2=[]
    s3=""

    for char in seq1:

        arr2.append(char)

    s3=(''.join(reversed(arr2)))
    
    
    master (seq1, s3,True,reptype,origlen)

def masterinvert (seq1, seq2,origlen):

    reptype=4
    
    print "\nInvert:"    

    arr1=[]
    s2=""




    for char in seq1:
        
        if char=='A':
            arr1.append('T')
        elif char=='T':
            arr1.append('A')
        elif char=='G':
            arr1.append('C')
        elif char=='C':
            arr1.append('G')
        else:
            arr1.append('N')

    arr3=reversed(arr1)
    s4=""

    s4=(''.join(arr3))
    

    master (seq1, s4,True,reptype,origlen)





pr=1


while True:

    name = pgen.readline()[1:-1]
    genome = pgen.readline()
    length=len(genome)



    genome=genome[:-1]+genome[:10]





    if ((pr>316) and (pr<318)) or ((pr>439) and (pr<441)):


        con = sqlite3.connect('%s_%s.sqlite' % (pr,name))

        cur = con.cursor()

        cur.execute('CREATE TABLE species (id INTEGER PRIMARY KEY, name VARCHAR(100))')
        con.commit()

        cur.execute('CREATE TABLE repeats (id INTEGER PRIMARY KEY, spece_id INTEGER, first_start INTEGER, second_start INTEGER, length INTEGER, id_type INTEGER, first_seq VARCHAR(5000), second_seq VARCHAR(5000), alt_second_seq VARCHAR(5000), errs INTEGER, degen FLOAT)')
        con.commit()

        reptype=1

       
        q = "INSERT INTO species (id, name) VALUES(NULL, \""+name+"\")"
        cur.execute(q)

    	with Profiler() as p:
            
            
            with Profiler() as a:
                
                print "\nSuper direct  for "+name+":"
                
         
                master(genome,genome,False,1,length)
                con.commit()

                



    
        
            with Profiler() as b:
               
                print "\nSuper compliment for "+name+":"
                
                mastercomp(genome,genome,length)
                con.commit()

                
            
            

    
        
            with Profiler() as c:
              
                print "\nSuper polindrom  for "+name+":"
               
                masterpoli(genome,genome,length)
                con.commit()



            

    
        
            with Profiler() as d:

                print "\nSuper invert  for "+name+":"
                
                masterinvert(genome,genome,length)
                con.commit()

                
        

            print "\nSuper all for "+name+":"
            



        con.commit()



    pr=pr+1

    if pr>3954:
	    break