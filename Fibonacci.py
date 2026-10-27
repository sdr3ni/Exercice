def fibonacci(n):
    if n < 1:
        return "ERREUR : n doit être supérieur à 1"
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
        return b 

test = [1, 2, 3, 4, 5, 6]

for val in test:
    res = fibonacci(val)
    print(f"Entre (n) = {val} -> {res}")
