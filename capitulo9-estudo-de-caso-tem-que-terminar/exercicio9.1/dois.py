"""Altere seu programa na seção anterior para imprimir
apenas as palavras que não têm “e” e calcule a
porcentagem de palavras na lista que não têm “e”.
"""

general_accountant = 0
e_counter = 0
fin = open('../words.txt')
for line in fin:
    general_accountant += 1
    if 'e' not in line:
        print(line.strip())
    else:
        e_counter += 1
if general_accountant > 0:
    percent_e = (e_counter / general_accountant) * 100
    print(f"percent of words that contains 'e': {percent_e:.2f}%")
