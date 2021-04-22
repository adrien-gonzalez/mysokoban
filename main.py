import sys
from tkinter import *

SIZE = 800
grille = [
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 3, 0, 2, 0],
    [0, 0, 0, 2, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 2, 0, 0, 1],
    [1, 1, 3, 0, 0, 0, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],

]
list_wood = []



def check(event):
    x = canvas.coords(W_image)[0]
    y = canvas.coords(W_image)[1]

    i=0
    j=0
    while j < (len(grille)):
        while i< len(grille[j]):
            if(event.keysym == 'Right'):
                if (grille[j][i]==3 or grille[j][i]==1) and ((x == (i*(SIZE/len(grille[0]))) - 60) and (y < j*(SIZE/len(grille[1]))+110 and y > j*(SIZE/len(grille[1]))-60)):
                    return False
                elif grille[j][i]==2 and ((x == (i*(SIZE/len(grille[0]))) - 60) and (y < j*(SIZE/len(grille[1]))+110 and y > j*(SIZE/len(grille[1]))-60)):
                    if (grille[j][i+1]!=1 and grille[j][i+1]!=2 and (x == (i*(SIZE/len(grille[0]))) - 60) and (y < j*(SIZE/len(grille[1]))+110 and y > j*(SIZE/len(grille[1]))-60)):
                        for p in range(len(list_wood)):
                            if (x+60 == canvas.coords(list_wood[p])[0] and (y < canvas.coords(list_wood[p])[1]+100 and y > canvas.coords(list_wood[p])[1]-20 )):
                                if(grille[j][i+1] == 3):
                                    grille[j][i] = 0
                                    grille[j][i+1] = 2
                                    canvas.move(list_wood[p],SIZE/len(grille[j]),0)
                                    map(grille)
                                else:
                                    grille[j][i] = 0
                                    grille[j][i+1] = 2
                                    canvas.move(list_wood[p],SIZE/len(grille[j]),0)


            elif(event.keysym == 'Left'):
                if (grille[j][i]==3 or grille[j][i]==1) and ((x == (i*(SIZE/len(grille[0]))) + 80) and (y < j*(SIZE/len(grille[1]))+110 and y > j*(SIZE/len(grille[1]))-60)):
                    return False
                elif grille[j][i]==2 and ((x == (i*(SIZE/len(grille[0]))) + 80) and (y < j*(SIZE/len(grille[1]))+110 and y > j*(SIZE/len(grille[1]))-60)):
                    if (grille[j][i-1]!=1 and grille[j][i-1]!=2 and (x == (i*(SIZE/len(grille[0]))) + 80) and (y < j*(SIZE/len(grille[1]))+110 and y > j*(SIZE/len(grille[1]))-60)):
                        for p in range(len(list_wood)):
                            if (x-80 == canvas.coords(list_wood[p])[0] and (y < canvas.coords(list_wood[p])[1]+100 and y > canvas.coords(list_wood[p])[1]-20)):
                                if(grille[j][i-1] == 3):
                                    grille[j][i] = 0
                                    grille[j][i-1] = 2
                                    canvas.move(list_wood[p],-SIZE/len(grille[j]),0)
                                    map(grille)
                                else:
                                    grille[j][i] = 0
                                    grille[j][i-1] = 2
                                    canvas.move(list_wood[p],-SIZE/len(grille[j]),0)


            elif(event.keysym == 'Down'):
                if (grille[j][i]==3 or grille[j][i]==1) and ((y == (j*(SIZE/len(grille[0]))) - 60) and (x < i*(SIZE/len(grille[1]))+80 and x > i*(SIZE/len(grille[1]))-60)):
                    return False
                elif grille[j][i]==2 and ((y == (j*(SIZE/len(grille[0]))) - 30) and (x < i*(SIZE/len(grille[1]))+80 and x > i*(SIZE/len(grille[1]))-60)):
                    if (grille[j+1][i]!=1 and grille[j+1][i]!=2 and (y == (j*(SIZE/len(grille[0]))) - 30) and (x < i*(SIZE/len(grille[1]))+80 and x > i*(SIZE/len(grille[1]))-60)):
                        for p in range(len(list_wood)):
                            if (y+30 == canvas.coords(list_wood[p])[1] and (x < canvas.coords(list_wood[p])[0]+80 and x > canvas.coords(list_wood[p])[0]-60)):
                                if(grille[j+1][i] == 3):
                                    grille[j][i] = 0
                                    grille[j+1][i] = 2
                                    canvas.move(list_wood[p],0,SIZE/len(grille[j]))
                                    map(grille)
                                else:
                                    grille[j][i] = 0
                                    grille[j+1][i] = 2
                                    canvas.move(list_wood[p],0,SIZE/len(grille[j]))
                                

                
            elif(event.keysym == 'Up'):
                if (grille[j][i]==3 or grille[j][i]==1) and ((y == (j*(SIZE/len(grille[0]))) + 120) and (x < i*(SIZE/len(grille[1]))+80 and x > i*(SIZE/len(grille[1]))-60)):
                    return False
                elif grille[j][i]==2 and ((y == (j*(SIZE/len(grille[0]))) + 120) and (x < i*(SIZE/len(grille[1]))+80 and x > i*(SIZE/len(grille[1]))-60)):
                    if (grille[j-1][i]!=1  and grille[j-1][i]!=2 and (y == (j*(SIZE/len(grille[0]))) + 120) and (x < i*(SIZE/len(grille[1]))+80 and x > i*(SIZE/len(grille[1]))-60)):
                        for p in range(len(list_wood)):
                            if (y-120 == canvas.coords(list_wood[p])[1] and (x < canvas.coords(list_wood[p])[0]+50 and x > canvas.coords(list_wood[p])[0]-50)):
                                if(grille[j-1][i] == 3):
                                    grille[j][i] = 0
                                    grille[j-1][i] = 2
                                    canvas.move(list_wood[p],0,-SIZE/len(grille[j]))
                                    map(grille)
                                else:
                                    grille[j][i] = 0
                                    grille[j-1][i] = 2
                                    canvas.move(list_wood[p],0,-SIZE/len(grille[j]))
            
            i=i+1
        i=0
        j=j+1


