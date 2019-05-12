import pygame
import poke

WIDTH = 600
HEIGHT = 400
BAG_MAX_SIZE = 20
POKEMON_MAX_SIZE = 6

class Game():

    def __init__(self,Name,image):


        self.player = poke.Player(name= Name,img= image)
        self.map = poke.Map(10)
        #todo create the scenarios outside in a function or in a class

    def detect_keyboard(self):
        while True:
            message = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                print(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        message = "left"
                        self.player.moveLeft()
                    elif event.key == pygame.K_RIGHT:
                        message = "right"
                        self.player.moveRight()
                    if event.key == pygame.K_UP:
                        message = "up"
                        self.player.moveUp()
                    elif event.key == pygame.K_DOWN:
                        message = "down"
                        self.player.moveDown()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        message = "release"

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        message = "release"
                        # if i put just one, it just updates ones

            if message is not None:
                print(message)

#if __name__ == "__main__":
 #   g = Game("vitor", 123)
  #  g.detect_keyboard()