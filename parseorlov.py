#!/home/aragret/anaconda3/bin/python
import re

def extract_patterns(species):
	repeats = []
	with open('{0}.input.out4out'.format(species)) as file:
		for line in file:
			if re.search('(\d+\s){4}([atgc]+\s){1,2}', line) != None:
				repeats.append(line.split('\t'))
	return repeats

def match_search(repeats_list):
	direct = []
	symm = []
	compl = []
	inv = []
	for x in repeats_list:
		if x[3] == 1:
			direct.append(x[4])
		elif x[3] == 4:
			inv.append(x[4])
		elif x[3] == 2:
			symm.append(x[4])
		elif x[3] == 3:
			compl.append(x[4])
	match = set(direct).intersection(set(inv), set(symm), set(compl))
	return match

# def repeats_table(species, repeats_list):
# 	with open('01_{0}.txt'.format(species), 'w') as outfile:
# 		outfile.write('RepeatType\tArm1\tArm2\tStartOfFirstArm\tStartOfSecondArm\n')
# 		for x in repeats_list:
# 			if x[3] == '1':
# 				outfile.write('dir\t{0}\t{1}\t{2}\t{3}\n'.format(x[4], x[5], x[0], x[1]))
# 			elif x[3] == '2':
# 				outfile.write('symm\t{0}\t{1}\t{2}\t{3}\n'.format(x[4], x[5], x[0], x[1]))
# 			elif x[3] == '3':
# 				outfile.write('compl\t{0}\t{1}\t{2}\t{3}\n'.format(x[4], x[5], x[0], x[1]))
# 			elif x[3] == '4':
# 				outfile.write('inv\t{0}\t{1}\t{2}\t{3}\n'.format(x[4], x[5], x[0], x[1]))

def common_table(species, repeats_list):
	endfile.write('Species\tRepeatType\tArm1\tArm2\tStartOfFirstArm\tStartOfSecondArm\n')
	for x in repeats_list:
		if x[3] == '1':
			endfile.write('{0}\tdir\t{1}\t{2}\t{3}\t{4}\n'.format(species, x[4], x[5], x[0], x[1]))
		elif x[3] == '2':
			endfile.write('{0}\tsymm\t{1}\t{2}\t{3}\t{4}\n'.format(species, x[4], x[5], x[0], x[1]))
		elif x[3] == '3':
			endfile.write('{0}\tcompl\t{1}\t{2}\t{3}\t{4}\n'.format(species, x[4], x[5], x[0], x[1]))
		elif x[3] == '4':
			endfile.write('{0}\tinv\t{1}\t{2}\t{3}\t{4}\n'.format(species, x[4], x[5], x[0], x[1]))


# with open('../species.txt') as infile, open('01_common_patterns_txt', 'w') as outfile:
# 	for line in infile:
# 		a = match_search(extract_patterns(line.strip()))
# 		if len(a) != 0:
# 			outfile.write('{0}\t{1}\n'.format(line.strip(), len(a)))

# repeats_table('Abramis_brama', extract_patterns('Abramis_brama'))


with open('../species.txt', 'r') as infile, open('../all_repeats.txt', 'w') as endfile:
	endfile.write('Species\tRepeatType\tArm1\tArm2\tStartOfFirstArm\tStartOfSecondArm\n')
	for line in infile:
		repeats_list = extract_patterns(line.strip())
		for x in repeats_list:
			if x[3] == '1':
				endfile.write('{0}\tdir\t{1}\t{2}\t{3}\t{4}\n'.format(line.strip(), x[4], x[5], x[0], x[1]))
			elif x[3] == '2':
				endfile.write('{0}\tsymm\t{1}\t{2}\t{3}\t{4}\n'.format(line.strip(), x[4], x[5], x[0], x[1]))
			elif x[3] == '3':
				endfile.write('{0}\tcompl\t{1}\t{2}\t{3}\t{4}\n'.format(line.strip(), x[4], x[5], x[0], x[1]))
			elif x[3] == '4':
				endfile.write('{0}\tinv\t{1}\t{2}\t{3}\t{4}\n'.format(line.strip(), x[4], x[5], x[0], x[1]))
