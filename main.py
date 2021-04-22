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
list_ice = []
list_fire = []
textId = ''


class jeu():
    
    def __init__(self, grille, list_wood, textId):
        self.grille = grille
        self.list_wood = list_wood
        self.textId = textId

    def setGrille(self, grille):
        self.grille = grille
   
    def setVictory(self, textId):
        self.textId = textId

    def getVictory(self):
        return self.textId

    def check(self, event):
        x = canvas.coords(W_image)[0]
        y = canvas.coords(W_image)[1]

       
        i=0
        j=0
        while j < (len(self.grille)):
            while i< len(self.grille[j]):
                if(event.keysym == 'Right'):
                    if (self.grille[j][i]==3 or self.grille[j][i]==1) and ((x == (i*(SIZE/len(self.grille[0]))) - 60) and (y < j*(SIZE/len(self.grille[1]))+110 and y > j*(SIZE/len(self.grille[1]))-60)):
                        return False
                    elif self.grille[j][i]==2 and ((x == (i*(SIZE/len(self.grille[0]))) - 60) and (y < j*(SIZE/len(self.grille[1]))+110 and y > j*(SIZE/len(self.grille[1]))-60)):
                        if (self.grille[j][i+1]!=1 and self.grille[j][i+1]!=2 and (x == (i*(SIZE/len(self.grille[0]))) - 60) and (y < j*(SIZE/len(self.grille[1]))+110 and y > j*(SIZE/len(self.grille[1]))-60)):
                            for p in range(len(self.list_wood)):
                                if(self.list_wood[p] in canvas.find_all()):
                                    if (x+60 == canvas.coords(self.list_wood[p])[0] and (y < canvas.coords(self.list_wood[p])[1]+100 and y > canvas.coords(self.list_wood[p])[1]-20 )):
                                        if(self.grille[j][i+1] == 3):
                                            self.grille[j][i] = 0
                                            self.grille[j][i+1] = 2
                                            canvas.move(self.list_wood[p],SIZE/len(self.grille[j]),0)
                                            self.map(self.grille)
                                        else:
                                            self.grille[j][i] = 0
                                            self.grille[j][i+1] = 2
                                            canvas.move(self.list_wood[p],SIZE/len(self.grille[j]),0)


                elif(event.keysym == 'Left'):
                    if (self.grille[j][i]==3 or self.grille[j][i]==1) and ((x == (i*(SIZE/len(self.grille[0]))) + 80) and (y < j*(SIZE/len(self.grille[1]))+110 and y > j*(SIZE/len(self.grille[1]))-60)):
                        return False
                    elif self.grille[j][i]==2 and ((x == (i*(SIZE/len(self.grille[0]))) + 80) and (y < j*(SIZE/len(self.grille[1]))+110 and y > j*(SIZE/len(self.grille[1]))-60)):
                        if (self.grille[j][i-1]!=1 and self.grille[j][i-1]!=2 and (x == (i*(SIZE/len(self.grille[0]))) + 80) and (y < j*(SIZE/len(self.grille[1]))+110 and y > j*(SIZE/len(self.grille[1]))-60)):
                            for p in range(len(self.list_wood)):
                                if(self.list_wood[p] in canvas.find_all()):
                                    if (x-80 == canvas.coords(self.list_wood[p])[0] and (y < canvas.coords(self.list_wood[p])[1]+100 and y > canvas.coords(self.list_wood[p])[1]-20)):
                                        if(self.grille[j][i-1] == 3):
                                            self.grille[j][i] = 0
                                            self.grille[j][i-1] = 2
                                            canvas.move(self.list_wood[p],-SIZE/len(self.grille[j]),0)
                                            self.map(self.grille)
                                        else:
                                            self.grille[j][i] = 0
                                            self.grille[j][i-1] = 2
                                            canvas.move(self.list_wood[p],-SIZE/len(self.grille[j]),0)


                elif(event.keysym == 'Down'):
                    if (self.grille[j][i]==3 or self.grille[j][i]==1) and ((y == (j*(SIZE/len(self.grille[0]))) - 60) and (x < i*(SIZE/len(self.grille[1]))+80 and x > i*(SIZE/len(self.grille[1]))-60)):
                        return False
                    elif self.grille[j][i]==2 and ((y == (j*(SIZE/len(self.grille[0]))) - 30) and (x < i*(SIZE/len(self.grille[1]))+80 and x > i*(SIZE/len(self.grille[1]))-60)):
                        if (self.grille[j+1][i]!=1 and self.grille[j+1][i]!=2 and (y == (j*(SIZE/len(self.grille[0]))) - 30) and (x < i*(SIZE/len(self.grille[1]))+80 and x > i*(SIZE/len(self.grille[1]))-60)):
                            for p in range(len(self.list_wood)):
                                if(self.list_wood[p] in canvas.find_all()):
                                    if (y+30 == canvas.coords(self.list_wood[p])[1] and (x < canvas.coords(self.list_wood[p])[0]+80 and x > canvas.coords(self.list_wood[p])[0]-60)):
                                        if(self.grille[j+1][i] == 3):
                                            self.grille[j][i] = 0
                                            self.grille[j+1][i] = 2
                                            canvas.move(self.list_wood[p],0,SIZE/len(self.grille[j]))
                                            self.map(self.grille)
                                        else:
                                            self.grille[j][i] = 0
                                            self.grille[j+1][i] = 2
                                            canvas.move(self.list_wood[p],0,SIZE/len(self.grille[j]))
                                    

                    
                elif(event.keysym == 'Up'):
                    if (self.grille[j][i]==3 or self.grille[j][i]==1) and ((y == (j*(SIZE/len(self.grille[0]))) + 120) and (x < i*(SIZE/len(self.grille[1]))+80 and x > i*(SIZE/len(self.grille[1]))-60)):
                        return False
                    elif self.grille[j][i]==2 and ((y == (j*(SIZE/len(self.grille[0]))) + 120) and (x < i*(SIZE/len(self.grille[1]))+80 and x > i*(SIZE/len(self.grille[1]))-60)):
                        if (self.grille[j-1][i]!=1  and self.grille[j-1][i]!=2 and (y == (j*(SIZE/len(self.grille[0]))) + 120) and (x < i*(SIZE/len(self.grille[1]))+80 and x > i*(SIZE/len(self.grille[1]))-60)):
                            for p in range(len(self.list_wood)):
                                if(self.list_wood[p] in canvas.find_all()):
                                    if (y-120 == canvas.coords(self.list_wood[p])[1] and (x < canvas.coords(self.list_wood[p])[0]+50 and x > canvas.coords(self.list_wood[p])[0]-50)):
                                        if(self.grille[j-1][i] == 3):
                                            self.grille[j][i] = 0
                                            self.grille[j-1][i] = 2
                                            canvas.move(self.list_wood[p],0,-SIZE/len(self.grille[j]))
                                            self.map(self.grille)
                                        else:
                                            self.grille[j][i] = 0
                                            self.grille[j-1][i] = 2
                                            canvas.move(self.list_wood[p],0,-SIZE/len(self.grille[j]))
                
                i=i+1
            i=0
            j=j+1



    def droite(self, event):
        if (canvas.coords(W_image)[0]<(SIZE-90) and self.check(event) != False):
            canvas.move(W_image,10,0)

        
    def gauche(self, event):
        if (canvas.coords(W_image)[0]>10 and self.check(event) != False):
            canvas.move(W_image,-10,0)

    def haut(self, event):
        if (canvas.coords(W_image)[1]>10 and self.check(event) != False):
            canvas.move(W_image,0,-10)

    def bas(self, event):
        if (canvas.coords(W_image)[1]<(SIZE-80) and self.check(event) != False):
            canvas.move(W_image,0,10)


    def map(self, grille):
        a=0
        i=0
        j=0

        while j < (len(grille)):
            while i< len(grille[j]):
                if grille[j][i]==1:
                    create_ice = canvas.create_image(i*(SIZE/len(grille[0])),j*(SIZE/len(grille[1])), anchor="nw",image=ice)
                    list_ice.append(create_ice)
                    create_ice
                elif grille[j][i]==2:
                    create_wood = canvas.create_image(i*(SIZE/len(grille[0])),j*(SIZE/len(grille[1])), anchor="nw",image=wood)
                    list_wood.append(create_wood)
                    create_wood
                    canvas.pack() 
                elif grille[j][i]==3:
                    create_fire = canvas.create_image(i*(SIZE/len(grille[0])),j*(SIZE/len(grille[1])), anchor="nw",image=fire)
                    list_fire.append(create_fire)
                    create_fire
                    

                i=i+1
            i=0
            j=j+1


        for i in range(len(grille)):
            for j in range(len(grille[i])):
                if grille[i][j] == 3:
                    a = a + 1

        if a == 0:
            victory = canvas.create_text(SIZE/2,SIZE/2, text="Victoire !!", fill="Red", font=('Pursia', 50))
            self.setVictory(victory)
            victory

        

