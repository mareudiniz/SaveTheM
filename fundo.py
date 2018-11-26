import pygame
import random
#cores--------------------------------------------
azul = ( 0,0,255)
verde = (0 , 255, 0 )
roxo = (255, 0, 255)
branco = (255,255,255)
preto = (0, 0, 0 )
marrom = (142,107,35)

#inicializaçao------------------------------------
linha = [0]*5
maxsquares = 4
tabuleiro = linha * 5
altura = 500
largura = 500
tamanho = 100
inix = 0
iniy = 0
pos_x = largura/5 * inix
pos_y = altura/5 * iniy
titulo = "Save The M"
sair = True
random.seed(157)
tamanhox = altura/(maxsquares+1)
tamanhoy = largura/(maxsquares+1)

#classes-------------------------------------------

class whiskas:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.a = tamanhox
        self.l = tamanhoy
        self.colour = colour
        self.alive = 1

    def draw(self):
        pygame.draw.rect( fundo, self.colour ,[self.x*tamanhox, self.y*tamanhoy, self.a, self.l])

        pygame.init()

try:
    pygame.init()
except:
    print('Error')

fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption(titulo)

w1x = 0
w1y = 0
while w1x == 0 and w1y == 0:
    w1x = random.randint(0, maxsquares)
    w1y = random.randint(0, maxsquares)

whiskas1 = whiskas(w1x, w1y, marrom)

w2x = w1x
w2y = w1y
while (w2x == w1x and w2y == w1y) or (w2x == 0 and w2y == 0):
    w2x = random.randint(0, maxsquares)
    w2y = random.randint(0, maxsquares)

whiskas2 = whiskas(w2x, w2y, marrom)

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.KEYUP   :
            if event.key == pygame.K_LEFT:
                if inix != 0:
                    inix = inix-1
            if event.key == pygame.K_RIGHT:
                if inix != maxsquares:
                    inix = inix+1
            if event.key == pygame.K_UP:
                if iniy != 0:
                    iniy = iniy-1
            if event.key == pygame.K_DOWN:
                if iniy != maxsquares:
                    iniy = iniy+1


    fundo.fill(preto)
    pygame.draw.rect( fundo, branco ,[pos_x, pos_y, tamanho, tamanho])

    if whiskas1.x == inix and whiskas1.y == iniy:
        whiskas1.alive = 0
    if(whiskas2.x == inix and whiskas2.y == iniy):
        whiskas2.alive = 0
    if(whiskas1.alive == 1):
        whiskas1.draw()
    if(whiskas2.alive == 1):
        whiskas2.draw()

    pos_x = (largura/(maxsquares+1)) * inix
    pos_y = (largura/(maxsquares+1)) * iniy

    pygame.display.update()

pygame.draw.rect (fundo,)
pygame.quit()
