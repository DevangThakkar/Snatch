string = []
with open('CSW15.txt','r') as f:
	for lines in f:
		string.append(lines.strip().rstrip())
with open('temp.txt','w') as f:
	f.write("{")
	for i in string:
		f.write("'"+i+"', ")