"""Escreva uma função chamada right_justify, que receba
uma string chamada s como parâmetro e exiba a string
com espaços suficientes à frente para que a última letra
da string esteja na coluna 70 da tela:
"""

def right_justify(word : str):
  space : str = " " * (70 - len('month') - 1) 
  print(space+word)

right_justify("word")