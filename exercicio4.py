from operator import itemgetter

lista = []

#funcao para cadastrar produtos
def cadastrar_produto(produto_para_cadastro: dict):
    lista.append(produto_para_cadastro)
    return
#variavel que recebe um numero inteiro
opcao = int(input('Cadastrar produto? 0 - Não    1 - Sim '))
while opcao == 1:
    novo_produto = {}

    novo_produto['codigo'] = int(input('Digite o codigo do produto: '))

    if novo_produto['codigo'] == 0:
        print('Codigo 0 , programa de cadastro encerrado. ')
        break

    novo_produto['estoque'] = int(input('Digite a quantidade em estoque: '))
    novo_produto['minimo'] = int(input('Digite a quantidade mínima do estoque: '))

#funcao recebe o parametro de cadastrar novo produto
    cadastrar_produto(novo_produto)
    opcao = int(input('Cadastrar produto? 0 - Não    1 - Sim '))

#funcao len que retorna o tamanho da lista
if len(lista) > 0:
    print('Lista de produto por codigo: ')
    print('Codigo'.center(10), end='')
    print('Estoque'.center(10), end='')
    print('Minimo'.center(10))

    for produto in sorted(lista, key=lambda item: item['codigo']):
        print(str(produto['codigo']).center(10), end='')
        print(str(produto['estoque']).center(10), end='')
        print(str(produto['minimo']).center(10))

else:
    print('Lista vazia.')


