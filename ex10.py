def is_prime(n):
    if n< 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True 
def goldbach(n):
    for p in range(2, n // 2 + 1):
        if is_prime(p) and is_prime(n-p):
            return (p, n - p)
    return None

#(b)
print("Prime below 50: ", end= " ")
for n in range (2, 50):
    if is_prime(n):
        print(n, end=" ")
print()
count = 0
for n in range (2, 100):
    if is_prime(n):
        count += 1
print("Number of primes below 100: ", count)

#(c)
for n in range(4, 31, 2):
    p, q = goldbach(n)
    print(f"{n} = {p} + {q}")

#(d)
holds = True
for n in  range(4, 10001, 2):
    if goldbach(n) is None:
        holds = False
        break 
print("Goldbach holds for every even numbers from 4 to 10000: ", holds)