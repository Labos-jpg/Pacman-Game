import turtle
import time
from turtle import *
from random import *

bodovi=0
zivoti=5
#21x22 kvadrata  #525x550 pixela # 1 kvadrat = 25
#pozadina, naslov i bodovi------------------------------------------------------------------------------------------------------------
poz=turtle.Screen()
poz.bgcolor("black")
poz.title("Pac-Man")
poz.setup(700,700)

turtle.color('white')
turtle.ht()
turtle.pu()
turtle.setpos(-330,300)
turtle.write(bodovi, font=('Times New Roman', 30, 'bold'))

turtle1 = turtle.Turtle()
turtlee = turtle.Screen()
pravokutnik = ((-20,10),(20,10),(20,-10),(-20,-10))
turtlee.register_shape('rectangle',pravokutnik)
turtle1.shape('rectangle')
turtle1.color('black')
turtle1.ht()
turtle1.pu()
turtle1.setpos(-330,315)
turtle1.setheading(90)
turtle1.shapesize(3)

zivotcratc=Turtle()
zivotcratc.color('white')
zivotcratc.ht()
zivotcratc.pu()
zivotcratc.setpos(180,300)
zivotcratc.write("Lives:", font=('Times New Roman', 30, 'bold'))

zivotbrojac=Turtle()
zivotbrojac.color('white')
zivotbrojac.ht()
zivotbrojac.pu()
zivotbrojac.setpos(300,300)
zivotbrojac.write(zivoti, font=('Times New Roman', 30, 'bold'))

zivotbrisac=Turtle()
zivotbrisac.color('black')
zivotbrisac.shape('square')
zivotbrisac.shapesize(2)
zivotbrisac.ht()
zivotbrisac.pu()
zivotbrisac.setpos(315,318)

#labirnito crtac---------------------------------------------------------------------------------------------------------------
lab=Turtle()
stamp=20
kv=21.5
lab.shape('square')
lab.color('#00009c')
lab.pu() 
lab.shapesize(kv/stamp) 
lab.speed(0)

#pacman------------------------------------------------------------------------------------------------------------------------
pacman=Turtle()
pacman.ht()
pacman.shape('circle')
pacman.color('#dded00')
pacman.pu()
pacman.shapesize(1) 
pacman.speed(3)


#kontroliranje pacmana-----------------------------------------------------------------------------------------------------------
def lijevo():
    global bodovi
    x2=pacman.xcor() - 25 #racunamo gdje je pacman ici
    y2=pacman.ycor()
    if(x2,y2) not in zidovi: #tu gledamo da pacman nemoze proci kroz zid
        pacman.goto(x2,y2) #ako nema zida tamo pacman moze ici na to mjesto
    if(x2,y2) in hrane:
        brisac.goto(x2,y2)
        tracer(0)
        brisac.stamp()
        tracer(1)
        bodovi=bodovi+100
        turtle1.stamp()
        turtle.write(bodovi, font=('Times New Roman', 30, 'bold'))
        hrane.remove((x2,y2)) #brise podatak iz liste kako bi bodovi bili tocni
        
def gore():
    global bodovi
    x2=pacman.xcor()
    y2=pacman.ycor() + 25
    if(x2,y2) not in zidovi:
        pacman.goto(x2,y2)
    if(x2,y2) in hrane:
        brisac.goto(x2,y2)
        tracer(0)
        brisac.stamp()
        tracer(1)
        bodovi=bodovi+100
        turtle1.stamp()
        turtle.write(bodovi, font=('Times New Roman', 30, 'bold'))
        hrane.remove((x2,y2))
def desno():
    global bodovi
    x2=pacman.xcor() + 25
    y2=pacman.ycor()
    if(x2,y2) not in zidovi:
        pacman.goto(x2,y2)
    if(x2,y2) in hrane:
        brisac.goto(x2,y2)
        tracer(0)
        brisac.stamp()
        tracer(1)
        bodovi=bodovi+100
        turtle1.stamp()
        turtle.write(bodovi, font=('Times New Roman', 30, 'bold'))
        hrane.remove((x2,y2))
def dolje():
    global bodovi
    x2=pacman.xcor()
    y2=pacman.ycor() - 25
    if(x2,y2) not in zidovi:
        pacman.goto(x2,y2)
    if(x2,y2) in hrane:
        brisac.goto(x2,y2)
        tracer(0)
        tracer(1)
        brisac.stamp()
        bodovi=bodovi+100
        turtle1.stamp()
        turtle.write(bodovi, font=('Times New Roman', 30, 'bold'))
        hrane.remove((x2,y2))
