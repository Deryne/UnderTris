## Ce programme est un Tetris combiné avec des boss de niveaux


from tkinter import *
# Extension pour afficher des images

from time import sleep
#Extension utile pour demander au programme de faire des pauses

from random import randrange
#Extension servant à importer le caractère aléatoire

import pygame
# Extension pour la musique



#-------------------------------------------------------------------------------
# Code pour insérer la musique en boucle
pygame.init()

#On initialise pour la musique
fenetre = pygame.display.set_mode((3,3))

#Ouverture d'une fenêtre pour le son
pygame.mixer.init()
son = pygame.mixer.Sound('Casse-noisette.wav')
son.play(loops=-1, maxtime=0, fade_ms=0)

#-------------------------------------------------------------------------------

### Entrée : niveau, score, img, nom_boss, vie, parole
### Sortie : Affichage d'un tableau, des pièces, des images, des textes
### Fonction : Elle a pour but de faire débuter la partie et d'afficher les\
# différents éléments

def début(niveau=1,score=0,img='Toriel7.gif',nom_boss="Toriel",\
                       vie=1200,parole="Je te briserai les os !"):
    
    global tableau_canvas,tableau_grille,tableau_couleur,coord_normales,Piece,label_vie,\
           label_nom,score_score,Points_de_vie,level
    
    # On insère les variables des paramètres dans la fonction
    
    score_score = score
    Points_de_vie = vie
    level = niveau
    image = img

    # Tableau de couleur pour les pièces
    
    tableau_couleur=['gray100','green3','goldenrod','red','dark turquoise','dark orchid',\
                 'DarkOrange','pale violet red']

    # On crée d'un tableau de 20 lignes et 10 colonnes avec sa matrice
    # On définit les pièces et leurs positions en fonction de coordonnées
    
    tableau_canvas=[]
    tableau_grille=[]
    for i in range(20):
        tableau_canvas.append([[]]*10)
        tableau_grille.append([[]]*10)

    grille_jeu = Frame(fen)
    for ligne in range(20):
        for colonne in range(10):
            couleur = tableau_couleur[0]
            tableau_canvas[ligne][colonne] = Canvas(grille_jeu,bg=couleur,height=20,
                                           width=20,borderwidth=1,relief=FLAT)
            tableau_canvas[ligne][colonne].grid(row=ligne,column=colonne)
            tableau_grille[ligne][colonne] = 0
            
    

    #------------------------------------
    # On crée 4 positions pour chaque pièces qui sont au nombre de 7
     

    Piece1 =[[(0,1,0,0),(0,1,1,0),(0,0,1,0),(0,0,0,0)],         #0 1 0 0
                   [(0,0,0,0),(0,0,1,1),(0,1,1,0),(0,0,0,0)],   #0 1 1 0 
                   [(0,1,0,0),(0,1,1,0),(0,0,1,0),(0,0,0,0)],   #0 0 1 0 
                   [(0,0,0,0),(0,0,1,1),(0,1,1,0),(0,0,0,0)]]   #0 0 0 0

    Piece2 = [[(0,2,2,0),(0,2,2,0),(0,0,0,0),(0,0,0,0)],        # 0 2 2 0
                 [(0,2,2,0),(0,2,2,0),(0,0,0,0),(0,0,0,0)],     # 0 2 2 0
                 [(0,2,2,0),(0,2,2,0),(0,0,0,0),(0,0,0,0)],     # 0 0 0 0
                 [(0,2,2,0),(0,2,2,0),(0,0,0,0),(0,0,0,0)]]     # 0 0 0 0

    Piece3 = [[(0,3,0,0),(0,3,0,0),(0,3,0,0),(0,3,0,0)],        # 0 3 0 0
                [(3,3,3,3),(0,0,0,0),(0,0,0,0),(0,0,0,0)],      # 0 3 0 0
                [(0,3,0,0),(0,3,0,0),(0,3,0,0),(0,3,0,0)],      # 0 3 0 0
                [(3,3,3,3),(0,0,0,0),(0,0,0,0),(0,0,0,0)]]      # 0 3 0 0

    Piece4 = [[(0,0,4,0),(0,4,4,0),(0,4,0,0),(0,0,0,0)],        # 0 0 4 0
                 [(0,0,0,0),(0,4,4,0),(0,0,4,4),(0,0,0,0)],     # 0 4 4 0
                 [(0,0,4,0),(0,4,4,0),(0,4,0,0),(0,0,0,0)],     # 0 4 0 0
                 [(0,0,0,0),(0,4,4,0),(0,0,4,4),(0,0,0,0)]]     # 0 0 0 0

    Piece5 = [[(0,5,0,0),(0,5,5,0),(0,5,0,0),(0,0,0,0)],        # 0 5 0 0
                 [(0,0,0,0),(0,0,5,0),(0,5,5,5),(0,0,0,0)],     # 0 5 5 0
                 [(0,0,0,5),(0,0,5,5),(0,0,0,5),(0,0,0,0)],     # 0 5 0 0
                 [(0,5,5,5),(0,0,5,0),(0,0,0,0),(0,0,0,0)]]     # 0 0 0 0

    Piece6 = [[(0,0,6,0),(0,0,6,0),(0,6,6,0),(0,0,0,0)],        # 0 0 6 0
                 [(0,0,0,0),(0,6,6,6),(0,0,0,6),(0,0,0,0)],     # 0 0 6 0
                 [(0,6,6,0),(0,6,0,0),(0,6,0,0),(0,0,0,0)],     # 0 6 6 0
                 [(0,0,0,0),(0,6,0,0),(0,6,6,6),(0,0,0,0)]]     # 0 0 0 0

    Piece7 = [[(0,7,0,0),(0,7,0,0),(0,7,7,0),(0,0,0,0)],        # 0 7 0 0
                 [(0,0,0,0),(0,0,0,7),(0,7,7,7),(0,0,0,0)],     # 0 7 0 0
                 [(0,7,7,0),(0,0,7,0),(0,0,7,0),(0,0,0,0)],     # 0 7 7 0
                 [(0,0,0,0),(0,7,7,7),(0,7,0,0),(0,0,0,0)]]     # 0 0 0 0

    # On tire une première pièce de manière aléatoire entre 1 et 7
    tab_Pieces =(Piece1,Piece2,Piece3,Piece4,Piece5,Piece6,Piece7)
    n = randrange(1,7)
    Piece = tab_Pieces[n]

    #------------------------------------
    #On crée un bandeau noir à gauche de la grille
    
    grille_jeu.grid(row=1,column=0)
    boss = Frame(fen,bg='gray14',width=200,height=605) 
    frame_suivante = Frame(boss,bg='green')
    frame_suivante = Canvas(width = 1, height = 1, bg = 'gray1')

    #On insère dedans l'image bu boss "img" fixé dans les paramètres de départ
    
    photo = PhotoImage(file = img )
    item_boss = frame_suivante.create_image(70, 155, image = photo)
    
    # On paramètre la taille et la place de l'image en format gif
    frame_suivante.place(x=272,y=70,width=140,height=300)
    boss.grid(row=1,column=1)
    
    #------------------------------------
    # On ajoute le logo "UnderTris" de la même manière
    
    frame_titre = Frame(boss, bg='red',width=200,height=200)
    logo = PhotoImage(file = "Titre4.gif")
    frame_titre = Canvas(width = 10, height = 1, bg = 'gray1')
    titre_projet = frame_titre.create_image(125, 23, image = logo)
    frame_titre.place(x=0,y=0,width=260,height=45)
    
    #---------
    # On insère aussi le nom du boss
    
    label_nom = Label(boss,text="BOSS\n"+str(nom_boss),
                             fg='white',font="Century 13 normal bold",
                                                  bg='gray1',relief=RIDGE)
    label_nom.place(x=23,y=9,width=120,height=45)
    
    #---------
    # On insère les points de vie
    
    label_vie = Label(boss,text="PTS DE VIE\n"+str(Points_de_vie),
                             fg='white',font="Century 13 normal bold",
                                                  bg='gray1',relief=RIDGE)
    label_vie.place(x=22,y=394,width=120,height=45)
    
    #---------
    # On insère le niveau du joueur
    
    label_niveau = Label(boss,text="NIVEAU\n"+str(niveau),
                             fg='white',font="Century 13 normal bold",
                                                  bg='gray1',relief=RIDGE)
    label_niveau.place(x=23,y=444,width=120,height=45)

    #---------
    # On insère les paroles du boss
    
    label_parole= Label(boss,text="DIT: \n"+str(parole),
                        fg='white',font="Century 11 normal",
                                            bg='gray1',relief=RIDGE)
    label_parole.place(x=2,y=505,width=160,height=40)
    
    #------------------------------------
    # On définit les touches utilisées pour jouer en ajoutant une fonction qui\
    # se déclenchera à chaque pression de la touche
    
    fen.bind('<Right>',droite)
    fen.bind('<Left>',gauche)
    fen.bind('<Up>',tourne)
    fen.bind('<Down>',tombe)    
    fen.bind('<KeyRelease-Down>',relache_bas)
    
    maj_Grille()
    nvelle_Piece()
    mainloop()
       
