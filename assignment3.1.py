hrs = input("Enter Hours:")
rate= input("Enter rate:")
h = float(hrs)
r=float(rate)
if h<=40:
    print(r*h)
else:
    print(40*r+1.5*(h-40)*r)
