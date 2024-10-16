import pytest
import sys
import FP2425P1 as fp


class TestCadeteTabuleiroPosicoes:

    def test_1a(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, True), (-1, 0, 0, -1))
        assert not fp.eh_tabuleiro(tab)

    def test_1b(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, False), (-1, 0, 0, -1))
        assert not fp.eh_tabuleiro(tab)

    def test_1c(self):
        tab = ()
        assert not fp.eh_tabuleiro(tab)

    def test_11a(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_coluna(tab, 1) == (1, 5, 9)

    def test_11b(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_coluna(tab, 4) == (4, 8, 12)

    def test_13a(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_linha(tab, 5) == (5, 6, 7, 8)

    def test_13b(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_linha(tab, 8) == (5, 6, 7, 8)

    def test_13c(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_linha(tab, 1) == (1, 2, 3, 4)

    def test_13d(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_linha(tab, 12) == (9, 10, 11, 12)

    def test_13e(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_linha(tab, 4) == (1, 2, 3, 4)

    def test_15a(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        assert fp.obtem_diagonais(tab, 8) == ((3, 8), (11, 8))


class TestCadeteInspectManip:
    def test_3a(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        with pytest.raises(ValueError) as erro:
            # Call the function that should raise the ValueError
            fp.eh_posicao_valida(tab, 'a')
        assert str(erro.value) == "eh_posicao_valida: argumentos invalidos"

    def test_3b(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        with pytest.raises(ValueError) as erro:
            fp.eh_posicao_valida(tab, True)
        assert str(erro.value) == "eh_posicao_valida: argumentos invalidos"

    def test_3c(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0), (-1, 0, 0, -1))
        with pytest.raises(ValueError) as erro:
            fp.eh_posicao_valida(tab, 11)
        assert str(erro.value) == "eh_posicao_valida: argumentos invalidos"

    def test_6a(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, '-1'))
        with pytest.raises(ValueError) as erro:
            fp.eh_posicao_livre(tab, 2)
        assert str(erro.value) == 'eh_posicao_livre: argumentos invalidos'

    def test_6b(self):
        tab = ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1))
        with pytest.raises(ValueError) as erro:
            fp.eh_posicao_livre(tab, -1)
        assert str(erro.value) == 'eh_posicao_livre: argumentos invalidos'


class TestCadeteJogo:

    def testAutoNormal1(self):
        assert fp.escolhe_posicao_auto_normal(
            ((1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, 0), (1, 0, 0, 1), (-1, 1, 0, 1), (-1, 0, 0, -1)), 1, 3,
        ) == 11

    def teste_descobre1(self):
        tab = ((0, 1, 0, 1, 1, 0, 1, -1),
               (0, 0, 0, 0, 0, 0, 0, 0))
        assert fp.descobre_L_possiveis_normal(tab, 1, 10) == (4, (3, 6))

    def teste_descobre2(self):
        tab = ((-1, 1, 0, 1, 1, -1),
               (0, 0, 0, 0, 0, 0))
        assert fp.descobre_L_possiveis_normal(tab, 1, 10) == (4, (3,))

    def teste_descobre3(self):
        tab = ((1, 1, -1, 1, 1, 0, 1),
               (0, 0, 0, 0, 0, 0, 0))
        assert fp.descobre_L_possiveis_normal(tab, 1, 10) == (4, (6,))

    def teste_normal1(self):
        tab = ((1, 0, -1),
               (-1, 1, 0),
               (1, 0, 0))
        assert fp.escolhe_posicao_auto_normal(tab, -1, 3) == 9

    def teste_normal2(self):
        tab = ((0, 0, 0),
               (0, 0, 0),
               (0, 0, 1))
        assert fp.escolhe_posicao_auto_normal(tab, -1, 3) == 5

    # De acordo com os testes privados, este é o teste que dura mais e o que produz um timeout com mais facilidade.
    def teste_timeouts(self):
        res = -1
        assert jogo_mnk_offline((5, 5, 4), 1, 'dificil', JOGADA_CADETE_1) == (res, OUTPUT_CADETE_1)


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


JOGADA_CADETE_1 = '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25'
OUTPUT_CADETE_1 = ('Bem-vindo ao JOGO MNK.\n'
                   "O jogador joga com 'X'.\n"
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do jogador. Escolha uma posicao livre: X---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do computador (dificil):\n'
                   'X---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do jogador. Escolha uma posicao livre: X---X---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do computador (dificil):\n'
                   'X---X---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---O---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do jogador. Escolha uma posicao livre: X---X---X---+---+\n'
                   '|   |   |   |   |\n'
                   '+---O---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do computador (dificil):\n'
                   'X---X---X---O---+\n'
                   '|   |   |   |   |\n'
                   '+---O---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma '
                   'posicao livre: X---X---X---O---X\n'
                   '|   |   |   |   |\n'
                   '+---O---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do computador (dificil):\n'
                   'X---X---X---O---X\n'
                   '|   |   |   |   |\n'
                   '+---O---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do jogador. Escolha uma posicao livre: X---X---X---O---X\n'
                   '|   |   |   |   |\n'
                   'X---O---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do computador (dificil):\n'
                   'X---X---X---O---X\n'
                   '|   |   |   |   |\n'
                   'X---O---O---O---+\n'
                   '|   |   |   |   |\n'
                   '+---+---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do jogador. Escolha uma posicao livre: Turno do jogador. Escolha uma '
                   'posicao livre: Turno do jogador. Escolha uma posicao livre: Turno do '
                   'jogador. Escolha uma posicao livre: X---X---X---O---X\n'
                   '|   |   |   |   |\n'
                   'X---O---O---O---X\n'
                   '|   |   |   |   |\n'
                   '+---+---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do computador (dificil):\n'
                   'X---X---X---O---X\n'
                   '|   |   |   |   |\n'
                   'X---O---O---O---X\n'
                   '|   |   |   |   |\n'
                   '+---O---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do jogador. Escolha uma posicao livre: X---X---X---O---X\n'
                   '|   |   |   |   |\n'
                   'X---O---O---O---X\n'
                   '|   |   |   |   |\n'
                   'X---O---O---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'Turno do computador (dificil):\n'
                   'X---X---X---O---X\n'
                   '|   |   |   |   |\n'
                   'X---O---O---O---X\n'
                   '|   |   |   |   |\n'
                   'X---O---O---+---+\n'
                   '|   |   |   |   |\n'
                   'O---+---+---+---+\n'
                   '|   |   |   |   |\n'
                   '+---+---+---+---+\n'
                   'DERROTA\n')
