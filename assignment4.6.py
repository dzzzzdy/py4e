def computepay(h, r):
    if h<=40:
        p=h*r
    else:
        p=40*r+(h-40)*r*1.5
    return p
hrs = input("Enter Hours:")
rate= input("Enter Rate:")
a=float(hrs)
b=float(rate)
p = computepay(a, b)
print("Pay", p)
