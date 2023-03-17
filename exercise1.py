import math
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Liste des couleurs de arcade.color
COULEURS = [arcade.color.WHITE, arcade.color.WHEAT, arcade.color.LIGHT_YELLOW, arcade.color.YELLOW,
            arcade.color.ORANGE, arcade.color.RED, arcade.color.GREEN,
            arcade.color.PURPLE, arcade.color.BROWN, arcade.color.CYAN, arcade.color.PINK,
            arcade.color.LIGHT_GREEN, arcade.color.ASH_GREY]


# La clase Cercle
class Cercle:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.rayon = 0
        self.color = (0, 0, 0)

    def draw(self):
        arcade.draw_circle_filled(self.x,
                                  self.y,
                                  self.rayon,
                                  self.color)


# La classe arcade
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exemple design")
        # La liste que contient des cercles
        self.liste_cercles = []

    def setup(self):
        # nombre total de cercles ajoutes
        # on ne sait pas en avance combien de cycles nous allons faire, car si
        # le cercle collide avec un autre cercle, on ne l'ajoute pas a la liste
        total_cercles = 0

        while total_cercles < 20:
            ajouter_cercle = True
            # parametres aleotoires d'un nouveau cercle
            rayon = random.randint(10, 30)
            center_x = random.randint(rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(rayon, SCREEN_HEIGHT - rayon)

            if len(self.liste_cercles) == 0:
                # si c'est le premier cercle, on l'ajoute, il n'y a pas de colision
                self.ajouter_cercle(center_x, center_y, rayon)
                total_cercles += 1
            else:
                # verifier si il y a des collisions avec les autres cercles
                for autre_cercle in self.liste_cercles:
                    # calculer distance cartesienne de chaque des autres cercles en utilisant theoreme de Pitagore
                    # si nous trouvons une intersection on n'ajoute pas ce cercle
                    # distance entre deux centres doit etre plus grand que la somme de rayons
                    dist_x = center_x - autre_cercle.x
                    dist_y = center_y - autre_cercle.y
                    # Distance actuelle
                    dist = math.sqrt(dist_x * dist_x + dist_y * dist_y)
                    # distance minimal entre deux centres pour que les cercles ne collident pas
                    dist_necessaire = rayon + autre_cercle.rayon
                    if dist < dist_necessaire:
                        # il y a une collision avec un autre cercle on sort de cycle et on ne ajoute pas ce cercle
                        ajouter_cercle = False
                        # nous sortons de cycle, pas besoin de verifier collision avec les autres cercles
                        break

                # Si il n'y a pas de collision, nous pouvons ajouter ce cercle
                if ajouter_cercle:
                    total_cercles += 1
                    self.ajouter_cercle(center_x, center_y, rayon)

    # Creer nouveau Cercle et ajouter a la liste de cercles
    def ajouter_cercle(self, x, y, r):
        cercle = Cercle()
        cercle.rayon = r
        cercle.x = x
        cercle.y = y
        cercle.color = random.choice(COULEURS)
        self.liste_cercles.append(cercle)

    def on_draw(self):
        arcade.start_render()
        # On appele draw pour chaque cercle
        for cercle in self.liste_cercles:
            cercle.draw()


def main():
    my_game = MyGame()
    my_game.setup()
    arcade.run()


main()
