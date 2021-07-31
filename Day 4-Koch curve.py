# Author: Gan Li
# Date: 7/31/21 1:31 下午
# Description: Chap 5 exercise 5
from __future__ import print_function, division

import turtle

t = turtle.Turtle()
t.pu()
t.pd()
angle = 60


def koch(t, n):
    if n < 3:
        t.forward(n)
        return
    x = n / 3
    koch(t, x)
    t.left(angle)
    koch(t, x)
    t.right(2 * angle)
    koch(t, x)
    t.left(angle)
    koch(t, x)


def snowflake(t, n):
    for i in range(3):
        koch(t, n)
        t.right(2 * angle)


snowflake(t, 60)

turtle.mainloop()
