from turtle import *

speed(70)

def f(length, depth):
   if depth == 0:
      forward(length)
   else:
      f(length/3, depth-1)
      right(60)
      f(length/3, depth-1)
      left(120)
      f(length/3, depth-1)
      right(60)
      f(length/3, depth-1)

for i in range(6):
   f(200,4)
   right(60)
