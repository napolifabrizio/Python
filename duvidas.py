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

