#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Résolveur de Rubik's Cube
import sys
import copy

# Génération de modèle, pour les tests de bon fonctionnement.
couleurs = ['w', 'b', 'o', 'v', 'r', 'j']
(W,B,O,V,R,J) = couleurs
 
# Chaîne de caractère décrivant un cube résolu.
modeleResolu = ",".join([ 9*clr for clr in couleurs])

# Chaîne de caractères décrivant un cube dont les deux premières couronnes sont résolues
modeleA = ",".join([9*W,\
    6*B+J+B+R, 6*O+J+R+R, 6*V+B+O+O, 6*R+J+V+V,\
    B+J+O+J+J+J+J+J+V])

# Chaîne de caractères décrivant un cube particulier, mais non résolu.
modeleB = ",".join([O+W+W+W+W+W+W+W+R,\
B+B+V+B+B+J+B+R+B, J+O+O+B+O+O+W+O+O, V+V+B+V+V+J+V+O+V, J+R+R+V+R+R+W+R+R,\
                                                          R+J+J+B+J+V+J+J+O])

# Chaîne de caractères décrivant un cube particulier, mais non résolu.
modeleC = ",".join([R+J+W+J+W+J+W+J+O,\
V+B+B+B+B+W+V+R+V, J+O+R+B+O+O+W+O+R, B+V+V+V+V+W+B+O+B, J+R+O+V+R+R+W+R+O,\
                                                          O+W+J+B+J+V+J+W+R])

# Chaîne de caractères décrivant un cube juste avant l'étape 1
# Complètement mélangé
modeleEtape1 = ",".join([J+R+V+W+W+O+W+B+J,\
O+W+B+J+B+W+R+V+W, R+B+J+R+O+V+V+R+V, R+B+O+J+V+J+J+V+W, B+O+B+O+R+B+R+O+B,\
                                                          V+V+W+W+J+R+O+J+O])

# Chaîne de caractères décrivant un cube pour les tests de l'étape 2
# Croix blanche faite
modeleEtape2 = ",".join([R+W+R+W+W+W+R+W+J,\
B+B+O+J+B+B+O+B+J, B+O+W+O+O+R+V+R+O, V+V+B+V+V+R+B+J+O, W+R+J+B+R+V+W+O+J,\
                                                          V+V+V+O+J+J+W+J+R])

# Chaîne de caractères décrivant un cube pour les tests de l'étape 3 
# Face blanche faite
modeleEtape3 = ",".join([9*W,\
3*B+B+B+B+J+O+O, 3*O+R+O+V+J+R+B, 3*V+O+V+J+J+R+V, 3*R+B+R+O+R+J+V,\
                                                  J+V+O+V+J+J+R+J+B])

# Chaîne de caractères décrivant un cube pour les tests de l'étape 4
# Deuxième couronne faite
modeleEtape4 = ",".join([9*W,\
                     6*B+B+J+B, 6*O+O+J+V, 6*V+J+O+J, 6*R+V+B+R,\
                                               R+J+J+J+J+R+O+V+J])

# Chaîne de caractères décrivant un cube pour les tests de l'étape 5
# Orientation des arêtes de la face Jaune faite
modeleEtape5 = ",".join([9*W,\
                     6*B+O+O+J, 6*O+V+R+J, 6*V+R+B+J, 6*R+O+V+B,\
                                                    V+5*J+B+J+R])

# Chaîne de caractères décrivant un cube pour les tests de l'étape 6
# Orientation et positionnement des arêtes de la face Jaune fait
modeleEtape6 = ",".join([ 9*W, 6*B+O+B+B, 8*O+J, 8*V+J, 8*R+J, B+J+V+3*J+R+J+J ])

# Chaîne de caractères décrivant un cube pour les tests de l'étape 6
# Orientation et positionnement des arêtes de la face Jaune fait
modeleEtape6B = ",".join([ 9*W, 6*B+O+B+J, 6*O+V+O+B, 6*V+J+V+O, 6*R+J+R+J, B+J+V+3*J+R+J+R ])

# Chaîne de caractères décrivant un cube juste avant l'étape 7
# Positionnement des sommets de la face Jaune faite
modeleEtape7 = ",".join([9*W,\
                   6*B+R+B+O, 6*O+J+O+O, 9*V, 8*R+J,\
                                   J+J+B+J+J+J+J+J+B])

def resoudreLeCube (description):
    """Cette fonction renvoie la liste des gestes à effectuer pour résoudre le cube d'après une chaine de caractère de la forme '*********,*********,*********,*********,*********,*********' ; chaque étoile correspondant à une lettre minuscule relative à la couleur de chaque facette.  """
    cube = Cube(description)
    print(cube.toutResoudre())
    L=cube.listeDesMouvements
    for k in range(0,len(L)-1,2):
        a=input("Faites entrer pour connaître le prochain geste à effectuer: ") # On donne les gestes à effectuer un par un 
        print(L[k:k+2])  
        
def resoudreEtapes (description):
    """donne la liste des mouvements à effectuer étapes par étapes"""
    cube = Cube(description)
    cube.toutResoudre()
    L=listeDesMouvementsoptimisée(cube.listeDesMouvements)
    A=""
    u=0
    for k in range(0,len(L)-1,2):
        if L[k]!="*":
            A+=str(L[k])+str(L[k+1])+" "
        else:
            print(A,len(A)/3)
            u+=(len(A)/3)
            A=""
            a=input("")
    print(u)
        
def listeDesMouvementsoptimisée(L):
        A=[]
        for i in range(0,len(L)-1,2):
            a=L[i]
            b=L[i+1]
            if A and a==A[-2] and b!="*" and A[-1]!="*":
                b=(int(b)+int(A[-1]))%4
                A.pop()
                A.pop()
            if b!=0:
                A.append(a)
                A.append(b)
        return(A)

def optimisation(L):
    """créé plusieurs chaînes de caractères correspondant à une vision différente du cube à partir de la chaîne de départ fournie par l'utilisateur"""
    L1=L[6]+L[3]+L[0]+L[7]+L[4]+L[1]+L[8]+L[5]+L[2]+","+L[20:49]+","+L[10:19]+","+L[52]+L[55]+L[58]+L[51]+L[54]+L[57]+L[50]+L[53]+L[56] #correspond à la description du cube avec W en haut et O en face de soi
    L2=L[8::-1]+","+L[30:49]+","+L[10:29]+","+L[58:49:-1] #correspond à la description du cube avec W en haut et V en face de soi
    L3=L[2]+L[5]+L[8]+L[1]+L[4]+L[7]+L[0]+L[3]+L[6]+","+L[40:49]+","+L[10:39]+","+L[56]+L[53]+L[50]+L[57]+L[54]+L[51]+L[58]+L[55]+L[52] #correspond à la description du cube avec W en haut et R en face de soi
    L4=L[::-1] #correspond à la description du cube avec J en haut et R en face de soi
    return ([L,L1,L2,L3,L4]) #n'hésitez pas à continuer
### Coeur du code ###
# print(resoudreLeCube(sys.argv[-1]))
#####################


def afficheur (text):
    qt = 4
    liste = [text[i:i+2] for i in range(0,len(text),2)]
    for i in range(0,len(liste),qt):
        input('  ' + " ".join(liste[i:i+qt]))



