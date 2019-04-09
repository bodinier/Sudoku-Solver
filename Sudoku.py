class grille :
    """Classe d'une grille : objet contenant neuf carrés stockés sous forme d'une matrice """
    def __init__(self, grille) :
        self.grille = grille
        self.taille = len(grille[0])
        self.dicoliste = {}

    def printg(self) :
        for i in range(9) :
            for j in range(9) :
                if j == 0 :
                    print("|", end = '')
                if j%3 == 0 and j>0:
                    print("     ", end='')
                    print('|', end = '')
                print(self.grille[i][j]," |", end = '  ')
            if( i+1)%3 == 0 and i>0 :
                print('')
            print('')

    def grid(self) :
        return self.grille

    def ligne(self, x, y) :
        """"Prend une coordonnée et renvoit la ligne correspondante"""
        if x<0 or x >8 or y<0 or y>8 :
            print("mauvaise valeurs de coordonnées")
            return None
        L = []
        for i in range(9) :
            L.append(self.grille[x][i])
        return L

    def colonne(self, x, y) :
        """"Prend une coordonnée et renvoit la ligne correspondante"""
        if x<0 or x >8 or y<0 or y>8 :
            print("mauvaise valeurs de coordonnées")
            return None
        L = []
        for i in range(9) :
            L.append(self.grille[i][y])
        return L

    def carre(self, x, y) :
        """Prend une coordonnée et renvoit la carré dans lequelle le point vit"""
        if x<0 or x >8 or y<0 or y>8 :
            print("mauvaise valeurs de coordonnées")
            return None
        M = [[], [], []]
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
    
    def possible_ligne(self,x, y) :
            """Prend en argument une ligne et un indice x et renvoit quelles sont les valeurs possibles en fonction des autres valeurs sur la ligne"""
            if x<0 or x >8 :
                print("mauvaise valeurs de coordonnées")
                return None
            possible = {1 : True, 2 : True, 3 : True, 4 : True, 5 : True, 6 : True, 7 : True, 8 : True, 9 : True}
            L_possible = []
            ligne1 = self.ligne(x, y)
            for i in range(9) :
                if 0<ligne1[i]<10 and i != x :
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
            colonne = self.colonne(x, y)
            for i in range(9) :
                if 0<colonne[i]<10 and i != y :
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
            M = self.carre(x, y)
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
        if self.grille[x][y] != 0 :
            print("Cette valeur est déjà connue ! (", self.grille[x][y], ")")
            return None
        possible = {1 : True, 2 : True, 3 : True, 4 : True, 5 : True, 6 : True, 7 : True, 8 : True, 9 : True}
        L1 = self.possible_ligne(x, y)
        L2 = self.possible_colonne(x,y)
        L3 = self.possible_carre(x, y)
        L_possible = []
        for x in possible :
            if x not in L1 or x not in L2 or x not in L3 :
                possible[x] = False
        for i in range(1, 10) :
            if possible[i] :
                L_possible.append(i)
        return (L_possible)
    
    def ecrire(self, x, y, valeur) :
        """Ecrit une valeur ou une liste de valeurs possibles dans la case de coord (x,y)"""
        self.grille[x][y] = valeur

    def cherche_tous_possible(self) :
        for i in range(9) :
            for j in range(9) :
                if self.grille[i][j] == 0 :
                    L_possible = self.possible_x_y(i,j)
                    self.dicoliste[(i,j)] = L_possible
        return self.dicoliste

    def miniz (self) :
        m = 9
        coord = (0,0)
        for (i,j) in self.dicoliste :
            if len(self.dicoliste[(i,j)]) < m :
                m = len(self.dicoliste[(i,j)])
                coord = (i,j)
        print("coordonnées = ", coord, " valeur : " , self.dicoliste[coord])
        return (coord, self.dicoliste[coord], m)

    def certain (self) :
        self.cherche_tous_possible()
        M = self.miniz()
        while M[2] == 1 :
            print("On place à la coordonée", M[0], "le chiffre", M[1])
            self.grille[M[0][0]][M[0][1]] = M[1][0]
            self.dicoliste = {}
            print(M)
            self.printg()
            self.cherche_tous_possible()                
            M = self.miniz()
        return None
                                 
            



A = [[1, 0, 0, 0, 0, 6, 7, 8, 9], [0, 2, 0, 4, 5, 6, 7, 8, 9], [1, 0, 7, 2, 0, 6, 0, 0, 9], [2, 1, 0,0 ,7 , 0, 3, 0, 0], [1, 0, 3, 0, 5, 0, 7, 2, 0], [8, 0, 0, 2, 0, 0, 0, 3, 9], [0, 2, 3, 4, 5, 6, 7, 8, 9], [1, 0, 3, 4, 2, 6, 0, 0, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
B =[[0,4,0,0,0,2,0,1,9],[0,0,0,3,5,1,0,8,6],[3,1,0,0,9,4,7,0,0],[0,9,4,0,0,0,0,0,7],[0,0,0,0,0,0,0,0,0],[2,0,0,0,0,0,8,9,0],[0,0,9,5,2,0,0,4,1],[4,2,0,1,6,9,0,0,0],[1,6,0,8,0,0,0,7,0]]
C=[[0,9,2,0,0,4,7,0,0],[1,5,0,0,6,0,2,0,8],[0,0,0,0,1,2,0,4,9],[0,0,0,0,5,8,6,0,0],[8,4,0,0,3,0,0,5,2],[0,0,3,2,9,0,0,0,0],[6,1,0,8,4,0,0,0,0],[2,0,5,0,7,0,0,6,1],[0,0,7,6,0,0,8,9,0]]


grille1 = grille(C)
grille1.printg()

def miniz (dico) :
        m = 9
        coord = (0,0)
        for (i,j) in dico :
            if len(dico[(i,j)]) < m :
                m = len(dico[(i,j)])
                coord = (i,j)
        print("coordonnées = ", coord, " valeur : " , dico[coord])
        return (coord, dico[coord], m)

dicotest = grille1.cherche_tous_possible()
R = miniz(dicotest)
grille1.certain()
