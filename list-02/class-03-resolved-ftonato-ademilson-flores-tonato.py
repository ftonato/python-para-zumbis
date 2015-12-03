# 3) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar.
# Caso contrário mostrar tais variáveis com o conteúdo ZERO.

weight = int(input('Digite a soma do peso dos peixes: '))

if weight > 50:
	excess = weight-50
	trafficTicket = excess*4
else:
	excess = trafficTicket = 0

print ('Valor a pagar R$ %.2f, pelo excesso de %d kg' %(trafficTicket, excess))