#---------------------------------------------------------------------------
### Entrée : Piece,can_Piece_apres
### Sortie : Pièce alétoire suivante
### Fonction : Elle a pour but de tirer la deuxième pièce alétoire
    
def tirage():
    
    global Piece,can_Piece_apres

    Piece1 =[[(0,1,0,0),(0,1,1,0),(0,0,1,0),(0,0,0,0)],         #0 1 0 0
                   [(0,0,0,0),(0,0,1,1),(0,1,1,0),(0,0,0,0)],   #0 1 1 0 
                   [(0,1,0,0),(0,1,1,0),(0,0,1,0),(0,0,0,0)],   #0 0 1 0 
                   [(0,0,0,0),(0,0,1,1),(0,1,1,0),(0,0,0,0)]]   #0 0 0 0

    Piece2 = [[(0,2,2,0),(0,2,2,0),(0,0,0,0),(0,0,0,0)],        # 0 2 2 0
                 [(0,2,2,0),(0,2,2,0),(0,0,0,0),(0,0,0,0)],     # 0 2 2 0
                 [(0,2,2,0),(0,2,2,0),(0,0,0,0),(0,0,0,0)],     # 0 0 0 0
                 [(0,2,2,0),(0,2,2,0),(0,0,0,0),(0,0,0,0)]]     # 0 0 0 0

    Piece3 = [[(0,3,0,0),(0,3,0,0),(0,3,0,0),(0,3,0,0)],        # 0 3 0 0
                [(3,3,3,3),(0,0,0,0),(0,0,0,0),(0,0,0,0)],      # 0 3 0 0
                [(0,3,0,0),(0,3,0,0),(0,3,0,0),(0,3,0,0)],      # 0 3 0 0
                [(3,3,3,3),(0,0,0,0),(0,0,0,0),(0,0,0,0)]]      # 0 3 0 0

    Piece4 = [[(0,0,4,0),(0,4,4,0),(0,4,0,0),(0,0,0,0)],        # 0 0 4 0
                 [(0,0,0,0),(0,4,4,0),(0,0,4,4),(0,0,0,0)],     # 0 4 4 0
                 [(0,0,4,0),(0,4,4,0),(0,4,0,0),(0,0,0,0)],     # 0 4 0 0
                 [(0,0,0,0),(0,4,4,0),(0,0,4,4),(0,0,0,0)]]     # 0 0 0 0

    Piece5 = [[(0,5,0,0),(0,5,5,0),(0,5,0,0),(0,0,0,0)],        # 0 5 0 0
                 [(0,0,0,0),(0,0,5,0),(0,5,5,5),(0,0,0,0)],     # 0 5 5 0
                 [(0,0,0,5),(0,0,5,5),(0,0,0,5),(0,0,0,0)],     # 0 5 0 0
                 [(0,5,5,5),(0,0,5,0),(0,0,0,0),(0,0,0,0)]]     # 0 0 0 0

    Piece6 = [[(0,0,6,0),(0,0,6,0),(0,6,6,0),(0,0,0,0)],        # 0 0 6 0
                 [(0,0,0,0),(0,6,6,6),(0,0,0,6),(0,0,0,0)],     # 0 0 6 0
                 [(0,6,6,0),(0,6,0,0),(0,6,0,0),(0,0,0,0)],     # 0 6 6 0
                 [(0,0,0,0),(0,6,0,0),(0,6,6,6),(0,0,0,0)]]     # 0 0 0 0

    Piece7 = [[(0,7,0,0),(0,7,0,0),(0,7,7,0),(0,0,0,0)],        # 0 7 0 0
                 [(0,0,0,0),(0,0,0,7),(0,7,7,7),(0,0,0,0)],     # 0 7 0 0
                 [(0,7,7,0),(0,0,7,0),(0,0,7,0),(0,0,0,0)],     # 0 7 7 0
                 [(0,0,0,0),(0,7,7,7),(0,7,0,0),(0,0,0,0)]]     # 0 0 0 0


    # On tire une première pièce de manière aléatoire entre 1 et 7
    tab_Pieces =(Piece1,Piece2,Piece3,Piece4,Piece5,Piece6,Piece7)
    index = randrange(0,len(tab_Pieces))
    Piece  = tab_Pieces[index]
    
