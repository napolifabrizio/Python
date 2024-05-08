
p1 = ("Fabrizio", 18)
print(p1)
p1 = ("Fabrizio", 20, 2)
print(p1)

number = "2"
number = list(number)
print(number)

###################################################### 1.0 List Comprehesion
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

############################## 2.0 saber aonde o codigo esta sendo executado
import os

diretorio_atual = os.getcwd()
print("O diretório atual é:", diretorio_atual)

########################################## 3.0 Ternary Operator

idade = 10
maior_de_idade = "maior de idade" if idade >= 18 else "menor de idade"
print(maior_de_idade)


nums = [1, 2, 3, 4, 5]

# 4.0 adiciona um elemento no final
nums.append(6)

# 4.1 remove um elemento
nums.remove(6)

# 4.2 remove todos os elementos
nums.clear()

# 4.3 adiciona mais de um elemento
nums.extend([1, 2, 3])
print(nums)

######################################## 5.0  tuplas, tuplas são imutáveis
fabrizio = ("fabrizio", 20)
# fabrizio[1] = 21 --> isso vai dar erro
# para mudar uma tupla, voce não a muda, vc muda a variavel. Olhe abaixo
def acrescenta_idade(tupla, valor):
    nova_idade = tupla[1] + valor
    return (tupla[0], nova_idade)

print(fabrizio)
fabrizio = acrescenta_idade(fabrizio, 2)
print(fabrizio)

############################################ 6.0 imprimindo index e valor

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

###################################### 7.0 ordenando numeros

nums = [10, 54, 1, 91, 29, 50, 33]
sorted(nums) #crescente, não muda o array
nums.sort() #crescente, muda o array

# troca a ordem da lista, trazendo o inverso

verso = [1, 2, 5, 3, 4]
inverso = list(reversed(verso))

####################################### 8.0 Melhor loop for
import time

def double_using_for(arr):
   result = []
   inicio = time.time()
   for num in arr:
      result.append(num*2)
   fim = time.time()
   print("FOR: ", fim - inicio)

def double_using_while(arr):
   result = []
   i = 0
   inicio = time.time()
   while i < len(arr):
      result.append(arr[i])
      i+=1
   fim = time.time()
   print("WHILE: ", fim - inicio)

def double_using_list_comprehension(arr):
   inicio = time.time()
   result = [num*2 for num in arr]
   fim = time.time()
   print("LIST COMPREHENSION: ", fim - inicio)

arr = list(range(1, 1_000_001))

double_using_for(arr)
   # FOR:  0.10441994667053223
double_using_while(arr)
   # WHILE:  0.1320939064025879
double_using_list_comprehension(arr)
   # LIST COMPREHENSION:  0.06599950790405273

# Portanto, quando puder substituir laço for ou while por list_comprehension, substitua!

######################################## 9.0 Como não precisar usar vários if/else

keyword = input("Digite a opção desejada: (A) - (B) - (C) - (D)")

# Má prática

if keyword == "A":
   print("Você escolheu A")
elif keyword == "B":
   print("Você escolheu B")
elif keyword == "C":
   print("Você escolheu C")
elif keyword == "D": 
   print("Você escolheu D")

# Boa prática

options = {
   "A": "Você escolheu A",
   "B": "Você escolheu B",
   "C": "Você escolheu C",
   "D": "Você escolheu D",
}

print(options[keyword])