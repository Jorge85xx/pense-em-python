"""O último teorema de Fermat diz que não existem números
inteiros a, b e c tais que a**n + b**n == c**n para quaisquer
valores de n maiores que 2.

1. Escreva uma função chamada check_fermat que
receba quatro parâmetros – a, b, c e n – e verifique se o
teorema de Fermat se mantém. Se n for maior que 2 e
a**n + b**n == c**n o programa deve imprimir, “Holy
smokes, Fermat was wrong!” Senão o programa deve
exibir “No, that doesn’t work.”"""

def check_fermat(a : int, b : int, c : int, n : int ):
  if n > 2:
    if a**n + b**n == c**n:
      print('Holy smokes, Fermat was wrong!')
    else:
      print('No, that doesn’t work.')
  else:
    print('The number of you enter is not larger than 2')

check_fermat(3, 4, 5, 2)  
check_fermat(3, 4, 5, 3)  
