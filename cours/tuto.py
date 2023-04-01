import pygame

# Comment fonctionne pygame ?
# Pygame fonctionne avec des surfaces (surface)
# Une surface est un espace rectangulaire qui peut être affiché à l'écran
# Sur une surface, on peut dessiner des formes géométriques
# ou afficher des images ou afficher du texte

# On initialise pygame avec une surface principale (ecran)
pygame.init()
ecran = pygame.display.set_mode((800, 600))

# On peut récupérer la largeur et la hauteur de la surface
largeur = ecran.get_width()
hauteur = ecran.get_height()

#############################################
###    Dessiner des trucs avec Pygame     ###
#############################################

# Afficher une image sur la surface
image = pygame.image.load("images/champi_rouge.png")
ecran.blit(image, (0, 0))

# On peut redimensionner une image
image = pygame.transform.scale(image, (100, 100))  # largeur, hauteur

# Afficher du texte sur la surface
police = pygame.font.Font("pixel.ttf", 50)  # police et taille
# texte, antialiasing, couleur
texte = police.render("Bonjour", False, (255, 0, 0))
ecran.blit(texte, (0, 0))  # position

# Créer une surface rectangulaire
surface = pygame.Surface((100, 100))
surface.fill((255, 0, 0))  # couleur
ecran.blit(surface, (0, 0))

# Actualiser l'affichage
# À chaque fois qu'on modifie la surface, il faut actualiser l'affichage
# On ne le fait qu'une fois pour toutes les modifications afin d'éviter
# de ralentir le programme
pygame.display.flip()

#############################################
###  Les événements avec Pygame           ###
#############################################

# On peut détecter lorsqu'un joueur appuie sur une touche du clavier
# ou lorsqu'il clique sur un bouton de la souris ou lorsqu'il bouge la souris
# grâce à des `événments` (event)

# À chaque tour de boucle, on récupère tous les événements et on actualise le jeu en fonction
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Si l'utilisateur clique sur la croix en haut à droite
            continuer = False
        elif event.type == pygame.KEYDOWN: # Si l'utilisateur appuie sur une touche
            if event.key == pygame.K_ESCAPE: # Si c'est la touche échap
                continuer = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Si l'utilisateur clique sur la souris
            if event.button == 1: # Si c'est le bouton gauche
                print("Clic gauche")
            elif event.button == 3: # Si c'est le bouton droit
                print("Clic droit")

    # On actualise l'affichage
    # pleins de lignes de code pour actualiser l'affichage
    # ...
    # ...
    # puis on actualise l'affichage
    pygame.display.flip()
