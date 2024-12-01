import random
ranking = {}
def Jogar():
    erros = 0
    print("Você escolheu jogar!\nDigite seu Nome: ")
    nomeDoJogador = input().strip()
    tentativas = 0
    acertos = 0
    with open("palavras.txt","r") as arquivo: #Abre o arquivo de texto onde tem as palavras e depois separa por espaço em branco as palavras em uma lista
        texto = arquivo.read()
        palavras = list(map(str,texto.split()))
    
    palavraAleatoria = random.choice(palavras) #Cria uma lista de "_" para cada letra na palavra Aleatoria e printa a "palava escondida"
    palavraEscondida = ["_" for _ in palavraAleatoria] 
    
    for letra in palavraEscondida: # printa a palavra escondida '_ _ _ _ _'
        print(letra , end=" ")  
    print("")
    
    letrasTentadas = set() #Cria array
    
    while "_" in palavraEscondida: #O código abaixo vai rodar enquanto todas as letras não estiverem sido descobertas
        
        if erros < 5:
            
            print("_______________________________")
            print("Digite uma letra: ")
            letraDigitada = input().lower()
            
            if letraDigitada.isalpha() == False:
                print("A entrada deve ser somente letra, tente novamente!")
                continue
            
            if len(letraDigitada) > 1:
                print("A entrada deve ser de somente 1 letra, tente novamente!")
                continue
              
            if letraDigitada in letrasTentadas: #Confere se a letra que ele escreveu não é uma repetida
                print("Você já tentou essa letra. Tente outra!")
                continue
            tentativas += 1
                       
            letrasTentadas.add(letraDigitada)
            
            if letraDigitada in palavraAleatoria: #Se a letra estiver na palavra ele adiciona a letra no indice i da palavra escondida trocando o valor "_" pela letra
                print(f"\nA letra '{letraDigitada}' esta na palavra! ")
                acertos += 1
                
                for i, char in enumerate(palavraAleatoria):
                    if char == letraDigitada:
                        palavraEscondida[i] = letraDigitada
                            
                for letra in palavraEscondida: # printa a palavra escondida '_ _ _ _ _'       
                    print(letra, end=" ")  
                print("")  
                            
            else:
                print("..............")
                print(f"A letra '{letraDigitada}' não está na palavra.")
                
                erros += 1
                
                print(f"Você tem {erros} erro(s) ")
                print("..............")
        else:
            print("")
            print("Voce perdeu!")
            print(f"A palavra era {palavraAleatoria}")
            print("")
            break
        
    if "_" not in palavraEscondida:
        print("-------------------------------")
        print("Você ganhou! Parabéns")
        print("-------------------------------")
        
    razaoDeacertos = round((acertos/tentativas)*100, 2)
        
    if nomeDoJogador in ranking:
        ranking[nomeDoJogador]["acertos"] += acertos
        ranking[nomeDoJogador]["tentativas"] += tentativas
        ranking[nomeDoJogador]["razao"] += razaoDeacertos
    else:
        ranking[nomeDoJogador] = {"acertos": acertos, "tentativas": tentativas, "razao": razaoDeacertos}
    
                    
def Ranking():
    global ranking # acessa o dicionario ranking
    
    print("\n=== Ranking ===")
    
    ranking_completo = [] #Inicializa uma lista para colocar os itens
    
    for nome, valores in ranking.items(): #Coloca todos os itens na lista
        acertos = valores["acertos"]
        tentativas = valores["tentativas"]
        razao = valores["razao"]
        ranking_completo.append((nome, acertos, tentativas, razao))

    ranking_ordenado = sorted(ranking_completo, key=lambda x: x[3], reverse=True) #ordena a lista de forma decrescente, pelo item 3 da tupla

    for i, (nome, acertos, tentativas, razao) in enumerate(ranking_ordenado, start=1): #printa a lista em ordem, comecando pelo número 1
        print(f"{i}º lugar: {nome} -  {razao}% de acerto")


def AdicionarPalavra():
    with open("palavras.txt", "a") as arquivo: #Abre o arquivos de texto, em modo de "adicao"
        
        nova_palavra = input("Digite a nova palavra para adicionar: ").strip().lower()
        
        if nova_palavra.isalpha(): 
            arquivo.write("\n" + nova_palavra)
            print("Palavra adicionada com sucesso!")
        else:
            print("A palavra deve conter apenas letras!")


i = ""
while i != "4":
    print("\nDigite a opção desejada\n1 - Jogar\n2 - Ver Ranking\n3 - Adicionar palavra ao conjunto de palavras\n4 - sair")
    i = input()
    match i:
        case "1":
            Jogar()
        case "2":
            Ranking()
        case "3":
            AdicionarPalavra()
        case "4":
            i = "4"
        case _:
            print("Opção inexistente, tente novamente!\n")
    