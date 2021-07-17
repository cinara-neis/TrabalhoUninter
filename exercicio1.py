#Escreva um programa que leia o nome de um aluno e sua nota final.
#
# Em seguida,
#informe o conceito conforme a tabela abaixo. A saída do programa deve exibir na tela uma
#frase com o padrão descrito a seguir:
#Nome do aluno: Fábio José
#Nota final: 3.5
#Frase a ser exibida: O aluno Fabio José tirou nota 3.5 e se enquadra no conceito D
continua = 0

continua = int(input("Inserir dados?  0 - Não   1 - Sim "))

while (continua == 1):
    nome_do_aluno = input("\nDigite o nome do aluno: ")
    nota_final = float(input("Digite a nota final do aluno: "))

    print("\nNome do aluno: "+nome_do_aluno)

    if (nota_final <= 0.0)  and (nota_final <=2.9):
        print("O aluno(a) {} tirou nota {} e se enquadra no conceito E".format(nome_do_aluno, nota_final))
    elif (nota_final <= 3.0) and (nota_final <= 4.9):
        print("O aluno(a) {} tirou nota {} e se enquadra no conceito D".format(nome_do_aluno, nota_final))
    elif (nota_final <= 5.0) and (nota_final <= 6.9):
        print("O aluno(a) {} tirou nota {} e se enquadra no conceito C".format(nome_do_aluno, nota_final))
    elif (nota_final <= 7.0) and (nota_final <= 8.9):
        print("O aluno(a) {} tirou nota {} e se enquadra no conceito B".format(nome_do_aluno, nota_final))
    else:
        print("O aluno(a) {} tirou nota {} e se enquadra no conceito A" .format(nome_do_aluno, nota_final))
    continua = int(input("\nInserir dados?  0 - Não   1 - Sim"))

if(continua == 0):
    print("\nPrograma finalizado!")