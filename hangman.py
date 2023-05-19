from random import *
print("###HANGMAN GAME###")
nome = input("Qual é o seu nome? ")
print(f"Ok {nome} vamos começar!")
palavras = ["python", "apartamento", "geladeira", "yejin", "advogada", "marina"]
resposta = choice(palavras)
vida = 7
while vida != 0:
    succeed = True
    print()
    for a in resposta:
        if a in palavras:
            print(a, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()
    if succeed:
        print("Success")
        break
    letter = input("Digite uma letra (nâo tem letra maiúscula) ")
    if letter not in palavras:
       palavras += letter
    if letter in resposta:
        print("Parabéns! Você acertou!")

    else:
        print("Ixi você errou :( ")
        vida -= 1
        print(f"Sua vida é {vida}")
if vida == 0:
    print("Você errou mais de 5 vezes! GAME OVER :(")
else:
    print("Parabéns! Você acertou todas as palavras!")
    
