import sys
import pygame
pygame.init()

x=400
y=250
velocidade = 15
fundo_path = "img_Mario_Jogo/fundo_mario.jpg"


janela =pygame.display.set_mode((800, 500))

pygame.display.set_caption("jogo mario bros")

fundo = pygame.image.load(fundo_path)


janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            janela_aberta= False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x -= velocidade

    janela.fill((0,0,0))

    pygame.display.update()

pygame.quit()
sys.exit()