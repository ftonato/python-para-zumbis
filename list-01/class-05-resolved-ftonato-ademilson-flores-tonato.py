# 5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
value = float(input('Digite o preço da mercadoria: '))
percent = float(input('Digite a porcentagem do desconto: '))
discount = percent*value/100
result = value-discount

print ('Desconto: R$  %.2f' %discount)
print ('Valor a pagar: R$  %.2f' %result)
