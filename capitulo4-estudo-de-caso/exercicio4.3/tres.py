""" Faça uma cópia do square e mude o nome para
polygon. Acrescente outro parâmetro chamado n e
altere o corpo para que desenhe um polígono regular
de n lados."""
import turtle

def polygon(t : turtle, length : int, n: int):
  for i in range(n):
    t.fd(length)
    t.rt(360/n)


madison = turtle.Turtle()
polygon(madison, 200, 5)

turtle.mainloop
