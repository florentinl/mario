import pygame


class Menu:
    def __init__(self, ecran, titre, options):
        self.ecran = ecran

        self.titre = titre
        self.options = options
        self.selection = 0

        # La police s'appelle "pixel.ttf" et taille 50
        self.police_option = "Au travail !"
        # La police s'appelle "mario.ttf" et taille 100
        self.police_titre = "Au travail !"

        self.champi_rouge = "Au travail !"  # Charger l'image "champi_rouge.png
        # Redimensionner l'image à 50x50 (même taille que les options)
        self.champi_rouge = "Au travail !"

        self.champi_gris = "Au travail !"  # Charger l'image "champi_gris.png
        self.champi_gris = "Au travail !" # Redimensionner l'image à 50x50

        self.fond = "Au travail !"  # Charger l'image "fond.png

    def afficher_fond(self):
        # Récupérer la hauteur de l'écran
        hauteur = "Au travail !"

        # Récupérer les dimensions de l'image
        hauteur_image = "Au travail !"
        largeur_image = "Au travail !"

        # Redimensionner l'image

        # fond = pygame.transform.scale(
        #    self.fond, (hauteur * largeur_image / hauteur_image, hauteur))

        # Afficher l'image
        "Au travail !"  # Afficher l'image en haut à gauche

    def afficher_titre(self, titre):
        # Récupérer la hauteur et la largeur de l'écran
        """

        Au travail !
        attention le texte doit être centré horizontalement

        """

    def afficher_options(self):
        # Récupérer la hauteur et la largeur de l'écran
        hauteur = "Au travail !"
        largeur = "Au travail !"

        # Afficher les options
        # Pour chaque option, on créé un rectangle
        # qui contient un champignon et le texte de l'option
        options = []
        for i in range(len(self.options)):
            texte = self.police_option.render(
                self.options[i], False, (255, 255, 255))
            options.append(texte)

        # On récupère la largeur et la hauteur maximale
        hauteur_max = max(option.get_height() for option in options)
        largeur_max = max(option.get_width()
                          for option in options) + hauteur_max + 40

        # On affiche les options
        for i in range(len(options)):
            if i == self.selection:
                self.ecran.blit(self.champi_rouge, (largeur // 2 - largeur_max // 2,
                                                    hauteur // 2 + i * (hauteur_max + 50)))
            else:
                self.ecran.blit(self.champi_gris, (largeur // 2 - largeur_max // 2,
                                                   hauteur // 2 + i * (hauteur_max + 50)))
            self.ecran.blit(options[i], (largeur // 2 - largeur_max // 2 + hauteur_max + 40,
                                         hauteur // 2 + i * (hauteur_max + 50)))

    def afficher(self):
        # Afficher arrière-plan
        self.afficher_fond()

        # Afficher le titre
        # self.afficher_titre("Mario")

        # Afficher les options
        # self.afficher_options()

    def gerer_evenement(self, evenement) -> str | None:
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_UP:
                "Au travail !"
                return None
            elif evenement.key == pygame.K_DOWN:
                "Au travail !"
                return None
            elif evenement.key == pygame.K_RETURN:
                return self.options[self.selection]
        return None
