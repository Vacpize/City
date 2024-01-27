from turtle import *

def fon(fon_color):
    penup()
    goto(-200, -200)
    pendown()
    color(fon_color)
    begin_fill()
    for i in range(4):
        forward(400)
        left(90)
    end_fill()
    penup()
    goto(0, 0)
    pendown()

def stolbs():
    color("gray")
    pensize(11)
    penup()
    goto(-50, -62)
    pendown()
    left(90)
    forward(132)
    left(180)
    

    color("light gray")
    penup()
    right(90)
    forward(2)
    left(90)
    pendown()
    pensize(7)
    forward(138)
    penup()
    goto(125, -36)
    pendown()
    pensize(7)
    color("gray")
    forward(105)
    right(180)
    color("light gray")
    penup()
    left(90)
    forward(2)
    right(90)
    pendown()
    pensize(5)
    forward(105)

def clouds():
    penup()
    goto(-150, -67)
    pendown()
    color("white")
    pensize(11)
    begin_fill()
    circle(50)
    end_fill()
    penup()
    goto(-87, -99)
    pendown()
    begin_fill()
    circle(47)
    end_fill()
    penup()
    goto(-25,-96)
    pendown()
    begin_fill()
    circle(49)
    end_fill()
    penup()
    goto(25, -97)
    pendown()
    begin_fill()
    circle(49)
    end_fill()
    penup()
    goto(36, -6)
    pendown()
    begin_fill()
    circle(30)
    end_fill()
    penup()
    goto(75, -95)
    pendown()
    begin_fill()
    circle(50)
    end_fill()
    penup()
    goto(123, -11)
    pendown()
    begin_fill()
    circle(30)
    end_fill()
    penup()
    goto(79, -166)
    pendown()
    begin_fill()
    circle(73)
    end_fill()
    penup()
    goto(150, -200)
    pendown()
    begin_fill()
    circle(78)
    end_fill()
    penup()
    goto(200, -100)
    pendown()
    begin_fill()
    right(90)
    forward(100)
    right(90)
    forward(400)
    right(90)
    forward(200)
    end_fill()
    right(90)

def clouds1():#тень облаков
    penup()
    x = -150
    y = -67
    goto(x+12, y-27)
    pendown()
    color("lavender")
    pensize(11)
    begin_fill()
    circle(50)
    end_fill()
    penup()
    goto(-87+17, -99-25)
    pendown()
    begin_fill()
    circle(47)
    end_fill()
    penup()
    goto(-25+25,-96-25)
    pendown()
    begin_fill()
    circle(50)
    end_fill()
    penup()
    goto(25+43, -97-45)
    pendown()
    begin_fill()
    circle(67)
    end_fill()
    penup()
    goto(36+9, -6)
    pendown()
    begin_fill()
    circle(19)
    end_fill()
    penup()
    goto(123+2, -11+1)
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()
    goto(79+25, -166-25)
    pendown()
    begin_fill()
    circle(73)
    end_fill()
    penup()
    goto(150+25, -200-25)
    pendown()
    begin_fill()
    circle(78)
    end_fill()
    penup()
    goto(200+25, -100-25)
    pendown()
    begin_fill()
    right(90)
    forward(100)
    right(90)
    forward(400)
    right(90)
    forward(200)
    end_fill()
    right(90)

def grass(): #старая версия
    color("light green")
    x_need = 208
    x = -200
    y = -2
    left(180)
    pensize(4)
    penup()
    goto(-200, -5)
    pendown()
    begin_fill()
    forward(200-2)
    left(90)
    forward(400)
    left(90)
    forward(60)
    end_fill()
    y_needdown = -13
    for i in range(4): 
        color("lawngreen")
        x = -200
        y = -12
        y += y_needdown
        penup()
        goto(-200, y)
        pendown()
        while x != x_need:
            forward(50)
            penup()
            x += 6
            y += -2
            goto(x, y)
            pendown() 
        x = -196
        y = -12
        y_needdown += -15
        y += y_needdown
        x_need = 206
        color("yellowgreen")
        penup()
        goto(x, y)
        pendown()
        while x != x_need:
            forward(50)
            penup()
            x += 6
            y += -2
            goto(x, y)
            pendown()
        x = -200
        y = -12
        y_needdown -= 25
        y += y_needdown
        x_need = 208
        color("olivedrab")
        penup()
        goto(x, y)
        pendown()
        while x != x_need:
            forward(50)
            penup()
            x += 6
            y += -2
            goto(x, y)
            pendown()
        x = -196
        y = -12
        y_needdown += -25
        y += y_needdown
        x_need = 206
        color("darkolivegreen")
        penup()
        goto(-200, y)
        pendown()
        while x != x_need:
            forward(50)
            penup()
            x += 6
            y += -2
            goto(x, y)
            pendown()
        
def grees(color_n, light_color, x1, y1):
    color(light_color)
    x = x1
    y = y1
    penup()
    goto(-200, y)
    pendown()
    for io in range(15):
        forward(15)
        penup()
        x += 6
        y += -2
        goto(x, y)
        pendown()

def grass1():
    color("green")
    x1 = -200
    y1 = -12
    x_need = 208
    x = -200
    y = -2
    left(180)
    pensize(4)
    penup()
    goto(-200, -5)
    pendown()
    begin_fill()
    forward(200-2)
    left(90)
    forward(400)
    left(90)
    forward(60)
    end_fill()
    y_needdown = -13 #фон травы 

def provoda(size210):
    right(90)
    right(32)
    color("black")
    pensize(1)
    forward(size210)

def provoda2(size):
    right(90)
    right(30)
    color("black")
    pensize(1)
    forward(size)