class Cube:
    #W = "w" # 0 # Dessus [W-J Axe 0]
    #B = "b" # 1 # En face [B-V Axe 1]
    #O = "o" # 2 # A droite [O-R Axe 2]
    #V = "v" # 3 # Derrière
    #R = "r" # 4 # A gauche
    #J = "j" # 5 # Dessous
        
    def __init__ (s, chaineU):
        
        ### Données figées, égales pour toutes les instances:
        s.sommetsPosParitee = [0,1,0,1,1,0,1,0]
        s.BOVR = [1,2,3,4]
        s.OVRB = [2,3,4,1]
        s.inf = float('inf')
        
# Numérotation arbitraire des arêtes:
# . 2 .                   
# 3 W 1                   
# . 0 .                   
# . 0 . . 1 . . 2 . . 3 . 
# 7 B 4 4 O 5 5 V 6 6 R 7 
# . 8 . . 9 . . A . . B . 
#                   . B . 
# [A = 10]          A J 8 
# [B = 11]          . 9 . 
        W = 0 ; B = 1 ; O = 2 ; V = 3 ; R = 4 ; J = 5
        s.v = (lambda a,b : 2**a+2**b) # v comme valeur
        v = s.v
        s.retrouverNumeroArete = {
        v(W,B):  0, v(W,O):  1, v(W,V):  2, v(W,R):  3, # Cas Blancs
        v(J,B):  8, v(J,O):  9, v(J,V): 10, v(J,R): 11, # Cas Jaunes
        v(B,O):  4, v(O,V):  5, v(V,R):  6, v(R,B):  7, # Cas de la `couronne_milieu`
        v(W,W): -1, v(B,B): -1, v(O,O): -1, v(V,V): -1, v(R,R): -1, v(J,J): -1,
        v(W,J): -2, v(B,V): -2, v(O,R): -2
        } # -1 est une erreur: deux fois la même couleur 
          # -2 est une erreur: couleurs de faces opposées
          # Remarque: nous sommes sur d'avoir énuméré toutes les possibilités, car
          # C(6;2) + C(6;1) = 6!/(2!*4!) + 6!/5! = (6*5/2) + 6 = 3*5 + 6 = 15 + 6 = 21
          # et nous avons bien 21 cas traités.


# Numérotation arbitraire des sommets et des arêtes:
# 2 . 1                    #  . 2 .                   
# . W .                    #  3 W 1                   
# 3 . 0                    #  . 0 .                   
# 3 . 0 0 . 1 1 . 2 2 . 3  #  . 0 . . 1 . . 2 . . 3 . 
# . B . . O . . V . . R .  #  7 B 4 4 O 5 5 V 6 6 R 7 
# 7 . 4 4 . 5 5 . 6 6 . 7  #  . 8 . . 9 . . A . . B . 
#                   6 . 7  #                    . B . 
#                   . J .  #   [A = 10]         A J 8 
#                   5 . 4  #   [B = 11]         . 9 . 
       # Tables de correspondance indiquant les positions dont les blocs vont bouger, ainsi que la nouvelle position associée.
        s.cyclesSommet = [[0,3,2,1], # Rotation de la face 0 : W : Blanche
                         [0,4,7,3], # 1: B : Bleu
                         [0,1,5,4], # 2: O
                         [1,2,6,5], # 3: V
                         [2,3,7,6], # 4: R
                         [4,5,6,7]] # 5: J
        
        s.cyclesArete = [[0,3,2,1], # Rotation de la face 0 : W : Blanche
                        [0,4,8,7], # 1: B
                        [1,5,9,4], # 2: O
                        [2,6,10,5], # 3: V
                        [3,7,11,6], # 4: R
                        [11,8,9,10]] # 5: J
        
        
        ### Initialisation (pré-création) de listes decrivant le cube, avec des valeurs temporaires:
        s.viSommets = [None]*8 # Nous pré-créons ces huit valeur, pour pouvoir les affecter
        s.viAretes = [None]*12 # plus facilement ensuite, en utilisant les indices 'L[i]' uniquement.
        # vi-* : Ces listes contiendronts la version 'VIsuel' des sommets et des arêtes. (deux ou trois facettes)
        
        s.sommetsBlocALaPos = [None]*8 # Numéro du bloc, en fonction de sa position.
        s.sommetsRoALaPos = [None]*8   # Rotation du bloc trouvé à la position.
        s.aretesBlocALaPos = [None]*12 #
        s.aretesRoALaPos = [None]*12   #
        
        s.sommetsPosDuBloc = [None]*8 # Position en fonction du numéro de bloc.
        s.sommetsRoDuBloc = [None]*8  # Rotation, en fonction du numéro de bloc.
        s.aretesPosDuBloc = [None]*12 # 
        s.aretesRoDuBloc = [None]*12  # 
        # Fin de la pré-création #

        ### Initialilisation de(s) liste(s) des mouvements à faire pour résoudre le cube :
        s.initialiserListesSolutions()

        ### Analyse de base des données de génération du cube (chaineU)
        s.initialiseur = chaineU
        s.faces = s.initialiseur.split(',')
        
        # La facette n°4 (le centre) définit la couleur de la face :
        s.couleurs = [ face[4] for face in s.faces ]      # Le quatrième caractère est le centre de la face.
        s.creerCorrespondanceCouleurs() # correspondance nom-couleur, et numéro-couleur :
       # (s.W, s.B, s.O, s.V, s.R, s.J) = s.couleurs       # Nous affectons des noms spécifique à chaque couleur.
        # s.numeroDeCouleur = { s.W: 0, s.B: 1, s.O: 2, s.V: 3, s.R: 4, s.J: 5} # Correspondance inverse couleur-nombre.
        (s.Wf, s.Bf, s.Of, s.Vf, s.Rf, s.Jf) = s.faces    # Nous affectons aussi des noms à chaque face.
        ## Définition des tableaux anneauHaut, anneauBas, couronneHaut, couronneMil et couronneBas
        # Notion d'anneau (haut et bas) correspond à une lecture particulière des faces :
        # 5 4 3
        # 6 . 2 - Face du haut, numérotation de l'anneau,    # 0 1 2
        # 7 0 1                 != Numérotation de la face : # 3 . 5
        # . . .                                              # 6 7 8
        # . . .
        # . . .                                                 # 2 5 8
        # 7 0 1                  != Numérotation de la face :   # 1 . 7
        # 6 . 2 - Face du bas, numérotation de l'anneau (aussi) # 0 3 6
        # 5 4 3
        # Code correspondant:
        Wf,Jf = s.Wf, s.Jf
        s.anneauHaut   = ''.join([ Wf[7:9], Wf[5], Wf[0:3][::-1], Wf[3], Wf[6]])
        s.anneauBas    = ''.join([ Jf[5], Jf[8:5:-1], Jf[3], Jf[0:3]])
        s.couronneHaut = ''.join([ strg[0:3] for strg in s.faces[1:5]]) # On récupère les couronnes à différentes hauteurs.
        s.couronneMil  = ''.join([ strg[3:6] for strg in s.faces[1:5]]) # Ceci facilitera l'identification ensuite.
        s.couronneBas  = ''.join([ strg[6:9] for strg in s.faces[1:5]])

        s.calculerCube()

        s.sommeRoAretes = sum(s.aretesRoALaPos)
        s.sommeRoSommets = sum(s.sommetsRoALaPos)
        if s.sommeRoAretes % 2 != 0:
            raise AssertionError("Somme des degrés des arêtes impaire!")
        if s.sommeRoSommets % 3 != 0:
            raise AssertionError("Somme des degrés des sommets incorrecte!")
        
        # Fin de __init__
        #(FIN DE __init__!)
     
    def printCube (s):
        """Affiche l'état du cube"""
        print("\n".join([
        "s.sommetsBlocALaPos = {}".format(s.sommetsBlocALaPos),
        "s.sommetsRoALaPos   = {}".format(s.sommetsRoALaPos),
        "s.aretesBlocALaPos = {}".format(s.aretesBlocALaPos),
        "s.aretesRoALaPos   = {}".format(s.aretesRoALaPos),
        
        #"s.sommetsPosDuBloc = {}".format(s.sommetsPosDuBloc),
        #"s.sommetsRoDuBloc  = {}".format(s.sommetsRoDuBloc),
        #"s.aretesPosDuBloc = {}".format(s.aretesPosDuBloc),
        #"s.aretesRoDuBloc  = {}".format(s.aretesRoDuBloc),
        
        "s.listeDesMouvements = {}".format(s.listeDesMouvements),
        "s.syntheseDesMvts    = {}".format(s.syntheseDesMvts),
        "s.decompte = {}".format(s.decompte),
        ]))
    
    def creerCorrespondanceCouleurs (s):
        """Crée les correspondance entre couleurs et numéro de face."""
        (s.W, s.B, s.O, s.V, s.R, s.J) = s.couleurs             # Nous affectons des noms spécifique à chaque couleur.
        s.numeroDeCouleur = { s.W: 0, s.B: 1, s.O: 2, s.V: 3, s.R: 4, s.J: 5} # Correspondance inverse couleur-nombre.

    def initialiserListesSolutions (s):
        """Initialilisation des listes de résolution (réposes) de l'algorithme:"""
        s.listeDesMouvements = ""
        s.listeMvtRotations = ['']
        s.listeMvtFaces = ['']
        s.syntheseDesMvts = ""
        s.decompte = 0
     
