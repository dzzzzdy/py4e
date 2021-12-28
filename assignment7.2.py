fname = input("Enter file name: ")
fh = open(fname)
num=0
tol=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line)
    sl=line
    lnum=line.find(":")
    wnum=sl[lnum+1:]
    fnum=float(wnum)
    num=num+1
    tol=tol+fnum
print("Average spam confidence:",tol/num)
