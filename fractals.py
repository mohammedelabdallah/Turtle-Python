## ELABDALLAH_KROL
from turtle import *
import turtle


def zigzag(l,n):
    for i in range(n):
        if i ==0:
            turtle.left(45)
            turtle.forward(l)
        elif i%2==0:
            turtle.right(90)
            turtle.forward(l)
        else:
            turtle.left(90)
            turtle.forward(l)
            

            
def koch(l, n):
    l=l*1.5
    if n == 0:
        forward(l)
    else:
        koch(l/3, n-1)
        turtle.left(60)
        koch(l/3, n-1)
        turtle.right(120)
        koch(l/3, n-1)
        turtle.left(60)
        koch(l/3, n-1)
 

def flocon(l, n):
    koch(l, n)
    turtle.right(120)
    koch(l, n)
    turtle.right(120)
    koch(l, n)
 
 

import math
def cesaro(L,n):
    L=L/(2*(math.cos(math.radians(80)))+1)
    if n ==0:
         turtle.forward(L)
    else:
        cesaro(L,n-1)
        turtle.left(80)
        cesaro(L,n-1)
        turtle.right(160)
        cesaro(L,n-1)
        turtle.left(80)
        cesaro(L,n-1)
        
def carre_cesaro(l,n):
    for i in range(4):
        cesaro(l,n)
        turtle.left(90)

def sierpinski(l,n):
    if n==0:
        turtle.forward(l)
        turtle.left(120)
        turtle.forward(l)
        turtle.left(120)
        turtle.forward(l)
        turtle.left(120)
            
       
    else:
        sierpinski(l/2,n-1)
        turtle.forward(l/2)
        sierpinski(l/2,n-1)
        turtle.backward(l/2)
        turtle.left(60)
        turtle.forward(l/2)
        turtle.right(60)
        sierpinski(l/2,n-1)
        turtle.left(60)
        turtle.backward(l/2)
        turtle.right(60)



    
    