# Numérotation arbitraire des sommets:
# 2 . 1                   
# . W .                   
# 3 . 0                   
# 3 . 0 0 . 1 1 . 2 2 . 3 
# . B . . O . . V . . R . 
# 7 . 4 4 . 5 5 . 6 6 . 7 
#                   6 . 7 
#                   . J . 
#                   5 . 4

    def identifieSommet (s,bloc3f):
        """ Caractérise un sommet du cube, à partir de trois couleurs d'un bloc.""" 
        # bloc3f contient trois couleurs: trois facettes
        # Identifions la rotation du sommet:
        orientation = s.inf
        for i,x in enumerate(bloc3f): 
            if x == s.W or x == s.J:
                orientation = i
        # Calculons le numero (entre 0 et 7) du sommet:
        if s.O in bloc3f:
            if s.B in bloc3f:
                num = 0
            elif s.V in bloc3f:
                num = 1
            else:
                num = s.inf
        elif s.R in bloc3f:
            if s.B in bloc3f:
                num = 3
            elif s.V in bloc3f:
                num = 2
            else:
                num = s.inf
        else:
            num = s.inf

        num += 4*(s.J in bloc3f)
        # Ainsi:
        # Si bloc3f contient du blanc: 0 <= num < 4
        # Si bloc3f contient du jaune: 4 <= num < 8 
        return (num,orientation)

# Numérotation arbitraire des arêtes:
# . 2 .                   
# 3 W 1                   
# . 0 .                   
# . 0 . . 1 . . 2 . . 3 . 
# 7 B 4 4 O 5 5 V 6 6 R 7 
# . 8 . . 9 . . A . . B . 
#                   . B . 
# [A = 10]          A J 8 
# [B = 11]          . 9 . 
    def identifieArete (s,bloc2f):
        """ Caractérise une arête du cube, à partir de deux couleurs d'un bloc."""
        # bloc2f contient deux couleurs: deux facettes
        # Identifions le numero du bloc:
        valeur0 = s.numeroDeCouleur[ bloc2f[0] ]
        valeur1 = s.numeroDeCouleur[ bloc2f[1] ]
        num = s.retrouverNumeroArete[ s.v(valeur0,valeur1) ]
        # Identifions maintenant l'orientation de l'arête:
        orientation = 2
        for i,x in enumerate(bloc2f):
            if x == s.W or x == s.J: # Verification de la couleur de la facette.
                orientation = i # Si une des deux facettes correspond, on le retient.
        if orientation == 2: # Si on a pas pu determiner l'orientation, on utilise le bleu-vert:
            for i,x in enumerate(bloc2f):
                if x == s.B or x == s.V:
                    orientation = i
        if orientation == 2: # Si l'orientation n'est toujours pas déterminée, c'est qu'il y a une erreur.
            raise AssertionErreur(" L'orientation des arêtes n'a pas pu être déterminée ")
        return (num,orientation)


