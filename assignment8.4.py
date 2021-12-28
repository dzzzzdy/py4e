fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words=line.rstrip().split()
    for word in words:
    	if word not in lst:
        	lst.append(word)
        else:
            continue
lst.sort()
print(lst)
