class grille :
    """Classe d'une grille : objet contenant neuf carrés stockés sous forme d'une matrice """
    def __init__(self, grille) :
        self.grille = grille

    def print_grille(self) :
        print(" ______________________________")
        for i in range(9) :
            for j in range(9) :
                if j == 0 :
                    print("|", end = '')
                print(self.grille[j][i],"|", end = '  ')
            print('')
            print(" ______________________________")

    def ligne(self, x, y) :
        """"Prend une coordonnée et renvoit la ligne correspondante"""
        if x<1 or x >9 or y<1 or y>9 :
            print("mauvaise valeurs de coordonnées)
            return None
        L = []
        for i in range(9) :
            L.append(self.grille[x][i])
        return L

    def colonne(self, x, y) :
        """"Prend une coordonnée et renvoit la ligne correspondante"""
        if x<1 or x >9 or y<1 or y>9 :
            print("mauvaise valeurs de coordonnées)
            return None
        L = []
        for i in range(9) :
            L.append(self.grille[i][y])
        return L

    def carre(self, x, y)
        """Prend une coordonnée et renvoit la carré dans lequelle le point vit""""
        if x<1 or x >9 or y<1 or y>9 :
            print("mauvaise valeurs de coordonnées)
            return None
        M = [[], [], []]
        #On appelle (x0, y0) la coordonnée du centre du carré en question
        x0 = 3*(x//3)+1
        y0 = 3*(y//3)+1
        i = x0-1
        while i<=x0+1 :
                  j = y0-1
                  while j<=y0+1 :
                      M[i].append(grille[i][j])
        return M
    
def possible_ligne(self, ligne, x) :
        """Prend en argument une ligne et un indice x et renvoit quelles sont les valeurs possibles en fonction des autres valeurs sur la ligne"""
        if x<1 or x >9 :
            print("mauvaise valeurs de coordonnées)
            return None
        possible = {1 : True, 2 : True, 3 : True, 4 : True, 5 : True, 6 : True, 7 : True, 8 : True, 9 : True}
        L_possible = []
        for i in range(9) :
            if 0<ligne[i]<10 and i != x :
                possible[ligne[i]] = False
        for j in range(9) :
            if possible[j] :
                L_possible.append(j)
        return L_possible

def possible_colonne(self, colonne, y) :
        """Prend en argument une colonne et un indice y et renvoit quelles sont les valeurs possibles en fonction des autres valeurs sur la ligne"""
        if x<1 or x >9 :
            print("mauvaise valeurs de coordonnées)
            return None
        possible = {1 : True, 2 : True, 3 : True, 4 : True, 5 : True, 6 : True, 7 : True, 8 : True, 9 : True}
        L_possible = []
        for i in range(9) :
            if 0<colonne[i]<10 and i != y :
                possible[ligne[i]] = False
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

class case :
    def __init_(self, valeur)
        self.valeur = valeur
    pass
                  
A = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
"""
grille1 = grille(A)
grille1.print_grille()
"""