onkey(gore,'w')
onkey(desno,'d')
onkey(dolje,'s')
onkey(lijevo,'a')

#duh1--------------------------------------------------------------------------------------------------------------------------
duh1=Turtle()
duh1.ht()
duh1.shape('triangle')
duh1.color('#cc0e0e')
duh1.pu() 
duh1.shapesize(1) 
duh1.speed(1)

#duh2--------------------------------------------------------------------------------------------------------------------------
duh2=Turtle()
duh2.ht()
duh2.shape('triangle')
duh2.color('#f2832e')
duh2.pu() 
duh2.shapesize(1) 
duh2.speed(1.5)

#duh3--------------------------------------------------------------------------------------------------------------------------
duh3=Turtle()
duh3.ht()
duh3.shape('triangle')
duh3.color('#db87f5')
duh3.pu() 
duh3.shapesize(1) 
duh3.speed(2)

#duh4--------------------------------------------------------------------------------------------------------------------------
duh4=Turtle()
duh4.ht()
duh4.shape('triangle')
duh4.color('#00e5ff')
duh4.pu() 
duh4.shapesize(1) 
duh4.speed(2.5)

#prvi teleporter-----------------------------------------------------------------------------------------------------------------
e=Turtle()
stamp=20
kv=21.5
e.shape('square')
e.color('black')
e.pu() 
e.shapesize(kv/stamp)
e.speed(0)
e.ht()

#drugi teleporter-----------------------------------------------------------------------------------------------------------------
f=Turtle()
stamp=20
kv=21.5
f.shape('square')
f.color('black')
f.pu() 
f.shapesize(kv/stamp)
f.speed(0)
f.ht()

#hrana------------------------------------------------------------------------------------------------------------------------------
hrana=Turtle()
hrana.shape('circle')
hrana.color('white')
hrana.pu()
hrana.ht()
hrana.shapesize(0.4) 
hrana.speed(0)


#hrano brisac--------------------------------------------------------------------------------------------------------------------
brisac=Turtle()
brisac.ht()
brisac.shape('circle')
brisac.color('black')
brisac.pu()
brisac.shapesize(0.7) 
brisac.speed(0)

