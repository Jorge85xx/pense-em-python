"""Um número a é uma potência de b se for divisível por b e
a/b for uma potência de b. Escreva uma função chamada
is_power que receba os parâmetros a e b e retorne True
se a for uma potência de b. Dica: pense no caso-base.
"""

def is_power(a, b):
  if a == b: #caso base
    return True
  elif a % b == 0 and is_power(a/b, b):
    return True
  else:
    return False
 
print(is_power(4,2))