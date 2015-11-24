# 3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
days = int(input('Digite a quantidade de dias: '))
hours = int(input('Digite a quantidade de horas: '))
minutes = int(input('Digite a quantidade de minutos: '))
seconds = int(input('Digite a quantidade de segundos: '))

daysToSeconds = days*86400
hoursToSeconds = hours*3600
minutesToSeconds = minutes*60

print(daysToSeconds+hoursToSeconds+minutesToSeconds+seconds)
