import pygame, sys
from Board.board import Board
from ShortestPathFinding.spf import *
pygame.init()

W, H = 1000, 500#Dimensiones de la ventana

pygame.display.set_caption("Visualización de Dijkstra's Algorithm")
def main():
    screen = pygame.display.set_mode((W, H))
    board = Board()
    newboard = board.board
    grid = gridElementToString(newboard)
    pathForDraw = None
    walls = []#Muros
    wallsStr = []#[x, y] -> str([x. y]) para pasarlo a la función dijkstra

    fps = pygame.time.Clock()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    for r in newboard:
                        for square in r:
                            if pygame.Rect(square[0], square[1], 25, 25).collidepoint(event.pos):
                                #si ya los puntos están posicionados
                                    walls.append(square)
                                    if str(square) not in walls:#si el muro no está en la lista lo agrega
                                        wallsStr.append(str(square))
            #Puntos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if board.start and board.end:
                        path = dijkstra(grid, G, str(board.start), str(board.end), wallsStr)#Actualizar la ruta
                        pathForDraw = []
                        for row in board.board:
                            for column in row:
                                if str(column) in path:
                                    pathForDraw.append(column)
                #Limpia el tablero(puntos, muros y ruta)
                if event.key == pygame.K_TAB:#Limpiar ruta y puntos
                    pathForDraw = None
                    board.start = []
                    board.end = []
                    walls = []
                    wallsStr = []

            board.setPoints(event)#Configura los puntos de inicio y final

        screen.fill((255,255,255))
        #Print walls 
        if pathForDraw:
            for square in pathForDraw:
                pygame.draw.rect(screen, (0,255,236), [square[0], square[1], 25, 25])
        board.draw(screen)
        for w in walls:
            pygame.draw.rect(screen, (0,0,0), [w[0], w[1], 25, 25])
        pygame.display.update()
        fps.tick(20)

if __name__ == "__main__":
    
    main()