"""Escreva uma função que peça ao usuário para digitar
valores para a, b, c e n, os converta em números
inteiros e use check_fermat para verificar se violam o
teorema de Fermat."""

def check_fermat(a : int, b : int, c : int, n : int ):
  if n > 2:
    if a**n + b**n == c**n:
      print('Holy smokes, Fermat was wrong!')
    else:
      print('No, that doesn’t work.')
  else:
    print('The number of you enter is not larger than 2')

def test_fermat():
  print('Enter the number a, b, c and n, for testing the fermat theorem')
  a = int(input('Enter the number a: '))
  b = int(input('Enter the number b: '))
  c = int(input('Enter the number c: '))
  n = int(input('Enter the number n: '))
  check_fermat(a, b, c, n)

test_fermat()