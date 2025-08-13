# Preencha um vetor com números inteiros e crie outro vetor contendo apenas os números primos encontrados.

numeros = [3, 4, 5, 10, 11, 15, 17, 22, 18, 1, 7, 111]
primos = []

for numero in numeros:
    primo = 1
    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                primo = 0
                break
        if primo == 1:
            primos.append(numero)

print("Lista original: ", numeros)
print("Números primos: ", primos)
