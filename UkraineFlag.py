import turtle

turtle.title("Ukraine Flag - BY Rauf")

def rectangle(height, widht, color):
    turtle.pencolor("white")
    turtle.fillcolor(color)
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(widht)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

rectangle(90, 300, "#FFD700")
turtle.left(90)
turtle.forward(90)
turtle.right(90)

rectangle(90, 300, "#0057B8")
turtle.left(90)
turtle.forward(90)
turtle.right(90)

turtle.done()