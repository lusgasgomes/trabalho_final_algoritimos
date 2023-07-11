
matriz_original = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]


matriz_resultado = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]


for i in range(3):
    for j in range(3):
        soma = 0
        for x in range(i+1):
            for y in range(j+1):
                soma += matriz_original[x][y]
        matriz_resultado[i][j] = soma


print("Matriz resultado:")
for linha in matriz_resultado:
    print(linha)
