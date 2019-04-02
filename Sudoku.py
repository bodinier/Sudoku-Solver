class grille :
    """Classe d'une grille : objet contenant neuf carrés stockés sous forme d'une matrice """
    def __init__(self, grille) :
        self.grille = grille
        #ex grille[1][2] est le deuxieme carré

    def print_grille(self) :
        print(" ______________________________")
        for i in range(9) :
            for j in range(9) :
                if j == 0 :
                    print("|", end = '')
                print(self.grille[j][i],"|", end = '  ')
            print('')
            print(" ______________________________")

    def possible_ligne(self, x, y) :
        """Prend en argument une coordonnée (x,y) et renvoit quelles sont les valeurs possibles en fonction des autres valeurs sur la ligne"""
    pass
    

class carre :
    """Classe d'une carre dans la grille qui est une matrice 3x3 où chaque case contient un entier entre 1 et 9"""
    def __init__(self, valeurs) :
        self.valeurs = valeurs
    #ex : valeurs = [2, 3, 1, 4, 7, 8, 6, 9, 5]

    def print_carre(self) :
        for i in range(3) :
            for j in range(3) :
                print(self.valeurs[i][j], end = '')
            print('')
    pass

class case :
    def __init_(self, valeur)
        self.valeur = valeur
    pass
                  
A = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
"""
grille1 = grille(A)
grille1.print_grille()
"""

def possible_ligne(self, x, y) :
        """Prend en argument une coordonnée (x,y) et renvoit quelles sont les valeurs possibles en fonction des autres valeurs sur la ligne"""
        if x<1 or x >9 or y<1 or y>9 :
            print("mauvaise valeurs de coordonnées)
            return None
        possible = {1 : True, 2 : True, 3 : True, 4 : True, 5 : True, 6 : True, 7 : True, 8 : True, 9 : True}
        L_possible = []
        for i in range(9) :
            if 0<grille[x][i]<10 and i != y :
                possible[grille[x][i]] = False
        for j in range(9) :
            if possible[j] :
                L_possible.append(j)
        return L_possible

def possible_colonne(self, x, y) :
        """Prend en argument une coordonnée (x,y) et renvoit quelles sont les valeurs possibles en fonction des autres valeurs sur la ligne"""
        if x<1 or x >9 or y<1 or y>9 :
            print("mauvaise valeurs de coordonnées)
            return None
        possible = {1 : True, 2 : True, 3 : True, 4 : True, 5 : True, 6 : True, 7 : True, 8 : True, 9 : True}
        L_possible = []
        for i in range(9) :
            if 0<grille[i][y]<10 and i != x :
                possible[grille[i][x]] = False
        for j in range(9) :
            if possible[j] :
                L_possible.append(j)
        return L_possible

def possible_carre(self, x, y) :
        """Prend en argument une coordonnée (x,y) et renvoit quelles sont les valeurs possibles en fonction des autres valeurs sur la ligne"""
        if x<1 or x >9 or y<1 or y>9 :
            print("mauvaise valeurs de coordonnées)
            return None
        possible = {1 : True, 2 : True, 3 : True, 4 : True, 5 : True, 6 : True, 7 : True, 8 : True, 9 : True}
        L_possible = []
        #On doit trouver les coordonnees du carre
        for i in range() :
                  for j in range() :
                      if 0<grille[i][j]<10 :
                          possible[grille[i][j]] = False
        return L_possible




  


