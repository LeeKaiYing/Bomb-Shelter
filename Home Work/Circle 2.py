from turtle import *

size = 36
bgcolor ("white")
pensize (5)
speed (-1)
for i in range (size):
    begin_fill() ; fillcolor ("orange")
    lt (120) ; pencolor ("black")
    circle (120,360)
    
    rt (90) ; pencolor ("black")
    circle (90,360)
    end_fill()
