# EtchSketch
An Etch-A-Sketch tool using the turtle module in Python allows users to draw on a screen by controlling a "turtle" that moves around, creating lines as it goes. The user can guide the turtle in different directions using the keyboard (e.g., arrow keys), simulating the classic Etch-A-Sketch experience. The tool typically involves simple commands for moving forward, backward, left, and right, with an option to clear the screen and start fresh. This basic setup helps users learn interactive graphics programming in Python.




forward(distance): Moves the turtle forward by the specified distance in the direction it's facing.
backward(distance): Moves the turtle backward by the specified distance in the direction opposite to where it's facing.
setheading(angle): Sets the turtle's orientation to the specified angle (0 degrees is to the right, 90 is upward, etc.).
clear(): Clears the drawing on the screen but keeps the turtle in the same position.
penup(): Lifts the turtle’s pen, so it moves without drawing.
pendown(): Lowers the turtle’s pen, so it resumes drawing as it moves.
home(): Moves the turtle to the origin (center of the screen), and resets its orientation to face right.

listen(): Puts the program in a state where it listens for keyboard inputs.
onkey(fun, key): Binds a function to a specific key. When the specified key is pressed, the associated function is executed.
