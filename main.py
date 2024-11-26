import random
def Jogar():
    erros = 0
    print("Você escolheu jogar!\nDigite seu Nome: ")
    nomeDoJogador = input()
    
    with open("palavras.txt","r") as arquivo: #Abre o arquivo de texto onde tem as palavras e depis separa por espaço em branco as palavras em uma lista
        texto = arquivo.read()
        palavras = list(map(str,texto.split()))
    
    palavraAleatoria = random.choice(palavras)
    
    print(palavraAleatoria)

i = ""
while i != "4":
    print("\nDigite a opção desejada\n1 - Jogar\n2 - Ver Ranking\n3 - Adicionar palavra ao conjunto de palavras\n4 - sair")
    i = input()
    match i:
        case "1":
            Jogar()
        case "2":
            print("2")
        case "3":
            print("3")
        case "4":
            i = "4"
        case _:
            print("Opção inexistente, tente novamente!\n")
    
