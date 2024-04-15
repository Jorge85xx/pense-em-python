""" Escreva uma função chamada square que receba um
parâmetro chamado t, que é um turtle. Ela deve usar
o turtle para desenhar um quadrado."""
import turtle

def square(t : turtle):
  for i in range(4):
    t.fd(100)
    t.rt(90)


madison = turtle.Turtle()
square(madison)

turtle.mainloop
