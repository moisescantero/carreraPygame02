"""Juego de 4 corredores"""
import pygame, sys, random

class Runner():
    __customes = ("turtle","fish","prawn","moray","octopus")
    def __init__(self,x=0,y=0,custome="turtle"):
        ixCustome = random.randint(0,4)
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))#cargo imagen de tortuguita
        self.position = [x,y]#defino posición para tortuguita
        self.name = custome#doy nombre a tortuguita
    def avanzar(self):
        
        self.position[0] += random.randint(1,6)#posición x le asigno un entero aleatorio de 1 a 6
              


class Game():
    runners = []
    __posY = (160,200,240,280)
    __names = ("Speedy","Lucera","Alonso","Torcuata")
    __startLine = -5
    __finishLine = 620
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640,480))#iniciamos pantalla dando tamaño
        self.__background = pygame.image.load("images/desert.png")#imagen de fondo de pantalla
        pygame.display.set_caption("Carrera de bichos")#nombre para la pantalla
        for i in range (4):
            theRunner = Runner(self.__startLine,self.__posY[i])#añado corredor que empieza en x e y
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
    
    def close(self):
        pygame.quit()
        sys.exit()           
    
    def competir(self):
        gameOver = False
        while not gameOver:#comprobamos eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#si el tipo de evento es igual a quitar pygame
                    gameOver = True#hasta aquí comprobamos eventos
                    
                for runner in self.runners:#actualizamos eventos
                    runner.avanzar()
                    if runner.position[0] >= self.__finishLine:
                        print("{} ha ganado.".format(runner.name))
                        gameOver = True#hasta aquí actualiz eventos
                        
                    #resfrescamos pantalla
                self.__screen.blit(self.__background, (0,0))#pintamos el fondo y damos coordenadas que empiezan arriba a la izquierda
                for runner in self.runners:
                    self.__screen.blit(runner.custome, runner.position)#pinto corredor y su posición
                
                pygame.display.flip()# función refrescar/renderizar pantalla, cogida directamente de la librería pygame
                    #hasta aquí refrescamos pantalla
                
        while True:#este while es para que no se llene el buffer y poder cerrar ventana antes de que se cuelgue la aplicación
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#si el tipo de evento es igual a quitar pygame
                    self.close()

            
        
    




if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()