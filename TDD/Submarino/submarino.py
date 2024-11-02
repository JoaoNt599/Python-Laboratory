"""
    A posição do submarino é representado pela notação (0, 0, 0, NORTE) que indica os pontos X, Y, Z e
    a direção que o submarino aponta (Norte, Sul, Leste e Oeste).

    Os cientistas utilizam uma serie de comandos simples para fazer a movimentação do submarino:

    + L e R para girar o submarino para esquerda ou direita,
    + M para mover o submarino e
    + U e D para subir ou descer o submarino.

    0 no eixo Z é a superfície do oceano.

    ## Entrada:

    Os comandos agrupados em uma única linha, como no exemplo:

    LMRDDMMUU

    ## Saída:

    A saída deverá conter a coordenada final do submarino junto com sua direção, como no exemplo:

    -1 2 0 NORTE

    Posição inicial do submarino é 0, 0, 0, NORTE
"""


class Submarino(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0 # superfície
        self.bussola = 0 #0 norte, 1 leste, 2 sul, 3 oeste


    # saída esperada
    def coordenada(self, comando=''):
        for coor in comando:
            if coor == 'R':
                self.right()
            elif coor == 'L':
                self.left()
            elif coor == 'U':
                self.up()
            elif coor == 'D':
                self.down()
            elif coor == 'M':
                self.movimentar()

        direcao = ['NORTE', 'LESTE', 'SUL', 'OESTE'][self.bussola]
        return "%s %s %s %s" % (self.x, self.y, self.z, direcao)
             
    
    # todo movimento quando o submarino estiver apontando para o NORTE, somará 1 ao eixo Y
    def movimentar(self):
        
        if (self.bussola == 0):
            self.y += 1
        
        if(self.bussola == 2):
            self.y -= 1

    # todo movimento quando o submarino estiver apontando para o LESTE somará 1 ao eixo X
        if (self.bussola == 1):
            self.x += 1

        if(self.bussola == 3):
            self.x -= 1

        return True
    

    def right(self):
        self.bussola = 0 if self.bussola == 3 else self.bussola + 1
        return self.bussola
    

    def left(self):
        self.bussola == 3 if self.bussola == 0 else self.bussola - 1
        return self.bussola
    

    def up(self):
        self.z = 0 if self.z == 0 else self.z + 1
        return self.z
    

    def down(self):
        self.z = self.z -1
        return self.z


