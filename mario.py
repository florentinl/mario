import pygame
from menu import Menu

HAUTEUR = 800
LARGEUR = 1200

pygame.init()
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))

etat = "menu"  # menu, jeu, fin
menu = Menu(ecran, "Mario", ["Jouer", "Quitter"])

running = True
while running:

    # Gérer les événements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            running = False
        elif etat == "menu":
            action = menu.gerer_evenement(evenement)
            if action == "Jouer":
                etat = "jeu"
            elif action == "Quitter":
                running = False

    # Afficher l'écran
    if etat == "menu":
        menu.afficher()
        pygame.time.wait(100)

    pygame.display.flip()
