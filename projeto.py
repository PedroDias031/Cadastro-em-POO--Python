#============================================================================================================
#                               Area de modelagem do objeto
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def __repr__(self):
        print('BANCO DE DADOS DOS USUARIOS')
        return f'NOME: {self.nome} | IDADE: {self.idade} | CPF: {self.cpf}'
#======================================================================================================  
#                          Area de criação de funções para o objeto
def adicionar():
    while True:
        user_name = input('Digite o seu nome: ').upper()
        if user_name.isalpha():
            print('Nome salvo com sucesso!')
            break
        else:
            print('Por favor informe um nome e não um numero!')
    
    while True:
        user_id = int(input('Digite a sua idade: '))
        if user_id <= 0:
            print('Informe uma idade valida acima de 0...')
        else:
            print(' Idade salva com sucesso!')
            break

    while True:
        user_cpf = (input('Digite o seu CPF: '))

        if user_cpf.isalpha():
             print('Isso não e um CPF!')
        else:
            if len(user_cpf) != 11:
                print('O seu CPF deve conter 11 digitos...')
            if len(user_cpf) == 11:
                print('CPF salvo com sucesso!')
                break
    
    return Pessoa(user_name,user_id,user_cpf)
        



#=====================================================================================================
#                           Corpo do codigo que vai chamar a função
user_list = []

print('-'*50)
print('SEJA BEM VINDO AO SISTEMA DE CADASTROS!')
print('='*50)
print('POR FAVOR INFORME OS PRIMEIROS DADO PARA COMEÇAR...')


while True: 

    usuario = adicionar()
    user_list.append(usuario)
    continuar = input('Deseja continuar?\n  ( s | n ):').lower()
    if continuar in ('s' , 'n'):
        continuar != 's'
        print('Informe o proximo cadastro')
    else:
        print('Informe apenas s | n ')
    if continuar =='n':
        print('Cadastro finalizado')
        break


print('Dados da lista')
for pessoa in user_list:
    print(pessoa)
        