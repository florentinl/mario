import pygame


class Menu:
    def __init__(self, ecran, titre, options):
        self.ecran = ecran

        self.titre = titre
        self.options = options
        self.selection = 0

        self.police_option = pygame.font.Font("pixel.ttf", 50)
        self.police_titre = pygame.font.Font("mario.ttf", 100)

        self.champi_rouge = pygame.image.load("images/champi_rouge.png")
        self.champi_rouge = pygame.transform.scale(
            self.champi_rouge, (50, 50))

        self.champi_gris = pygame.image.load("images/champi_gris.png")
        self.champi_gris = pygame.transform.scale(
            self.champi_gris, (50, 50))

        self.fond = pygame.image.load("images/fond.png")

    def afficher_fond(self):
        # Récupérer la hauteur de l'écran
        hauteur = self.ecran.get_height()

        # Récupérer les dimensions de l'image
        hauteur_image = self.fond.get_height()
        largeur_image = self.fond.get_width()

        # Redimensionner l'image
        fond = pygame.transform.scale(
            self.fond, (hauteur * largeur_image / hauteur_image, hauteur))

        # Afficher l'image
        self.ecran.blit(fond, (0, 0))

    def afficher_titre(self, titre):
        # Récupérer la hauteur et la largeur de l'écran
        largeur = self.ecran.get_width()

        surface = self.police_titre.render(titre, False, (255, 0, 0))
        self.ecran.blit(
            surface, (largeur // 2 - surface.get_width() // 2, 100))

    def afficher_options(self):
        # Récupérer la hauteur et la largeur de l'écran
        hauteur = self.ecran.get_height()
        largeur = self.ecran.get_width()

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
        self.afficher_titre("Mario")

        # Afficher les options
        self.afficher_options()

    def gerer_evenement(self, evenement) -> str | None:
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_UP:
                self.selection = (self.selection - 1) % len(self.options)
                return None
            elif evenement.key == pygame.K_DOWN:
                self.selection = (self.selection + 1) % len(self.options)
                return None
            elif evenement.key == pygame.K_RETURN:
                return self.options[self.selection]
        return None
