from turtle import *
import math

def hearta(k):
	return 15 * math.sin(k) ** 3

def heartb(k):
	return (12 * math.cos(k)
			- 5 * math.cos(2 * k)
			- 2 * math.cos(3 * k)
			- math.cos(4 * k))

speed(0)
bgcolor("black")

# Draw the heart curve
penup()
# move to the first point to avoid drawing a stray line
goto(hearta(0) * 20, heartb(0) * 20)
pendown()
for i in range(6000):
	goto(hearta(i) * 20, heartb(i) * 20)

# reset color and return to center a few times
for j in range(5):
	color("#5A5AF5")
	goto(0, 0)

done()