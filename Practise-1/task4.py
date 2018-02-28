A = 1  # int(input("enter A "))
B = 2  # int(input("enter B "))
C = 3  # int(input("enter C "))
result = 10  # int(input("enter result "))
x = 1
y = 1
z = 1
print("Уравнение:")
print("%dx + %dy + %dz = %d" % (A, B, C, result))
i = 1
while x <= 10:
    while y <= 10:
        while z <= 10:
            if (x * A + y * B + z * C) == 10:
                print("набор %d: %d %d %d" % (i, x, y, z))
                i += 1
            z += 1
        y += 1
        z = 1
    y = 1
    x += 1
