from things import *
from turtle import *


speed(50)
fon_color = "light blue"
fon(fon_color)
clouds()
clouds1()
stolbs()




grass1()
color_n = "green"
light_color = "lime"
penup()
goto(-200, -12)
pendown()
x1 = -200
y1 = -12
grees(color_n, light_color, x1, y1)


penup()
goto(-23, -116)
pendown()
x1 = -90
y1 = -78
grees(color_n, light_color, x1, y1)

penup()
goto(-120, -120)
pendown()
x1 = 21
y1 = -154
grees(color_n, light_color, x1, y1)

penup() 
goto(-200, -47)
pendown()
color("green")
pensize(4)
left(180)
forward(149)
left(180) 




penup()#провод 1
goto(-50, 54)
pendown()
size210 = 210
provoda(size210)

penup()#провод 2
goto(-200, 52)
left(180)
right(45)
pendown()
size = 150
provoda2(size)

penup()#провод 3
goto(-200, 32)
left(180)
right(57)
pendown()
size = 149
provoda2(size)

penup()#провод 4
goto(-50, 33)
left(109)
pendown()
size210 = 195
provoda(size210)
penup()
goto(130, -62)
left(132)
pendown()
size = 72
provoda2(size)



pendown() #Обрезнаие рисунка
pensize(50)
color("white")
penup()
goto(230, -230)
pendown()
left(180)
right(75)
for i in range(4):
    forward(460)
    left(90)
#конец прграммы 

hideturtle()
exitonclick()