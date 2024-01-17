import turtle

def draw_rainbow_circle():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    turtle.speed(0) # Speed=max

    for i in range(180):
        for color in colors:
            turtle.color(color)
            turtle.forward(2)
            turtle.right(1)
        turtle.right(2)

    turtle.done()

draw_rainbow_circle()

def draw_rainbow_square(length=50):
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    turtle.speed(0) #speed=max

    for i in range(4):  # Loop for each side of the square
        for color in colors:
            turtle.color(color)
            for _ in range(length // len(colors)):
                turtle.forward(1)  # Move forward in small steps to create the rainbow effect
        turtle.right(90)  # Turn right by 90 degrees to make a square

    turtle.done()

draw_rainbow_square()