# Le regroupement des sommets et des arêtes:
# Pour les SOMMETS :      # Pour les ARÊTES :
#        CECI :           #        CECI :           
# 0 . 2                   # . 1 .                   
# . W .                   # 3 W 5                   
# 6 . 8                   # . 7 .                   
# 0 . 2 0 . 2 0 . 2 0 . 2 # . 1 . . 1 . . 1 . . 1 . 
# . B . . O . . V . . R . # 3 B 5 3 O 5 3 V 5 3 R 5 
# 6 . 8 6 . 8 6 . 8 6 . 8 # . 7 . . 7 . . 7 . . 7 . 
#                   0 . 2 #                   . 1 . 
#                   . J . #                   3 J 5 
#                   6 . 8 #                   . 7 . 
#      DOIT DEVENIR :     #      DOIT DEVENIR :     
# 2 . 1                   # . 2 .                   
# . W .                   # 3 W 1                   
# 3 . 0                   # . 0 .                   
# 3 . 0 0 . 1 1 . 2 2 . 3 # . 0 . . 1 . . 2 . . 3 . 
# . B . . O . . V . . R . # 7 B 4 4 O 5 5 V 6 6 R 7 
# 7 . 4 4 . 5 5 . 6 6 . 7 # . 8 . . 9 . . A . . B . 
#                   6 . 7 #                   . B . 
#                   . J . # [A = 10]          A J 8 
#                   5 . 4 # [B = 11]          . 9 . 

    def groupSommets (s):
        """Regroupe les facettes des sommets par 2, selon leur numéro, en vue de leur identification"""
        # On va remplir le tableau viSommets, avec les valeurs voulues.
        # On s'occupe des couches Haut et Bas en même temps.
        for i in range(0,4): # Pour chaque sommet...
            s.viSommets[i]   = (s.anneauHaut[2*i+1],
                                 s.couronneHaut[(3*i+3)%12],
                                 s.couronneHaut[(3*i+2)%12])
            s.viSommets[i+4] = (s.anneauBas[2*i+1],
                                 s.couronneBas[(3*i+2)%12],
                                 s.couronneBas[(3*i+3)%12])

    def groupAretes (s):
        """Regroupe les facettes des arêtes par 2, selon leur numéro, en vue de leur identification"""
        # On va remplir le tableau viArêtes, avec les valeurs voulues.
        # Les quatres premières et quatre dernières arêtes de la liste peuvent s'identifier ainsi :
        for x in range(4):
            s.viAretes[x]   = (s.anneauHaut[2*x],s.couronneHaut[3*x+1])
            s.viAretes[8+x] = (s.anneauBas[2*x],s.couronneBas[3*x+1])
        # Les arêtes suivantes sont identifiées manuellement :
        s.viAretes[4] = tuple(s.couronneMil[2:4])
        s.viAretes[5] = (s.couronneMil[6],s.couronneMil[5])
        s.viAretes[6] = tuple(s.couronneMil[8:10])
        s.viAretes[7] = (s.couronneMil[0],s.couronneMil[11])
    
    def mapSommets (s):
        """Utilise la liste s.viSommet et la methode s.identifieSommet pour générer la double indexation position-bloc des sommets du cube. (Génère les listes s.sommetsBloc et s.sommetsPos)"""
        # Remarque: s.viSommets indexe les BLOCS trouvés, pour chaque POSITION
        for pos,sommet in enumerate(s.viSommets):
            (bloc_lu, rot) = s.identifieSommet(sommet)
            s.sommetsBlocALaPos[pos] = bloc_lu # A chaque position, on associe le sommet correspondant
            s.sommetsRoALaPos[pos] = rot
            s.sommetsPosDuBloc[bloc_lu] = pos # A chaque sommet, on associe la position corespondante
            s.sommetsRoDuBloc[bloc_lu] = rot
        
    def mapAretes (s):
        """Utilise la liste s.viArete et la methode s.identifieArete pour générer la double indexation position-bloc des aretes du cube. (Génère les listes s.aretesBloc et s.aretesPos)"""
        # Remarque: s.viAretes indexe les BLOCS trouvés, pour chaque POSITION
        for pos,arete in enumerate(s.viAretes):
            (bloc_lu, rot) = s.identifieArete(arete)
            s.aretesBlocALaPos[pos] = bloc_lu # A chaque position, on associe l'arête correspondante
            s.aretesRoALaPos[pos] = rot
            s.aretesPosDuBloc[bloc_lu] = pos # A chaque arête, on associe la position corespondante
            s.aretesRoDuBloc[bloc_lu] = rot

    def calculerCube (s):
        """ Création des listes décrivant le cube """
        s.groupSommets() # Formation des sommets
        s.groupAretes()  # Fomration des arêtes
        s.mapSommets()   # Identification et rangement des sommets
        s.mapAretes()    # ~ ~ des arêtes
        

    def pariteeRoSommet (s,fNum,oldPos):
        """Renvoie l'écart de degré d'un sommet pour la rotation d'une des 4 faces latérales du cube"""
        return ( fNum + s.sommetsPosParitee[oldPos] ) % 2
     
    def diffRoSommets (s,fNum,nbQuarts,oldPos):
        """Calcule l'écart de degré d'un sommet à la position old_Pos entre avant et après une rotation de la face de numéro fNum, de nbQuarts quarts de tours. """
        if (not (fNum in [0,5])) and (nbQuarts % 2 != 0) :
            return 1 + s.pariteeRoSommet(fNum,oldPos)
        else:
            return 0
     
    def diffNumRoSommets (s,fNum,nbQuarts,oldPos):
        """Calcule l'écart de degré d'un sommet à la position old_Pos entre avant et après une rotation de la face de numéro fNum, de nbQuarts quarts de tours. """
        if (not (fNum in [0,5])) and (nbQuarts % 2 != 0) :
            return 2 - s.pariteeRoSommet(fNum,oldPos)
        else:
            return 0

    def rotationSommets (s,fNum,nbQuarts):
        """Applique aux sommets du cube les changements que causent une rotation de la face de numéro fNum, de nbQuarts quarts de tours. """
        cycle = s.cyclesSommet[fNum]
        # On gère en même temps la position et la rotation
        # On établit d'abord une liste temporaire, indiquant un bloc, sa nouvelle position, et sa nouvelle rotation.
        # On a nbQuarts = 0,1,2 ou 3
        bloc_pos_ro_list = []
        for i in range(-4,0):
            oldPos = cycle[i]
            newPos = cycle[i+nbQuarts]
            bloc = s.sommetsBlocALaPos[oldPos]
            oldRo = s.sommetsRoALaPos[oldPos]
            newRo = (oldRo + s.diffRoSommets(fNum,nbQuarts,oldPos) ) % 3
            bloc_pos_ro_list.append( (bloc,newPos,newRo) )
        # Puis on applique ces valeurs:
        for bloc,pos,ro in bloc_pos_ro_list:
            s.sommetsPosDuBloc[bloc] = pos
            s.sommetsBlocALaPos[pos] = bloc
            s.sommetsRoDuBloc[bloc] = ro
            s.sommetsRoALaPos[pos] = ro

    def reNumSommets (s,fNum,nbQuarts):
        """Renumérote les sommets, suivant le cycle. Change aussi le degré des blocs suivant les instructions."""
        cycle = s.cyclesSommet[fNum]
        # On gère en même temps la position et la rotation
        # On établit d'abord une liste temporaire, indiquant un bloc, sa nouvelle position, et sa nouvelle rotation.
        bloc_pos_ro_list = []
        for i in range(-4,0):
            oldBloc = cycle[i]
            newBloc = cycle[i+nbQuarts]
            pos = s.sommetsPosDuBloc[oldBloc]
            oldRo = s.sommetsRoDuBloc[oldBloc]
            newRo = (oldRo + s.diffNumRoSommets(fNum,nbQuarts,oldBloc) ) % 3
            bloc_pos_ro_list.append( (newBloc,pos,newRo) )
        # Puis on applique ces valeurs:
        for bloc,pos,ro in bloc_pos_ro_list:
            s.sommetsPosDuBloc[bloc] = pos
            s.sommetsBlocALaPos[pos] = bloc
            s.sommetsRoDuBloc[bloc] = ro
            s.sommetsRoALaPos[pos] = ro
        
    def diffRoAretes (s,fNum,nbQuarts):
        """ Indique, pour la rotation d'une face, si les arêtes subissent un changement de degré. """
        return (nbQuarts % 2) * (fNum in [1,3])
        
    def cycleAretes (s,cycle,nbQuarts,addRo):
        """Décales les blocs-arêtes suivant le cycle indiqué, de nbQuarts cases"""
        # On gère en même temps la position et la rotation
        # On établit d'abord une liste temporaire, indiquant un bloc, sa nouvelle position, et sa nouvelle rotation.
        # On a nbQuarts = 0,1,2 ou 3
        bloc_pos_ro_list = []
        for i in range(-4,0):
            oldPos = cycle[i]
            newPos = cycle[i+nbQuarts]
            bloc = s.aretesBlocALaPos[oldPos]
            oldRo = s.aretesRoALaPos[oldPos]
            newRo = (oldRo + addRo) % 2
            bloc_pos_ro_list.append( (bloc,newPos,newRo) )
        # Puis on applique ces valeurs:
        for bloc,pos,ro in bloc_pos_ro_list:
            s.aretesPosDuBloc[bloc] = pos
            s.aretesBlocALaPos[pos] = bloc
            s.aretesRoDuBloc[bloc] = ro
            s.aretesRoALaPos[pos] = ro

    def cycleNumAretes (s,cycle,nbQuarts,addRo):
        """Renumérote les arêtes, suivant le cycle. Change aussi la rotation des blocs suivant les instructions."""
        # On gère en même temps la position et la rotation
        # On établit d'abord une liste temporaire, indiquant un bloc, sa nouvelle position, et sa nouvelle rotation.
        bloc_pos_ro_list = []
        for i in range(-4,0):
            oldBloc = cycle[i]
            newBloc = cycle[i+nbQuarts]
            pos = s.aretesPosDuBloc[oldBloc]
            oldRo = s.aretesRoDuBloc[oldBloc]
            newRo = (oldRo + addRo) % 2
            bloc_pos_ro_list.append( (newBloc,pos,newRo) )
        # Puis on applique ces valeurs:
        for bloc,pos,ro in bloc_pos_ro_list:
            s.aretesPosDuBloc[bloc] = pos
            s.aretesBlocALaPos[pos] = bloc
            s.aretesRoDuBloc[bloc] = ro
            s.aretesRoALaPos[pos] = ro
        
    def rotationAretes (s,fNum,nbQuarts):
        """Applique aux arêtes du cube les changements que causent une rotation de la face de numéro fNum, de nbQuarts quarts de tours. """
        cycle = s.cyclesArete[fNum]           # On aquière le cycle correspondant
        addRo = s.diffRoAretes(fNum,nbQuarts) # On calcule la différence de rotation a appliquer
        s.cycleAretes(cycle,nbQuarts,addRo)   # On opère les changements

    def reNumAretes (s,cNum,nbQuarts):
        """Applique la renumérotation des arêtes aux arêtes qui comporte la couleur cNum. Change aussi la rotation si nécéssaire."""
        cycle = s.cyclesArete[cNum]           # On aquière le cycle correspondant
        addRo = s.diffRoAretes(cNum,nbQuarts) # On calcule la différence de rotation a appliquer
        s.cycleNumAretes(cycle,nbQuarts,addRo)   # On opère les changements
     
    def rotationFace (s,fNum,nbQuarts):
        """ Applique aux blocs du cube les changements que causent une rotation de la face de numéro fNum, de nbQuarts quarts de tours. """
        s.rotationSommets(fNum,nbQuarts)
        s.rotationAretes(fNum,nbQuarts)

    def clonerCube (s) :
        """ Clone le cube, et renvoie le clone """
        cube = copy.deepcopy(s)
        # Reinitialisation de certaines valeurs:
        s.faces = ""
        s.initialiseur
        cube.initialiserListesSolutions()
        s.viSommets = [None]*8
        s.viAretes = [None]*12
        return cube
        
    def tournerCube (s):
        """Re-génère le cube, pris de tel sorte que la face blanche soit en haut, et la orange en face de nous."""
        # Ce "changement de base" s'effectue en deux étapes:
        # * D'abord on déplace tout les blocs vers leur nouvelle place (en faisant les bons changements de rotation).
        # * Ensuite, on renumérote les blocs et on calcule les changements de degré à faire, en fonction des anciens numéros des blocs.
        
        # 0 :: Les faces à tourner pour simuler le changement sont ::
        faceA = 0 # Blanc
        nbqA = 1 # Sens positif
        faceB = 5 # Jaune
        nbqB = 3 # Sens negatif
        cycleAnneauCentre = [7,6,5,4] # avec nbq = 1
        
        # 1 :: Création d'un nouveau cube ::
        # cube = Cube(s.initialiseur)
        cube = s.clonerCube()
        
        # 2 :: Déplacement des blocs ::
        # Déplacement des centres:
        c = cube.couleurs
        cube.couleurs = [c[0],c[2],c[3],c[4],c[1],c[5]]
        cube.creerCorrespondanceCouleurs()
        # Déplacement des sommets et arêtes extérieurs
        cube.rotationFace(faceA,nbqA)
        cube.rotationFace(faceB,nbqB)
        # Dépacements des arêtes restantes:
        cube.cycleAretes(cycleAnneauCentre,1,1) # addRo=1, pour changer le degré des arêtes.

        # 3 :: Renumérotation des blocs, et calcule des degrés ::
        # Les 'couleurs polaires de repli' sont désormais le orange et le rouge, à la place du bleu et du vert.
        # Donc seul les degrés des arêtes qui étaient défini par une 'couleur polaire de repli', doivent être changés.
        cube.reNumAretes(faceA,nbqA)
        cube.reNumAretes(faceB,nbqB)
        cube.cycleNumAretes(cycleAnneauCentre,1,1) # On fait la renumérotation, et le changement de polarité.
        # Il n'y a pas de changement de rotation à faire pour les sommets, car ils utilisent les face blanches et jaunes comme faces polaires, et que le centre de celles-ci n'est pas affécté par le fait de tourner le cube:
        cube.reNumSommets(faceA,nbqA)
        cube.reNumSommets(faceB,nbqB)
        return cube

    def basculerCube (s):
        """Re-génère le cube, pris de tel sorte que la face verte soit en haut, et la blanche en face de nous."""
        # Ce "changement de base" s'effectue en deux étapes:
        # * D'abord on déplace tout les blocs vers leur nouvelle place (en faisant les bons changements de rotation).
        # * Ensuite, on renumérote les blocs et on calcule les changements de degré à faire, en fonction des anciens numéros des blocs.

        # 0 :: Les faces à tourner pour simuler le changement sont ::
        faceA = 4 # Rouge
        nbqA = 1 # Sens positif
        faceB = 2 # Orange
        nbqB = 3 # Sens negatif
        cycleAnneauCentre = [0,8,10,2] # avec nbq = 1
        
        # 1 :: Création d'un nouveau cube ::
        # cube = Cube(s.initialiseur)
        cube = s.clonerCube()
        
        # 2 :: Déplacement des blocs ::
        # Déplacement des centres:
        c = cube.couleurs
        cube.couleurs = [c[3],c[0],c[2],c[5],c[4],c[1]]
        cube.creerCorrespondanceCouleurs()
        # Déplacement des sommets et arêtes extérieurs
        cube.rotationFace(faceA,nbqA)
        cube.rotationFace(faceB,nbqB)
        # Dépacements des arêtes restantes:
        cube.cycleAretes(cycleAnneauCentre,1,1) # addRo=1, pour changer le degré des arêtes.

        # 3 :: Renumérotation des blocs, et calcule des degrés ::
        # Les couleurs polaires principale sont désormais le vert et le bleu, à la place du blanc et du jaune.
        # Donc les degrés des arêtes qui étaient définis par:
        # << une couleur polaire, gagnant contre une couleur polaire de repli >>, doivent être changés.
        cube.reNumAretes(faceA,nbqA)
        cube.reNumAretes(faceB,nbqB)
        cube.cycleNumAretes(cycleAnneauCentre,1,1) # On fait la renumérotation, et le changement de polarité.

        # Un changement de rotation des sommets est nécéssaire car les faces polaires deviennent la verte et la bleu, à la place de la blanche et la jaune.
        cube.reNumSommets(faceA,nbqA)
        cube.reNumSommets(faceB,nbqB)
        
        return cube

    def generer4 (s):
        """Renvoie la liste des quatres cubes obtensibles, en 'tournant' horizontalement le cube"""
        cubes = [s] # Est la liste des 4 cubes
        for i in range(3):
            cubes.append(cubes[-1].tournerCube())
        return cubes

    def generer24 (s):
        """Renvoie la liste des vingt-quatres cubes obtensibles, en tournant et en basculant le cube"""
        base = s   # Est le cube obtenu par basculement.
        cubes = [] # Est la liste des 24 cubes
        for i in range(3):
            quadriCube = base.generer4()
            cubes += quadriCube
            base = quadriCube[3].basculerCube()
            quadriCube = base.generer4()
            cubes += quadriCube
            base = quadriCube[1].basculerCube()
        if base == s.clonerCube():
            print("genrer24 super!")
        return cubes
    
    def memMove (s,fNum,nbQuarts):
        """Ajoute (intelligemment) le mouvement donné, à la liste totalisants les mouvements utilisés"""
        # On compare le mouvement à ajouter au dernier muvement effectué, pour savoir si on peut les combinner
        if fNum == s.listeMvtFaces[-1]: # On tourne deux fois la même face d'affilier: optimisation:
            roTot = ( s.listeMvtRotations[-1] + nbQuarts ) % 4
            if roTot == 0: # Les mouvements s'annules!
                s.listeMvtFaces.pop()
                s.listeMvtRotations.pop()
            else: # Les mouvements se combinnent:
                s.listeMvtRotations[-1] = roTot
        else: # On ajoute simplement les mouvement à la liste.
            s.listeMvtFaces.append(fNum)
            s.listeMvtRotations.append(nbQuarts)        

    def genListe (s):
        """Génère la liste (chaine) des mouvements à effectuer pour finir le cube"""
        s.syntheseDesMvts = ""
        s.decompte = len(s.listeMvtFaces)-1
        if s.decompte != len(s.listeMvtRotations)-1:
            raise AssertionError("Erreur dans la memorisation des mouvements: len(s.listeMvtFaces) == {} != {} == len(s.listeMvtRotations)".format(len(s.listeMvtFaces),len(s.listeMvtRotations)))
        for i in range(1,s.decompte+1): #! on ignore le premier élément, c.f. initialisation des listes
            nbQuarts = s.listeMvtRotations[i]
            if nbQuarts == 1:
                action = "+"
            elif nbQuarts == 2:
                action = "²"
            elif nbQuarts == 3:
                action = "-"
            else: # nbQuarts == 0 
                raise AssertionError("Rotation nulle trouvée dans listeMvtRotations à l'indice {}.".format(i))
            s.syntheseDesMvts += s.couleurs[s.listeMvtFaces[i]] + action
            
    
    def move (s,fNum,nbQuarts): # Finalement, il semble plus simple de n'utiliser que le numero des faces.
        """ Opère la rotation d'une des face du cube """
        nbQuarts %= 4
        if nbQuarts != 0:
            s.memMove(fNum,nbQuarts)
            s.rotationFace(fNum,nbQuarts)
        
        couleurFace = s.couleurs[fNum]
        if nbQuarts == 1:
            action = "1"
        elif nbQuarts == 3:
            action = "3"
        elif nbQuarts == 2:
            action = "2"
        else: # nbQuarts == 0
            action = ''
            couleurFace = ''
        s.listeDesMouvements += couleurFace + action
        
    def act (s,action):
        """ Tourne une face, spécifiée selon le code convention-utilisateur """
        fNum = s.numeroDeCouleur[action[0]]
        symbol = action[1]
        if symbol == "+":
            nbQuarts = 1
        elif symbol == "-":
            nbQuarts = 3
        elif symbol == "²":
            nbQuarts = 2
        else:
            nbQuarts = 0
        s.move(fNum,nbQuarts)

    def appliquer (s,instruction):
        """Applique la série de mouvements donnée (selon la convention utilisateur)"""
        for i in range(0, len(instruction), 2):
            s.act(instruction[i:i+2])

    ## Réalisation du cube, étape par étape ##
    ## Etape 1: Les arêtes de la première face ##
    def croixW(s):
        """ Effectue une succession de mouvements établissant une croix de blocs bien placés sur la face s.W (Etape 1) """
        W,J = 0,5 # Les numéros correspondant aux faces
        for k in range(4):
            arete = [0,1,2,3][k] # Les 4 blocs à déplacer.
            
            (currentPos,currentDeg) = (s.aretesPosDuBloc[arete],s.aretesRoDuBloc[arete])
            
            if not(currentPos == arete and currentDeg == 0): # Est-il mal placé ?
            
                if currentPos in (0,1,2,3): # Cas face supérieure
                    s.move(s.BOVR[currentPos],2)
                elif currentPos in (4,5,6,7): # Cas 2ème couronne
                    c = (k+4-currentPos)
                    s.move(W,c)
                    s.move(s.BOVR[arete-c%4],1)
                    s.move(W,-c) # Toujours réorienter la face supérieure !
                
                # On se ramène au cas inférieur :
                (currentPos,currentDeg) = (s.aretesPosDuBloc[arete],s.aretesRoDuBloc[arete])
                
                s.move(J,(k-currentPos)%4)
                
                # 2 cas sont possibles:
                if currentDeg == 0:
                    s.move(s.BOVR[arete],2)   # -> combinaison
                else:
                    s.move(s.BOVR[arete],1)   # -> combinaison
                    s.move(W,1)               # -> -----------
                    s.move(s.BOVR[arete-1],3) # -> -----------
                    s.move(W,3)               # -> ----------- # Toujours réorienter la face supérieure !
    
    ## Etape 2: Les sommets de la première face ##
    def indicefacedroiteW(s,Posisommet):
        """donne l'indice de la face située à droite du bloc lorsque le bloc se situe en haut à droite de la face centrale avec la face blanche au-dessus"""
        if Posisommet!=3:
            return (Posisommet+2)
        else:
            return 1

    def indicefacedroiteJ(s,Posisommet):
        """donne l'indice de la face située à droite du bloc lorsque le bloc se situe en bas à droite de la face centrale avec la face jaune en-dessous"""
        if Posisommet!=7:
            return (Posisommet-2)
        else:
            return (1)
    
    def indiceface(s,Posisommet):
        """donne l'indice de la face lorsque le bloc est situé en bas à droite de la face centrale (avec face blanche au-dessus et face jaune en-dessous)"""
        if Posisommet!=7:
            return (s.indicefacedroiteJ(Posisommet)-1)
        else:
            return (4)
    
    def sommetsW(s):
        """place les sommets de la face blanche"""
        J = 5
        for k in range(4):
            sommet = k #pour plus de lisibilité
            (currentPos,currentDeg) = (s.sommetsPosDuBloc[sommet],s.sommetsRoDuBloc[sommet])
            if not(currentPos == sommet and currentDeg == 0): # Est-il mal placé ? Si oui on l'envoie sur la 3e couronne avec Deg=1 ou Deg=2
                if currentPos in (0,1,2,3) and currentDeg==0: # Cas face blanche avec la bonne orientation
                    s.move(s.indicefacedroiteW(currentPos),3)
                    s.move(J,3)
                    s.move(s.indicefacedroiteW(currentPos),1)
                elif currentPos in (0,1,2,3) and currentDeg==1: #cas face blanche avec un degré de rotation=1
                    s.move(s.indicefacedroiteW(currentPos),3)
                    s.move(J,3)
                    s.move(s.indicefacedroiteW(currentPos),1)
                elif currentPos in (0,1,2,3) and currentDeg==2: #cas face blanche avec un degré de rotation=2
                    s.move(s.indicefacedroiteW(currentPos),3)
                    s.move(J,1)
                    s.move(s.indicefacedroiteW(currentPos),1)
                elif currentPos in (4,5,6,7) and currentDeg==0: #cas face jaune avec un degré de rotation=0
                    while s.sommetsPosDuBloc[sommet]!=sommet+4:
                        s.move(J,1)
                    res=s.sommetsPosDuBloc[sommet]    
                    s.move(s.indicefacedroiteJ(res),3)
                    s.move(J,1)
                    s.move(s.indicefacedroiteJ(res),1)
                while s.sommetsPosDuBloc[sommet]!=sommet+4: #on place le bloc en dessous de sa future position
                        s.move(J,1)    
                currentPos2=s.sommetsPosDuBloc[sommet]
                currentDeg2=s.sommetsRoDuBloc[sommet]   #notre bloc est maintenant sur la 3e couronne avec un degré de rotation=1ou2
                if currentDeg2==1:  #Si son deg de rotation=1, on réalise ces manipulations pour bien le placer
                    s.move(J,3)
                    s.move(s.indicefacedroiteJ(currentPos2),3)
                    s.move(J,1)
                    s.move(s.indicefacedroiteJ(currentPos2),1)
                else:
                    s.move(J,1)
                    s.move(s.indiceface(currentPos2),1)
                    s.move(J,3)
                    s.move(s.indiceface(currentPos2),3)
    
    ## Etape 3: Les arêtes de la deuxième couronne ##    
    def belge(s):
        """ Effectue une succession de mouvements établissant la deuxième couronne (Etape 3) """
        
        J = 5 # 5 est le numéro de la face jaune
        
        # on essaie d'abord de se débarasser des cas simples
        for k in range(4,8):
            if s.aretesPosDuBloc[k]==(k+2)%4+4 and s.aretesRoDuBloc[k]==0 and (k!=7 or s.aretesPosDuBloc[4]!=4):
                a=(k+2)%4+1
                b=(a+2)%4+1
                s.move(a,2)
                s.move(J,2)
                s.move(a,2)
                s.move(J,2)
                s.move(a,2)
                s.move(b,2)
                s.move(J,2)
                s.move(b,2)
                s.move(J,2)
                s.move(b,2)
        
            elif s.aretesPosDuBloc[k]==(k+3)%4+4 and s.aretesRoDuBloc[k]==0:
                a=k-3
                s.move(a,2)
                s.move(J,2)
                s.move(a,2)
                s.move(J,2)
                s.move(a,2)

            elif s.aretesPosDuBloc[k]==(k+1)%4+4 and s.aretesRoDuBloc[k]==0:
                a=(k+1)%4+1
                s.move(a,2)
                s.move(J,2)
                s.move(a,2)
                s.move(J,2)
                s.move(a,2)
        
        for k in range(4):
            arete = [4,5,6,7][k] # Les 4 blocs à déplacer.
            
            (currentPos,currentDeg) = (s.aretesPosDuBloc[arete],s.aretesRoDuBloc[arete])
            
            if not(currentPos == arete and currentDeg == 0):# Est-il mal placé ?
                if currentPos in (4,5,6,7):
                    s.move(s.BOVR[currentPos%4],1)
                    s.move(J,3)
                    s.move(s.BOVR[currentPos%4],3)
                    s.move(J,3)
                    s.move(s.OVRB[currentPos%4],3)
                    s.move(J,1)
                    s.move(s.OVRB[currentPos%4],1)
                    #L'arête est désormais sur la face jaune
                    (currentPos,currentDeg) = (s.aretesPosDuBloc[arete],s.aretesRoDuBloc[arete])
                    
                if k%2==0:
                    a=k-currentPos+1-currentDeg
                else:
                    a=k-currentPos+currentDeg
                s.move(J,a)
                currentPos=s.aretesPosDuBloc[arete]
                #On place le bloc sous la bonne face pour commencer le belge
                        
                #Doit-on faire le belge à droite ou à gauche?
                if (currentPos-arete)%2==1:     #à gauche
                    s.move(J,1)
                    s.move(s.BOVR[currentPos%4-1],1)
                    s.move(J,3)
                    s.move(s.BOVR[currentPos%4-1],3)
                    s.move(J,3)
                    s.move(s.BOVR[currentPos%4],3)
                    s.move(J,1)
                    s.move(s.BOVR[currentPos%4],1)
                else:                           # à droite
                    s.move(J,3)
                    s.move(s.OVRB[currentPos%4],3)
                    s.move(J,1)
                    s.move(s.OVRB[currentPos%4],1)
                    s.move(J,1)
                    s.move(s.BOVR[currentPos%4],1)
                    s.move(J,3)
                    s.move(s.BOVR[currentPos%4],3)
    
    
