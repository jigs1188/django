import turtle

# Create a Turtle object
pen = turtle.Turtle()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("silver")  # Set background color to yellowish-green

# Customize the pen for drawing the heart
pen.shape("turtle")
pen.color("red")
pen.fillcolor("red")
pen.speed(1)

# Draw the heart shape
pen.begin_fill()
pen.fillcolor("red")
pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)
pen.end_fill()

# Customize the pen for writing inside the heart (aquaish color)
pen.color("silver")  # Change color to aquamarine or any desired aquaish color
pen.penup()
pen.goto(0, 80)  # Adjust the position for writing

# Write "It's you" in the heart
pen.write("It's you", align="center", font=("Arial", 20, "bold"))

# Hide the turtle
pen.hideturtle()

# Close the window when clicked
screen.exitonclick()
