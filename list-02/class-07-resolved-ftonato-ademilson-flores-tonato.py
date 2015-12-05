# -*- coding: UTF-8 -*-

# 7) Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# Obs. : somente são vendidos um número inteiro de latas.
totalSize = int(input('Digite o tamanho em metros quadrados da área a ser pintada: '))

if totalSize % 54 == 0:
	amount = totalSize / 54
else:
	amount = int(totalSize / 54) + 1

value = amount * 80
print ('Serão necessários %d latas de tinta' %amount)
print ('Total a pagar: R$ %.2f' %value)
