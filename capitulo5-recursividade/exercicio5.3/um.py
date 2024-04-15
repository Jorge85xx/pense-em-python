"""Se você tiver três gravetos, pode ser que consiga arranjálos em um triângulo ou não. Por exemplo, se um dos
gravetos tiver 12 polegadas de comprimento e outros dois
tiverem uma polegada de comprimento, não será possível
fazer com que os gravetos curtos se encontrem no meio.
Há um teste simples para ver se é possível formar um
triângulo para quaisquer três comprimentos:
Se algum dos três comprimentos for maior que a soma dos
outros dois, então você não pode formar um triângulo.
Senão, você pode. (Se a soma de dois comprimentos
igualar o terceiro, eles formam um triângulo chamado
“degenerado”.)
1. Escreva uma função chamada is_triangle que receba
três números inteiros como argumentos, e que imprima
“Yes” ou “No”, dependendo da possibilidade de formar
ou não um triângulo de gravetos com os comprimentos
dados."""

def is_triangle(side1 : int, side2 : int, side3 : int):
  if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print('Yes')
  else:
    print('No')

is_triangle(3,4,5)
is_triangle(1,2,5)