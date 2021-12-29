import re
name = input("Enter file:")
handle = open(name)
content=handle.read()
y=re.findall("[0-9]+",content)
#print(y)
sum=0
for number in y:
    num=int(number)
    sum=sum+num
print(sum)
