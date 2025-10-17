def somaImpares(n):
    if n == 0:
        return n

    if n % 2 != 0:
        return n + somaImpares(n - 1)
    else:
        return somaImpares(n - 1)

print("Soma dos ímpares: ", somaImpares(10))
