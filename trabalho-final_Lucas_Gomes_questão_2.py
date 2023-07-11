n = int(input("Digite o tamanho da matriz: "))

matriz = [[0] * n for _ in range(n)]

num = 1  
linha, coluna = 0, 0  


cima, baixo = 0, n - 1
esquerda, direita = 0, n - 1

direcão = 0  

while num <= n * n:
   
    if direcão == 0:
        while coluna <= direita:
            matriz[linha][coluna] = num
            coluna += 1
            num += 1
        coluna -= 1
        cima += 1
        linha += 1
    
    elif direcão == 1:
        while linha <= baixo:
            matriz[linha][coluna] = num
            linha += 1
            num += 1
        linha -= 1
        direita -= 1
        coluna -= 1
   
    elif direcão == 2:
        while coluna >= esquerda:
            matriz[linha][coluna] = num
            coluna -= 1
            num += 1
        coluna += 1
        baixo -= 1
        linha -= 1
    
    elif direcão == 3:
        while linha >= cima:
            matriz[linha][coluna] = num
            linha -= 1
            num += 1
        linha += 1
        esquerda += 1
        coluna += 1
    
    direcão = (direcão + 1) % 4  


print("Matriz NxN, onde N = {}: ".format(n))
for linha in matriz:
    print(f'[{linha}]')