j = jeu(grille, list_wood, textId)
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

class niveaux():

    def __init__(self, list_fire, list_ice, list_wood, textId):
        self.list_fire = list_fire
        self.list_ice = list_ice
        self.list_wood = list_wood
        self.textId = textId



    def niveau1(self):
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
        self.update(grille)

    def niveau2(self):
        grille = [
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [0, 2, 0, 1, 1, 3, 0, 0, 2, 1],
            [0, 0, 0, 1, 1, 2, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 3, 1, 1, 0, 0, 0, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.update(grille)

    def niveau3(self):
        grille = [
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 3, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 3, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
        ]
        self.update(grille)


    def update(self, grille):
        for i in range(len(list_wood)):
            canvas.delete(list_wood[i])
        for i in range(len(list_ice)):
            canvas.delete(list_ice[i])
        for i in range(len(list_fire)):
            canvas.delete(list_fire[i])

        canvas.coords(W_image,10,10)
        canvas.itemconfigure(j.getVictory(), text='')
        j.setGrille(grille)
        j.map(grille)
        



n = niveaux(list_fire, list_ice, list_wood, textId)
mainmenu = Menu(root)
first_menu = Menu(mainmenu, tearoff=0)
first_menu.add_command(label='Niveau 1', command=n.niveau1)
first_menu.add_separator()
first_menu.add_command(label='Niveau 2', command=n.niveau2)
first_menu.add_separator()
first_menu.add_command(label='Niveau 3', command=n.niveau3)
mainmenu.add_cascade(label='Niveaux', menu=first_menu)
root.config(menu=mainmenu)

# NW=Nord West, le coin haut guche de l'image sera positionne a (10,10):
canvas.create_image(0,0, image=bg,  anchor="nw")
W_image=canvas.create_image(10,10,anchor=NW,image=img_2)

# Quitter
Bouton_Quitter=Button(root, text ='Quitter', command = root.destroy)
Bouton_Quitter.pack()
 
#On associe les fleches du clavier aux fonctions de déplacement:
canvas.bind_all('<Right>', j.droite)
canvas.bind_all('<Left>', j.gauche)
canvas.bind_all('<Up>', j.haut)
canvas.bind_all('<Down>', j.bas)

       

j.map(grille)
root.mainloop()


