def isPrime(num): #Простое число
    if num < 4:
        return True
    for x in range(2, int(num / 2) + 1):
        if num % x is 0:
            return False
    return True

def isPrimeRoot(g, p): #Первообразный корень
    if g ** (p - 1) % p != 1:
        return False
    for L in range(1, p - 2):
        if g ** L % p == 1:
            return False
    return True

def isCoprime(first, second): #Взаимно простые числа
    max = first if (first <= first) else first
    if first == second:
        return False
    elif max < 4:
        return True
    for x in range(2, int(max / 2) + 1):
        if first % x == 0 and second % x == 0:
            return False
    return True

p = int(input("p: "))
while not isPrime(p):
    p = int(input("P: "))

g = int(input("g: "))
while not isPrime(g) or not isPrimeRoot(g, p):
    if not isPrime(g):
        g = int(input("g: "))
    else:
        g = int(input("g: "))

x = int(input("x: "))
while x < 2 or x > p - 2:
    x = int(input("x: "))

y = g ** x % p
print(f"y = {y}")

print(f"OpenKey (p, g, y) ({p}, {g}, {y})")
print(f"Closedkey {x}")

m = int(input("msg: "))
while m < 0 or m > p - 1:
    m = int(input("msg: "))

k = int(input("k: "))
while k < 2 or k > p - 2 or not isCoprime(k, p - 1):
    if k < 2 or k > p - 2:
        k = int(input("k: "))
    else:
        k = int(input("k: "))

a = g ** k % p
d = (y ** k) * m % p
b =  ((m - x * a) * k) % (p - 1)

print(f"Ciphertext: ({a}, {d})")

solution = (d * (a ** x) ** (p - 2)) % p
print(f"Decrypted: {solution}")
print()

print(f"DigSign: ({a}, {b})")

q = (y ** a) * (a ** b) % p
w = (g ** m) % p

print(f"EXX: ({q}, {w})")