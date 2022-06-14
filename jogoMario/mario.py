

ESQUERDA = 0
DIREITA = 1
FRENTE = 2
RE = 3
VERTICAL = 0
HORIZONTAL = 1

class Mario():
    def __init__(self, direcao,sentido=VERTICAL, velocidade=10, position=(0,0), mario_path="img/mario_sprite_sheet.png"):
        self.position = position
        self.velocidade = velocidade
        self.direcao = VERTICAL # 0 - vertical, 1 - horizontal
        self.sentido = FRENTE  # 0 - esquerda, 1 - direita
        self.pulo = False #pois é uma variavel bolean
        self.mario_path = mario_path


    def setPosition(self, position=(0,0)):
        self.position = position

    def getPosition(self):
        return self.position

    def getStatus(self):
        return self.status

    def acelerar(self):
        self.velocidade += 10

    def freiar(self):
        self.velocidade = 0

    def virar_esquerda(self):
        self.sentido = ESQUERDA

    def virar_direita(self):
        self.sentido = DIREITA

    def re(self):
        self.sentido = RE

    def frente(self):
        self.sentido = FRENTE

    def setImage(self, carro_path):
        self.mario_path = mario_path

    def getImagem(self):
        return self.mario_path

    def pular(self):
        self.pulo = True


    def update(self):
        if self.pulo == True:
            self.rect.y -= 20
