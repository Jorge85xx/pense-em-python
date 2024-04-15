"""Acrescente outro parâmetro, chamado length, ao
square. Altere o corpo para que o comprimento dos
lados seja length e então altere a chamada da função
para fornecer um segundo argumento. Execute o
programa novamente. Teste o seu programa com
uma variedade de valores para length.
"""
import turtle

def square(t : turtle, lenght : int):
  for i in range(4):
    t.fd(lenght)
    t.rt(90)


madison = turtle.Turtle()
square(madison, 400)

turtle.mainloop
