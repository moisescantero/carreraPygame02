import pygame, sys

class Game():
    runners = []
    __startLine = 20
    __finishLine = 620

    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))#iniciamos pantalla dando tamaño
        self.__background = pygame.image.load("images/desert.png")#imagen de fondo de pantalla
        pygame.display.set_caption("Carrera de bichos")#nombre para la pantalla

    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#si el tipo de evento es igual a quitar pygame
                    gameOver = True
            
                self.__screen.blit(self.__background, (0,0))#pintamos el fondo y damos coordenadas que empiezan arriba a la izquierda
                
                pygame.display.flip()# función refrescar/renderizar pantalla, cogida directamente de la librería pygame

        pygame.quit()
        sys.exit()           
               
    




if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()