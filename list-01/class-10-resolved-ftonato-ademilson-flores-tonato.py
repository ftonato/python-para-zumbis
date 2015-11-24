# 10) Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá.
# Exiba o total de dias.
amount = float(input('Digite a quantidade de cigarros fumados por dia: '))
years = float(input('Digite a quantidade de anos que já fumou: '))

# 1 dia = 1440 minutos = 144 cigarros
result = (years*365*amount) / 144

print ('Total de dias de vida perdido(s): %.2f' %result)
