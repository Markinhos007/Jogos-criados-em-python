import random
nu1=random.randrange(1,10)
nu2=random.randrange(1,10)
nu3=random.randrange(1,10)
nu4=random.randrange(1,10)
matriz=[
        [nu1,nu2],
        [nu3,nu4]
        ]

jogar = True
while (jogar):
    print('''--Jogo Matemático--
    1-Como Jogar ?
    2-Créditos do criador
    3-Jogar''')
    op=int(input("Escolha a opção que você deseja:"))
    if op==1:
        print("==INSTRUÇÕES==")
        print("O jogo tem o objetivo de incentivar o jogador a exercitar seu cérebro")
        print("1º-Some todos os números dentro da matriz")
        print("2º-Digite o resultado da soma de todos os números dentro da matriz")
        op=input("Voltar para o menu(escreva OK):")
    elif op==2:
        print("==CRÉDITOS AO CRIADOR==")
        print("Está aba foi criada com o intuito de dar os créditos ao criador deste programa(Markos Samuell).\n Que projetou este sistema com a finalidade de criar um jogo simples para as crianças aprenderem matemática de forma interativa.\nSendo projetado este sistema aos cargos do SENAI-CTTI")
        op=input("Voltar para o menu(escreva OK)")  
    elif op==3:
        print("Matriz(2x2)")
        for i in matriz:
            print(i)
        soma_matrizes=nu1+nu2+nu3+nu4
        print("Seja bem vindo ao JOGO MATEMÁTICO")
        resul=int(input("Digite o resultado da soma de todos os números dentro da matriz:"))
        if resul!=soma_matrizes:
            print("Resultado digitado esta errado :(")
            print(f"O resultado verdadeiro é {soma_matrizes}")
            print("Obrigado por jogar !!")
            print("Programa Finalizado")
            break
        else:
            print("Parabéns,você acertou :)")
            print("Obrigado por jogar !!")
            print("Programa Finalizado")
            break
    else:
        jogar=False
        print("Número digitado inválido\nPrograma encerrado")














            
    
