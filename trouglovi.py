import turtle

def nacrtajTrougao(tacka, t):
    t.up()
    t.begin_fill()
    t.goto(tacka[0][0], tacka[0][1])
    t.down()
    t.goto(tacka[1][0], tacka[1][1])
    t.goto(tacka[2][0], tacka[2][1])
    t.goto(tacka[0][0], tacka[0][1])
    t.end_fill()

def sredina(p1,p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def fraktal(tacka, stepen, t):
    nacrtajTrougao(tacka, t)
    if stepen > 0:
        fraktal([tacka[0],
                 sredina(tacka[0], tacka[1]),
                 sredina(tacka[0], tacka[2])],
                stepen - 1, t)
        fraktal([tacka[1],
                 sredina(tacka[0], tacka[1]),
                 sredina(tacka[1], tacka[2])],
                stepen - 1, t)
        fraktal([tacka[2],
                 sredina(tacka[2], tacka[1]),
                 sredina(tacka[0], tacka[2])],
                stepen - 1, t)

def main():
   t = turtle.Turtle()
   t.color('black', 'red')
   t.pensize(2)
   t.shape()
   t.speed(10)
   kraj = turtle.Screen()
   k = input("unesi velicinu (500): ")
   k = int(k)
   tacke = [[-k*0.86,-k/1.5],[0,k/1.5],[k*0.86 ,-k/1.5
                                      ]]
   stepen = input("unesi stepen: ")
   stepen = int(stepen)

   fraktal(tacke,stepen,t)
   kraj.exitonclick()

main()











