a = int(input("nhap gia tri a: "))
b = int(input("nhap gia tri b: "))
c = int(input("nhap gia tri c: "))

delta = b^2 - 4*a*c

if delta < 0:
    print("no solution")
elif delta == 0:
    x = -b/(2*a)
    print("1 solution, x=", x)
else:
    x1 = (-b + delta_sqrt) / a_2
    x2 = (-b - delta_sqrt) / a_2
    print("2 solution, x1, ")