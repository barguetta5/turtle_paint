import turtle as t
import random
import colorgram
#
# colores = []
# colors = colorgram.extract('rainbow-waves-background-free-vector.jpg', 6)
# print('[',end="")
# for i in range(6):
#     r = colors[i].rgb.r
#     b = colors[i].rgb.b
#     g = colors[i].rgb.g
#     new_color = (r,b,g)
#     colores.append(new_color)
#
# print(colores)

t.colormode(255)
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
(134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
(232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
(19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
(176, 192, 208), (168, 99, 102)]

turtle = t.Turtle()
turtle.penup()
turtle.setheading(220)
turtle.forward(400)
turtle.setheading(0)
turtle.speed("fastest")
for j in range(24):
    for i in range(32):
        turtle.dot(20,random.choice(color_list))
        turtle.forward(20)
    turtle.setheading(178)
    turtle.forward(640)
    # turtle.dot(20,random.choice(color_list))
    turtle.setheading(0)



screen = t.Screen()
screen.exitonclick()