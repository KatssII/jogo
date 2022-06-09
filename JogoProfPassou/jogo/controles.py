import pygame

coluna, linha = 400, 300

def ctrl_key(key):

    global linha
    global coluna

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        coluna -= 1

    if keys[pygame.K_RIGHT]:
        coluna += 1

    if keys[pygame.K_UP]:
        linha -= 1


    if keys[pygame.K_DOWN]:
        linha += 1
        # carro_path = "img/seta_baixo.png"
        # carro1.setImage(carro_path)

    # travar o objeto na tela.
    # if coluna < 0: coluna=0
    # if coluna > 765: coluna=765

    if linha > 560: linha = 560

    # if linha < 409: linha= 409
    # if linha < 30: linha = 30
