"""
  Função recursiva para imprimir a soma acumulada de n e s.

  Parâmetros:
  n : int -> O número de chamadas recursivas restantes.
  s : int -> O valor acumulado até o momento.

  Não retorna nada, apenas imprime o resultado na tela 
"""
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
