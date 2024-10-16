import pytest
import sys
import FP2425P1 as fp  # <--- Change the name projectoFP to the file name with your project
from FP2425P1 import simular_jogo, descobre_L_possiveis_normal


class TestPublicTabuleiroPosicoes:
    def test_1(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.eh_tabuleiro(tab)

    def test_2(self):
        tab = ((1, 0, 0, 1), (-1, 1, 'O', 1), (-1, 0, 0, -1))
        assert not fp.eh_tabuleiro(tab)

    def test_3(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0))
        assert not fp.eh_tabuleiro(tab)

    def test_4(self):
        assert fp.eh_posicao(9)

    def test_5(self):
        assert not fp.eh_posicao(-2)

    def test_6(self):
        assert not fp.eh_posicao((1,))

    def test_7(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_dimensao(tab) == (3, 4)

    def test_8(self):
        tab = ((1, 0, 0), (-1, 1, 0), (-1, 0, 1), (1, -1, 0), (0, -1, 0))
        assert fp.obtem_dimensao(tab) == (5, 3)

    def test_9(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert (fp.obtem_valor(tab, 1), fp.obtem_valor(tab, 2), fp.obtem_valor(tab, 5)) == (1, 0, -1)

    def test_10(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_coluna(tab, 2) == (2, 6, 10)

    def test_11(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_coluna(tab, 7) == (3, 7, 11)

    def test_12(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_linha(tab, 3) == (1, 2, 3, 4)

    def test_13(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_linha(tab, 7) == (5, 6, 7, 8)

    def test_14(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_diagonais(tab, 6) == ((1, 6, 11), (9, 6, 3))

    def test_15(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_diagonais(tab, 5) == ((5, 10), (5, 2))

    def test_16(self):
        tab = ((1, 0, 0), (-1, 1, 0), (-1, 0, 0))
        assert fp.tabuleiro_para_str(tab) == 'X---+---+\n|   |   |\nO---X---+\n|   |   |\nO---+---+'

    def test_17(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.tabuleiro_para_str(tab) == 'X---+---+---X\n|   |   |   |\nO---X---+---X\n|   |   |   |\nO---+---+---O'



class TestPublicInspectManip:
    def test_1(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.eh_posicao_valida(tab, 9)

    def test_2(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.eh_posicao_valida(tab, 12)

    def test_3(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert not fp.eh_posicao_valida(tab, 13)

    def test_4(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.eh_posicao_livre(tab, 2)

    def test_5(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert not fp.eh_posicao_livre(tab, 4)

    def test_6(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert not fp.eh_posicao_livre(tab, 12)

    def test_7(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_posicoes_livres(tab) == (2, 3, 7, 10, 11)

    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            tab = ((1, -1, 0), (1, -1, 0), (1, -1))
            fp.obtem_posicoes_livres(tab)
        assert "obtem_posicoes_livres: argumento invalido" == str(excinfo.value)

    def test_9(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_posicoes_jogador(tab, 1) == (1, 4, 6, 8)

    def test_10(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_posicoes_jogador(tab, -1) == (5, 9, 12)

    def test_11(self):
        with pytest.raises(ValueError) as excinfo:
            tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
            fp.obtem_posicoes_jogador(tab, -2)
        assert "obtem_posicoes_jogador: argumentos invalidos" == str(excinfo.value)

    def test_12(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_posicoes_adjacentes(tab, 1) == (2, 5, 6)

    def test_13(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_posicoes_adjacentes(tab, 6) == (1, 2, 3, 5, 7, 9, 10, 11)

    def test_14(self):
        with pytest.raises(ValueError) as excinfo:
            tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
            fp.obtem_posicoes_adjacentes(tab, 13)
        assert "obtem_posicoes_adjacentes: argumentos invalidos" == str(excinfo.value)

    def test_15(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.ordena_posicoes_tabuleiro(tab, tuple(range(1, 13))) == (7, 2, 3, 4, 6, 8, 10, 11, 12, 1, 5, 9)

    def test_16(self):
        with pytest.raises(ValueError) as excinfo:
            tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
            fp.ordena_posicoes_tabuleiro(tab, '123')
        assert "ordena_posicoes_tabuleiro: argumentos invalidos" == str(excinfo.value)

    def test_17(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.marca_posicao(tab, 11, -1) == ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, -1, -1))

    def test_18(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.marca_posicao(tab, 7, -1) == ((1, 0, 0, 1), (-1, 1, -1, 1), (-1, 0, 0, -1))

    def test_19(self):
        with pytest.raises(ValueError) as excinfo:
            tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
            fp.marca_posicao(tab, 1, -1)
        assert "marca_posicao: argumentos invalidos" == str(excinfo.value)

    def test_20(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert (fp.verifica_k_linhas(tab, 4, 1, 2), fp.verifica_k_linhas(tab, 12, 1, 2)) == (True, False)

    def test_21(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert (fp.verifica_k_linhas(tab, 1, 1, 3), fp.verifica_k_linhas(tab, 9, -1, 3)) == (False, False)

    def test_22(self):
        tab = ((1, 0, 0, 0), (-1, 1, 0, 1), (-1, 0, 1, -1), (0, 0, 0, 0))
        assert (fp.verifica_k_linhas(tab, 6, 1, 3), fp.verifica_k_linhas(tab, 16, 1, 3)) == (True, False)

    def test_23(self):
        with pytest.raises(ValueError) as excinfo:
            tab = ((1, 0, 0, 0), (-1, 1, 0, 1), (-1, 0, 1, -1))
            fp.verifica_k_linhas(tab, 2, 1, -3)
        assert "verifica_k_linhas: argumentos invalidos" == str(excinfo.value)


class TestPublicJogo:
    def test_1(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert not fp.eh_fim_jogo(tab, 3)

    def test_2(self):
        tab = ((1, 0, 0, 0), (-1, 1, 0, 1), (-1, 0, 1, -1))
        assert fp.eh_fim_jogo(tab, 3)

    def test_3(self):
        tab = ((1, 1, -1),
               (-1, -1, 1),
               (1, -1, 1))
        assert fp.eh_fim_jogo(tab, 3)

    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            fp.eh_fim_jogo(((1, -1), (-1, -1, 1)), 2)
        assert "eh_fim_jogo: argumentos invalidos" == str(excinfo.value)

    def test_5(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        res, text = 2, 'Turno do jogador. Escolha uma posicao livre: '
        assert escolhe_posicao_manual_offline(tab, "2\n") == (res, text)

    def test_6(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        res, text = 3, 'Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma posicao livre: '
        assert escolhe_posicao_manual_offline(tab, "1\n13\n3\n") == (res, text)

    def test_7(self):
        tab = ((0, 0, 0),
               (0, 1, 0),
               (-1, 0, 1))
        assert fp.escolhe_posicao_auto(tab, -1, 3, 'facil') == 4

    def test_8(self):
        tab = ((0, 0, 0),
               (0, 1, 0),
               (-1, 0, 1))
        assert fp.escolhe_posicao_auto(tab, -1, 3, 'normal') == 1

    def test_9(self):
        tab = ((0, 0, -1),
               (-1, 1, 0),
               (1, 0, 0))
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'normal') == 1

    def test_10(self):
        tab = ((0, 0, -1),
               (-1, 1, 0),
               (1, 0, 0))
        assert fp.escolhe_posicao_auto(tab, 1, 3, 'dificil') == 8

    def test_11(self):
        res = 1
        assert jogo_mnk_offline((3, 3, 3), 1, 'facil', JOGADA_PUBLIC_1) == (res, OUTPUT_PUBLIC_1)

    def test_12(self):
        res = 1
        assert jogo_mnk_offline((3, 3, 3), -1, 'dificil', JOGADA_PUBLIC_2) == (res, OUTPUT_PUBLIC_2)

    def test_13(self):
        with pytest.raises(ValueError) as excinfo:
            escolhe_posicao_manual_offline((1, 1), '1\n')
        assert "escolhe_posicao_manual: argumento invalido" == str(excinfo.value)


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
        return result


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

    oldstdout, newstdout = sys.stdout, ReplaceStdOut()
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

    oldstdout, newstdout = sys.stdout, ReplaceStdOut()
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


# JOGOS AUTOMATICOS
JOGADA_PUBLIC_1 = '5\n4\n6\n'
OUTPUT_PUBLIC_1 = """Bem-vindo ao JOGO MNK.
O jogador joga com 'X'.
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
Turno do jogador. Escolha uma posicao livre: +---+---+
|   |   |
+---X---+
|   |   |
+---+---+
Turno do computador (facil):
O---+---+
|   |   |
+---X---+
|   |   |
+---+---+
Turno do jogador. Escolha uma posicao livre: O---+---+
|   |   |
X---X---+
|   |   |
+---+---+
Turno do computador (facil):
O---O---+
|   |   |
X---X---+
|   |   |
+---+---+
Turno do jogador. Escolha uma posicao livre: O---O---+
|   |   |
X---X---X
|   |   |
+---+---+
VITORIA
"""

JOGADA_PUBLIC_2 = "2\n7\n6\n"
OUTPUT_PUBLIC_2 = """Bem-vindo ao JOGO MNK.
O jogador joga com 'O'.
+---+---+
|   |   |
+---+---+
|   |   |
+---+---+
Turno do computador (dificil):
X---+---+
|   |   |
+---+---+
|   |   |
+---+---+
Turno do jogador. Escolha uma posicao livre: X---O---+
|   |   |
+---+---+
|   |   |
+---+---+
Turno do computador (dificil):
X---O---+
|   |   |
X---+---+
|   |   |
+---+---+
Turno do jogador. Escolha uma posicao livre: X---O---+
|   |   |
X---+---+
|   |   |
O---+---+
Turno do computador (dificil):
X---O---+
|   |   |
X---X---+
|   |   |
O---+---+
Turno do jogador. Escolha uma posicao livre: X---O---+
|   |   |
X---X---O
|   |   |
O---+---+
Turno do computador (dificil):
X---O---+
|   |   |
X---X---O
|   |   |
O---+---X
DERROTA
"""

JOGADA_CADETE_1 = '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25'