#win znak----------------------------------------------------------------------------------------------------------------------
win=Turtle()
win.ht()
stamp=20
kv=21.5
win.shape('square')
win.color('#26ff00')
win.pu() 
win.shapesize(kv/stamp) 
win.speed(0)
wznak=[
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "  X     X X XX    X  ",
    "  X     X X X X   X  ",
    "  X     X X X X   X  ",
    "  X  X  X X X  X  X  ",
    "  X  X  X X X  X  X  ",
    "  X  X  X X X   X X  ",
    "  X  X  X X X   X X  ",
    "   XX XX  X X    XX  ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    ]
def winus():
    for x in range(21):
        for y in range(22):
            polje = wznak[y][x]
            x1 = -262.5 + (x * 25)
            y1 = 262.5 - (y * 25)
            if polje == "X":
                win.goto(x1,y1)
                win.stamp()

#lose znak----------------------------------------------------------------------------------------------------------------------
lose=Turtle()
lose.ht()
stamp=20
kv=21.5
lose.shape('square')
lose.color('#ff0000')
lose.pu() 
lose.shapesize(kv/stamp) 
lose.speed(0)
lznak=[
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    " X     XX   XXX XXXX ",
    " X    X  X X    X    ",
    " X    X  X X    X    ",
    " X    X  X  XX  XXX  ",
    " X    X  X    X X    ",
    " X    X  X    X X    ",
    " XXXX  XX  XXX  XXXX ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    "                     ",
    ]
def loser():
    for x in range(21):
        for y in range(22):
            polje = lznak[y][x]
            x1 = -262.5 + (x * 25)
            y1 = 262.5 - (y * 25)
            if polje == "X":
                lose.goto(x1,y1)
                lose.stamp()

#pozadino brisac-----------------------------------------------------------------------------------------------------------------
deletus=Turtle()
deletus.color('black')
deletus.ht()
deletus.setheading(0)
deletus.setpos(0,0)
deletus.shape('square')
deletus.shapesize(30)


#labirint-----------------------------------------------------------------------------------------------------------------------
labirint=[
    "XXXXXXXXXXXXXXXXXXXXX",#gore lijevi kut -262.5,275
    "X1        X        2X",#gore desni kut 262.5,275
    "X XX XXXX X XXXX XX X",#dolje lijevi kut -262.5,-275
    "X XX XXXX X XXXX XX X",#dolje desni kut 262.5,-275
    "X                   X",
    "X XX X XXXXXXX X XX X",
    "X    X    X    X    X",
    "XXXX XXXX X XXXX XXXX",
    "XXXX X         X XXXX",
    "XXXX X XXXXXXX X XXXX",
    "EA     XXXXXXX     CF",
    "XXXX X XXXXXXX X XXXX",
    "XXXX X         X XXXX",
    "XXXX X XXXXXXX X XXXX",
    "X         X         X",
    "X XX XXXX X XXXX XX X",
    "X  X             X  X",
    "XX X X XXXXXXX X X XX",
    "X    X    X    X    X",
    "X XXXXXXX X XXXXXXX X",
    "X3                 4X",
    "XXXXXXXXXXXXXXXXXXXXX"
    ]
def maze():
    for x in range(21):
        for y in range(22):
            polje = labirint[y][x]
            x1 = -262.5 + (x * 25)
            y1 = 262.5 - (y * 25)
            if polje == "X": #mijenja mjesta gdje je slovo X u kvadratice
                lab.goto(x1,y1)
                lab.stamp()
                zidovi.append((x1,y1)) #dvije zagrade da se zapise kao par koordinati
            if polje == " ":
                hrana.goto(x1,y1)
                hrana.stamp()
                hrane.append((x1,y1))
            if polje == "A": #pacman
                pacman.goto(x1,y1)
                pacman.showturtle()
            if polje == "1": #duh1
                duh1.goto(x1,y1)
                duh1.showturtle()
            if polje == "2": #duh2
                duh2.goto(x1,y1)
                duh2.showturtle()
            if polje == "3": #duh3
                duh3.goto(x1,y1)
                duh3.showturtle()
            if polje == "4": #duh4
                duh4.goto(x1,y1)
                duh4.showturtle()
            if polje == "E":
                e.goto(x1,y1)
                e.showturtle()
            if polje == "F":
                f.goto(x1,y1)
                f.showturtle()
zidovi=[]
hrane=[]
tracer(0)
maze()
tracer(1)
listen()

while True:
    update()
    if pacman.distance(e)<20: #teleport pacman
        pacman.ht()
        pacman.goto(212.5,12.5)
        pacman.showturtle()
    if pacman.distance(f)<20: #teleport pacman
        pacman.ht()
        pacman.goto(-237.5,12.5)
        pacman.showturtle()
    if pacman.distance(duh1)<20: #minus zivot
        zivoti=zivoti-1
        pacman.ht()
        pacman.goto(-237.5,12.5)
        pacman.showturtle()
        zivotbrisac.stamp()
        if zivoti==0:
            zivotbrojac.color('#ff7300')
            zivotbrojac.write(zivoti, font=('Times New Roman', 30, 'bold'))
        else:
            zivotbrojac.write(zivoti, font=('Times New Roman', 30, 'bold'))
    if pacman.distance(duh2)<20: #minus zivot
        zivoti=zivoti-1
        pacman.ht()
        pacman.goto(-237.5,12.5)
        pacman.showturtle()
        zivotbrisac.stamp()
        if zivoti==0:
            zivotbrojac.color('#ff7300')
            zivotbrojac.write(zivoti, font=('Times New Roman', 30, 'bold'))
        else:
            zivotbrojac.write(zivoti, font=('Times New Roman', 30, 'bold'))
    if pacman.distance(duh3)<20: #minus zivot
        zivoti=zivoti-1
        pacman.ht()
        pacman.goto(-237.5,12.5)
        pacman.showturtle()
        zivotbrisac.stamp()
        if zivoti==0:
            zivotbrojac.color('#ff7300')
            zivotbrojac.write(zivoti, font=('Times New Roman', 30, 'bold'))
        else:
            zivotbrojac.write(zivoti, font=('Times New Roman', 30, 'bold'))
    if pacman.distance(duh4)<20: #minus zivot
        zivoti=zivoti-1
        pacman.ht()
        pacman.goto(-237.5,12.5)
        pacman.showturtle()
        zivotbrisac.stamp()
        if zivoti==0:
            zivotbrojac.color('#ff7300')
            zivotbrojac.write(zivoti, font=('Times New Roman', 30, 'bold'))
        else:
            zivotbrojac.write(zivoti, font=('Times New Roman', 30, 'bold'))
    if duh1.distance(e)<20: #teleport duhovi
        duh1.ht()
        duh1.goto(212.5,12.5)
        duh1.showturtle()
    if duh1.distance(f)<20: #teleport duhovi
        duh1.ht()
        duh1.goto(-237.5,12.5)
        duh1.showturtle()
    if duh2.distance(e)<20: #teleport duhovi
        duh2.ht()
        duh2.goto(212.5,12.5)
        duh2.showturtle()
    if duh2.distance(f)<20: #teleport duhovi
        duh2.ht()
        duh2.goto(-237.5,12.5)
        duh2.showturtle()
    if duh3.distance(e)<20: #teleport duhovi
        duh3.ht()
        duh3.goto(212.5,12.5)
        duh3.showturtle()
    if duh3.distance(f)<20: #teleport duhovi
        duh3.ht()
        duh3.goto(-237.5,12.5)
        duh3.showturtle()
    if duh4.distance(e)<20: #teleport duhovi
        duh4.ht()
        duh4.goto(212.5,12.5)
        duh4.showturtle()
    if duh4.distance(f)<20: #teleport duhovi
        duh4.ht()
        duh4.goto(-237.5,12.5)
        duh4.showturtle()
    okret=randint(1,4) #kretanje duha 1------------------------------------------------------------------------------------------
    if okret==1:          #desno
        x3=duh1.xcor() + 25
        y3=duh1.ycor()
        if(x3,y3) not in zidovi:
            duh1.goto(x3,y3)
    if okret==2:           #gore
        x3=duh1.xcor()
        y3=duh1.ycor() + 25
        if(x3,y3) not in zidovi:
            duh1.goto(x3,y3)
    if okret==3:           #lijevo
        x3=duh1.xcor() - 25
        y3=duh1.ycor()
        if(x3,y3) not in zidovi:
            duh1.goto(x3,y3)
    if okret==4:           #dolje
        x3=duh1.xcor()
        y3=duh1.ycor() - 25
        if(x3,y3) not in zidovi:
            duh1.goto(x3,y3)
    if okret==1:          #desno #kretanje duha 2------------------------------------------------------------------------------------------
        x3=duh2.xcor() + 25
        y3=duh2.ycor()
        if(x3,y3) not in zidovi:
            duh2.goto(x3,y3)
    if okret==2:           #gore
        x3=duh2.xcor()
        y3=duh2.ycor() + 25
        if(x3,y3) not in zidovi:
            duh2.goto(x3,y3)
    if okret==3:           #lijevo
        x3=duh2.xcor() - 25
        y3=duh2.ycor()
        if(x3,y3) not in zidovi:
            duh2.goto(x3,y3)
    if okret==4:           #dolje
        x3=duh2.xcor()
        y3=duh2.ycor() - 25
        if(x3,y3) not in zidovi:
            duh2.goto(x3,y3)
    if okret==1:          #desno #kretanje duha 3------------------------------------------------------------------------------------------
        x3=duh3.xcor() + 25
        y3=duh3.ycor()
        if(x3,y3) not in zidovi:
            duh3.goto(x3,y3)
    if okret==2:           #gore
        x3=duh3.xcor()
        y3=duh3.ycor() + 25
        if(x3,y3) not in zidovi:
            duh3.goto(x3,y3)
    if okret==3:           #lijevo
        x3=duh3.xcor() - 25
        y3=duh3.ycor()
        if(x3,y3) not in zidovi:
            duh3.goto(x3,y3)
    if okret==4:           #dolje
        x3=duh3.xcor()
        y3=duh3.ycor() - 25
        if(x3,y3) not in zidovi:
            duh3.goto(x3,y3)
    if okret==1:          #desno #kretanje duha 4------------------------------------------------------------------------------------------
        x3=duh4.xcor() + 25
        y3=duh4.ycor()
        if(x3,y3) not in zidovi:
            duh4.goto(x3,y3)
    if okret==2:           #gore
        x3=duh4.xcor()
        y3=duh4.ycor() + 25
        if(x3,y3) not in zidovi:
            duh4.goto(x3,y3)
    if okret==3:           #lijevo
        x3=duh4.xcor() - 25
        y3=duh4.ycor()
        if(x3,y3) not in zidovi:
            duh4.goto(x3,y3)
    if okret==4:           #dolje
        x3=duh4.xcor()
        y3=duh4.ycor() - 25
        if(x3,y3) not in zidovi:
            duh4.goto(x3,y3)
    if zivoti == 0: #loser------------------------------------------------------------------------------------------------------------
        duh1.ht()
        duh2.ht()
        duh3.ht()
        duh4.ht()
        time.sleep(1)
        pacman.ht()
        tracer(0)
        deletus.stamp()
        loser()
        exitonclick()
    if bodovi == 20100: #winner------------------------------------------------------------------------------------------------------------
        duh1.ht()
        duh2.ht()
        duh3.ht()
        duh4.ht()
        time.sleep(1)
        pacman.ht()
        tracer(0)
        deletus.stamp()
        winus()
        exitonclick()
        
mainloop()
