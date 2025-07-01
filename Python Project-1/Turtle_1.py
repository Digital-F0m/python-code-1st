import turtle as t
t.speed(20)
t.color("red")
t.bgcolor("black")
b = 200

while b > 0:
    t.left(b)
    t.forward(b * 3)
    b = b - 1


