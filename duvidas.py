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
##
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


nums = [1, 2, 3, 4, 5]

# adiciona um elemento no final
nums.append(6)

# remove um elemento
nums.remove(6)

# remove todos os elementos
nums.clear()

# adiciona mais de um elemento
nums.extend([1, 2, 3])
print(nums)

# recurso maneiro
idades = [18, 19, 20, 21, 22]
idades_ano_que_vem = [(idade+1) for idade in idades]
print(idades_ano_que_vem)

maior_21 = [idade for idade in idades if idade > 21]
print(maior_21)

# tuplas, tuplas são imutáveis
fabrizio = ("fabrizio", 20)
# fabrizio[1] = 21 --> isso vai dar erro
# para mudar uma tupla, voce não a muda, vc muda a variavel. Olhe abaixo
def acrescenta_idade(tupla, valor):
    nova_idade = tupla[1] + valor
    return (tupla[0], nova_idade)

print(fabrizio)
fabrizio = acrescenta_idade(fabrizio, 2)
print(fabrizio)

# imprimindo index e valor

nums = [1, 2, 3, 4, 5]
for i in range(len(nums)):
   print(i, nums[i])

for i, num in enumerate(nums):
   print(i, num)

# desempacotando

usuarios = [
   ("Fabrizio", 20, 2003),
   ("Isabella", 24, 1999),
   ("Talia", 1, 2022)
]

for nome, idade, ano_nascimento in usuarios:
   print(nome, idade, ano_nascimento)

for _, idade, _ in usuarios:
   print(idade)

# ordenando numeros

nums = [10, 54, 1, 91, 29, 50, 33]
sorted(nums) #crescente, não muda o array
nums.sort() #crescente, muda o array

# troca a ordem da lista, trazendo o inverso

verso = [1, 2, 5, 3, 4]
inverso = list(reversed(verso))
