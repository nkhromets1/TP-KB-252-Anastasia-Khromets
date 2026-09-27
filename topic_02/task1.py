def discriminant(a, b, c):
    result = b**2 - 4*a*c
    return result 

def roots(a, b, c):
    d = discriminant(a, b, c)

    if d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        print("x1=", x1)
        print("x2=", x2)

    elif d == 0:
        x = -b / (2*a)
        print("x=", x)

    else:
        print("No real roots")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

roots(a, b, c)