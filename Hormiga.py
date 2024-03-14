import turtle
"""
Cruz Pineda Fernando
Hormiga de Langton
Implementacion con diccionarios
"""
def moverse(turtle):
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    
def correr():
    posiciones={}
    #Ventana
    ventana=turtle.Screen()
    ventana.bgcolor('white')
    ventana.screensize(1000,1000)
    #Hormiga
    hormiga = turtle.Turtle()
    hormiga.shape('square')
    hormiga.shapesize(1)
    hormiga.speed(10000)
    while True:
        pos=hormiga.position()
        pos=(round(pos[0],2), round(pos[1],2))
        if pos not in posiciones or posiciones[pos]==0:
            hormiga.color("red")
            hormiga.stamp()
            hormiga.right(90)
            moverse(hormiga)
            posiciones[pos]=1
        elif posiciones[pos]==1:
            hormiga.color("green")
            hormiga.stamp()
            hormiga.left(90)
            moverse(hormiga)
            posiciones[pos]=0



correr()
