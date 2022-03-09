# Programa que le um numero e imprime todos os pares entre 1 e ele.

number = int(input("Digite um numero: "))

for i in range(2,number+1,2):
  print(i)

'''
for i in range(2,number+1):
  if i % 2 == 0:
    print(i)

'''