#-------------------------------------------------------------------------------    
### Entrée : coord_normales,sens,vitesse_normale,vitesse,level
### Sortie : Affichage score, vitesse
### Fonction : Elle a pour but de définir une vitesse en fonction du niveau\
    # et d'arrêter le jeu quand le joueur a perdu

def nvelle_Piece():

    global coord_normales,sens,vitesse_normale,vitesse,level

    vitesse_normale = 550 - (level*50)
    coord_normales = [0,3]
    sens = 0
    sleep(1)
    tirage()
    if not Mouvement_verif(0,0,0):
        print_Piece(sens)
        # On arrêre la musique
        son.stop()
        def fairetoplevel() :
            top=Toplevel(root)
            lab=Label(top, text=score_score, bg="gray100")
            lab.place(x=0,y=0,width=260,height=45)
            top.geometry("%dx%d%+d%+d" % (424,560,26,26))
            lab.pack()

        root = Tk()
        root.geometry("%dx%d%+d%+d" % (24,60,26,26)) #modifie la taille fen
        go=Button (root , text="SCORE" , command=fairetoplevel)
        go.pack()
        root.mainloop()
        
    else:
        print_Piece(sens)
        sleep(1)
        descente()
    
#-------------------------------------------------------------------------------    
### Entrée : Piece_apres,vitesse,vitesse_normale
### Sortie : Affichage pièce avec sens
### Fonction : Elle a pour but de faire descendre ligne par ligne le bloc\
    #si c'est possible.Autrement on appelle nvelle_Piece avec Piece_apres\
        #en parametre.
