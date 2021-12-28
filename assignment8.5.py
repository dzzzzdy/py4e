fname = input("Enter file name: ")
lst=list()
count=0
fhand=open(fname)
for line in fhand:
    line=line.rstrip()
    if len(line.split())<3 or not line.startswith("From"):
        continue
    else:
    	words=line.split()
        lst.append(words[1])
        count=count+1
for email in lst:
	print(email)
print("There were", count, "lines in the file with From as the first word")
