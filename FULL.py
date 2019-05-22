import time
import copy
import tkinter as tk
from tkinter import *
from tkinter import filedialog

#               Dimensions de l'écran interface

height = 450
width  = 450
size_square = 50
global grille_sudoku
grille_sudoku = []


#               Définition des fonctions pour l'interface

def oopen():
    """Permet d'ouvrir une grille dans un menu déroulant"""
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/home/moulan",title = "Select file",filetypes = (("txt files","*.txt"),("all files",".*")))
    file=open(root.filename,'r')
    for i in range (9):
        grille_sudoku.append(list(file.readline()))
        del grille_sudoku[i][9]
        for j in range(9):
            grille_sudoku[i][j]=int(grille_sudoku[i][j])

    fill_sudoku(canvas,grille_sudoku) #Remplit la grille avec les chiffres initiaux 
    print(grille_sudoku)
    print("Open !")
    



def save():
    """Permet de sauvegarder la grille dans un fichier"""
    print("Save !")
    root = Tk()
    root.filename =  filedialog.asksaveasfilename(initialdir = "/home",title = "Select file",filetypes = (("jpeg files",".jpg"),("all files",".*")))
    print (root.filename)


def solve():
    """Lance la résolution du sudoku"""
    """ En ce qui concerne les temps d'éxécution"""
    grille1 = C_grid(H)
    t1 = time.perf_counter()
    grille1.sudoku()
    t2 = time.perf_counter()
    T = t2-t1
    print("Le programe s'éxécute en " ,T, "s")

    print("Solve !")


def initWin(window):
    """Initialise l'interface"""
    canvas = tk.Canvas(window,width=width,height=height)
    canvas.pack()
    menu_bar = tk.Menu(window) #barre du menu
    filemenu = tk.Menu(menu_bar)
    filemenu.add_command(label="Open", command=oopen)
    filemenu.add_command(label="Save", command=save)
    filemenu.add_command(label="Solve", command=solve)
    menu_bar.add_cascade(label="File", menu=filemenu)
    window.config(menu=menu_bar)
    return  canvas


def draw_grid(canvas):
    """Affichage des chiffres dans la grille de sudoku"""
    for i in range(0,10):
        if i%3 == 0:
            canvas.create_line(i*size_square, 0,i*size_square, size_square*9,width=3)
            canvas.create_line(0,i*size_square, size_square*9,i*size_square,width=3)
        else:
            canvas.create_line(i*size_square, 0,i*size_square, size_square*9,width=1)
            canvas.create_line(0,i*size_square, size_square*9,i*size_square,width=1)


def clear_grid(canvas):
    """Réinitialise une grille"""
    canvas.delete("all")
    draw_grid(canvas)


def draw_sudoku(canvas,x,y,num):
    """Création de la grille"""
    canvas.create_text((2*x+1)*size_square/2,(2*y+1)*size_square/2,text=str(num))


def fill_sudoku(canvas, M) :
    """Remplit le sudoku des chiffres manquants, contenus dans la matrice M"""
    for i in range(9):
        for j in range(9) :
            if M[i][j] != 0 :
                canvas.create_text((2*j+1)*size_square/2,(2*i+1)*size_square/2,text=str(M[i][j]))


#               Définition des fonctions pour la résolution

class C_grid :
    """Classe d'une grille : matrice carrée où chaque case est soit un zéro soit un entier entre 1 et 9"""
#               Initialisation

    def __init__(self, grille) :
        """On initialise nos dictionnaires et on défini les variables"""
        self.bareme = 0
        self.grille = grille
        self.possibilitees_par_case = {}
        self.sauvegarde = {}
        self.compteur_de_choix = 0


    def print_grille(self) :
        """Méthode qui affiche la grille"""
        for i in range(9) :
            for j in range(9) :
                if j == 0 :
                    print("|", end = '')
                if j%3 == 0 and j>0:
                    print("     ", end ='')
                    print('|', end = '')
                print(self.grille[i][j]," |", end = '  ')
            if( i+1)%3 == 0 and i>0 :
                print('')
            print('')
            
            
    def print_grille_2(self, M) :
        """Méthode qui affiche la grille M placée en argument"""
        for i in range(9) :
            for j in range(9) :
                if j == 0 :
                    print("|", end = '')
                if j%3 == 0 and j>0:
                    print("     ", end='')
                    print('|', end = '')
                print(M[i][j]," |", end = '  ')
            if( i+1)%3 == 0 and i>0 :
                print('')
            print('')


    def grid(self) :
        """Permet d'acccéder à la grille"""
        return self.grille


