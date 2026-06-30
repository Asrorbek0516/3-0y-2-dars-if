a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

if a<b and a<c:
    print(f"kichigi= {a}")
elif b<a and b<c:
    print(f"kichigi= {b}")
else:
    print(f"kichigi= {c}")