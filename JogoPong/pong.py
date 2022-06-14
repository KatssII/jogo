import  pygame

class bola:
    def __init__(self, janela, cor, pX, pY, radius):
        self.janela = janela
        self.cor = cor
        self.pX = pX  # posicao do X
        self.pY = pY  # posicao do Y
        self.radius = radius
        self.mostrar()

        def mostrar(self):
            pygame.draw.circle(self.janela, self.cor, (self.pX, self.pY), self.radius)


pygame.init()
largura = 800
altura = 500
centro = 400, 250
PI = 3.1416


janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("jogo ping e pong")

def paint_back():
    janela.fill((34, 139, 34))
    pygame.draw.line(janela, (255, 255, 255), (largura//2, 0), (largura//2, altura), 5)
    pygame.draw.circle(janela, (255, 255, 255), (centro), 60, 5)
    pygame.draw.circle(janela, (34, 139, 34), (centro), 55, 0)

paint_back()
#objetos
Bola = bola(janela, (255, 255, 255), largura / 2, altura//2, 7)


janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            janela_aberta= False

    pygame.display.update()