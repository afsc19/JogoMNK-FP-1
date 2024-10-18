import pytest 
import sys
import FP2425P1 as fp  # <--- Change the name projectoFP to the file name with your project


class TestEhTabuleiro:
    def test_1(self):
        tab = 10001
        assert not fp.eh_tabuleiro(tab)

    def test_2(self):
        tab = ((),())
        assert not fp.eh_tabuleiro(tab)
    
    def test_3(self):
        tab = [(1,0,0,1),(-1,1,0,1), (-1,0,0,-1)]
        assert not fp.eh_tabuleiro(tab)
        
    def test_4(self):
        tab = ((1,0,0,1),(-1,1,0,1), [-1,0,0,-1])
        assert not fp.eh_tabuleiro(tab)
        
    def test_5(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0))
        assert not fp.eh_tabuleiro(tab)
        
    def test_6(self):
        tab = ((1,0,0,2),(-1,1,0,1))
        assert not fp.eh_tabuleiro(tab)
        
    def test_7(self):
        tab = ((1,0,0,1),(-1,1,0,0.0))
        assert not fp.eh_tabuleiro(tab)
        
    def test_8(self):
        tab = ((1,0,0,1),)
        assert not fp.eh_tabuleiro(tab)

    def test_9(self):
        tab = ((1,),(-1,))
        assert not fp.eh_tabuleiro(tab)
        
    def test_10(self):
        tab = ((1,)*101,(-1,)*101)
        assert not fp.eh_tabuleiro(tab)
        
    def test_11(self):
        tab = ((1,)*100,(-1,)*100)
        assert fp.eh_tabuleiro(tab)
        
    def test_12(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0))
        assert fp.eh_tabuleiro(tab)
        
    def test_13(self):
        tab = ()
        assert not fp.eh_tabuleiro(tab)
        
    def test_14(self):
        tab = (1,)
        assert not fp.eh_tabuleiro(tab)
        
    def test_15(self):
        tab = ((0,1,0,0),1,(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert not fp.eh_tabuleiro(tab)
        
    def test_16(self):
        tab = ('000','111','000','111')
        assert not fp.eh_tabuleiro(tab)
        
        
class TestEhPosicao:
    def test_1(self):
        assert not fp.eh_posicao(5.0)
        
    def test_2(self):
        assert not fp.eh_posicao(True)
        
    def test_3(self):
        assert not fp.eh_posicao('25')
        
    def test_4(self):
        assert not fp.eh_posicao(0)
        
    def test_5(self):
        assert not fp.eh_posicao(-100)
        
    def test_6(self):
        assert not fp.eh_posicao(200*100)
        
    def test_7(self):
        assert all(fp.eh_posicao(n) for n in range(1, 100*100, 100))
        

class TestObtemDimensao:
    def test_1(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0))
        assert fp.obtem_dimensao(tab) == (4,4)
        
    def test_2(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0))
        assert fp.obtem_dimensao(tab) == (6,4)
        
    def test_3(self):
        tab = ((1,0,0,1,0,0),(-1,1,0,1,0,0), (-1,0,0,-1,0,0), (0,0,0,0,0,0))
        assert fp.obtem_dimensao(tab) == (4,6)
        
    def test_4(self):
        tab = ((1,)*100,(-1,)*100,(0,)*100)
        assert  fp.obtem_dimensao(tab) == (3,100)
        
