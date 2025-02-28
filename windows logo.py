#Windows Logo
#importing turtle
from turtle import *
#setting turtle speed
speed (1)
width(4)
#setting background color
color('black')
#setting color to blue
color ('blue')

begin_fill()
penup()
#moving turtle to starting point
goto(-50,60)
pendown()
goto(100,100)
goto(100,-100)
goto(-50,-60)
goto(-50,60)
end_fill()
penup()
color('white')
width(10)
goto(-50,0)
pendown()
goto(100,0)
penup()
goto(25,80)
pendown()
goto(25,-80)
done()
