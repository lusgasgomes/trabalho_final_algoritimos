tam_vetor = int(input('Digite o valor do tamanho do vetor: '))
vetor = []

objetivo = int(input('Digite um número objetivo: '))

for i in range(tam_vetor):
    nuns = int(input('Digite os valores do vetor: '))
    vetor.append(nuns)

pares = []

for i in range(len(vetor)):
    for j in range(i+1, len(vetor)):
        if vetor[i] + vetor[j]==objetivo:
            pares.append((vetor[i],vetor[j]))
    
if pares:
    print("Pares encontrados:")
    for par in pares:
        print(f'{par[0]} + {par[1]} = {objetivo}')
else:
    print("Nenhum par encontrado.")









