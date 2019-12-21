import unittest
import server

class TestServer(unittest.TestCase):
    def setUp(self):
        self.tabuleiro = ['X','X','X','0','0','0','0','0','0']
        self.tabString = 'XXX000000'

    def testWinner(self):
        tabuleiro1 = ['X','X','X','0','0','0','0','0','0']
        tabuleiro2 = ['0','0','0','O','O','O','X','O','0']
        tabuleiro3 = ['X','X','X','0','0','0','X','X','X']
        tabuleiro4 = ['X','O','O','X','0','0','X','O','O']
        tabuleiro5 = ['0','O','O','X','O','0','0','O','X']
        tabuleiro6 = ['O','0','X','0','0','X','O','O','X']
        tabuleiro7 = ['X','O','X','O','X','O','0','0','X']
        tabuleiro8 = ['X','0','O','0','O','0','O','0','X']


        self.assertEqual(server.winner(tabuleiro1), 'X')
        self.assertEqual(server.winner(tabuleiro2), 'O')
        self.assertEqual(server.winner(tabuleiro3), 'X')
        self.assertEqual(server.winner(tabuleiro4), 'X')
        self.assertEqual(server.winner(tabuleiro5), 'O')
        self.assertEqual(server.winner(tabuleiro6), 'X')
        self.assertEqual(server.winner(tabuleiro7), 'X')
        self.assertEqual(server.winner(tabuleiro8), 'O')
       
    def testSalvaEstadoJogo(self):
        add1 = '127.1.2.3'
        add2 = '122.9.4.5'
        numJogada = 2
        pontuacaoXis = 2
        pontuacaoBola = 0

        self.assertIsNone(server.salvaEstadoJogo(add1,add2,self.tabuleiro,
            numJogada,pontuacaoXis,pontuacaoBola))

    def testRecuperaEstadodoJogo(self):
        add1 = '127.1.2.3'
        add2 = '122.9.4.5'
        add0 = '24.323.3.5'
        add01 = '25.33.55.5'

        numJogada, pontuacaoBola, pontuacaoXis, tabString = server.recuperaEstadoJogo(add0,add01)

        self.assertEqual(numJogada,0)
        self.assertEqual(pontuacaoBola,0)
        self.assertEqual(pontuacaoXis,0)
        self.assertEqual(tabString,'000000000')

        numJogada1, pontuacaoBola1, pontuacaoXis1, tabString1 = server.recuperaEstadoJogo(add1,add2)

        self.assertEqual(numJogada1,2)
        self.assertEqual(pontuacaoBola1,0)
        self.assertEqual(pontuacaoXis1,2)
        self.assertEqual(tabString1,'XXX000000')

    def testArrumaTabuleio(self):

        self.assertEqual(server.arrumaTabuleiro(self.tabString),self.tabuleiro)

if __name__ == "__main__":
    unittest.main()
    