## Etape 4: L'orientation des arêtes de la dernière face, càd la petite croix ##
    def mvtligne(s,fNum3):
        """fait les mouvements correspondant à une configuration de type ligne horizontale avec la face d'indice fNum3 à droite de la ligne horizontale et fNum4 en face de soi"""
        if fNum3!=4: #on créée fNum4, l'indice de la face en dessous de la ligne
            fNum4=fNum3+1
        else:
            fNum4=1
        J=5
        s.move(fNum4,1)
        s.move(fNum3,1)
        s.move(J,1)
        s.move(fNum3,3)    
        s.move(J,3)
        s.move(fNum4,3)
    
    def mvttypeJ(s,fNum1,fNum2):
        """fait les mouvements correspondant à une configuration de type J avec la face d'indice fNum1 à gauche du J et la face d'indice fNum2 au dessus du J"""
        if fNum2!=4:    #on créée fNum3, l'indice de la face à droite du J
            fNum3=fNum2+1
        else:
            fNum3=1
        if fNum1!=1:    #on créée fNum4, l'indice de la face en dessous du J
            fNum4=fNum1-1
        else:
            fNum4=4
        J=5
        s.move(fNum3,3)
        s.move(J,3)
        s.move(fNum4,3)
        s.move(J,1)
        s.move(fNum4,1)
        s.move(fNum3,1)
        
    def petiteCroixJ(s):
        """réalise la petite croix jaune du cube"""
        J=5
        if s.aretesRoALaPos[8:]!=[0,0,0,0]: #on ne traite pas le cas où la petite croix jaune serait déjà faite
            if s.aretesRoALaPos[8:]==[1,1,1,1]: #on traite le cas où le centre jaune est la seule facette jaune sur sa face
                s.mvtligne(1)
            k=8    
            while s.aretesRoALaPos[8:]!=[0,0,0,0]:  #on a alors forcément une configuration de type J ou ligne horizontale
                if k!=11 and s.aretesRoALaPos[k]==0 and s.aretesRoALaPos[k+1]==0: #on cherche les config de type J
                    s.mvttypeJ(k-7,k-6)
                elif k==11 and s.aretesRoALaPos[11]==0 and s.aretesRoALaPos[8]==0:
                    s.mvttypeJ(4,1)
                elif k!=10 and k!=11 and s.aretesRoALaPos[k]==0 and s.aretesRoALaPos[k+2]==0:     #on cherche les config de type ligne horyzontale
                    s.mvtligne(k-7)
                k=k+1
                    
    
    
    
