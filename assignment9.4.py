name = input("Enter file:")
handle = open(name)
lst=list()
emails=dict()
for line in handle:
    if len(line.split())>3 and line.startswith("From"):
        words=line.split()
        lst.append(words[1])
    else:
        continue
for email in lst:
	emails[email]=emails.get(email,0)+1
maxemail=None
maxnum=None
for k,v in emails.items():
    if maxnum is None or v>maxnum:
        maxemail=k
        maxnum=v
print(maxemail,maxnum)
    	
