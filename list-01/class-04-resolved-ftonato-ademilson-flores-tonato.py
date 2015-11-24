# 4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salary = float(input('Digite o seu salário: '))
percent = float(input('Digite a porcentagem do aumento: '))
increase = percent*salary/100
result = salary+increase

print ('Aumento: R$  %.2f' %increase)
print ('Novo salário: R$  %.2f' %result)
