# READ POW files

def readPowFile(path):
	infile = open(path)
	days = []
	T = []
	name = ''
	vals = []
	for line in infile:
		data = line.strip().split()
		if len(data) > 0 and '!' in data[0]:
			if len(days)>0:
				vals.append([name, days, T])
				#print 'appended'+name
			
			name = data[1]
			for i in range(2, len(data)):
				name += '_'
				name += data[i]			
			days = []
			T = []
		elif len(data)> 0 and '#' in data[0]:
			pass
		elif 'END' in data[0]:
			pass
		else:
			days.append(float(data[0]))
			T.append(float(data[1]))
	vals.append([name, days, T])		
			
	infile.close()
	return vals
