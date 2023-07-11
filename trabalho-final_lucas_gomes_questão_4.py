from dataclasses import dataclass
@dataclass
class carros:
    id:str
    marca:str
    modelo:str
    preço:float

print(f'''-=-=-=-=-= Bem vindo a Tesla =-=-=-=-=-
      
    Aperte L para listar os veículos.
    Apert C para cadastrar algum veículo.
    Aperte T para alterar o valor do veículo.
    Aperte R para remover um veículo do sistema.
    Aperte S para sair do sistema.
      
{'-='*20}''')

veiculos = []

while True:
    opção = str(input('Digite a opção de sua preferência: '))

    if opção == 'C' or opção=='c':
        quant = int(input('Quantos carros você deseja cadastrar? '))
        for i in range(quant):
            id = str(input('ID do veículo: ')) 
            marca = str(input('Marca do veículo: ')) 
            modelo = str(input('Modelo do veículo: ')) 
            preço = float(input('Valor do veículo: ')) 

            carro = carros(id, marca, modelo, preço)
            veiculos.append(carro)

    elif opção =='L' or opção =='l':
        for carro in list(veiculos):
            print(f'ID - {carro.id}\n Marca - {carro.marca}\nModelo - {carro.modelo}\nPreço - R$ {carro.preço}')
    
    elif opção =='T' or opção =='t':
        alt_valor = str(input('Digite o id do veículo que deseja alterar o preço: '))
        novo_preço= float(input('Digite o preço atual: '))

        for carro in veiculos:
            if alt_valor == carro.id:
                carro.preço=novo_preço
                

    elif opção =='R' or opção =='r':
        excluir_veiculo = str(input('Digite o id do veículo que deseja remover: '))
        for carro in veiculos:
            if excluir_veiculo == carro.id:
                veiculos.remove(carro)

   
    elif opção =='S' or opção =='s':
        exit()
    
    else:
        print('opção inválida.')
    
        