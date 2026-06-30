a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

if a>b>c or a<b<c:
    print(f"o'rtachasi: {b}")
elif b>a>c or b<a<c:
    print(f"ortachasi: {a}")
else:
    print(f"ortachasi: {c}")