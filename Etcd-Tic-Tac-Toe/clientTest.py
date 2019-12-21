import unittest
import client

class TestClient(unittest.TestCase):
    def setUp(self):
        self.tabuleiro = ['1', '2', '3',
                          '4', '5', '6',
                          '7', '8', '9']
        self.tabString = 'XXX000000'

    def testResetTabuleiro(self):
        self.assertEqual(client.resetTabuleiro(), self.tabuleiro)

    def testAtualizaTabuleiro(self):
        self.assertEqual(client.atualizaTabuleiro(
            self.tabuleiro,
            5,
            'X'
        ),['1', '2', '3',
           '4', 'X', '6',
           '7', '8', '9'] )
        
        self.assertEqual(client.atualizaTabuleiro(
            self.tabuleiro,
            1,
            'O'
        ),['O', '2', '3',
           '4', 'X', '6',
           '7', '8', '9'])

    def testArrumaTabuleiro(self):
        self.assertEqual(client.arrumaTabuleiro(
            self.tabString
        ), ['X','X','X','4','5','6','7','8','9'])
    


if __name__ == "__main__":
    unittest.main()