def droite(event):
    if (canvas.coords(W_image)[0]<(SIZE-90) and check(event) != False):
        canvas.move(W_image,10,0)

    
def gauche(event):
    if (canvas.coords(W_image)[0]>10 and check(event) != False):
        canvas.move(W_image,-10,0)

def haut(event):
    if (canvas.coords(W_image)[1]>10 and check(event) != False):
        canvas.move(W_image,0,-10)

def bas(event):
    if (canvas.coords(W_image)[1]<(SIZE-80) and check(event) != False):
        canvas.move(W_image,0,10)


root = Tk()
imgfile = 'img/perso.png'
# Utilisation d'un dictionnaire pour conserver une reference:
gifsdict={}

# #Creation de l'image:
img = PhotoImage(file = imgfile)
ice = PhotoImage(file = 'img/ice.png')
wood = PhotoImage(file = 'img/wood.png')
fire = PhotoImage(file = 'img/fire.png')
bg = PhotoImage(file = 'img/fond.png')
gifsdict[imgfile] = img
img_2 = img.subsample(3, 3)

# #Creation du canvas:
canvas = Canvas(root, height=SIZE, width=SIZE)
root.title("My Sokoban")
canvas.pack(padx=10,pady=10)

def niveaux():
    grille = [
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 3, 0, 2, 0],
        [0, 0, 0, 2, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 2, 0, 0, 1],
        [1, 1, 3, 0, 0, 0, 3, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]
    map(grille)

mainmenu = Menu(root)
first_menu = Menu(mainmenu)
first_menu.add_command(label='Niveau 1', command=niveaux)
first_menu.add_command(label='Niveau 2')
first_menu.add_command(label='Niveau 3')
mainmenu.add_cascade(label='Niveaux', menu=first_menu)
root.config(menu=mainmenu)

# NW=Nord West, le coin haut guche de l'image sera positionne a (10,10):
canvas.create_image(0,0, image=bg,  anchor="nw")
W_image=canvas.create_image(10,10,anchor=NW,image=img_2)

# Quitter
Bouton_Quitter=Button(root, text ='Quitter', command = root.destroy)
Bouton_Quitter.pack()
 
#On associe les fleches du clavier aux fonctions de déplacement:
canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
canvas.bind_all('<Up>', haut)
canvas.bind_all('<Down>', bas)


def map(grille):
    a=0
    i=0
    j=0

    while j < (len(grille)):
        while i< len(grille[j]):
            if grille[j][i]==1:
                create_ice = canvas.create_image(i*(SIZE/len(grille[0])),j*(SIZE/len(grille[1])), anchor="nw",image=ice)
                create_ice
            elif grille[j][i]==2:
                create_wood = canvas.create_image(i*(SIZE/len(grille[0])),j*(SIZE/len(grille[1])), anchor="nw",image=wood)
                list_wood.append(create_wood)
                create_wood
                canvas.pack() 
            elif grille[j][i]==3:
                create_fire = canvas.create_image(i*(SIZE/len(grille[0])),j*(SIZE/len(grille[1])), anchor="nw",image=fire)
                create_fire
                

            i=i+1
        i=0
        j=j+1

    
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == 3:
                a = a + 1

    if a == 0:
        canvas.create_text(SIZE/2,SIZE/2, text="Victoire !!", fill="Red", font=('Pursia', 50))
       

map(grille)
root.mainloop()