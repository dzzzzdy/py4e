name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lst=list()
hr=dict()
for line in handle:
    if len(line.split())>3 and line.startswith("From"):
        words=line.split()
        time=words[5]
        hours=time.split(":")
        lst.append(hours[0])
    else:
        continue
for hour in lst:
    hr[hour]=hr.get(hour,0)+1
for key,value in sorted(hr.items()):
    print(key,value)
