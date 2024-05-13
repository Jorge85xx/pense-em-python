"""Escreva uma função chamada eval_loop que
iterativamente peça uma entrada ao usuário, a avalie
usando eval e exiba o resultado.
Ela deve continuar até que o usuário digite done; então
deverá exibir o valor da última expressão avaliada.
"""


def eval_loop():
    answer = '0'
    while answer != 'done':
        print(eval(answer))
        answer = str(input('Digite algo: '))


eval_loop()
