# Leia um vetor de inteiros e mostre quantas vezes cada número aparece no vetor, sem repetir a contagem para o mesmo valor.

vetor = [2, 3, 2, 5, 3, 3, 6, 7, 8, 1, 9]
vistos = []

for i in range(len(vetor)):
    for numeroVisto in vistos:
        if numeroVisto == vetor[i]:
            break
    else:
        contador = 0
        for num in vetor:
            if num == vetor[i]:
                contador += 1
        print(vetor[i], "aparece", contador, "vez(es)")
        vistos.append(vetor[i])
      
