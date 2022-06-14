import sys
import pygame
#from pygame.examples.headless_no_windows_needed import screen
from jogoMario.mario import Mario

pygame.init()
x=400 #vertical
y=250 #horizontal
velocidade = 15
#coluna_pista = 55
#linha_pista = 0

fundo = pygame.image.load("img_Mario_Jogo/fundo_mario.jpg")
mario = pygame.image.load("img_Mario_Jogo/Mario1.png")

#mario = Mario.Mario(direcao=0, sentido=0, velocidade=10, mario_path=mario_path)

janela = pygame.display.set_mode((800, 500))
pygame.display.set_caption("jogo mario")

# fundo = pygame.image.load(fundo_path)
# mario = pygame.image.load(mario.getImagem())

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    # mover_fundo(position=(coluna_pista, linha_pista))
    # carro = pygame.image.load(mario.getImagem())
    #
    # mover_fundo((coluna_pista, linha_pista))
    #
    # mario.setPosition(position=(coluna_pista, linha_pista))

    # def mover_fundo(position=(coluna_pista, linha_pista)):
    #     if position[0] >= 600:
    #         pygame.display.flip()
    #         position[0] = 0


    #limite da tela
    if y > 350: y = 350
    if y < -10: y = -10
    if x < -30: x = -30
    if x > 680: x = 680


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            janela_aberta= False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if event.type == KEY_DOWN:
         if event.key == K_SPACE:
                mario.pular()

    janela.blit(fundo,(0,0))
    janela.blit(mario,(x,y))

    pygame.display.update()
    #pygame.quit()
    #sys.exit()