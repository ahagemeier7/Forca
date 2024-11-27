import random
def Jogar():
    erros = 0
    print("Você escolheu jogar!\nDigite seu Nome: ")
    nomeDoJogador = input()
    
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
            
            print("Digite uma letra: ")
            letraDigitada = input()
            if len(letraDigitada) > 1:
                print("A entrada deve ser de somente 1 letra, tente novamente!")
                continue
                
            if letraDigitada in letrasTentadas: #Confere se a letra que ele escreveu não é uma repetida
                print("Você já tentou essa letra. Tente outra!")
                continue
                        
            letrasTentadas.add(letraDigitada)
            if letraDigitada in palavraAleatoria: #Se a letra estiver na palavra ele adiciona a letra no indice i da palavra escondida trocando o valor "_" pela letra
                print(f"A letra '{letraDigitada}' esta na palavra! ")
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
    
