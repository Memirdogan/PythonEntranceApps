import turtle as t
import random as rd

t.bgcolor("yellow")

# caterpillar
caterpillar = t.Turtle()
caterpillar.shape("square")
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

# leaf
leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape("leaf", leaf_shape)
leaf.shape("leaf")
leaf.color("green")
leaf.penup()
leaf.hideturtle()
leaf.speed()

# game
game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align='center', font=('Arial', 18, 'bold'))
text_turtle.hideturtle()

# score
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)


