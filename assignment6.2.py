text = "X-DSPAM-Confidence:    0.8475"
atpo=text.find(":")
num=text[atpo+1:].strip()
fnum=float(num)
print(fnum)
