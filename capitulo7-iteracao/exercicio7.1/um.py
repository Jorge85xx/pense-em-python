"""Copie o loop de “Raízes quadradas”, na página 111, e
encapsule-o em uma função chamada mysqrt que receba
a como parâmetro, escolha um valor razoável de x e
devolva uma estimativa da raiz quadrada de a.
Para testar, escreva uma função denominada
test_square_root, que exibe uma tabela como esta:
a     mysqrt(a)      math.sqrt(a)      diff
-     ---------      ------------      ----
1.0   1.0            1.0               0.0
2.0   1.41421356237  1.41421356237     2.22044604925e-16
3.0   1.73205080757  1.73205080757     0.0
4.0   2.0            2.0               0.0
5.0   2.2360679775   2.2360679775      0.0
6.0   2.44948974278  2.44948974278     0.0
7.0   2.64575131106  2.64575131106     0.0
"""

import math


def mysqrt(a):
    x = 20
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x


def test_square_root(a, mysqrt, math):
    diff = abs(mysqrt) - abs(math)
    print('a          mysqrt(a)           math.sqrt(a)           diff\n'
          '-          ---------           ------------           -----\n'
          f'{a}         {mysqrt}                  {math}                     {diff}   ')


a = 2.0
test_square_root(a, mysqrt(a), math.sqrt(a))
