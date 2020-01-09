import turtle

t = turtle.Turtle()
t.color("white")
t.pensize(2)
t.shape('turtle')
t.speed(0)
t.goto(-300,200)

def fraktalZvezda(i, k):
    if k == 0:
        t.forward(i)
    else:
        fraktalZvezda(i, k-1)
        t.left(60)
        fraktalZvezda(i, k-1)
        t.right(120)
        fraktalZvezda(i, k-1)
        t.left(60)
        fraktalZvezda(i, k-1)

def nacrtajFraktal(i,n):
    fraktalZvezda(i,n)
    t.right(120)
    fraktalZvezda(i,n)
    t.right(120)
    fraktalZvezda(i,n)



korak = float(input("unesite korak: "))
stepen = int(input('Unesi stepen: '))

kraj = turtle.Screen()

t.color('black', 'red')
t.begin_fill()
nacrtajFraktal(korak,stepen)
t.end_fill()

kraj.exitonclick()











