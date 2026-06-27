a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

if a>b and a>c:
    print(f"kattasi= {a}")
elif b>a and b>c:
    print(f"kattasi= {b}")
else:
    print(f"kattasi= {c}")