def descente():

    global Piece_apres,vitesse,vitesse_normale

    Piece_Efface()
    vitesse = vitesse_normale
    
    if Mouvement_verif(1,0,0):
        coord_normales[0] += 1
        print_Piece(sens)
        fen.after(vitesse,descente)
    else :
        print_Piece(sens)
        verif_Ligne()
        nvelle_Piece()

#-------------------------------------------------------------------------------
### Entrée : \
### Sortie : Affichage pièce avec sens
### Fonction : Elle a pour but d'afficher une pièce quand elle est allée à gauche
        
def gauche(event):

    Piece_Efface()
    if Mouvement_verif(0,-1,0):
        coord_normales[1] -=1
        print_Piece(sens)
    else:
        print_Piece(sens)
    return

#-------------------------------------------------------------------------------
### Entrée : \
### Sortie : Affichage pièce avec sens
### Fonction : Elle a pour but d'afficher une pièce quand elle est allée à droite

def droite(event):

    Piece_Efface()
    if Mouvement_verif(0,1,0):
        coord_normales[1] += 1
        print_Piece(sens)
    else:
        print_Piece(sens)
    return

#-------------------------------------------------------------------------------
### Entrée : sens
### Sortie : Affichage pièce avec sens
### Fonction : Elle a pour but d'afficher une pièce quand elle a tourné

def tourne(event):

    global sens
    
    Piece_Efface()
    if Mouvement_verif(0,0,1):
        sens += 1
        if sens == 4:
            sens = 0
        print_Piece(sens)
    else:
        print_Piece(sens)

#-------------------------------------------------------------------------------
### Entrée : vitesse
### Sortie : Affichage pièce avec vitesse rapide
### Fonction : Elle a pour but d'accéler la descente de la pièce quand on\
    # maintient la touche "bas" enfoncée
        
def tombe(event):

    global vitesse

    vitesse = 10

#-------------------------------------------------------------------------------
### Entrée : \
### Sortie : Affichage pièce avec vitesse normale
### Fonction : Elle a pour but de faire ralentir la pièce quand on lâche la\
    #touche "bas"
    
def relache_bas(event):

    global vitesse,vitesse_normale

    vitesse = vitesse_normale

#-------------------------------------------------------------------------------
### Entrée : \
### Sortie : Afficher pièce
### Fonction : Elle a pour but d'effacer la pièce de la matrice par rapport à\
    # sa coordonnée courante

def Piece_Efface():

    for i in range(4):
        for j in range(4):
            if Piece[sens][i][j] == 0:
                continue
            tableau_grille[coord_normales[0]+i][coord_normales[1]+j] = 0


#-----------------------------------------------------------------------------
### Entrée : sens
### Sortie : Affichage pièce
### Fonction : Elle a pour but d'effacer la pièce de la matrice par rapport à\
    # sa coordonnée courante et de passer les coordonnées dans la matrice à\
        #la valeur de la pièce

def print_Piece(sens):

    for i in range(4):
        for j in range(4):
            if Piece[sens][i][j] == 0:
                continue
            tableau_grille[coord_normales[0]+i][coord_normales[1]+j] =\
                                                               Piece[sens][i][j]
    maj_Grille()