## Etape 5: positionnement des aretes de la derniere face, càd grande croix ##
    def petitechaise(s,fNum,cote):              #à renommer si vous voulez
        """effectue les 8 mouvements de la chaise sur une face et dans un sens donné"""
        [B,O,V,R,J]=[1,2,3,4,5]
        s.move(fNum,1+2*cote)   #cote=0 =>droite
        s.move(J,2)             #cote=1 =>gauche
        s.move(fNum,3-2*cote)
        s.move(J,3-2*cote)
        s.move(fNum,1+2*cote)
        s.move(J,3-2*cote)
        s.move(fNum,3-2*cote)
    
    def chaise(s):
        """établit la grande croix/positionne les 4 dernières arêtes (étape 5)"""
        PosB=s.aretesPosDuBloc[8]
        [B,O,V,R,J]=[1,2,3,4,5]
        a=8-PosB
        c=0
        s.move(J,a)  #le bloc 8 est correctement placé      
        
        PosB=s.aretesPosDuBloc[8]
        PosO=s.aretesPosDuBloc[9]
        PosV=s.aretesPosDuBloc[10]
        PosR=s.aretesPosDuBloc[11]
        if not([PosO,PosV,PosR]==[9,10,11]): #sont-ils bien placé?
            
            if PosV==10:                            #   .o.
                #Chaise                             #   xox
                s.petitechaise(R,0)                 #   .o.
                PosO=s.aretesPosDuBloc[9]
                PosR=s.aretesPosDuBloc[11]
                    
            if PosO==9:                             #   .x.
                #Chaise Verte                       #   oox
                s.move(J,3)                         #   .o.
                b=O
                    
            elif PosR==11:                          #   .x.
                #Chaise Orange                      #   xoo
                s.move(J,3)                         #   .o.
                b=B
                    
            elif PosO==11:
                #Chaise droite
                b=R
            else:
                #Chaise gauche
                b=O
                c=1
            s.petitechaise(b,c)
     
