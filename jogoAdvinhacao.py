import random

numero_secreto = random.randint(1,350)
acertou = False
pontos = 1000
print("Chute um numero: ")
chute = int(input("Qual é o seu chute? "))

while (acertou == False): 
    if chute == numero_secreto:
        print(f"Você acertou! O número secreto é {chute}")
        print(f"Sua pontuação foi: {pontos}")
        acertou = True
    elif chute > numero_secreto:
        chute = int(input("Errou! Seu chute foi maior que o numero. Tente de novo: "))
        pontos = pontos - 50
    elif chute < numero_secreto:
        chute = int(input("Errou! Seu chute foi menor que o numero. Tente de novo: "))
        pontos = pontos - 50
    
    if pontos ==0:
        print("Você perdeu!")
        break




        


