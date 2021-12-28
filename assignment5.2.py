largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum=float(num)
    except:
        print("Invalid input")
    if largest is None or fnum>largest:
        largest=fnum
    elif smallest is None or fnum<smallest:
        smallest=fnum
    else:
        continue
print("Maximum is", int(largest))
print("Minimum is",int(smallest))