### Etape 6: positionnement des sommets de la dernière face ###
    ## Schéma:
    # Des sommets en haut :  . B . O . V . R . B .
    # Numéro de la face:     . 1 . 2 . 3 . 4 . 1 .
    # Numéro du sommet fixe: 3 . 0 . 1 . 2 . 3 . 0
    def coinsPermuPosJ (s,sommet_fixe,sns):
        """Permute trois sommets de la face J sans affecter les autres blocs du cube.
    `sommet_fixe` indique le numéro (0-3) du sommet qui ne sera pas déplacé.
    `sns` indique le sens (1 ou -1) de la permutation. 1: sens horaire, -1: sens anti-horaire"""
        w = lambda k: 1 + (sommet_fixe+k-1) % 4 # Calcule le numéro de la face.
        face     = [w(0),   5,w(2),   5,w(0),   5,w(2),   5]
        nbQuarts = [ sns,-sns,-sns, sns,-sns,-sns, sns, sns] # Le sens de rotation des faces dépend de la diretion de permutation.
        # Si la permutation doit être anti-horaire, on inverse l'ordre des mouvements (et leur direction, voire ci-dessus)
        for i in range(0,8)[::sns]:
            s.move(face[i],nbQuarts[i])
    
    def quelCoinsJEstBienPlaces (s):
        estBienPlace = []
        for i in range(4,8):
            if s.sommetsBlocALaPos[i] == i:
                estBienPlace.append(i)
        return estBienPlace
        
    def coinsPosJ (s):
        """Place les sommets de la face J à leur position, sans affecter la position, ni la rotation des autres blocs du cube."""
        global sav
        sav = s.clonerCube()
        # Trois cas sont possibles:
        # 1) aucun sommet n'est à la bonne position. (1 -> 2)
        # 2) seule un sommet est la bonne position. 
        # 3) les quatres sommets sont correctemments placés.
        estBienPlace = s.quelCoinsJEstBienPlaces()
        compte = len(estBienPlace) # On compte le nombre de sommets bien placés

        if compte == 0: # Si aucun n'est bien placé, 
            s.coinsPermuPosJ(0,1)  # n'importe quels mouvement démèle la situation
            estBienPlace = s.quelCoinsJEstBienPlaces()
            compte = len(estBienPlace) # On (re)compte le nombre de sommets bien placés
        
        if compte == 1: # Un unique sommet est bien placé
            fixe = estBienPlace[0] % 4 + 4 # On trouve le sommet qui est bien place
            suivant = (fixe + 1) % 4 + 4  # Le sommet suivant
            oppose =  (fixe + 2) % 4 + 4  # Et le sommet encore après, afin de déterminer le sens du mouvement
            sens = (1 if s.sommetsBlocALaPos[oppose] == suivant else -1) # On établi le sens de la permutation
            s.coinsPermuPosJ(fixe,sens)
        
        if compte == 2: # Il ne peut jamais y avoir exactement 2 sommets bien positionnés.
            raise AssertionError("coinsPosJ: Cube irrésolvable car mal remonté: imparité des positions sommets-arêtes.")

        if compte == 3:
            raise AssertionError("coinsPosJ: Nombre de coins mal placé impossible (1 coins): Érreur à l'identification des blocs ?")
        
        compte = sum([ s.sommetsBlocALaPos[i] == i for i in range(4,8)]) # On recompte le nombre de sommet bien placés,
        if compte != 4: # pour s'assurer que tout à bien fonctionné.
            raise AssertionError("\n".join(["coinsPosJ: Echec du placement des sommets de la dernières face:",
                                            "estBienPlace = {}".format(estBienPlace),
                                            "compte(finale) = {}".format(compte)
                                            ]) )

    ### Orientation des sommets de la dernière face
    def coinsDegJ (s):
        """ Effectue une succession de mouvements établissant une rotation des derniers blocs mal orientés sur la face s.J (Etape 7) """
        J = 5 # 5 est le numéro de la face jaune
        for k in range(3):
            sommet = [4,5,6][k]
            
            currentDeg = s.sommetsRoDuBloc[sommet]
            
            while not(currentDeg == 0):
                for i in range(2): # Partie 1 face de gauche (k+1), Partie 2 face de droite (k-1)
                    s.move(s.BOVR[[k+1,k-1][i]],[3,1][i]) # -> combinaison partie (i+1)/2
                    s.move(J,2)                           # -> ----------- ------ -------
                    s.move(s.BOVR[[k+1,k-1][i]],[1,3][i]) # -> ----------- ------ -------
                    s.move(J,[1,3][i])                    # -> ----------- ------ -------
                    s.move(s.BOVR[[k+1,k-1][i]],[3,1][i]) # -> ----------- ------ -------
                    s.move(J,[1,3][i])                    # -> ----------- ------ -------
                    s.move(s.BOVR[[k+1,k-1][i]],[1,3][i]) # -> ----------- ------ -------
                
                currentDeg = s.sommetsRoDuBloc[sommet]

    def toutResoudre (s):
        """Fait la résolution complete du cube"""
        etapes = [s.croixW, s.sommetsW, s.belge, s.petiteCroixJ, s.chaise, s.coinsPosJ, s.coinsDegJ, s.genListe]
        i = 0
        for action in etapes:
            action()
            s.listeDesMouvements += "**"  # Commentez cette ligne pour enlever les * 
        return s.syntheseDesMvts
