""" Escreva uma função chamada circle que use o turtle,
t e um raio r como parâmetros e desenhe um círculo
aproximado ao chamar polygon com um
comprimento e número de lados adequados. Teste a
sua função com uma série de valores de r.
"""
import turtle
import math

def polygon(t : turtle, length : int, n: int):
  for i in range(n):
    t.fd(length)
    t.rt(360/n)

def circle(t : turtle, r: int):
  circumference = 2 * math.pi * r
  n = 50 
  length = circumference / n
  polygon(t, length, n)
 
  
madison = turtle.Turtle()
radii = [50, 100, 150, 200]

for r in radii:
    circle(madison, r)

turtle.mainloop