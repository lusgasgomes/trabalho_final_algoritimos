from dataclasses import dataclass
@dataclass
class Pacientes:
    id:str
    nome:str
    doença:str
    idade:int

print(f'''-=-=-=-=-= Bem vindo ao Hospital municipal =-=-=-=-=-
      
    Aperte L para listar os pacientes.
    Apert C para cadastrar algum paciente.
    Aperte T para alterar a doença do paciente.
    Aperte R para remover um paciente do sistema.
    Aperte M para ver a média das idades dos pacientes. 
    Aperte S para sair do sistema.
      
{'-='*20}''')

pacientes = []

while True:
    opção = str(input('Digite a opção de sua preferência: '))

    if opção == 'C' or opção=='c':
        quant = int(input('Quantos pacientes você deseja cadastrar? '))
        for i in range(quant):
            id = str(input('ID do paciente: ')) 
            nome = str(input('Nome: ')) 
            doença = str(input('Doença: ')) 
            idade = int(input('Idade: ')) 

            paciente = Pacientes(id, nome, doença, idade)
            pacientes.append(paciente)

    elif opção =='L' or opção =='l':
        for paciente in list(pacientes):
            print(f'ID - {paciente.id}\n Nome - {paciente.nome}\nDoença - {paciente.doença}\nIdade {paciente.idade} anos')
    
    elif opção =='T' or opção =='t':
        alt_doença = str(input('Digite o id do paciente que deseja alterar a doença: '))
        nova_doença= str(input('Digite a doença atual: '))

        for paciente in pacientes:
            if alt_doença == paciente.id:
                paciente.doença=nova_doença
                

    elif opção =='R' or opção =='r':
        excluir_paciente = str(input('Digite o id do paciente que deseja remover: '))
        for paciente in pacientes:
            if excluir_paciente == paciente.id:
                pacientes.remove(paciente)

    
    elif opção =='M' or opção =='m':
        soma_idades = sum([paciente.idade for paciente in pacientes])
        quant_pacientes = len([paciente.idade for paciente in pacientes])
        if quant_pacientes > 0:
            media = soma_idades/quant_pacientes
            print('Média das idades - {:.1f}'.format(media))

   
    elif opção =='S' or opção =='s':
        exit()
    
    else:
        print('opção inválida.')
