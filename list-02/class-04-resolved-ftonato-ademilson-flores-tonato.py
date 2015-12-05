# -*- coding: UTF-8 -*-

# 4) Faça um Programa que leia três números e mostre o maior deles.
amount = 0
moreBig = None
while amount < 3:
	number = int(input('Digite o %dº número: ' %(amount+1)))

	if number > moreBig:
		moreBig = number

	amount = amount + 1

print ('O maior número digitado é: %d' %moreBig)
