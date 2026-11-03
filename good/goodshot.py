import pgzrun
width=600
height=600
#Actor - used to load the picture into the display screen 
aln_img= Actor ("alein.png")
aln_img.pos= (101,101)


def draw():
    screen.clear()
    screen.fill("white")

    aln_img.draw()

pgzrun.go()    