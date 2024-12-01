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
    
    #mudar
    palavraEscondida = ["_" for _ in palavraAleatoria]
    
    for traco in palavraEscondida: # printa a palavra escondida '_ _ _ _ _'
        print(traco, end=" ")
    print("")
    
    letrasTentadas = [] #Cria array
    
    while "_" in palavraEscondida: #O código abaixo vai rodar enquanto todas as letras não estiverem sido descobertas
        
        if erros < 5:
            
            print("_______________________________")
            print("Digite uma letra: ")
            letraDigitada = input().lower()
            
            if letraDigitada.isalpha() == False: # confere se e uma letra do alfabeto e nao numeros etc...
                print("A entrada deve ser somente letra, tente novamente!")
                continue
            
            if len(letraDigitada) > 1: # confere se e somente uma letra o chute da pessoa
                print("A entrada deve ser de somente 1 letra, tente novamente!")
                continue
              
            if letraDigitada in letrasTentadas: #Confere se a letra que ele escreveu não é uma repetida
                print("Você já tentou essa letra. Tente outra!")
                continue
            tentativas += 1
                       
            letrasTentadas.add(letraDigitada) #adiciona a letra na lista
            
            if letraDigitada in palavraAleatoria: #Se a letra estiver na palavra ele adiciona a letra no indice i da palavra escondida trocando o valor "_" pela letra
                print("\nA letra ", letraDigitada," esta na palavra! ")
                acertos += 1

                for indice, char in enumerate(palavraAleatoria): # troca o _ pela letra digitada na posicao certa
                    if char == letraDigitada:                    
                        palavraEscondida[indice] = letraDigitada 
                            
                for letra in palavraEscondida: # printa a palavra escondida '_ _ _ _ _'       
                    print(letra, end=" ") # end= " " printa um espaco a cada letra
                print("")             
            else:
                print("..............")
                print(f"A letra '{letraDigitada}' não está na palavra.")
                
                erros += 1
                
                print(f"Você tem {erros} erro(s) ")
                print("..............")
        else:
            print("Voce perdeu!")
            print("A palavra era ",palavraAleatoria)
            break
        
    if "_" not in palavraEscondida: #confere se a palavra realmente foi totalmente descoberto
        print("-------------------------------")
        print("Você ganhou! Parabéns")
        print("-------------------------------")
        
    razaoDeacertos = round((acertos/tentativas)*100, 2)
        
    if nomeDoJogador in ranking:
        ranking[nomeDoJogador]["acertos"] += acertos
        ranking[nomeDoJogador]["tentativas"] += tentativas

        razaoDeacertos = round((ranking[nomeDoJogador]["acertos"]/ranking[nomeDoJogador]["tentativas"])*100, 2)
        ranking[nomeDoJogador]["razao"] = razaoDeacertos
    else:
        ranking[nomeDoJogador] = {"acertos": acertos, "tentativas": tentativas, "razao": razaoDeacertos}

#ranking = {
    # jogador1: {acerto: 2, tentativas: 5, razao: 20}
    # jogador2: {acerto: 5, tentativas: 9, razao: x}
# }
      
def Ranking():
    #mudar 
    print("\n=== Ranking ===")
    ranking_completo = [] #Inicializa uma lista para colocar os itens
    
    for nome, valores in ranking.items(): #Coloca todos os itens na lista
        razao = valores["razao"]
        ranking_completo.append((nome, razao))

    ranking_ordenado = sorted(ranking_completo, key=lambda x: x[1], reverse=True) #ordena a lista de forma decrescente, pelo item 3 da tupla

    for i, (nome, razao) in enumerate(ranking_ordenado, start=1): #printa a lista em ordem, comecando pelo número 1
        print(i,"º lugar: ", nome, " - ",  razao,"% de acerto")


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
    if i == "1":
        Jogar()
    elif i == "2":
        Ranking()
    elif i == "3":
        AdicionarPalavra()
    elif i == "4":
        i = "4"
    else:
        print("Opção inexistente, tente novamente!\n")
    