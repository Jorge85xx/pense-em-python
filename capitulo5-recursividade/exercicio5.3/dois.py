"""Escreva uma função que peça ao usuário para digitar
três comprimentos de gravetos, os converta em
números inteiros e use is_triangle para verificar se os
gravetos com os comprimentos dados podem formar
um triângulo."""

def is_triangle(side1 : int, side2 : int, side3 : int):
  if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print('Yes')
  else:
    print('No')

def verificar_triângulo():
  
    lado_a = int(input("Enter the length of the first stick: "))
    lado_b = int(input("Enter the length of the second stick: "))
    lado_c = int(input("Enter the length of the third stick: "))

    # Verificar se os gravetos com os comprimentos fornecidos podem formar um triângulo
    print("Os gravetos com os comprimentos fornecidos podem formar um triângulo?")
    is_triangle(lado_a, lado_b, lado_c)