import random

doadores = []
#funcao para cadastrar doadores
def cadastrar_doadores(nome:str, doacao:float):
    doadores.extend( ((nome + ' ') * int(doacao//10)).split() )
#funcao de sorteio usando o random shuffle
def sortear_ganhador():
    random.shuffle(doadores)
    print(f'lista de doadores embaralhados: {doadores}\n ')
    return random.choice(doadores)

opcao = int(input('Cadastrar doador? 0 - Não    1 - Sim '))

while opcao == 1:
    doador = input('Nome do doador: ')
    valor = float(input('Valor doado: '))

#chamar o metodo strip para limpar os espaços em brancos
    while len(doador.strip()) == 0 or valor < 10:
        print('O nome é obrigatorio e o valor mínimo para doação é de R$ 10')
        doador = input('Nome do doador: ')
        valor = float(input('Valor doado: '))

    cadastrar_doadores(doador, valor)

    opcao = int(input('Cadastrar doador? 0 - Não   1 - Sim '))

#funcao len retorna o tamanho da lista
if len(doadores) > 0:
    print(f'Lista de doadores para sorteio: {doadores}\n ')
    print(f'O ganhador (a) foi: {sortear_ganhador()}')


