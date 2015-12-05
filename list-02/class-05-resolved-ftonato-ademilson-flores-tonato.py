# -*- coding: UTF-8 -*-

# 5) Faça um Programa que leia três números e mostre o maior e o menor deles.
amount = 0
moreBig = None
smaller = None
while amount < 3:
	number = int(input('Digite o %dº número: ' %(amount+1)))

	if moreBig == None or number > moreBig:
		moreBig = number

	if smaller == None or number < smaller:
		smaller = number

	amount = amount + 1

print ('O maior número digitado é: %d' %moreBig)
print ('O menor número digitado é: %d' %smaller)
