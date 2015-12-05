# -*- coding: UTF-8 -*-

# 6) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
# Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato (5%) : R$
# e. = Salário Liquido : R$
salaryHours = float(input('Digite quanto você ganha por hora: '))
hourWork = int(input('Digite a quantidade de horas trabalhadas por mês: '))

salaryGross = salaryHours*hourWork
ir = salaryGross * 0.11
inss = salaryGross * 0.08
syndicate = salaryGross * 0.05
salaryNet = salaryGross - ir - inss - syndicate

print ('+ Salário Bruto : R$ %5.2f' %salaryGross)
print ('- IR (11 por cento) : R$ %5.2f' %ir)
print ('- INSS (8 por cento) : R$ %5.2f' %inss)
print ('- Sindicato (5 por cento) : R$ %5.2f' %syndicate)
print ('= Salário Liquido : R$ %5.2f' %salaryNet)
