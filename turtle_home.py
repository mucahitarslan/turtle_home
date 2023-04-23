import turtle

pencere = turtle.Screen()
pencere.bgcolor("skyblue")
pen = turtle.Turtle()

pen.penup()
pen.setpos(-100, 0)  
pen.pendown()

#evin govdesi
pen.color("grey")
pen.fillcolor("grey")
pen.begin_fill()

for i in range(4):
    pen.forward(200)    
    pen.right(90)

pen.end_fill()

#evin çatısı
pen.color("red")
pen.fillcolor("red")
pen.begin_fill()

for a in range(3):

    pen.forward(200)
    pen.left(120)

pen.end_fill()    


pen.penup()  
pen.setpos(-25, -200)
pen.pendown()

# Kapının ana gövdesi
pen.color("brown")
pen.begin_fill()
for i in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
pen.end_fill()

# Kapı kolu
pen.penup()
pen.goto(-25, -150)
pen.pendown()
pen.color("black")
pen.pensize(3)
pen.forward(20)

#pencere çizimi
pen.penup()
pen.goto(-80, -40)
pen.pendown()
pen.color("white")
pen.begin_fill()

for i in range(4):
    pen.forward(50)
    pen.right(90)
pen.end_fill()

pen.penup()
pen.goto(30, -40)
pen.pendown()
pen.color("white")
pen.begin_fill()

for i in range(4):
    pen.forward(50)
    pen.right(90)
pen.end_fill()


pen.hideturtle()
pencere.exitonclick()
pencere.mainloop()

