import turtle

"""Cruz Pineda Fernando
Hormiga de Langton
Implementacion con arreglo
"""
def moverse(turtle):
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

def correr():
    # Tamaño de la cuadrícula
    GRID_SIZE = 10000

    # Inicializar la cuadrícula
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    # Ventana
    ventana = turtle.Screen()
    ventana.bgcolor('white')
    ventana.screensize(1000, 1000)

    # Hormiga
    hormiga = turtle.Turtle()
    hormiga.shape('square')
    hormiga.shapesize(1)
    hormiga.speed(10000)
    x, y = GRID_SIZE // 2, GRID_SIZE // 2  # Posición inicial
    direccion = 0  # Dirección inicial (0: arriba, 1: derecha, 2: abajo, 3: izquierda)
    while True:
        # Cambiar color de la hormiga
        if grid[y][x] == 0:
            hormiga.color("red")
            direccion = (direccion + 1) % 4
        else:
            hormiga.color("green")
            direccion = (direccion - 1) % 4

        # Actualizar la cuadrícula
        grid[y][x] = 1 - grid[y][x]

        # Mover la hormiga
        if direccion == 0:
            y -= 1
        elif direccion == 1:
            x += 1
        elif direccion == 2:
            y += 1
        elif direccion == 3:
            x -= 1

        # Evitar que la hormiga salga de la cuadrícula
        x = max(0, min(x, GRID_SIZE - 1))
        y = max(0, min(y, GRID_SIZE - 1))

        # Dibujar la celda
        hormiga.goto((x - GRID_SIZE // 2) * 10, (y - GRID_SIZE // 2) * 10)
        hormiga.stamp()

correr()