#               Fonctions d'accès aux donnée d'une case par coordonnées

    def ligne(self, x, y) :
        """"Prend les coordonnée d'une case et renvoit la ligne (sous forme de liste) sur laquelle cette case se trouve"""
        if x<0 or x >8 or y<0 or y>8 :
            print("mauvaise valeurs de coordonnées")
            return None
        L = []
        for i in range(9) :
            L.append(self.grille[x][i])
        return L


    def colonne(self, x, y) :
        """Prend les coordonnée d'une case et renvoit la colonne (sous forme de liste) sur laquelle cette case se trouve"""
        if x<0 or x >8 or y<0 or y>8 :
            print("mauvaise valeurs de coordonnées")
            return None
        L = []
        for i in range(9) :
            L.append(self.grille[i][y])
        return L


    def carre(self, x, y) :
        """Prend les coordonnée d'une case et renvoit dans  lequelle cette case se trouve sous forme de matrice 3x3"""
        if x<0 or x >8 or y<0 or y>8 :
            print("mauvaise valeurs de coordonnées")
            return None
        M = [[], [], []] #Initialisation de la matrice
        #On appelle (x0, y0) la coordonnée du centre du carré en question
        x0 = 3*(x//3)+1
        y0 = 3*(y//3)+1
        i = x0-1
        c = 0
        while i<=x0+1 :
            j = y0-1
            while j<=y0+1 :
                M[c].append(self.grille[i][j])
                j +=1
            i +=1
            c +=1
        return M
    
#               Fonctions calculant les valeurs possibles par cases

    def possible_ligne(self,x, y) :
            """Prend en argument les coordonées d'une case et  renvoit quelles sont les valeurs possibles en fonction des autres valeurs sur la ligne"""
            if x<0 or x >8 :
                print("mauvaise valeurs de coordonnées")
                return None
            #On va créer une liste initialisée à toutes les valeurs sont possibles, puis on les barre 
            #au fur et à mesure
            possible = {1 : True, 2 : True, 3 : True, 4 : True, 5 : True, 6 : True, 7 : True, 8 : True, 9 : True}
            L_possible = []
            ligne1 = self.ligne(x, y) #extraction de la ligne
            for i in range(9) :
                if 0<ligne1[i]<10 :
                    possible[ligne1[i]] = False
            for j in range(1, 10) :
                if possible[j] :
                    L_possible.append(j)
            return L_possible


    def possible_colonne(self, x, y) :
            """Prend en argument une colonne et un indice y et renvoit quelles sont les valeurs possibles en fonction des autres valeurs sur la ligne"""
            if y<0 or y >8 :
                print("mauvaise valeurs de coordonnées")
                return None
            possible = {1 : True, 2 : True, 3 : True, 4 : True, 5 : True, 6 : True, 7 : True, 8 : True, 9 : True}
            L_possible = []
            colonne = self.colonne(x, y) # extraction de la colonne
            for i in range(9) :
                if 0<colonne[i]<10 :
                    possible[colonne[i]] = False
            for j in range(1, 10) :
                if possible[j] :
                    L_possible.append(j)
            return L_possible


    def possible_carre(self, x, y) :
            """Prend en argument une coordonnée (x,y) et renvoit quelles sont les valeurs possibles en fonction des autres valeurs sur la ligne"""
            if x<0 or x >8 or y<0 or y>8 :
                print("mauvaise valeurs de coordonnées")
                return None
            M = self.carre(x, y) # extraction du carré
            possible = {1 : True, 2 : True, 3 : True, 4 : True, 5 : True, 6 : True, 7 : True, 8 : True, 9 : True}
            L_possible = []
            for i in range(3) :
                      for j in range(3) :
                          if 0<M[i][j]<10 :
                              possible[M[i][j]] = False
            for i in range(1, 10) :
                if possible[i] :
                    L_possible.append(i)
            return L_possible


    def possible_x_y(self, x, y) :
        """Prend les coordoonnées d'une case et renvoit quelles sont les valeurs possibles"""
        if self.grille[x][y] != 0 :
            print("Cette valeur est déjà connue ! (", self.grille[x][y], ")")
            return None
        possible = {1 : True, 2 : True, 3 : True, 4 : True, 5 : True, 6 : True, 7 : True, 8 : True, 9 : True}
        L1 = self.possible_ligne(x, y)
        L2 = self.possible_colonne(x,y)
        L3 = self.possible_carre(x, y)
        L_possible = []
        # On va juste faire l'intersection des possibilités selon lignes, colonnes et carrés
        for x in possible :
            if x not in L1 or x not in L2 or x not in L3 :
                possible[x] = False
        for i in range(1, 10) :
            if possible[i] :
                L_possible.append(i)
        return (L_possible)
    
    
    def remplit_possibilitees_par_case(self) :
        """Cette fonction parcourt toutes les cases et si elles sont libres, on regarde quelles sont les valeurs possibles
ensuite, on va renvoyer un dictionnaire avec comme clé les coordonnées d'une case libre et comme valeur la liste
des possibles"""
        for i in range(9) :
            for j in range(9) :
                if self.grille[i][j] == 0 :
                    L_possible = self.possible_x_y(i,j)
                    self.possibilitees_par_case[(i,j)] = L_possible
        return self.possibilitees_par_case


    def minimum_de_possibilitees (self) :
        """Cette fonction renvoit un tuple (les coordonnées de la case où il y a le moins de possibilités,
la liste de valeurs possibles, et le nombre de possibilités)"""
        m = 9 
        coord = (0,0)
        if len(self.possibilitees_par_case) == 0 :
            #print("Le dico est vide \n")
            return None
        for (i,j) in self.possibilitees_par_case :
            if len(self.possibilitees_par_case[(i,j)]) < m :
                m = len(self.possibilitees_par_case[(i,j)])
                coord = (i,j)
        #print("coordonnées = ", coord, " valeur : " , self.possibilitees_par_case[coord])
        return (coord, self.possibilitees_par_case[coord], m)


#               Main :


    def sudoku (self) :
        """Fonction principale qui résolve le sudoku"""
        #Initialisation : On remplit le dictionnaire des possibilitées
        self.remplit_possibilitees_par_case()

        #On enregistre dans une matrice ce que nous renvoit minimum_de_possibilitees pour éviter de calculer plusieurs fois
        M = self.minimum_de_possibilitees()
        if len(self.possibilitees_par_case) == 0 :
            print("Le sudoku est fini \n\n")
            return None
        if M[2] == 0 :
            # On a du faire un mauvais choix car aucune valeur n'est possible, on revient à la sauvegarde précédente
            self.grille = self.sauvegarde[self.compteur_de_choix]
            clear_grid(canvas)
            fill_sudoku(canvas,self.grille)
            del[self.sauvegarde[self.compteur_de_choix]]
            self.compteur_de_choix -=1
            self.sudoku()
            return None
        if M[2] == 1 :
            # Il n'y a qu'une seule possibilité, on la place donc
            self.grille[M[0][0]][M[0][1]] = M[1][0]
            draw_sudoku(canvas,M[0][1], M[0][0], M[1][0])
            self.possibilitees_par_case = {}
            self.remplit_possibilitees_par_case()
            self.bareme +=1
            self.sudoku()
        if M[2] >1 :
            # Il va falloir faire un choix car on a plusieurs possibilitées
            self.compteur_de_choix +=1
            self.sauvegarde[self.compteur_de_choix] = copy.deepcopy(self.grille) #Sauvegarde de la grille avant le choix
            self.sauvegarde[self.compteur_de_choix][M[0][0]][M[0][1]] = M[1][1] #On place le deuxieme choix dans notre sauvegarde
            self.grille[M[0][0]][M[0][1]] = M[1][0] # On choisi le premier de la liste
            #des possibles
            draw_sudoku(canvas,M[0][1], M[0][0], M[1][0])
            self.possibilitees_par_case = {}
            self.remplit_possibilitees_par_case()
            if M[2] > 2 :
                self.bareme += 3
            self.bareme += 3
            self.sudoku()
        return None


#               Grilles de Sudoku pré-enregistrées :

"""Sudoku faciles : """
A=[[0,9,2,0,0,4,7,0,0],[1,5,0,0,6,0,2,0,8],[0,0,0,0,1,2,0,4,9],[0,0,0,0,5,8,6,0,0],[8,4,0,0,3,0,0,5,2],[0,0,3,2,9,0,0,0,0],[6,1,0,8,4,0,0,0,0],[2,0,5,0,7,0,0,6,1],[0,0,7,6,0,0,8,9,0]]


B=[[8,1,0,0,9,0,4,7,5],[0,9,5,0,1,4,6,8,2],[6,0,0,5,8,7,0,9,1],[0,0,8,7,2,0,0,6,3],[2,5,7,0,6,0,9,4,8],[9,0,6,8,0,0,1,2,7],[4,7,1,0,3,6,8,0,9],[3,6,2,9,5,0,7,1,0],[5,0,0,0,7,1,2,0,6]]


C=[[1,0,2,4,9,0,0,0,0],[4,5,0,0,6,3,0,9,2],[3,6,9,0,2,0,1,5,4],[6,9,1,5,4,0,0,7,8],[0,2,3,6,8,7,4,1,0],[7,4,0,0,1,9,5,2,6],[2,1,6,0,5,0,7,8,3],[9,3,0,8,7,0,0,4,1],[0,0,0,0,3,1,9,0,5]] 

D =[[0,4,0,0,0,2,0,1,9],[0,0,0,3,5,1,0,8,6],[3,1,0,0,9,4,7,0,0],[0,9,4,0,0,0,0,0,7],[0,0,0,0,0,0,0,0,0],[2,0,0,0,0,0,8,9,0],[0,0,9,5,2,0,0,4,1],[4,2,0,1,6,9,0,0,0],[1,6,0,8,0,0,0,7,0]]

"""Sudoku médium : """

E=[[0,0,0,4,0,2,0,0,0],[2,0,9,0,0,0,3,0,1],[0,8,0,0,0,0,0,7,0],[0,0,0,5,0,6,0,0,0],[9,0,0,0,0,0,0,0,4],[7,1,0,8,0,3,0,2,6],[0,0,0,0,6,0,0,0,0],[0,9,0,0,7,0,0,3,0],[0,4,7,0,8,0,5,6,0]]

"""Sudoku durs"""

F = [[0,4,0,0,0,2,0,1,9],[0,0,0,3,5,1,0,8,6],[3,1,0,0,9,4,7,0,0],[0,9,4,0,0,0,0,0,7],[0,0,0,0,0,0,0,0,0],[2,0,0,0,0,0,8,9,0],[0,0,9,5,2,0,0,4,1],[4,2,0,1,6,9,0,0,0],[1,6,0,8,0,0,0,7,0]]

G=[[1,0,0,0,0,7,0,9,0],[0,3,0,0,2,0,0,0,8],[0,0,9,6,0,0,5,0,0],[0,0,5,3,0,0,9,0,0],[0,1,0,0,8,0,0,0,2],[6,0,0,0,0,4,0,0,0],[3,0,0,0,0,0,0,1,0],[0,4,0,0,0,0,0,0,7],[0,0,7,0,0,0,3,0,0]]

H = [[0,0,0,0,0,7,0,8,9],[1,0,8,0,5,0,0,0,0],[7,0,0,2,0,0,0,0,0],[0,5,0,0,2,0,9,0,8],[0,0,7,0,0,0,3,0,0],[8,0,6,0,7,0,0,2,0],[0,0,0,0,0,4,0,0,3],[0,0,0,0,6,0,1,0,4],[2,4,0,9,0,0,0,0,0]]


#               Main : 

if __name__ == '__main__':
    window = tk.Tk()
    canvas = initWin(window)
    draw_grid(canvas) #crée une grille vierge
    #fill_sudoku(canvas,B) #Remplit la grille avec les chiffres initiaux 

    """Evaluation de la difficulté"""
    #if grille1.bareme <= 35 :
     #   print("Le Sudoku est facile")
    #if grille1.bareme >35 and grille1.bareme <= 80 :
     #   print("Le Sudoku est moyen")
    #if grille1.bareme >80 :
     #   print("Le Sudoku est dur")
    
    
    
    window.mainloop()


