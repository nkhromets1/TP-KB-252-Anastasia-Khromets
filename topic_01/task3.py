def discriminant(a, b, c):
    result = b ** 2 - 4 * a * c
    return result
a = float (input("Enter a: "))
b = float (input("Enter b: "))
c = float (input("Enter c: "))
result = discriminant(a, b, c)
print("Discriminant =", result)
