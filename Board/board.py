import pygame

pygame.init()



class Board:

    size = 25
    def __init__(self):
        self.board = []#Multiarray
        self.start = []#Punto de comienzo
        self.end = []#Punto final
        self.generate()

    def draw(self, screen):

        if len(self.start) > 0:
            pygame.draw.rect(screen, (255, 0, 0), [self.start[0], self.start[1], self.size, self.size])
        if len(self.end) > 0:
            pygame.draw.rect(screen, (0, 0, 255), [self.end[0], self.end[1], self.size, self.size])


        #Dibuja el tablero
        for r in self.board:
            for s in r:
                pygame.draw.rect(screen, (0,0,0), [s[0], s[1], self.size, self.size], 1)
            
    def setPoints(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for r in self.board:
                        for s in r:
                            if pygame.Rect(s[0], s[1], 25, 25).collidepoint(event.pos):
                                if not self.start:
                                    self.start = s
                                elif not self.end:
                                    self.end = s


    def generate(self):
        """
        Genera el grid
        """
        for r in range(0, 20):#500(screen height) / 25 = 20
            row = []
            for c in range(0, 40):#1000(screen width) / 25 = 40
                row.append([c*self.size, r*self.size])

            self.board.append(row)
            row = []