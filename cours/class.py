# Les classes en python

# Un objet est une sorte de "boîte" qui contient des variables et des fonctions

# Par exemple une liste est un objet qui contient des variables et des fonctions
l = list() # l est un objet de type list
l.append(1) # l.append est une fonction de l'objet l
l.append(2) # l.append est une fonction de l'objet l
l[0] # l contient une variable à l'indice 0

# Une classe c'est une sorte de "modèle" qui permet de créer des objets, une
# sorte de "plan" pour construire des objets.
class Personnage:
    # La fonction __init__ est appelée quand on crée un objet de type Personnage
    def __init__(self, nom, vie, attaque): # __init__ est spéciale
        # On peut créer des variables dans un objet
        self.nom = nom # self veut dire "cet objet" : on l'a mis dans notre boîte
        self.vie = vie
        self.attaque = attaque

# On peut créer plusieurs objets à partir d'une seule classe (c'est une recette)
mario = Personnage("Mario", 100, 10)
luigi = Personnage("Luigi", 100, 10)


# On peut accéder aux variables d'un objet
print(mario.nom) # Mario
print(mario.vie) # 100
print(mario.attaque) # 10

# On peut modifier les variables d'un objet
mario.vie = 50
print(mario.vie) # 50

# On peut aussi créer des fonctions dans une classe
class Personnage2:
    def __init__(self, nom, vie, attaque):
        self.nom = nom
        self.vie = vie
        self.attaque = attaque

    # On peut aussi créer des fonctions dans une classe
    def attaquer(self, cible): # self est toujours le premier argument
        cible.vie -= self.attaque
