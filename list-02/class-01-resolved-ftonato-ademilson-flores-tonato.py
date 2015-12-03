# 1) Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
leftNumber = int(input('Digite o tamanho do lado esquerdo: '))
rightNumber = int(input('Digite o tamanho do lado direito: '))
baseNumber = int(input('Digite o tamanho da base: '))

if leftNumber == rightNumber or leftNumber == baseNumber or rightNumber == baseNumber:
	print ('Seu triângulo é isósceles')
elif leftNumber == rightNumber or == baseNumber:
	print ('Seu triângulo é equilátero')
elif leftNumber != rightNumber and leftNumber != baseNumber and rightNumber != baseNumber:
	print ('Seu triângulo é escaleno')
else:
	print ('Isso não pode ser um triângulo!')