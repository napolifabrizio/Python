p1 = ("Fabrizio", 18)
print(p1)
p1 = ("Fabrizio", 20, 2)
print(p1)

number = "2"
number = list(number)
print(number)

###################################################### List Comprehesion
contas_idade = [14, 23, 16, 18, 32]
maiores_de_idade = []

for idade in contas_idade:
  if idade >= 18:
    maiores_de_idade.append(idade)

print(maiores_de_idade)
###########################################
contas_idade2 = [14, 23, 16, 18, 32]

maiores_de_idade2 = [idade for idade in contas_idade2 if idade >= 18]

print(maiores_de_idade2)
##################################################### List Comprehesion

############################## saber aonde o codigo esta sendo executado
import os

diretorio_atual = os.getcwd()
print("O diretório atual é:", diretorio_atual)
#####################################################

########################################## Ternary Operator

idade = 10
maior_de_idade = "maior de idade" if idade >= 18 else "menor de idade"
print(maior_de_idade)