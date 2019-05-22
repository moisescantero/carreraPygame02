"""juegos 4 corredores moverlo por pantalla"""

import pygame, sys, random
from pygame.locals import *

class Runner():
    __customes = ("turtle","fish","prawn","moray","octopus")
    def __init__(self,x=0,y=0):
        ixCustome = random.randint(0,4)
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))#cargo imagen de tortuguita
        self.position = [x,y]#defino posición para tortuguita
        self.name = ""#doy nombre a tortuguita

class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))#iniciamos pantalla dando tamaño
        self.__background = pygame.image.load("images/desert.png")#imagen de fondo de pantalla
        pygame.display.set_caption("Carrera de bichos")#nombre para la pantalla
        
        self.runner = Runner(320,240)
    
    def start(self):
        gameOver = False
        while not gameOver:#comprobamos eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#si el tipo de evento es igual a quitar pygame
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:#mover hacia arriba runner
                        self.runner.position[1] -= 5#extraigo posiciónY del runner, incremento y guardo nueva posición
                    elif event.key == K_DOWN:#mover hacia abajao runner
                        self.runner.position[1] += 5#extraigo posiciónY del runner, decremento y guardo nueva posición
                    elif event.key == K_LEFT:#mover hacia izquierda
                        self.runner.position[0] -= 5#extraigo posiciónX del runner, decremento y guardo nueva posición
                    elif event.key == K_RIGHT:#mover hacia derecha
                        self.runner.position[0] += 5#extraigo posiciónX del runner, decremento y guardo nueva posición
                    else:
                        pass
            #resfrescamos pantalla
            self.__screen.blit(self.__background, (0,0))#pintamos el fondo y damos coordenadas que empiezan arriba a la izquierda
            self.__screen.blit(self.runner.custome, self.runner.position)#pinto corredor y su posición
            
            pygame.display.flip()
        while True:#este while es para que no se llene el buffer y poder cerrar ventana antes de que se cuelgue la aplicación
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#si el tipo de evento es igual a quitar pygame
                    self.close()
            

if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.start()
    



                    
            