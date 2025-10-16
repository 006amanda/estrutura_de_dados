garagem = ["Carro1","Carro2","Carro3","Carro4","Carro5","Carro6","Carro7","Carro8","Carro9","Carro10","Carro11","Carro12","Carro13","Carro14","Carro15","Carro16","Carro17","Carro18","Carro19","Carro20"]

print("Garagem atual: ")
for carro in garagem:
    print("-> ", carro)
    print()

carro_desejado = input("Qual carro você deseja retirar? ")
print()

if carro_desejado not in garagem:
    print("Carro não encontrado")
else:
    retirados = []
    while True:
        topo = garagem.pop()
        retirados.append(topo)
        if topo == carro_desejado:
            break

    print("Carros retirados da garagem: ")
    for carro in retirados:
        print("->", carro)
        print()

    print("Garagem atualizada: ")
    for carro in garagem:
        print("-> ", carro)
        print()
