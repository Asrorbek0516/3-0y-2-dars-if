a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

yigindi_ab = a+b
yigindi_ac = a+c
yigindi_bc = b+c

if yigindi_ab >= yigindi_ac and yigindi_ab >= yigindi_bc:
    print(f"yigindisi katta sonlar: {a} va {b} yigindi: {yigindi_ab}")
elif yigindi_ac >= yigindi_ab and yigindi_ac >= yigindi_bc:
    print(f"yigindisi katta sonlar: {a} va {c} yigindi: {yigindi_ac}")
else:
    print(f"yigindisi katta sonlar: {c} va {b} yigindi: {yigindi_bc}")