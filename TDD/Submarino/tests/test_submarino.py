try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../../submarine'
            )
        )
    )
except:
    raise

import unittest

from submarino import *

class SubmarinoTest(unittest.TestCase):


    def test_coordenada(self):
        sub = Submarino() # entrada dos cientistas
        self.assertEqual('-1 2 0 NORTE', sub.coordenada("LMRDDMMUU")) # saida

        sub = Submarino()
        self.assertEqual('2 3 -2 SUL', sub.coordenada("RMMLMMMDDLL"))

       
    def test_posicao_inicial(self):
        sub = Submarino()
        self.assertEqual('0 0 0 NORTE', sub.coordenada())
        

#       Norte
#         0
# Oeste         Leste
#   3             1
#        Sul
#         2

def test_posicionamento(self):
    sub = Submarino()
    self.assertEqual(0, sub.bussola)
    self.assertEqual(3, sub.left())
    self.assertEqual(0, sub.right())
    self.assertEqual(1, sub.right())
    self.assertEqual(2, sub.right())


def test_profundidade(self): # 0 é a superfície
    sub = Submarino()
    self.assertEqual(0, sub.z)
    self.assertEqual(0, sub.up())
    self.assertEqual(-1, sub.down())
    self.assertEqual(-2, sub.down())
    self.assertEqual(-3, sub.down())
    self.assertEqual(-2, sub.up())


def test_movimentar_apontando_para_norte(self):
    sub = Submarino()
    sub.bussola = 0

    sub.movimentar()
    self.assertEqual(0, sub.x)
    self.assertEqual(1, sub.y)

    sub.movimentar()
    self.assertEqual(0, sub.x)
    self.assertEqual(2, sub.y)

    sub.movimentar()
    self.assertEqual(0, sub.x)
    self.assertEqual(3, sub.y)


def test_movimentar_apontando_para_sul(self):
    sub = Submarino()
    sub.bussola = 2

    sub.movimentar()
    self.assertEqual(0, sub.x)
    self.assertEqual(-1, sub.y)

    sub.movimentar()
    self.assertEqual(0, sub.x)
    self.assertEqual(-2, sub.y)

    sub.movimentar()
    self.assertEqual(0, sub.x)
    self.assertEqual(-3, sub.y)


def test_movimentar_apontando_para_oeste(self):
    sub = Submarino()
    sub.bussola = 3

    sub.movimentar()
    self.assertEqual(-1, sub.x)
    self.assertEqual(0, sub.y)

    sub.movimentar()
    self.assertEqual(-2, sub.x)
    self.assertEqual(0, sub.y)

    sub.movimentar()
    self.assertEqual(-3, sub.x)
    self.assertEqual(0, sub.y)

    
if __name__ == '__main__':
    unittest.main(verbosity=2)