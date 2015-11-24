# 6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distance = float(input('Digite a distância em km: '))
velocity = float(input('Digite a velocidade média em km/h: '))

time = distance/velocity
print ('Tempo aproximado: %.1f' %time)