class TestObtemValor:
    
    def test_1(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0))
        m, n = 6, 4
        assert all(fp.obtem_valor(tab, pos) == tab[(pos-1)//n][(pos-1)%n] for pos in range(1, m*n+1))
        
    def test_2(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0))
        m, n = 4, 4
        assert all(fp.obtem_valor(tab, pos) == tab[(pos-1)//n][(pos-1)%n] for pos in range(1, m*n+1))
        
    def test_3(self):
        tab = ((1,0,0,1,0,0),(-1,1,0,1,0,0), (-1,0,0,-1,0,0), (0,0,0,0,0,0))
        m, n = 4, 6
        assert all(fp.obtem_valor(tab, pos) == tab[(pos-1)//n][(pos-1)%n] for pos in range(1, m*n+1))
        
    
class TestObtemColuna:
    def test_1(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))
        res = tuple(tuple((i*len(tab[0]) + j) for i in range(len(tab))) for j in range(1,len(tab[0])+1))
                                            
        assert tuple(fp.obtem_coluna(tab, p) for p in range(1, len(tab[0]) + 1)) == res and \
            tuple(fp.obtem_coluna(tab, p+2*len(tab[0])) for p in range(1, len(tab[0]) + 1)) == res
    
    
    def test_2(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))
        res = tuple(tuple((i*len(tab[0]) + j) for i in range(len(tab))) for j in range(1,len(tab[0])+1))
                                            
        assert tuple(fp.obtem_coluna(tab, p) for p in range(1, len(tab[0]) + 1)) == res and \
            tuple(fp.obtem_coluna(tab, p+3*len(tab[0])) for p in range(1, len(tab[0]) + 1)) == res
    
class TestObtemLinha:
    def test_1(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                                       
        
        assert tuple(fp.obtem_linha(tab, 1 + i*len(tab[0])) for i in range(len(tab))) == \
            tuple(tuple(range(1 + i*len(tab[0]),1 + (i+1)*len(tab[0]))) for i in range(len(tab))) and \
                tuple(fp.obtem_linha(tab, 3 + i*len(tab[0])) for i in range(len(tab))) == \
                    tuple(tuple(range(1 + i*len(tab[0]),1 + (i+1)*len(tab[0]))) for i in range(len(tab))) 
    
    
    def test_2(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))
        assert tuple(fp.obtem_linha(tab, 4 + i*len(tab[0])) for i in range(len(tab))) == \
            tuple(tuple(range(1 + i*len(tab[0]),1 + (i+1)*len(tab[0]))) for i in range(len(tab))) and \
                tuple(fp.obtem_linha(tab, 9 + i*len(tab[0])) for i in range(len(tab))) == \
                    tuple(tuple(range(1 + i*len(tab[0]),1 + (i+1)*len(tab[0]))) for i in range(len(tab))) 
    
    def test_3(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                                       
        assert all((fp.obtem_linha(tab, pos)== tuple(range(1, len(tab[0]) +1)) for pos in range(1, len(tab[0])+1))) and \
            all((fp.obtem_linha(tab, pos)== tuple(range(1+2*len(tab[0]), 3*len(tab[0]) +1)) for pos in range(1 + 2*len(tab[0]), 3*len(tab[0])+1)))
    
    def test_4(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))
        assert all((fp.obtem_linha(tab, pos)== tuple(range(1, len(tab[0]) +1)) for pos in range(1, len(tab[0])+1))) and \
            all((fp.obtem_linha(tab, pos)== tuple(range(1+3*len(tab[0]), 4*len(tab[0]) +1)) for pos in range(1 + 3*len(tab[0]), 4*len(tab[0])+1)))
    
class TestObtemDiagonais:
    def test_1(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))
        assert fp.obtem_diagonais(tab, 1) == ((1, 13, 25, 37), (1,)) 
        
    def test_2(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))
        assert fp.obtem_diagonais(tab, 11) == ((11,), (41, 31, 21, 11)) 
      
    def test_3(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))
        assert fp.obtem_diagonais(tab, 28) == ((4, 16, 28, 40), (38, 28, 18, 8))
          
    def test_4(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))
        assert fp.obtem_diagonais(tab, 44) == ((8, 20, 32, 44), (44,))

    def test_5(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))
        assert fp.obtem_diagonais(tab, 23) ==  ((23, 35), (23, 13, 3))

    def test_6(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                                       
        assert fp.obtem_diagonais(tab, 17) == ((17, 22, 27, 32), (17, 14, 11, 8))

    def test_7(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                                       
        assert fp.obtem_diagonais(tab, 4) == ((4,), (13, 10, 7, 4))

    def test_8(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                                       
        assert fp.obtem_diagonais(tab, 23) == ((13, 18, 23, 28), (29, 26, 23, 20))

    def test_9(self):
        tab = ((0,)*20,)*25
        res = ((11, 32, 53, 74, 95, 116, 137, 158, 179, 200), (485, 466, 447, 428, 409, 390, 371, 352, 333, 314, 295, 276, 257, 238, 219, 200))
        assert fp.obtem_diagonais(tab, 200) == res
        
    def test_10(self):
        tab = ((0,)*30,)*17
        res = ((21, 52, 83, 114, 145, 176, 207, 238, 269, 300),(503, 474, 445, 416, 387, 358, 329, 300))
        assert fp.obtem_diagonais(tab, 300) == res
      
class TestTabuleiroParaStr:
    def test_1(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))
        res = \
"""X---+---+---X---+---+---+---+---X---+---+
|   |   |   |   |   |   |   |   |   |   |
O---X---+---X---+---+---+---+---X---+---+
|   |   |   |   |   |   |   |   |   |   |
O---+---+---O---+---+---+---+---O---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---O---+---+"""

        assert fp.tabuleiro_para_str(tab) == res

    def test_2(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                                       
        res = \
"""X---+---+---X
|   |   |   |
O---X---+---X
|   |   |   |
O---+---+---O
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
X---+---+---X
|   |   |   |
O---X---+---X
|   |   |   |
O---+---+---O"""

        assert fp.tabuleiro_para_str(tab) == res

    def test_3(self):
        tab = ((1,)*100,(0,)*100,(-1,)*100)
        res = \
"""X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X---X
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O---O"""

        assert fp.tabuleiro_para_str(tab) == res

    def test_4(self):
        tab = ((1,0),(-1,1))
        res = \
"""X---+
|   |
O---X"""
        assert fp.tabuleiro_para_str(tab) == res
        
class TestEhPosicaoValida:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            fp.eh_posicao_valida(((1,-1),(-1,-1,1)), 2)
        assert "eh_posicao_valida: argumentos invalidos" == str(excinfo.value)
    
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            fp.eh_posicao_valida(((1,-1),(-1,-1)), 2.0)
        assert "eh_posicao_valida: argumentos invalidos" == str(excinfo.value)
    
    def test_3(self):
        tab = ((1,)*100,(0,)*100,(-1,)*100)
        assert all(fp.eh_posicao_valida(tab, pos) for pos in range(1, 3*100+1, 20)) and all(not fp.eh_posicao_valida(tab, pos) for pos in range(3*100+1, 6*100, 20))


class TestEhPosicaoLivre:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            fp.eh_posicao_livre("((1,-1),(-1,-1,1))", 2)
        assert "eh_posicao_livre: argumentos invalidos" == str(excinfo.value)
    
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            fp.eh_posicao_livre(((1,-1),(-1,-1)), "2.0")
        assert "eh_posicao_livre: argumentos invalidos" == str(excinfo.value)
    
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            fp.eh_posicao_livre(((1,-1),(-1,-1)), 5)
        assert "eh_posicao_livre: argumentos invalidos" == str(excinfo.value)
    
    def test_4(self):
        tab = ((1,)*100,(0,)*100,(-1,)*100)
        assert not all(fp.eh_posicao_livre(tab, pos) for pos in range(1, 100+1)) \
            and all(fp.eh_posicao_livre(tab, pos) for pos in range(100+1, 200+1)) \
                and not all(fp.eh_posicao_livre(tab, pos) for pos in range(200+1, 300+1))

    def test_5(self):
        tab = ((1,0),(-1,1))
        assert not fp.eh_posicao_livre(tab, 1) and fp.eh_posicao_livre(tab, 2) \
            and not fp.eh_posicao_livre(tab, 3) and not fp.eh_posicao_livre(tab, 4) 
            
class TestObtemPosLivres:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_posicoes_livres(((1,-1),[-1,-1]))
        assert "obtem_posicoes_livres: argumento invalido" == str(excinfo.value)
    
    def test_2(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))
        res = (2, 3, 5, 6, 7, 8, 10, 11, 14, 16, 17, 18, 19, 21, 22, 24, 25, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44)
        assert fp.obtem_posicoes_livres(tab) == res
        
    def test_3(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                                       
        res = (2, 3, 7, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 31, 34, 35)
        assert fp.obtem_posicoes_livres(tab) == res
        
    def test_4(self):
        tab = ((1,0),(-1,1))
        res = (2,)
        assert fp.obtem_posicoes_livres(tab) == res
          
    def test_5(self):
        tab = ((1,-1),(-1,1))
        res = ()
        assert fp.obtem_posicoes_livres(tab) == res
        
class TestObtemPosJogador:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_posicoes_jogador((), 1)
        assert "obtem_posicoes_jogador: argumentos invalidos" == str(excinfo.value)
    
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_posicoes_jogador(((1,0),(0,-1)), 1.0)
        assert "obtem_posicoes_jogador: argumentos invalidos" == str(excinfo.value)
    
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_posicoes_jogador(((1,0),(0,-1)), 0)
        assert "obtem_posicoes_jogador: argumentos invalidos" == str(excinfo.value)
    
    def test_4(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))
        jX = (1, 4, 9, 13, 15, 20)
        jO = (12, 23, 26, 31, 42)
        assert fp.obtem_posicoes_jogador(tab, 1) == jX and fp.obtem_posicoes_jogador(tab, -1) == jO
        
    def test_5(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                                       
        jX = (1, 4, 6, 8, 25, 28, 30, 32)
        jO = (5, 9, 12, 29, 33, 36)
        assert fp.obtem_posicoes_jogador(tab, 1) == jX and fp.obtem_posicoes_jogador(tab, -1) == jO
        
    def test_6(self):
        tab = ((0,0),(0,0))                                       
        assert fp.obtem_posicoes_jogador(tab, 1) == () and fp.obtem_posicoes_jogador(tab, -1) == ()
        
    
class TestObtemPosAdjacentes:
    def test_1(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                                       
        assert fp.obtem_posicoes_adjacentes(tab, 1) == (2, 5, 6)
        
    def test_2(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                                       
        assert fp.obtem_posicoes_adjacentes(tab, 22) == (17, 18, 19, 21, 23)
        
    def test_3(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                                       
        assert fp.obtem_posicoes_adjacentes(tab, 10) == (5, 6, 7, 9, 11, 13, 14, 15)
        
    def test_4(self):
        tab = ((0,0),(0,0),(0,0))              
        assert fp.obtem_posicoes_adjacentes(tab, 3) == (1, 2, 4, 5, 6)
      
    def test_5(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))              
        assert fp.obtem_posicoes_adjacentes(tab, 20) == (8, 9, 10, 19, 21, 30, 31, 32)
      
    def test_6(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))              
        assert fp.obtem_posicoes_adjacentes(tab, 44) == (32, 33, 43)
      
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_posicoes_adjacentes(7, 2)
        assert "obtem_posicoes_adjacentes: argumentos invalidos" == str(excinfo.value)
    
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_posicoes_adjacentes(((1,-1),(-1,-1)), (2,))
        assert "obtem_posicoes_adjacentes: argumentos invalidos" == str(excinfo.value)
    
    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_posicoes_adjacentes(((1,-1),(-1,-1)), 15)
        assert "obtem_posicoes_adjacentes: argumentos invalidos" == str(excinfo.value)
    
    
class TestOrdenaPosTabuleiro:
    def test_1(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                                       
        m, n = 9, 4
        res = (19, 14, 15, 16, 18, 20, 22, 23, 24, 9, 10, 11, 12, 13, 17, 21, 25, 26, 27, 28, 5, 6, 7, 8, 29, 30, 31, 32, 1, 2, 3, 4, 33, 34, 35, 36)
        assert fp.ordena_posicoes_tabuleiro(tab, tuple(range(1,m*n+1))) == res

    def test_2(self):
        tab = ((1,0,0,1,0,0,0,0,1,0,0),(-1,1,0,1,0,0,0,0,1,0,0), (-1,0,0,-1,0,0,0,0,-1,0,0), (0,0,0,0,0,0,0,0,-1,0,0))
        m, n = 4, 11
        res = (28, 16, 17, 18, 27, 29, 38, 39, 40, 4, 5, 6, 7, 8, 15, 19, 26, 30, 37, 41, 3, 9, 14, 20, 25, 31, 36, 42, 2, 10, 13, 21, 24, 32, 35, 43, 1, 11, 12, 22, 23, 33, 34, 44)
        assert fp.ordena_posicoes_tabuleiro(tab, tuple(range(1,m*n+1))) == res
    
    def test_3(self):
        tab = ((0,0),(0,0))  
        m, n = 2, 2
        res = (4, 1, 2, 3)
        assert fp.ordena_posicoes_tabuleiro(tab, tuple(range(1,m*n+1))) == res

    def test_4(self):
        tab = ((0,0),(0,0))  
        res = ()
        assert fp.ordena_posicoes_tabuleiro(tab, ()) == res
        
    def test_5(self):
        tab = ((0,0),(0,0))  
        res = (1,)
        assert fp.ordena_posicoes_tabuleiro(tab, (1,)) == res
        
    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            fp.ordena_posicoes_tabuleiro(((1,-1),[-1,-1]), (1,2))
        assert "ordena_posicoes_tabuleiro: argumentos invalidos" == str(excinfo.value)
    
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            fp.ordena_posicoes_tabuleiro(((1,-1),(-1,-1)), 1)
        assert "ordena_posicoes_tabuleiro: argumentos invalidos" == str(excinfo.value)
    
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            fp.ordena_posicoes_tabuleiro(((1,-1),(-1,-1)), [1,2])
        assert "ordena_posicoes_tabuleiro: argumentos invalidos" == str(excinfo.value)
    
    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            fp.ordena_posicoes_tabuleiro(((1,-1),(-1,-1)), (1,'o'))
        assert "ordena_posicoes_tabuleiro: argumentos invalidos" == str(excinfo.value)
    
    def test_10(self):
        with pytest.raises(ValueError) as excinfo:
            fp.ordena_posicoes_tabuleiro(((1,-1),(-1,-1)), (1,5))
        assert "ordena_posicoes_tabuleiro: argumentos invalidos" == str(excinfo.value)
    

class TestMarcaPosicao:
    def test_1(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,0,0,0), (0,0,0,0), (0,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        res = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1), (0,1,0,0), (0,0,0,0), (0,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))                 
        assert fp.marca_posicao(tab, 14, 1) == res         
                     
    def test_2(self):                                   
        tab = ((0,0,0,0),(0,0,0,0), (0,0,0,0))
        m, n = 3, 4
        assert all(tuple(tuple((1 if (i*n + j + 1) == pos else 0)  for j in range(n)) for i in range(m)) == fp.marca_posicao(tab, pos, 1) for pos in range(1,n*m+1))

    def test_3(self):                                   
        tab = ((0,0),(0,0), (0,0), (0,0),(0,0), (0,0))
        m, n = 6, 2
        assert all(tuple(tuple((-1 if (i*n + j + 1) == pos else 0)  for j in range(n)) for i in range(m)) == fp.marca_posicao(tab, pos, -1) for pos in range(1,n*m+1))

     
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            fp.marca_posicao({}, 2, 1)
        assert "marca_posicao: argumentos invalidos" == str(excinfo.value)
    
    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            fp.marca_posicao(((1,0),(-1,0)), 5.5, 1)
        assert "marca_posicao: argumentos invalidos" == str(excinfo.value)
    
    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            fp.marca_posicao(((1,0),(0,-1)), 8, 1)
        assert "marca_posicao: argumentos invalidos" == str(excinfo.value)
    
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            fp.marca_posicao(((1,0),(0,-1)), 1, 1)
        assert "marca_posicao: argumentos invalidos" == str(excinfo.value)
    
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            fp.marca_posicao(((1,0),(0,-1)), 2, 'j1')
        assert "marca_posicao: argumentos invalidos" == str(excinfo.value)
    
class TestVerificaKLinhas:
    def test_1(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,1,-1), (1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        pos = 1, 6, 11, 16
        assert all(fp.verifica_k_linhas(tab, p, 1, 4) for p in pos)  

    def test_2(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,1,-1), (1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        k_seq = 1, 2, 3, 4, 5
        res = True, True, False, False, False
        assert tuple(fp.verifica_k_linhas(tab, 8, 1, k) for k in k_seq) == res   

    def test_3(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,1,-1), (1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        k_seq = 1, 2, 3, 4, 5
        res = True, True, False, False, False
        assert tuple(fp.verifica_k_linhas(tab, 5, -1, k) for k in k_seq) == res   

    def test_4(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,1,-1), (1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        k_seq = 1, 2, 3, 4, 5, 6, 7
        res = False, False, False, False, False, False, False
        assert tuple(fp.verifica_k_linhas(tab, 6, -1, k) for k in k_seq) == res  and \
            tuple(fp.verifica_k_linhas(tab, 9, 1, k) for k in k_seq) == res and \
                tuple(fp.verifica_k_linhas(tab, 7, -1, k) for k in k_seq) == res 


    def test_5(self):    
        tab = ((-1,-1,-1,0),(-1,0,0,0),(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0))
        assert fp.verifica_k_linhas(tab, 3, -1, 3) and not fp.verifica_k_linhas(tab, 4, -1, 3)
      
    def test_6(self):    
        tab = ((-1,-1,-1,0),(-1,0,0,0),(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0))
        assert all(fp.verifica_k_linhas(tab, 18, 1, k) for k in (1,2,3,4))

    def test_7(self):    
        tab = ((0,0,0,0,0,0),(0,0,0,0,0,0),(-1,-1,1,-1,-1,-1),(-1,0,0,0,0,0),(0,0,0,1,0,0),(0,0,1,0,0,0),(0,1,0,0,0,0),(1,0,0,0,0,0))
        assert (not fp.verifica_k_linhas(tab, 13, -1, 3)) and \
            fp.verifica_k_linhas(tab, 14, -1, 2) and \
                fp.verifica_k_linhas(tab, 16, -1, 2) and \
                    fp.verifica_k_linhas(tab, 16, -1, 3)
        
    def test_8(self):    
        tab = ((-1,0, 0),(0,0,1),(-1,0,1))
        assert (not fp.verifica_k_linhas(tab, 7, -1, 2)) and \
            fp.verifica_k_linhas(tab, 9, 1, 2) and  \
                not fp.verifica_k_linhas(tab, 3, 1, 2)

    def test_9(self):
        tab = ((1,1,1,1,1,1),(-1,-1,-1,-1,-1,-1),(0,0,0,0,0,0))
        assert all(fp.verifica_k_linhas(tab, p, 1, p) for p in range(1,len(tab[0])+1)) and \
            all(fp.verifica_k_linhas(tab, p+len(tab[0]), -1, p) for p in range(1,len(tab[0])+1)) and \
                all(not fp.verifica_k_linhas(tab, p+2*len(tab[0]), 1, p) for p in range(1,len(tab[0])+1))

    def test_10(self):
        with pytest.raises(ValueError) as excinfo:
            fp.verifica_k_linhas(((1,0),(-1,0,0)), 1, 1, 1)
        assert "verifica_k_linhas: argumentos invalidos" == str(excinfo.value)
    
    def test_11(self):
        with pytest.raises(ValueError) as excinfo:
            fp.verifica_k_linhas(((1,0),(0,-1)), -8, 1, 1)
        assert "verifica_k_linhas: argumentos invalidos" == str(excinfo.value)
    
    def test_12(self):
        with pytest.raises(ValueError) as excinfo:
            fp.verifica_k_linhas(((1,0),(0,-1)), 8, 1, 1)
        assert "verifica_k_linhas: argumentos invalidos" == str(excinfo.value)
    
    def test_13(self):
        with pytest.raises(ValueError) as excinfo:
            fp.verifica_k_linhas(((1,0),(0,-1)), 2, 1.0, 2)
        assert "verifica_k_linhas: argumentos invalidos" == str(excinfo.value)
    
    def test_14(self):
        with pytest.raises(ValueError) as excinfo:
            fp.verifica_k_linhas(((1,0),(0,-1)), 3, 1, 0)
        assert "verifica_k_linhas: argumentos invalidos" == str(excinfo.value)
    
class TestEhFimJogo:
    def test_1(self):
        tab = ((1,-1,1,-1),(-1,0,0,1),(1,-1,1,-1),(-1,1,-1,1))
        res = (True, True, True)
        assert tuple(fp.eh_fim_jogo(tab, k) for k in range(1, 4)) == res 


    def test_2(self):
        tab = ((1,-1,1,-1),(-1,0,0,1),(1,-1,1,-1),(-1,1,-1,1))
        res = (True, True, True, False, False)
        assert tuple(fp.eh_fim_jogo(tab, k) for k in range(1, 6)) == res 

    def test_3(self):
        tab = ((1,-1,1,-1),(-1,1,-1,1),(1,-1,1,-1),(-1,1,-1,1),(1,-1,1,-1),(-1,1,-1,1),(1,-1,1,-1),(-1,1,-1,1))
        assert all(fp.eh_fim_jogo(tab, k) for k in range(1, 5)) 


    def test_4(self):
        tab = ((1,-1,1,-1),(-1,1,-1,1),(1,-1,1,-1),(-1,1,-1,1),(1,-1,1,-1),(-1,1,-1,1),(1,-1,1,-1),(-1,1,-1,1))
        assert all(fp.eh_fim_jogo(tab, k) for k in range(1, 10)) 

    def test_5(self):
        tab = ((0,0,0,0,0,0,0),)*20
        assert all(not fp.eh_fim_jogo(tab, k) for k in range(1, 8)) 
        
    def test_6(self):
        tab = ((0,0,0,0,0,0,0),)*20
        assert all(not fp.eh_fim_jogo(tab, k) for k in range(1, 20)) 


    def test_7(self):
        tab = ((0,0),(0,0))
        res = (False, False)
        assert tuple(fp.eh_fim_jogo(tab, k) for k in range(1, 3)) == res

    def test_8(self):
        tab = ((1,0),(-1,0))
        res = (True, False)
        assert tuple(fp.eh_fim_jogo(tab, k) for k in range(1, 3)) == res

    def test_9(self):
        tab = ((1,-1),(-1,0))
        res = (True, True)
        assert tuple(fp.eh_fim_jogo(tab, k) for k in range(1, 3)) == res

    def test_10(self):
        tab = ((1,-1),(0,1))
        res = (True, True)
        assert tuple(fp.eh_fim_jogo(tab, k) for k in range(1, 3)) == res


    def test_11(self):
        with pytest.raises(ValueError) as excinfo:
            fp.eh_fim_jogo((), 1)
        assert "eh_fim_jogo: argumentos invalidos" == str(excinfo.value)
    
    def test_12(self):
        with pytest.raises(ValueError) as excinfo:
            fp.eh_fim_jogo(((1,0),(0,-1)), -2)
        assert "eh_fim_jogo: argumentos invalidos" == str(excinfo.value)

    def test_13(self):
        tab = ((0,-1,0,-1),(-1,0,0,0),(0,-1,0,-1),(-1,0,-1,0))
        res = (True, True, True)
        assert tuple(fp.eh_fim_jogo(tab, k) for k in range(1, 4)) == res 

    def test_14(self):
        tab = ((1,0,1,0),(0,0,0,1),(1,0,1,0),(0,1,0,1))
        res = (True, True, True)
        assert tuple(fp.eh_fim_jogo(tab, k) for k in range(1, 4)) == res 

class TestEscolhePosManual:
    def test_1(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        res, text = 22, 'Turno do jogador. Escolha uma posicao livre: '
        assert escolhe_posicao_manual_offline(tab, "22\n") == (res, text)
        
    def test_2(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        res, text = 7, 'Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: '
        assert escolhe_posicao_manual_offline(tab, "21\n5\n7\n") == (res, text) 

    def test_3(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        res, text = 10, 'Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: '
        assert escolhe_posicao_manual_offline(tab, "0\n16\n10\n") == (res, text) 
        
    def test_4(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        res, text = 11, 'Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: '
        assert escolhe_posicao_manual_offline(tab, "2.0\n7.6\n11\n") == (res, text) 

    def test_5(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        res, text = 14, 'Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: '
        assert escolhe_posicao_manual_offline(tab, "\n\n14\n") == (res, text) 

    def test_6(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,-1),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        res, text = 19, 'Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: '
        assert escolhe_posicao_manual_offline(tab, "ola\nadeus\n19\n") == (res, text) 
        
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            escolhe_posicao_manual_offline(((1,1),[1,0]), '4\n')
        assert "escolhe_posicao_manual: argumento invalido" == str(excinfo.value)
    
class TestEscolhePosAutoFacil:
    
    def test_1(self):
        lvl = 'facil'
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        assert fp.escolhe_posicao_auto(tab, -1, 3, lvl) == 10 
        
    def test_2(self):
        lvl = 'facil'
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, lvl) == 15 
        
    
    def test_3(self):
        lvl = 'facil'
        tab = ((0,0,0,1),(0,0,0,0), (0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, lvl) == 7 and  fp.escolhe_posicao_auto(tab, -1, 3, lvl) == 15
        
    def test_4(self):
        lvl = 'facil'
        tab = ((0,0,0,0),(0,0,0,0), (0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, lvl) == 15 and  fp.escolhe_posicao_auto(tab, -1, 3, lvl) == 15
           
    def test_5(self):
        lvl = 'facil'
        tab = ((0,0,-1,1),(0,0,-1,-1), (0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, lvl) == 15 and  fp.escolhe_posicao_auto(tab, -1, 10, lvl) == 10
        
    def test_6(self):
        lvl = 'facil'
        tab = ((0,0,-1,1),(0,0,-1,-1), (0,0,0,0),(0,0,0,0),(0,0,0,0),(1,0,0,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, lvl) == 18
        
    def test_7(self):
        lvl = 'facil'
        tab = ((1,-1,-1),(-1,1,1), (-1,1,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, lvl) == 9 and fp.escolhe_posicao_auto(tab, -1, 3, lvl) == 9
        
    def test_8(self):
        lvl = 'facil'
        assert fp.escolhe_posicao_auto(((0,0),)*25, 1, 3, lvl) == 26 and \
           fp.escolhe_posicao_auto(((0,0,0,0,0),)*12, -1, 3, lvl) == 33 

    def test_9(self):
        lvl = 'facil'
        tab = (1,0,0,0,0),(0,-1,1,1,0),(0,0,-1,0,0),(0,0,0,0,0),(0,0,0,0,0)
        assert fp.escolhe_posicao_auto(tab, -1, 4, lvl) == 12
         
                       
    def test_10(self):
        lvl = 'facil'
        tab = ((1,-1,0,0,0),(1,0,0,0,0),(0,0,0,0,0), (0,0,0,0,0), (0,0,0,0,0))
        assert fp.escolhe_posicao_auto(tab, -1, 4, lvl) == 7
              
    def test_11(self):
        tab = ((-1,-1,-1,1),(-1,1,1,1),(1,0,1,0),(-1,-1,0,0))
        assert fp.escolhe_posicao_auto(tab, 1, 4, 'facil') == 10 and \
            fp.escolhe_posicao_auto(tab, -1, 4, 'facil') == 10
                 
        
class TestEscolhePosAutoNormal:
    def test_1(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'normal') == 11 
        
    def test_2(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        assert fp.escolhe_posicao_auto(tab, -1, 3, 'normal') == 11
    
    def test_3(self):
        tab = ((1,1,0,0),(-1,-1,0,0), (-0,0,0,0),(1,0,0,0),(-1,0, 1,0), (0,0,-1,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 4, 'normal') == 3 and fp.escolhe_posicao_auto(tab, -1, 4, 'normal') == 7
        
    def test_4(self):
        tab = ((0,0,0,1),(0,0,0,0), (0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 5, 'normal') == 7 and  fp.escolhe_posicao_auto(tab, -1, 5, 'normal') == 7
        
    def test_5(self):
        tab = ((0,0,0,0,0,0,0,0,0),)*7  
        assert fp.escolhe_posicao_auto(((0,0,0,0,0,0,0,0,0),)*7  , 1, 4, 'normal') == 32 and  fp.escolhe_posicao_auto(((0,0,0,0,0),)*9  , -1, 4, 'normal') == 23
        
    def test_6(self):
        tab = ((0,0,-1,1),(0,0,-1,-1), (0,0,0,0),(0,0,0,0),(0,-1,0,0),(0,-1,0,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'normal') == 11 and  fp.escolhe_posicao_auto(tab, -1, 3, 'normal') == 11
   
    def test_7(self):
        tab = ((0,0,-1,1),(0,0,-1,-1), (0,0,0,0),(0,0,0,0),(0,0,-1,0),(0,0,-1,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'normal') == 15 and  fp.escolhe_posicao_auto(tab, -1, 3, 'normal') == 15

    def test_8(self):
        tab = ((1,-1,-1),(-1,0,1), (-1,1,-1))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'normal') == 5 and fp.escolhe_posicao_auto(tab, -1, 3, 'normal') == 5
        
    def test_9(self):
        tab = ((1,0,0),(0,-1,0),(0,0,0))
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'normal') == 2 
        
    def test_10(self):
        tab = ((0,0,0),(0,0,0),(0,0,0))
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'normal') == 5
        
    def test_11(self):
        tab = (1,0,0,0,0),(0,-1,1,1,0),(0,0,-1,0,0),(0,0,0,0,0),(0,0,0,0,0)
        assert fp.escolhe_posicao_auto(tab, -1, 4, 'normal') == 19
        
    def test_12(self):
        lvl = 'normal'
        tab = ((0,0,-1,1),(0,0,-1,-1), (0,0,0,0),(0,0,0,0),(0,0,0,0),(1,0,0,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, lvl) == 11
       
    def test_13(self):
        lvl = 'normal'
        tab = (1,0,0,0,0),(0,-1,1,1,0),(0,0,-1,0,0),(0,0,0,0,0),(0,0,0,0,0)
        assert fp.escolhe_posicao_auto(tab, -1, 4, lvl) == 19
        
    def test_14(self):
        lvl = 'normal'
        tab = ((0,0,0,1),(0,0,0,0), (0,0,0,0),(0,0,0,0))  
        assert fp.escolhe_posicao_auto(tab, -1, 3, lvl) == 7 and fp.escolhe_posicao_auto(tab, 1, 3, lvl) == 7 
                    
    def test_15(self):
        lvl = 'normal'
        tab = ((1,-1,0,0,0),(1,0,0,0,0),(0,0,0,0,0), (0,0,0,0,0), (0,0,0,0,0))
        assert fp.escolhe_posicao_auto(tab, -1, 4, lvl) == 11
        
    def test_16(self):
        tab = ((-1,-1,-1,1),(-1,1,1,0),(0,0,1,0),(0,0,0,0))
        assert fp.escolhe_posicao_auto(tab, 1, 4, 'normal') == 8 and \
            fp.escolhe_posicao_auto(tab, -1, 4, 'normal') == 9 
            
    def test_17(self):
        tab = ((-1,-1,-1,1),(-1,1,1,1),(1,0,1,0),(-1,-1,0,0))
        assert fp.escolhe_posicao_auto(tab, 1, 4, 'normal') == 10 and \
            fp.escolhe_posicao_auto(tab, -1, 4, 'normal') == 15
     
    def test_18(self):
        lvl = 'normal'
        tab = ((0,0,0,1),(0,0,0,0), (0,0,0,0),(0,0,0,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, lvl) == 7
                    
class TestEscolhePosAutoDificil:
    def test_1(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        assert fp.escolhe_posicao_auto(tab, -1, 3, 'dificil') == 11 

    def test_2(self):
        tab = ((1,0,0,1),(-1,1,0,1), (-1,0,0,0),(1,0,0,1),(-1,1,0,1), (-1,0,0,-1))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'dificil') == 11 
        
    def test_3(self):
        tab = ((1,0,0),(0,-1,0),(0,0,0))
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'dificil') == 6 
        
    def test_4(self):
        tab = ((1,0,0),(0,-1,0),(0,0,0))
        assert fp.escolhe_posicao_auto(tab, -1, 3, 'dificil') == 9 
        
    def test_5(self):
        tab = ((0,0,0),(0,0,0),(0,0,0))
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'dificil') == 1 
 
    def test_6(self):
        tab = ((1,-1,-1),(-1,0,1), (-1,1,-1))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'dificil') == 5 and fp.escolhe_posicao_auto(tab, -1, 3, 'dificil') == 5
        
    def test_7(self):  
        lvl = 'dificil'
        tab = ((0,0,0,1),(0,0,0,0), (0,0,0,0),(0,0,0,0))  
        assert fp.escolhe_posicao_auto(tab, -1, 3, lvl) == 11 and fp.escolhe_posicao_auto(tab, -1, 3, lvl) == 11 
                    
    def test_8(self):
        lvl = 'dificil'
        tab = ((1,-1,0,0,0),(1,0,0,0,0),(0,0,0,0,0), (0,0,0,0,0), (0,0,0,0,0))
        assert fp.escolhe_posicao_auto(tab, -1, 4, lvl) == 13
        
    def test_9(self):
        lvl = 'dificil'
        tab = ((0,0,0,1),(0,0,0,0), (0,0,0,0),(0,0,0,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, lvl) == 11
        
    def test_10(self):
        tab = ((0,0,0,0),(0,0,0,0), (0,0,0,0))  
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'dificil') == 2 and \
            fp.escolhe_posicao_auto(tab, -1, 3, 'dificil') == 2
         
        
    def test_11(self):
        tab = ((-1,-1,-1,1),(-1,1,1,0),(0,0,1,0),(0,0,0,0))
        assert fp.escolhe_posicao_auto(tab, 1, 4, 'dificil') == 9
    
    def test_12(self):
        tab = ((-1,-1,-1,1),(-1,1,1,0),(0,0,1,0),(0,0,0,0))
        assert fp.escolhe_posicao_auto(tab, -1, 4, 'dificil') == 8    
       
    def test_13(self):
        tab = ((-1,-1,-1,1),(-1,1,1,1),(1,0,1,0),(-1,-1,0,0))
        assert fp.escolhe_posicao_auto(tab, 1, 4, 'dificil') == 12 and \
            fp.escolhe_posicao_auto(tab, -1, 4, 'dificil') == 10 
                 
   
              
   

class TestEscolhePosAutoExcept:
    
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            fp.escolhe_posicao_auto(((1,1),(1.5,0)), -1, 4, 'dificil')
        assert "escolhe_posicao_auto: argumentos invalidos" == str(excinfo.value)
    
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            fp.escolhe_posicao_auto(((1,-1,1),(-1,1,-1),(-1,1,-1)), -1, 3, 'facil')
        assert "escolhe_posicao_auto: argumentos invalidos" == str(excinfo.value)
        
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            fp.escolhe_posicao_auto(((1,1,1),(0,0,0),(-1,1,-1)), -1, 3, 'facil')
        assert "escolhe_posicao_auto: argumentos invalidos" == str(excinfo.value)
    
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            fp.escolhe_posicao_auto(((1,-1,1),(0,0,0),(-1,1,-1)), 'jog', 3, 'facil')
        assert "escolhe_posicao_auto: argumentos invalidos" == str(excinfo.value)
    
    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            fp.escolhe_posicao_auto(((1,-1,1),(0,0,0),(-1,1,-1)), 1, 'k', 'facil')
        assert "escolhe_posicao_auto: argumentos invalidos" == str(excinfo.value)
    
    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            fp.escolhe_posicao_auto(((1,-1,1),(0,0,0),(-1,1,-1)), 1, 3, 2)
        assert "escolhe_posicao_auto: argumentos invalidos" == str(excinfo.value)
    
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            fp.escolhe_posicao_auto(((1,-1,1),(0,0,0),(-1,1,-1)), 1, 3, '')
        assert "escolhe_posicao_auto: argumentos invalidos" == str(excinfo.value)
    
class TestJogoMNK:

    def test_1(self):
        res = 1
        assert jogo_mnk_offline((4,4,4), 1, 'facil', JOGADA_PRIVATE_2) == (res, OUTPUT_PRIVATE_2)
         
    def test_2(self):
        res = -1
        assert jogo_mnk_offline((3,6,3), -1, 'facil', JOGADA_PRIVATE_3) == (res, OUTPUT_PRIVATE_3)
           
    def test_3(self):
        res = -1
        assert jogo_mnk_offline((7,3,3), -1, 'facil', JOGADA_PRIVATE_4) == (res, OUTPUT_PRIVATE_4)
    
    def test_4(self):
        res = -1
        assert jogo_mnk_offline((3,3,3), -1, 'facil', JOGADA_PRIVATE_7) == (res, OUTPUT_PRIVATE_7)
         
         
    def test_5(self):
        res = 0
        assert jogo_mnk_offline((4,4,4), 1, 'normal', JOGADA_PRIVATE_5) == (res, OUTPUT_PRIVATE_5)
           
    def test_6(self):
        res = 1
        assert jogo_mnk_offline((3,3,3), -1, 'normal', JOGADA_PRIVATE_1) == (res, OUTPUT_PRIVATE_1)
         
    def test_7(self):
        res = -1
        assert jogo_mnk_offline((5,5,4), 1, 'dificil', JOGADA_PRIVATE_6) == (res, OUTPUT_PRIVATE_6)
         
class TestJogoMNKExcept:
    
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            fp.jogo_mnk(5, -1, 'facil')
        assert "jogo_mnk: argumentos invalidos" == str(excinfo.value)
    
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            fp.jogo_mnk([3,3,3], -1, 'facil')
        assert "jogo_mnk: argumentos invalidos" == str(excinfo.value)
    
    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            fp.jogo_mnk((), -1, 'facil')
        assert "jogo_mnk: argumentos invalidos" == str(excinfo.value)
    
    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            fp.jogo_mnk((3,3,3,3), -1, 'facil')
        assert "jogo_mnk: argumentos invalidos" == str(excinfo.value)
    
    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            fp.jogo_mnk((3.0,3.0,3.0), -1, 'facil')
        assert "jogo_mnk: argumentos invalidos" == str(excinfo.value)
    
    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            fp.jogo_mnk((3,3,3), '0', 'facil')
        assert "jogo_mnk: argumentos invalidos" == str(excinfo.value)
        
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            fp.jogo_mnk((3,3,3), 1, 'l')
        assert "jogo_mnk: argumentos invalidos" == str(excinfo.value)
    
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            fp.jogo_mnk((101,3,3), 1, 'facil')
        assert "jogo_mnk: argumentos invalidos" == str(excinfo.value)
    
    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            fp.jogo_mnk((100,1,3), 1, 'facil')
        assert "jogo_mnk: argumentos invalidos" == str(excinfo.value)
    
    def test_10(self):
        with pytest.raises(ValueError) as excinfo:
            fp.jogo_mnk((4,4,-3), 1, 'facil')
        assert "jogo_mnk: argumentos invalidos" == str(excinfo.value)
    
### AUXILIAR CODE NECESSARY TO REPLACE STANDARD INPUT 
class ReplaceStdIn:
    def __init__(self, input_handle):
        self.input = input_handle.split('\n')
        self.line = 0

    def readline(self):
        if len(self.input) == self.line:
            return ''
        result = self.input[self.line]
        self.line += 1
        return result if result else ' '

class ReplaceStdOut:
    def __init__(self):
        self.output = ''

    def write(self, s):
        self.output += s
        return len(s)

    def flush(self):
        return 


def escolhe_posicao_manual_offline(tab, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = fp.escolhe_posicao_manual(tab)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout


def jogo_mnk_offline(config, human_symbol, strategy, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = fp.jogo_mnk(config, human_symbol, strategy)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout

JOGADA_PRIVATE_1 = "8\n9\n4\n"
OUTPUT_PRIVATE_1 = \
"""Bem-vindo ao JOGO MNK.
O jogador joga com 'O'.
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
Turno do computador (normal):
+---+---+
|   |   |
+---X---+
|   |   |
+---+---+
Turno do jogador. Escolha uma posicao livre: +---+---+
|   |   |
+---X---+
|   |   |
+---O---+
Turno do computador (normal):
X---+---+
|   |   |
+---X---+
|   |   |
+---O---+
Turno do jogador. Escolha uma posicao livre: X---+---+
|   |   |
+---X---+
|   |   |
+---O---O
Turno do computador (normal):
X---+---+
|   |   |
+---X---+
|   |   |
X---O---O
Turno do jogador. Escolha uma posicao livre: X---+---+
|   |   |
O---X---+
|   |   |
X---O---O
Turno do computador (normal):
X---+---X
|   |   |
O---X---+
|   |   |
X---O---O
DERROTA
"""

JOGADA_PRIVATE_2 = "14\n13\n16\n15\n"
OUTPUT_PRIVATE_2 = \
"""Bem-vindo ao JOGO MNK.
O jogador joga com 'X'.
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Turno do jogador. Escolha uma posicao livre: +---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---X---+---+
Turno do computador (facil):
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---O---+
|   |   |   |
+---X---+---+
Turno do jogador. Escolha uma posicao livre: +---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---O---+
|   |   |   |
X---X---+---+
Turno do computador (facil):
+---+---+---+
|   |   |   |
+---O---+---+
|   |   |   |
+---+---O---+
|   |   |   |
X---X---+---+
Turno do jogador. Escolha uma posicao livre: +---+---+---+
|   |   |   |
+---O---+---+
|   |   |   |
+---+---O---+
|   |   |   |
X---X---+---X
Turno do computador (facil):
+---+---+---+
|   |   |   |
+---O---O---+
|   |   |   |
+---+---O---+
|   |   |   |
X---X---+---X
Turno do jogador. Escolha uma posicao livre: +---+---+---+
|   |   |   |
+---O---O---+
|   |   |   |
+---+---O---+
|   |   |   |
X---X---X---X
VITORIA
"""


JOGADA_PRIVATE_3 = "1\n8\n5\n15\n"
OUTPUT_PRIVATE_3 = \
"""Bem-vindo ao JOGO MNK.
O jogador joga com 'O'.
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---+---+---+
Turno do computador (facil):
+---+---+---+---+---+
|   |   |   |   |   |
+---+---+---X---+---+
|   |   |   |   |   |
+---+---+---+---+---+
Turno do jogador. Escolha uma posicao livre: O---+---+---+---+---+
|   |   |   |   |   |
+---+---+---X---+---+
|   |   |   |   |   |
+---+---+---+---+---+
Turno do computador (facil):
O---+---X---+---+---+
|   |   |   |   |   |
+---+---+---X---+---+
|   |   |   |   |   |
+---+---+---+---+---+
Turno do jogador. Escolha uma posicao livre: O---+---X---+---+---+
|   |   |   |   |   |
+---O---+---X---+---+
|   |   |   |   |   |
+---+---+---+---+---+
Turno do computador (facil):
O---+---X---X---+---+
|   |   |   |   |   |
+---O---+---X---+---+
|   |   |   |   |   |
+---+---+---+---+---+
Turno do jogador. Escolha uma posicao livre: O---+---X---X---O---+
|   |   |   |   |   |
+---O---+---X---+---+
|   |   |   |   |   |
+---+---+---+---+---+
Turno do computador (facil):
O---+---X---X---O---+
|   |   |   |   |   |
+---O---X---X---+---+
|   |   |   |   |   |
+---+---+---+---+---+
Turno do jogador. Escolha uma posicao livre: O---+---X---X---O---+
|   |   |   |   |   |
+---O---X---X---+---+
|   |   |   |   |   |
+---+---O---+---+---+
VITORIA
"""

JOGADA_PRIVATE_4 = "8\n15\n15\n100\n13\n13\n14\n"
OUTPUT_PRIVATE_4 = \
"""Bem-vindo ao JOGO MNK.
O jogador joga com 'O'.
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
Turno do computador (facil):
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
|   |   |
+---X---+
|   |   |
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
Turno do jogador. Escolha uma posicao livre: +---+---+
|   |   |
+---+---+
|   |   |
+---O---+
|   |   |
+---X---+
|   |   |
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
Turno do computador (facil):
+---+---+
|   |   |
+---+---+
|   |   |
X---O---+
|   |   |
+---X---+
|   |   |
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
Turno do jogador. Escolha uma posicao livre: +---+---+
|   |   |
+---+---+
|   |   |
X---O---+
|   |   |
+---X---+
|   |   |
+---+---O
|   |   |
+---+---+
|   |   |
+---+---+
Turno do computador (facil):
+---+---+
|   |   |
+---+---+
|   |   |
X---O---X
|   |   |
+---X---+
|   |   |
+---+---O
|   |   |
+---+---+
|   |   |
+---+---+
Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: +---+---+
|   |   |
+---+---+
|   |   |
X---O---X
|   |   |
+---X---+
|   |   |
O---+---O
|   |   |
+---+---+
|   |   |
+---+---+
Turno do computador (facil):
+---+---+
|   |   |
+---+---+
|   |   |
X---O---X
|   |   |
X---X---+
|   |   |
O---+---O
|   |   |
+---+---+
|   |   |
+---+---+
Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: +---+---+
|   |   |
+---+---+
|   |   |
X---O---X
|   |   |
X---X---+
|   |   |
O---O---O
|   |   |
+---+---+
|   |   |
+---+---+
VITORIA
"""

JOGADA_PRIVATE_5 = "2\n3\n11\n5\n9\n13\n12\n16\n"
OUTPUT_PRIVATE_5 = \
"""Bem-vindo ao JOGO MNK.
O jogador joga com 'X'.
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Turno do jogador. Escolha uma posicao livre: +---X---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Turno do computador (normal):
+---X---+---+
|   |   |   |
+---O---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Turno do jogador. Escolha uma posicao livre: +---X---X---+
|   |   |   |
+---O---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Turno do computador (normal):
O---X---X---+
|   |   |   |
+---O---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
Turno do jogador. Escolha uma posicao livre: O---X---X---+
|   |   |   |
+---O---+---+
|   |   |   |
+---+---X---+
|   |   |   |
+---+---+---+
Turno do computador (normal):
O---X---X---+
|   |   |   |
+---O---O---+
|   |   |   |
+---+---X---+
|   |   |   |
+---+---+---+
Turno do jogador. Escolha uma posicao livre: O---X---X---+
|   |   |   |
X---O---O---+
|   |   |   |
+---+---X---+
|   |   |   |
+---+---+---+
Turno do computador (normal):
O---X---X---+
|   |   |   |
X---O---O---O
|   |   |   |
+---+---X---+
|   |   |   |
+---+---+---+
Turno do jogador. Escolha uma posicao livre: O---X---X---+
|   |   |   |
X---O---O---O
|   |   |   |
X---+---X---+
|   |   |   |
+---+---+---+
Turno do computador (normal):
O---X---X---+
|   |   |   |
X---O---O---O
|   |   |   |
X---O---X---+
|   |   |   |
+---+---+---+
Turno do jogador. Escolha uma posicao livre: O---X---X---+
|   |   |   |
X---O---O---O
|   |   |   |
X---O---X---+
|   |   |   |
X---+---+---+
Turno do computador (normal):
O---X---X---+
|   |   |   |
X---O---O---O
|   |   |   |
X---O---X---+
|   |   |   |
X---O---+---+
Turno do jogador. Escolha uma posicao livre: O---X---X---+
|   |   |   |
X---O---O---O
|   |   |   |
X---O---X---X
|   |   |   |
X---O---+---+
Turno do computador (normal):
O---X---X---O
|   |   |   |
X---O---O---O
|   |   |   |
X---O---X---X
|   |   |   |
X---O---+---+
Turno do jogador. Escolha uma posicao livre: O---X---X---O
|   |   |   |
X---O---O---O
|   |   |   |
X---O---X---X
|   |   |   |
X---O---+---X
Turno do computador (normal):
O---X---X---O
|   |   |   |
X---O---O---O
|   |   |   |
X---O---X---X
|   |   |   |
X---O---O---X
EMPATE
"""

JOGADA_PRIVATE_6 = "13\n12\n4\n19\n10\n"
OUTPUT_PRIVATE_6 = \
"""Bem-vindo ao JOGO MNK.
O jogador joga com 'X'.
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
Turno do jogador. Escolha uma posicao livre: +---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---X---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
Turno do computador (dificil):
+---+---+---+---+
|   |   |   |   |
+---+---+---O---+
|   |   |   |   |
+---+---X---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
Turno do jogador. Escolha uma posicao livre: +---+---+---+---+
|   |   |   |   |
+---+---+---O---+
|   |   |   |   |
+---X---X---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
Turno do computador (dificil):
+---+---+---+---+
|   |   |   |   |
+---+---+---O---+
|   |   |   |   |
+---X---X---O---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
Turno do jogador. Escolha uma posicao livre: +---+---+---X---+
|   |   |   |   |
+---+---+---O---+
|   |   |   |   |
+---X---X---O---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
Turno do computador (dificil):
+---+---+---X---+
|   |   |   |   |
+---+---O---O---+
|   |   |   |   |
+---X---X---O---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
Turno do jogador. Escolha uma posicao livre: +---+---+---X---+
|   |   |   |   |
+---+---O---O---+
|   |   |   |   |
+---X---X---O---+
|   |   |   |   |
+---+---+---X---+
|   |   |   |   |
+---+---+---+---+
Turno do computador (dificil):
+---+---+---X---+
|   |   |   |   |
+---O---O---O---+
|   |   |   |   |
+---X---X---O---+
|   |   |   |   |
+---+---+---X---+
|   |   |   |   |
+---+---+---+---+
Turno do jogador. Escolha uma posicao livre: +---+---+---X---+
|   |   |   |   |
+---O---O---O---X
|   |   |   |   |
+---X---X---O---+
|   |   |   |   |
+---+---+---X---+
|   |   |   |   |
+---+---+---+---+
Turno do computador (dificil):
+---+---+---X---+
|   |   |   |   |
O---O---O---O---X
|   |   |   |   |
+---X---X---O---+
|   |   |   |   |
+---+---+---X---+
|   |   |   |   |
+---+---+---+---+
DERROTA
"""

JOGADA_PRIVATE_7 = "1\n8\n7\n9\n"
OUTPUT_PRIVATE_7 = \
"""Bem-vindo ao JOGO MNK.
O jogador joga com 'O'.
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
Turno do computador (facil):
+---+---+
|   |   |
+---X---+
|   |   |
+---+---+
Turno do jogador. Escolha uma posicao livre: O---+---+
|   |   |
+---X---+
|   |   |
+---+---+
Turno do computador (facil):
O---X---+
|   |   |
+---X---+
|   |   |
+---+---+
Turno do jogador. Escolha uma posicao livre: O---X---+
|   |   |
+---X---+
|   |   |
+---O---+
Turno do computador (facil):
O---X---X
|   |   |
+---X---+
|   |   |
+---O---+
Turno do jogador. Escolha uma posicao livre: O---X---X
|   |   |
+---X---+
|   |   |
O---O---+
Turno do computador (facil):
O---X---X
|   |   |
X---X---+
|   |   |
O---O---+
Turno do jogador. Escolha uma posicao livre: O---X---X
|   |   |
X---X---+
|   |   |
O---O---O
VITORIA
"""