#-------------------------------------------------------------------------------            
### Entrée : dx, dy, pivot
### Sortie : Affichage pièce
### Fonction : Elle a pour but de vérifier si la pièce ne débordera pas de la\
    # matrice. Si c'est la cas on renvoit un déplacement non possible à la\
        # méthode appelante. Si non, on teste si elle ne chevauchera pas des\
            # blocs déja présent
    
def Mouvement_verif(dx,dy,pivot):

    rotation = sens + pivot
    if rotation == 4:
        rotation = 0
    for i in range(4):
        for j in range(4):
            if coord_normales[1]+(dy+j) > 9 or coord_normales[1]+(dy+j) < 0 or\
                                                   coord_normales[0]+(dx+i) >19:
                if Piece[rotation][i][j] != 0:
                    return False
                else:
                    continue
            if (Piece[rotation][i][j] * tableau_grille[coord_normales[0]+(dx+i)]\
                                                [coord_normales[1]+j+dy]) != 0:
                return False
    return True

#-------------------------------------------------------------------------------
### Entrée : score,Points_de_vie,label_vie,label_nom,nom_boss,score_score,level
### Sortie : Affichage score et points de vie du boss, affichage si le joueur\
        #gagne
### Fonction : Elle a pour but de vérifier par récursivité si au moins une\
        # ligne à été construite
            
def verif_Ligne():

    global score,Points_de_vie,label_vie,label_nom,nom_boss,score_score,level
    
    for ligne in range(19,-1,-1):
        ligne_complete = True
        for colonne in range(10):
            if tableau_grille[ligne][colonne] == 0:
                ligne_complete = False
                
        if ligne_complete:
            del tableau_grille[ligne]
            tableau_grille[0:0] = [[0,0,0,0,0,0,0,0,0,0]]
            maj_Grille()
            verif_Ligne()
            score_score = score_score + 100
            Points_de_vie = Points_de_vie - 100
            label_vie.configure(text="PTS DE VIE\n"+str(Points_de_vie))
            
            # Animation sonore quand une ligne est détruite
            pygame.mixer.music.load("heat-vision.wav")
            pygame.mixer.music.play()
            
            #Retourne la valeur du volume, entre 0 et 1
            volume = pygame.mixer.music.get_volume()
            pygame.mixer.music.set_volume(1)

            # Passage au niveau 2
            if Points_de_vie == 0 and level == 1:
                levelup()
                
            # Passage au niveau 3   
            if Points_de_vie == 0 and level == 2:
                levelup2()
                
            #Passage au niveau 4   
            if Points_de_vie == 0 and level == 3:
                levelup3()
                
            # Fin du jeu   
            if Points_de_vie == 0 and level == 4:

                print("Bravo")
                son.stop()
                
            
#-------------------------------------------------------------------------------
### Entrée : \
### Sortie : Initilialisation avec de nouveaux paramètres
### Fonction : Elle a pour but de passer au niveau suivant
        
def levelup():
    début(niveau=2,score=1200,img="Undyne1.gif",nom_boss="Undyne",\
                   vie=2000,parole="Capitulez !")

#-------------------------------------------------------------------------------
### Entrée : \
### Sortie : Initilialisation avec de nouveaux paramètres
### Fonction : Elle a pour but de passer au niveau suivant
    
def levelup2():
    début(niveau=3,score=3200,img="Papyrus2.gif",nom_boss="Papyrus",\
                   vie=3000,parole="Retournez au néant !")

#-------------------------------------------------------------------------------
### Entrée : \
### Sortie : Initilialisation avec de nouveaux paramètres
### Fonction : Elle a pour but de passer au niveau suivant

def levelup3():
    début(niveau=4,score=6200,img="undertale3.gif",nom_boss="Sans",\
                   vie=4000,parole="L'échec est inevitable !") 
    

#-------------------------------------------------------------------------------
### Entrée : \
### Sortie : Initilialisation avec de nouveaux paramètres
### Fonction : Elle a pour but mettre a jour des canevas en fonction des\
    # couleurs référencées par les valeurs de la matrice

def maj_Grille():
    """Mise a jour des canevas en fonction des couleurs référencées par les
    valeurs de la matrice."""
    for ligne in range(20):
        for colonne in range(10):
            couleur = tableau_couleur[tableau_grille[ligne][colonne]]
            tableau_canvas[ligne][colonne].configure(bg=couleur)

    fen.update()
#-------------------------------------------------------------------------------

fen = Tk()
fen.wm_geometry(newGeometry='+210+0')
fen.resizable(0,0)

# On modifie la taille de la fenêtre
fen.geometry("%dx%d%+d%+d" % (424,560,26,26))

# On ajoute un titre à la fenêtre
fen.title("** UnderTris ISN **")

# On débute le jeu
début()
fen.mainloop()
