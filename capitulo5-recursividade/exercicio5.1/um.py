"""Escreva um script que leia a hora atual e a converta em um
tempo em horas, minutos e segundos, mais o número de
dias desde a época.
Escreva um script que leia a hora atual e a converta em um
tempo em horas, minutos e segundos, mais o número de
dias desde a época.
"""
import time

tempo_atual = time.time()

dias_desde_epoca = tempo_atual // (24 * 60 * 60) #soma dos segundos de horas minutos e segundos

horas = int((tempo_atual / 3600) % 24) 
minutos = int((tempo_atual / 60) % 60)
segundos = int(tempo_atual % 60)

print("Tempo atual:")
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)
print("Número de dias desde a época:", int(dias_desde_epoca))