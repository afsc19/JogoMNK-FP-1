# Projeto 1 FP 2024/2025
# Criado por André Cadete
# Aluno 114254 - ist1114254
# email: andre.cadete@tecnico.ulisboa.pt


def eh_tabuleiro(arg):
    """
    eh_tabuleiro: universal → booleano

    Devolve True se o argumento for um tabuleiro.
    """
    # Verifica o argumento. (primeiro tuplo e nº de linhas)
    if not (isinstance(arg, tuple) and 2 <= len(arg) <= 100 and isinstance(arg[0], tuple) and 2 <= len(arg[0]) <= 100):
        return False

    n = len(arg[0])
    # Percorre cada valor contido no primeiro tuplo. (segundos tuplos e nºs de colunas)
    for linha in arg:
        # Verifica se é tuple,
        # se está contido nos limites máximos de um tabuleiro,
        # E se o nº de colunas é o mesmo em todas as linhas.
        if not (isinstance(linha, tuple) and 2 <= len(linha) <= 100 and len(linha) == n):
            return False

        # Verifica se os valores de cada posição do tabuleiro são inteiros.
        for valor in linha:
            if not (type(valor) == int and -1 <= valor <= 1):
                return False
    return True


def eh_posicao(arg):
    """
    eh_posicao: universal → booleano
    Devolve True se o argumento é uma posição que pode existir num tabuleiro.
    """
    return type(arg) == int \
        and 0 < arg <= 100 * 100  # Como o tabuleiro só pode ser 100x100, só pode ter 100 000 posições.


def obtem_dimensao(tab):
    """
    obtem_dimensao: tabuleiro → tuplo
    Devolve um tuplo formado pelo nº de linhas e pelo nº de colunas do tabuleiro recebido no argumento.
    """

    # Como o tabuleiro é constituido por um tuplo de tuplos, em que cada tuplo contido no primeiro representam filas,
    # o nº de colunas pode ser dado pelo tamanho do primeiro tuplo, ou seja, pela contagem das filas neste contidas.
    m = len(tab)

    # Considerando que os tamanhos de cada fila são iguais no tabuleiro inteiro, (após eh_tabuleiro),
    # Para obter o nº de colunas basta calcular o tamanho de um das filas (a fila 0 estará sempre presente, dado que n >= 2).
    n = len(tab[0])
    return (m, n)


def obtem_valor(tab, pos):
    """
    obtem_valor: tabuleiro × posicao → inteiro

    Recebe um tabuleiro e uma posição do tabuleiro.
    Devolve o inteiro contido nessa posição.
    """
    return tab[qual_linha(tab, pos)][qual_coluna(tab, pos)]


def obtem_coluna(tab, pos):
    """
    obtem_coluna: tabuleiro × posicao → tuplo

    Recebe um tabuleiro e uma posição do tabuleiro.
    Devolve um tuplo com todas as posições que formam a coluna em que está contida a posição recebida.
    """
    m, n = obtem_dimensao(tab)
    # Calcula a primeira posição da coluna, sendo que será o resto da divisão pelo nº de colunas.
    # À exceção de quando o resto for zero, o que significa que a coluna será a última (n).
    posicoes_col = (qual_coluna(tab, pos) + 1,)

    # Adiciona n posições à coluna anterior sendo que a diferença entre duas linhas é o nº de colunas = n.
    # Isto ocorre até o último elemento adicionado pertencer à última coluna.
    # (enquanto o último elemento adicinoado ainda não pertencer à última coluna)
    while posicoes_col[-1] <= n * (m - 1):
        posicoes_col += (posicoes_col[-1] + n,)
    return posicoes_col


def obtem_linha(tab, pos):
    """
    obtem_linha: tabuleiro × posicao → tuplo

    Recebe um tabuleiro e uma posição do tabuleiro.
    Devolve um tuplo com todas as posições que formam a linha em que está contida a posição.
    """
    m, n = obtem_dimensao(tab)
    # Calcula a primeira posição da linha (coluna 0).
    posicoes_linha = (qual_linha(tab, pos) * n + 1,)

    # Adiciona 1 à posição anterior da linha até chegar ao fim da linha
    # (o tamanho do tuplo será o nº de colunas)
    while len(posicoes_linha) < n:
        posicoes_linha += (posicoes_linha[-1] + 1,)

    return posicoes_linha


def obtem_diagonais(tab, pos):
    """
    obtem_diagonais: tabuleiro × posicao → tuplo

    Recebe um tabuleiro e uma posição.
    Devolve um tuplo formado por dois tuplos de posições correspondetes à diagonal e à antidiagonal.
    """

    return (obtem_diagonal(tab, pos), obtem_antidiagonal(tab, pos))


# Função Auxiliar
def obtem_diagonal(tab, pos):
    """
    obtem_diagonal: tabuleiro × posicao → tuplo

    Recebe um tabuleiro e uma posição.
    Devolve um tuplo com as posições da diagonal à qual a posição pertence.
    """
    # Calcular o nº total de linhas e de colunas
    m, n = obtem_dimensao(tab)
    # Calcular a linha e a coluna da posição
    linha = qual_linha(tab, pos)
    col = qual_coluna(tab, pos)

    # Se a posição recebida estiver mais perto da primeira coluna do que da primeira fila,
    # a coluna passa a ser zero e a linha é subtraída pela coluna original.
    if linha >= col:
        col, linha = 0, linha - col
    else:
        # Caso contrário, se a posição recebida estiver mais perto da primeira linha:
        # A linha passa a ser zero,
        # e a coluna é subtraída pela linha original.
        linha, col = 0, col - linha

    # Calcula e adiciona a posição nessa linha e coluna.
    # (+1 dado que as posições começam no 1, enquanto os índices das colunas começam no 0)
    diagonal = (linha * n + col + 1,)

    # Enquanto ainda não tiver adicionado uma posição da última linha ou da última coluna:
    while diagonal[-1] <= n * (m - 1) and diagonal[-1] % n > 0:
        # A próxima diagonal será dada pela linha abaixo (+n) e pela coluna seguinte (+1).
        diagonal += (diagonal[-1] + n + 1,)

    return diagonal


# Função Auxiliar
def obtem_antidiagonal(tab, pos):
    """
    obtem_antidiagonal: tabuleiro × posicao → tuplo

    Recebe um tabuleiro e uma posição.
    Devolve um tuplo com as posições da antidiagonal à qual a posição pertence.
    """
    # Calcular o nº total de linhas e de colunas
    m, n = obtem_dimensao(tab)
    # Volta a definir a linha e a coluna da posição recebida.
    linha = qual_linha(tab, pos)
    col = qual_coluna(tab, pos)

    # Se a posição recebida estiver mais perto da primeira coluna do que da última linha,
    # a coluna passa a ser zero e à linha é somada a coluna original.
    if m - 1 - linha >= col:
        col, linha = 0, linha + col
    else:
        # Caso contrário, ou seja, se a posição recebida estiver mais perto da última linha
        # A linha passa a ser a última
        # E a coluna é subtraída pela diferença entre a última linha e a linha original.
        linha, col = m - 1, col - (m - 1 - linha)

    # Calcula e adiciona a posição nessa linha e coluna.
    # (+1 dado que as posições começam no 1, enquanto os índices das colunas começam no 0)
    antidiagonal = (linha * n + col + 1,)

    # Enquanto ainda não tiver adicionado uma posição da primeira linha ou da última coluna:
    while antidiagonal[-1] > n and antidiagonal[-1] % n > 0:
        # A próxima antidiagonal será dada pela linha acima (-n) e pela coluna seguinte (+1).
        antidiagonal += (antidiagonal[-1] - n + 1,)
    return antidiagonal


def tabuleiro_para_str(tab):
    """
    tabuleiro para str: tabuleiro → cad. carateres

    Recebe um tabuleiro.
    Devolve a cadeia de caracteres que o representa.
    """
    rep = ''
    n = obtem_dimensao(tab)[1]

    # Percorre cada linha
    for ilinha, linha in enumerate(tab):
        # À exceção da primeira, adiciona separadores entre linhas:
        if ilinha > 0:
            rep += '\n' + '|   ' * (n - 1) + '|\n'
        for icol, col in enumerate(linha):
            # Para cada linha,
            if icol > 0:
                rep += "---"
            # Traduz o valor presente no tuplo da coluna para o símbolo correspondente.
            # (utilizei um tuplo para encurtecer o código.)
            rep += ('+', 'X', 'O')[col]

    return rep


def eh_posicao_valida(tab, pos):
    """
    eh_posicao_valida: tabuleiro × posicao → booleano

    Recebe um tabuleiro e uma posição.
    Devolve True se a posição corresponde a uma posição do tabuleiro.
    Caso contrário devolve False.

    Se algum dos argumentos recebidos for inválido, a função irá gerar um erro.
    """
    # Verifica os argumentos.
    if not (eh_posicao(pos) and eh_tabuleiro(tab)):
        raise ValueError('eh_posicao_valida: argumentos invalidos')

    m, n = obtem_dimensao(tab)
    # Calcula a posição máxima do tabuleiro.
    p_max = m * n
    # Verifica se a posição está entre os limites do tabuleiro.
    return 1 <= pos <= p_max


def eh_posicao_livre(tab, pos):
    """
    eh_posicao_livre: tabuleiro × posicao → booleano

    Recebe um tabuleiro e uma posição do tabuleiro.
    Devolve True se a posição corresponde a uma posição livre.
    Caso contrário devolve False.

    Se algum dos argumentos recebidos for inválido, a função irá gerar um erro.
    """
    # Verifica os argumentos.
    if not (eh_posicao(pos) and eh_tabuleiro(tab) and eh_posicao_valida(tab, pos)):
        raise ValueError("eh_posicao_livre: argumentos invalidos")
    # Se a posição for livre, o valor correspondente será 0.
    return obtem_valor(tab, pos) == 0


def obtem_posicoes_livres(tab):
    """
    obtem_posicoes_livres: tabuleiro → tuplo

    Recebe um tabuleiro
    Devolve o tuplo com todas as posições livres do tabuleiro, ordenadas de menor para maior.
    
    Se o recebido for inválido, a função irá gerar um erro.
    """
    # Verifica o argumento
    if not eh_tabuleiro(tab):
        raise ValueError("obtem_posicoes_livres: argumento invalido")
    # Percorre as posições de 1 até à última posição e verifica se o seu valor é 0.
    m, n = obtem_dimensao(tab)
    p_max = m * n
    return tuple(pos
                 for pos in range(1, p_max + 1)
                 if obtem_valor(tab, pos) == 0)


def obtem_posicoes_jogador(tab, jog):
    """
    obtem_posicoes_jogador: tabuleiro × inteiro → tuplo

    Recebe um tabuleiro e um inteiro identificando um jogador (1 para as pedras pretas ou -1 para as pedras brancas).
    Devolve o tuplo com todas as posições do tabuleiro ocupadas por pedras do jogador, ordenadas de menor para maior.
    
    Se algum dos argumentos recebidos for inválido, a função irá gerar um erro.
    """
    # Verifica os argumentos
    if not (eh_tabuleiro(tab) and eh_jog(jog)):
        raise ValueError("obtem_posicoes_jogador: argumentos invalidos")

    m, n = obtem_dimensao(tab)
    p_max = m * n
    # Percorre as posições de 1 até à última posição e verifica se o seu valor é o valor do argumento jog.
    return tuple(pos
                 for pos in range(1, p_max + 1)
                 if obtem_valor(tab, pos) == jog)


def obtem_posicoes_adjacentes(tab, pos):
    """
    obtem_posicoes_adjacentes: tabuleiro × posicao → tuplo

    Recebe um tabuleiro e uma posição do tabuleiro.
    Devolve o tuplo formado pelas posições do tabuleiro adjacentes (horizontal, vertical e diagonal), ordenadas de menor para maior.
    
    Se algum dos argumentos recebidos for inválido, a função irá gerar um erro.
    """
    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab, pos)):
        raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")
    posicoes = ()
    m, n = obtem_dimensao(tab)
    p_max = m * n
    # Percorre todas as posições
    for p in range(1, p_max + 1):
        # Caso a distância chebyshev seja igual a 1, adiciona ao tuplo das posições.
        if chebyshev(tab, pos, p) == 1 and p != pos:
            posicoes += (p,)
    # Devolve o tuplo das posições.
    return posicoes


def ordena_posicoes_tabuleiro(tab, tup):
    """
    ordena_posicoes_tabuleiro: tabuleiro × tuplo → tuplo

    Recebe um tabuleiro e um tuplo de posições do tabuleiro (potencialmente vazio).
    Devolve o tuplo com as posições em ordem ascendente de distância à posição central do tabuleiro.
    Posições com igual distância à posição central, são ordenadas de menor a maior de acordo com a posição que ocupam no tabuleiro.
    
    Se algum dos argumentos recebidos for inválido, a função irá gerar um erro.
    """
    # Verifica os argumentos
    if not (eh_tabuleiro(tab) and isinstance(tup, tuple)):
        raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")

    # Calcula o centro
    centro = posicao_central(tab)

    # Verifica se o tuplo recebido contém posições válidas.
    for pos in tup:
        if not (type(pos) == int and eh_posicao(pos) and eh_posicao_valida(tab, pos)):
            raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")

    # Função utilizada para calcular as chaves de ordenação do tuplo.
    def transforma_chebyshev(x):
        # O primeiro critério é a distância da posição x ao centro.
        criterio1 = chebyshev(tab, centro, x)
        # O segundo critério é a própria posição x.
        criterio2 = x

        # Define a ordem os critérios
        return (criterio1, criterio2)

    # Devolve um tuplo ordenado de acordo com os critérios definidos com as posições presentes no tuplo inicialmente recebido.
    return tuple(sorted(tup, key=transforma_chebyshev))


def marca_posicao(tab, pos, jog):
    """
    marca_posicao: tabuleiro × posicao × inteiro → tabuleiro

    Recebe um tabuleiro, uma posição livre do tabuleiro e um inteiro identificando o jogador (1 pedras pretas ou -1 pedras brancas)
    Devolve um novo tabuleiro com uma nova pedra do jogador indicado nessa posição.
    
    Se algum dos argumentos recebidos for inválido, a função irá gerar um erro.
    """
    # Verifica os argumentos
    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab, pos) and eh_posicao_livre(tab, pos)
            and eh_jog(jog)):
        raise ValueError('marca_posicao: argumentos invalidos')
    linha = qual_linha(tab, pos)
    coluna = qual_coluna(tab, pos)
    # Converte o tabuleiro para lista
    tab = list(tab)
    # Converte a linha calculada para lista
    tab[linha] = list(tab[linha])
    # Altera esta lista
    tab[linha][coluna] = jog
    # Volta a converter a linha para tuplo
    tab[linha] = tuple(tab[linha])
    # Volta a converter o tabuleiro para tuplo e devolve-o.
    return tuple(tab)


def verifica_k_linhas(tab, pos, jog, k):
    """
    verifica_k_linhas: tabuleiro × posicao × inteiro × inteiro → booleano

    Recebe um tabuleiro, uma posição do tabuleiro,
    um valor inteiro identificando o jogador (1 pedras pretas ou -1 pedras brancas), e um valor inteiro positivo k.
    Devolve True se existe pelo menos uma linha (horizontal, vertical ou diagonal)
    que contenha a posição com uma ou mais pedras consecutivas do jogador indicado.
    Devolve False caso contrário.

    Se algum dos argumentos recebidos for inválido, a função irá gerar um erro.
    """
    # Verifica os argumentos
    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab, pos) and eh_jog(jog) and eh_k(k)):
        raise ValueError("verifica_k_linhas: argumentos invalidos")

    # Caso a posição recebida nem tenha uma pedra da cor correspondente ao jogador, não existe sequência de pedras repetidas.
    if obtem_valor(tab, pos) != jog:
        return False

    if k == 1:
        return True

    # Obtem as posicoes do jogador para
    posicoes_jogador = obtem_posicoes_jogador(tab, jog)
    # Junta todas as linhas (horizontal, vertical, diagonal, antidiagonal)
    diagonais = obtem_diagonais(tab, pos)
    linhas = (obtem_linha(tab, pos), obtem_coluna(tab, pos), diagonais[0], diagonais[1])

    # Percorre cada uma das linhas
    for linha in linhas:
        # Memoriza se esta contagem incluiu a pedra correspondente à posição recebida.
        contem_pos = False
        # Conta quantas pedras existem de seguida
        contagem_p = 0
        # Percorre as posições das linhas
        for p in linha:
            # Caso a posição atual seja uma posição do jogador, aumenta a contagem
            if p in posicoes_jogador:
                contagem_p += 1
            else:
                # Se a pedra da posição recebida já tinha sido contabilizada, não exisite sequência alguma que inclua ela própria.
                if contem_pos:
                    break
                # O contador volta a 0
                contagem_p = 0
            # A contagem atual passa a incluir a posição recebida
            if p == pos:
                contem_pos = True
            # Devolve True se existem k ou mais pedras seguidas e se nestas está incluída a pedra da posição recebida.
            if contem_pos and contagem_p >= k:
                return True
    return False


def eh_fim_jogo(tab, k):
    """
    eh_fim_jogo: tabuleiro × inteiro → booleano

    Recebe um tabuleiro e um valor inteiro positivo k.
    Devolve True se o jogo terminou.
    Caso contrário devolve False.

    Se algum dos argumentos recebidos for inválido, a função irá gerar um erro.
    """
    # Verifica os argumentos
    if not (eh_tabuleiro(tab) and eh_k(k)):
        raise ValueError("eh_fim_jogo: argumentos invalidos")

    # Devolve True se o tabuleiro está cheio, ou seja, se não tiver posições livres.
    n_livres = len(obtem_posicoes_livres(tab))
    if n_livres == 0:
        return True

    m, n = obtem_dimensao(tab)

    # Calcula algumas posições
    ultima_pos_primeira_linha = n
    primeira_pos_segunda_linha = n + 1
    primeira_pos_ultima_linha = n * (m - 1) + 1
    segunda_pos_ultima_linha = primeira_pos_ultima_linha + 1
    ultima_pos_ultima_linha = m * n

    # Para verificar o tabuleiro utilizando a função verifica_k_linhas,
    # apenas é necessário percorrer 3 lados do tabuleiro para se verificar todas as linhas,
    # colunas, diagonais e antidiagonais, independentemente do tamanho do tabuleiro
    laterais = (range(1, ultima_pos_primeira_linha + 1),
                range(primeira_pos_segunda_linha, primeira_pos_ultima_linha + 1, n),
                range(segunda_pos_ultima_linha, ultima_pos_ultima_linha + 1))
    # Percorre-se todas as posições de cada lateral
    for lateral in laterais:
        for p in lateral:
            # Verifica se algum dos jogadores (-1 ou 1) já tem k linhas seguidas
            if verifica_k_linhas(tab, p, -1, k) or verifica_k_linhas(tab, p, 1, k):
                return True

    # A este ponto da função, já se verificou que:
    # O tabuleiro não está vazio nem totalmente cheio.
    # Ainda nenhum dos jogadores marcou k pedras seguidas.
    # Logo o jogo ainda não acabou
    return False


# Função Auxiliar
def obtem_linhas(tab):
    """
    obtem_linhas: tabuleiro → tuplo

    Recebe um tabuleiro.
    Devolve um tuplo com todas as linhas (horizontais, verticais, diagonais e antidiagonais) do tabuleiro.
    """

    m, n = obtem_dimensao(tab)

    # Calcula algumas posições
    ultima_pos_primeira_linha = n
    primeira_pos_segunda_linha = n + 1
    primeira_pos_ultima_linha = n * (m - 1) + 1
    segunda_pos_ultima_linha = primeira_pos_ultima_linha + 1
    ultima_pos_ultima_linha = m * n

    # Para verificar o tabuleiro utilizando a função verifica_k_linhas,
    # apenas é necessário percorrer 3 lados do tabuleiro para se verificar todas as linhas,
    # colunas, diagonais e antidiagonais, independentemente do tamanho do tabuleiro
    laterais = (range(1, ultima_pos_primeira_linha + 1),
                range(primeira_pos_segunda_linha, primeira_pos_ultima_linha + 1, n),
                range(segunda_pos_ultima_linha, ultima_pos_ultima_linha + 1))

    linhas = []

    # Com o intuito de prevenir linhas repetidas:
    def adiciona_linhas(tup_linhas):
        """
        adiciona_linhas: tuplo → None

        Função que adiciona cada linha dentro do tuplo recebido à lista linhas,
        caso esta ainda não esteja presente na lista.
        """
        for linha in tup_linhas:
            if linha not in linhas:
                linhas.append(linha)

    # Adiciona cada linha, coluna, diagonal e antidiagonal do tabuleiro à lista das linhas.
    for linha in laterais:
        for pos in linha:
            horizontal = obtem_linha(tab, pos)
            vertical = obtem_coluna(tab, pos)
            diagonal, antidiagonal = obtem_diagonais(tab, pos)
            adiciona_linhas((horizontal, vertical, diagonal, antidiagonal))
    return linhas


def escolhe_posicao_manual(tab):
    """
    escolhe_posicao_manual: tabuleiro → posicao

    Recebe um tabuleiro.
    Devolve uma posição introduzida manualmente pelo jogador.
    Caso o jogador introduza uma posição que não esteja livre, a função irá pedir a posição de novo.

    Se o argumento recebido for inválido, a função irá gerar um erro.
    """
    # Verifica o argumento
    if not eh_tabuleiro(tab):
        raise ValueError('escolhe_posicao_manual: argumento invalido')

    # Define uma posição que force a entrada no ciclo while.
    p = -1
    # Enquanto a posição não for válida nem corresponder a uma posição livre,
    # Pergunta ao jogador a posição que deseja jogar.
    while not (eh_posicao(p) and eh_posicao_valida(tab, p) and eh_posicao_livre(tab, p)):
        resposta = input('Turno do jogador. Escolha uma posicao livre: ')
        # Verifica se a resposta é um inteiro.
        if resposta.isdigit():
            p = int(resposta)
    return p


def escolhe_posicao_auto(tab, jog, k, lvl):
    """
    escolhe_posicao_auto: tabuleiro × inteiro × inteiro × cad. carateres → posicao

    Recebe um tabuleiro (em que o jogo não terminou ainda),
    um inteiro identificando um jogador (1 pedras pretas ou -1 pedras brancas),
    um inteiro positivo correspondendo ao valor k dum jogo m,n,k,
    e a cadeia de carateres correspondente à estratégia.
    Devolve a posição escolhida automaticamente de acordo com a estratégia selecionada.

    As estratégias aceites são: 'facil', 'normal' ou 'dificil'.
    Sempre que houver mais do que uma posição que cumpra um dos critérios definidos nas estratégias anteriores,
    a função irá escolher a posição mais próxima da posição central do tabuleiro.

    Caso algum dos argumentos seja inválido, a função irá gerar um erro.
    """
    # Verifica os argumentos.
    if not (eh_tabuleiro(tab) and eh_jog(jog) and eh_k(k) and eh_lvl(lvl) and not eh_fim_jogo(tab, k)):
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')

    # Para o nivel facil:
    if lvl == 'facil':
        # Regista todas as posições livres.
        livres = obtem_posicoes_livres(tab)
        possiveis = []
        # Para cada posição livre, se essa posição é adjacente a uma posição marcada pelo jogador,
        # adiciona-a à lista das posições possíveis.
        for livre in livres:
            for adjacente in obtem_posicoes_adjacentes(tab, livre):
                if obtem_valor(tab, adjacente) == jog:
                    possiveis.append(livre)
                    break
        # Caso tenha encontrado uma ou mais posições livres adjacentes às peças do jogador, joga numa dessas posições.
        if len(possiveis) > 0:
            # Para decidir em qual das várias posições equivalentes irá jogar,
            # seleciona a cuja sua distância à posição central é menor.
            return ordena_posicoes_tabuleiro(tab, tuple(possiveis))[0]
        # Caso não tenha encontrado nenhuma posição livre adjacente às peças do jogador, joga numa posição livre.
        # Para decidir em qual das várias posições equivalentes irá jogar,
        # seleciona a cuja sua distância à posição central é menor.
        return ordena_posicoes_tabuleiro(tab, livres)[0]
    elif lvl == 'normal':
        return escolhe_posicao_auto_normal(tab, jog, k)
    else:
        # Calcula todas as posições mais favoráveis (com o intuito de obter o maior nº de peças próprias consecutivas)
        # para cada jogador marcar, bem como o nº de peças consecutivas no caso de marcar numa dessas posições.
        L_jog, possiveis_jog = descobre_L_possiveis_normal(tab, jog, k)
        L_adv, possiveis_adv = descobre_L_possiveis_normal(tab, -jog, k)

        # Caso o jogador consiga marcar k peças consecutivas,
        # marca na mais próxima do centro dessas peças.
        if L_jog == k:
            # Para decidir em qual das várias posições equivalentes irá jogar,
            # seleciona a cuja sua distância à posição central é menor.
            return ordena_posicoes_tabuleiro(tab, possiveis_jog)[0]
        # Caso o jogador consiga bloquear k peças consecutivas do seu adversário,
        # marca na mais próxima do centro dessas peças.
        elif L_adv == k:
            # Para decidir em qual das várias posições equivalentes irá jogar,
            # seleciona a cuja sua distância à posição central é menor.
            return ordena_posicoes_tabuleiro(tab, possiveis_adv)[0]
        # Caso nenhum dos jogadores consiga atingir k linhas na próxima jogada de cada um:
        else:
            # Prepara um inteiro para guardar o melhor resultado devolvido das simulações
            melhor_resultado = 0
            # Prepara uma lista para guardar as posições favoráveis de obter o melhor resultado.
            p_favoraveis = []
            # Simula um jogo para cada posição e guarda o seu resultado.
            for p_livre in obtem_posicoes_livres(tab):
                resultado = simular_jogo(tab, jog, p_livre, k)
                # Caso o resultado não seja pior, irá adicionar a posição à lista de posições possíveis.
                if resultado >= melhor_resultado:
                    # Caso o resultado seja melhor do que o melhor resultado encontrado anteriormente:
                    if resultado > melhor_resultado:
                        # Atualiza o inteiro que guarda o melhor resultado.
                        melhor_resultado = resultado
                        # Limpa a lista com as posições favoráveis de obter o melhor resultado anterior.
                        p_favoraveis.clear()
                    # Adiciona a posição atual à lista dos resultados.
                    p_favoraveis.append(p_livre)

            # Para decidir em qual das várias posições equivalentes irá jogar,
            # seleciona a cuja sua distância à posição central é menor.
            return ordena_posicoes_tabuleiro(tab, tuple(p_favoraveis))[0]


# Fução EXTRA
def escolhe_posicao_auto_normal(tab, jog, k):
    """
    escolhe_pos_normal: tabuleiro × inteiro × inteiro → posicao

    Recebe um tabuleiro (em que o jogo não terminou ainda),
    um inteiro identificando um jogador (1 pedras pretas ou -1 pedras brancas) e
    um inteiro positivo correspondendo ao valor k dum jogo m,n,k.
    Utiliza a estratégia de jogo normal para escolher uma posição livre do tabuleiro e devolve-a.
    """
    # Calcula todas as posições mais favoráveis (com o intuito de obter o maior nº de peças próprias consecutivas)
    # para cada jogador marcar, bem como o nº de peças consecutivas no caso de marcar numa dessas posições.
    L_jog, possiveis_jog = descobre_L_possiveis_normal(tab, jog, k)
    L_adv, possiveis_adv = descobre_L_possiveis_normal(tab, -jog, k)

    # Caso o jogador consiga marcar mais ou iguais peças que o adversário,
    # irá jogar numa posição favorável ao seu nº de peças consecutivas (devolverá essa posição).
    if L_jog >= L_adv:
        # Para decidir em qual das várias posições equivalentes irá jogar,
        # seleciona a cuja sua distância à posição central é menor.
        return ordena_posicoes_tabuleiro(tab, possiveis_jog)[0]
    # Caso contrário, irá jogar numa posição favorável ao nº de peças consecutivas do adversário.
    # Para decidir em qual das várias posições equivalentes irá jogar,
    # seleciona a cuja sua distância à posição central é menor.
    return ordena_posicoes_tabuleiro(tab, possiveis_adv)[0]


def simular_jogo(tab, jog, pos_inicial, k):
    """
    simular_jogo: tabuleiro × inteiro × posicao × inteiro → inteiro

    Recebe um tabuleiro (em que o jogo não terminou ainda),
    um inteiro identificando um jogador (1 pedras pretas ou -1 pedras brancas),
    uma posição que irá ser marcada de início e
    um inteiro positivo correspondendo ao valor k dum jogo m,n,k.

    Simula um jogo, até ao fim, entre dois computadores, utilizando a estratégia normal,
    após marcar a posição pos_inicial recebida.

    Devolve:
    0 se não conseguir ganhar nem empatar o jogo
    1 se conseguir empatar o jogo
    2 se conseguir ganhar o jogo
    """
    # Cria uma cópia do tabuleiro recebido
    # e marca a posição escolhida para ser marcada de início.
    tabuleiro = marca_posicao(tab, pos_inicial, jog)

    # Como o jogador jog acabou de jogar, o próximo será o adversário do jog.
    jogador_atual = -jog
    # Só sai da simulação quando o jogo acabar.
    while not eh_fim_jogo(tabuleiro, k):
        # O jogador escolhe a posição a jogar utilizando a estratégia normal.
        pos = escolhe_posicao_auto_normal(tabuleiro, jogador_atual, k)
        # Marca essa posição no tabuleiro.
        tabuleiro = marca_posicao(tabuleiro, pos, jogador_atual)

        # Caso o algum dos jogadores tenha ganho
        if verifica_k_linhas(tabuleiro, pos, jogador_atual, k):
            # Se o jogador jog foi quem ganhou, devolve 2
            # Caso contrário, devolve 0
            return 2 if jogador_atual == jog else 0

        # Após jogar, troca o jogador.
        jogador_atual = -jogador_atual

    # A este ponto do código, não existem mais posições para jogar e nenhum dos jogadores ganhou,
    # ou seja, houve um empate, e nesse caso devolve 1.
    return 1


def descobre_L_possiveis_normal(tab, jog, k):
    """
    descobre_L_possiveis_normal: tabuleiro × inteiro × inteiro → tuplo

    Recebe um tabuleiro, um tuplo formado de linhas, por sua vez formadas de posições do tabuleiro
    e um inteiro correspondente ao jogador (1 pedras pretas ou -1 pedras brancas).

    Devolve tuplo formado por um inteiro L (L ≤ K),
    que representa o nº de peças consecutivas que o jogador consegue marcar se jogar numa das posições possíveis,
    e pelas posições possíveis anteriormente mencionadas,
    """

    linhas = obtem_linhas(tab)

    # Prepara um inteiro L, que irá corresponder a um nº de posições cujo valor é jog consecutivas,
    # que começa em 0, pois estamos à procura de um L cada vez maior.
    L = 0
    # Prepara um tuplo que vai guardar todas as posições possíveis de se alcançar esse L.
    possiveis = ()
    # Percorre todas as linhas.
    for linha in linhas:
        # Inteiro para contar o nº de posições com o valor jog consecutivas
        cont = 0
        # Inteiro para guardar uma posição livre antes da contagem de posições com o valor jog consecutivas.
        p_livre_antes = 0
        # Inteiro para guardar a contagem anterior,
        # para, no caso de se obter uma posição vazia entre outras com o valor jog,
        # ele calcular o L se marca-se essa posição vazia.
        # Exemplo (com valores): jog jog 0 jog => L=4, adiciona a posição 3 (vazia)
        cont_anterior = 0
        for p in linha:
            # Verifica o valor da posição atual.
            v = obtem_valor(tab, p)
            # Caso esse valor seja pos, incrementa o contador.
            if v == jog:
                cont += 1
                # Se o nº de posições com valor jog consecutivas, ao marcar a posição livre anterior, caso exista,
                # for igual ao L atual, adiciona a posição livre anterior à lista das posições possíveis para se alcançar o L.
                if cont + cont_anterior >= L and p_livre_antes > 0:
                    # Caso este nº seja maior do que o L, atualiza o L e limpa a lista das posições possíveis para se alcançar o L
                    # antes de se adicionar (ou não, ler comentário anterior) a posição livre.
                    if cont + cont_anterior > L and k > L:
                        L = cont + cont_anterior
                        possiveis = ()

                    possiveis += (p_livre_antes,) if p_livre_antes not in possiveis else ()
            # Caso o valor seja 0, ou seja, a posição esteja livre,
            # a contagem anterior (cont_anterior) passa a ser o valor do contador mais a posição livre que se acabou de encontrar.
            elif v == 0:
                cont_anterior = cont + 1
                # Caso já se consiga obter uma contagem maior ou igual ao L ao marcar nesta posição,
                # adiciona-a à lista se ainda não o tiver feito.
                if cont_anterior >= L:
                    # Antes de adicionar à lista, verifica se esta contagem é maior que o L anterior.
                    # Nesse caso, atualiza o L e limpa a lista dos valores possíveis para se alcançar o L antes de adicionar o novo possível.
                    if cont_anterior > L and k > L:
                        L = cont_anterior
                        possiveis = ()
                    possiveis += (p,) if p not in possiveis else ()
                # Regista a posição livre antes da próxima contagem, se for caso disso.
                p_livre_antes = p
                # O contador volta a 0, porque a sequência de posições consecutivas
                cont = 0
            else:
                # Caso não se encontre uma posição marcada pelo jogador nem livre,
                # os contadores voltam a 0, bem como a posição livre antes da contagem.
                p_livre_antes = 0
                cont_anterior = 0
                cont = 0

    # Devolve o maior L encontrado e as posições possíveis de se marcar para se alcançar esse L.
    return (L, possiveis)


def jogo_mnk(cfg, jog, lvl):
    """
    jogo_mnk: tuplo × inteiro × cad. carateres → inteiro

    Função principal que permite jogar um jogo completo m,n,k.
    Recebe um tuplo de três valores inteiros correspondentes aos valores de configuração do jogo m,n e k,
    um inteiro identificando a cor das pedras do jogador humano (1 para as pedras pretas ou -1 para as pedras brancas)
    e uma cadeia de caracteres identificando a estratégia de jogo utilizada pela máquina ('facil', 'normal' ou 'dificil').

    O jogo começa sempre com o jogador com pedras pretas a marcar posição livre e termina quando um dos jogadores vence
    ou se não existirem posições livres no tabuleiro.
    A função mostra o resultado do jogo (VITORIA, DERROTA ou EMPATE) e
    Devolve um inteiro identificando o jogador vencedor
    (1 para preto ou -1 para branco), ou 0 em caso de empate.

    Caso algum dos argumentos seja inválido, a função irá gerar um erro.
    """
    # Verifica os argumentos
    if not (isinstance(cfg, tuple) and len(cfg) == 3 and eh_dimensao(cfg[0]) and eh_dimensao(cfg[1]) and eh_k(
            cfg[2]) and eh_jog(jog) and eh_lvl(lvl)):
        raise ValueError("jogo_mnk: argumentos invalidos")

    # Obtém o nº de linhas (m), o nº de colunas (n) e o nº de posições consecutivas necessárias para ganhar o jogo (k).
    m, n, k = cfg
    # Cria um tuplo que representará um tabuleiro.
    tabuleiro = ()
    # Adiciona m tuplos (linhas) dentro do tabuleiro formadas de n tuplos (colunas) contendo espaços vazios (zeros).
    for linha in range(m):
        nova_linha = ()
        for coluna in range(n):
            nova_linha += (0,)
        tabuleiro += (nova_linha,)

    # Mensagens iniciais.
    print("Bem-vindo ao JOGO MNK.")
    # Caso o jog seja 1, o jogador irá jogar com o 'X', caso contrário, irá jogar com o 'O'.
    simbolo_jogador = 'X' if jog == 1 else 'O'
    print(f"O jogador joga com '{simbolo_jogador}'.")
    # Mostra o tabuleiro vazio.
    print(tabuleiro_para_str(tabuleiro))
    # O primeiro jogador a jogar é o 'X', ou seja, o 1.
    jogador_atual = 1
    # Os jogadores só param de jogar quando o jogo tiver acabado, informação dada pela função eh_fim_jogo.
    while not eh_fim_jogo(tabuleiro, k):
        # Se o jogador for o jogador atual:
        if jogador_atual == jog:
            # Pede ao utilizador para inserir a posição que pretende jogar.
            pos = escolhe_posicao_manual(tabuleiro)
            # Marca essa posição no tabuleiro.
            tabuleiro = marca_posicao(tabuleiro, pos, jog)

        # Caso seja o computador a jogar:
        else:
            # Imprime uma mensagem que indica que é o turno do computador e o seu nível de dificuldade.
            print(f"Turno do computador ({lvl}):")
            # Escolhe automaticamente, de acordo com o tabuleiro atual, com o seu símbolo, com o k e com o seu nível,
            # a posição que o computador irá jogar.
            pos = escolhe_posicao_auto(tabuleiro, -jog, k, lvl)
            # Marca essa posição no tabuleiro.
            tabuleiro = marca_posicao(tabuleiro, pos, -jog)

        # Mostra o tabuleiro após a jogada atual.
        print(tabuleiro_para_str(tabuleiro))

        # Veririca se algum dos jogadores ganhou, caso tenha marcado k posições consecutivas.
        if verifica_k_linhas(tabuleiro, pos, jogador_atual, k):
            # Imprime 'VITORIA' se o jogador ganhou, ou, caso contrário, 'DERROTA' caso o computador tenha ganho.
            print("VITORIA" if jogador_atual == jog else "DERROTA")
            # Devolve o jogador vencedor.
            return jogador_atual

        # Seleciona o jogador que não jogou para jogar a seguir.
        jogador_atual = -jogador_atual

    # Como já foi verificado se o último jogador a jogar ganhou,
    # a este ponto do código, isto indica que o jogo ficou empatado.
    print("EMPATE")
    return 0


def eh_dimensao(arg):
    """
    eh_dimensao: argumento → booleano

    Recebe um argumento.
    Devolve True se o argumento corresponder a uma possível dimensão de um tabuleiro
    """
    return type(arg) == int and 2 <= arg <= 100


# Função Auxiliar
def eh_lvl(arg):
    """
    eh_lvl: argumento → booleano

    Devolve True se o argumento for uma cadeia de carateres
    e se corresponde a uma das estratégias indicadas: facil, normal ou dificil
    """
    return isinstance(arg, str) and arg in ('facil', 'normal', 'dificil')


# Função Auxiliar
def eh_k(arg):
    """
    eh_k: argumento → booleano

    Devolve True se o argumento for um inteiro positivo k,
    que poderá corresponder a um número de pedras consecutivas num tabuleiro.
    Caso contrário devolve False.
    """
    return type(arg) == int and arg > 0


# Função Auxiliar
def eh_jog(arg):
    """
    eh_jog: argumento → booleano

    Devolve True se o argumento corresponder a um jogador.
    Caso contrário devolve False.
    """
    return type(arg) == int and arg in (-1, 1)


# Função Auxiliar
def posicao_central(tab):
    """
    posicao_central: tabuleiro → inteiro

    Recebe um tabuleiro.
    Devolve um inteiro representando a posição central,
    de acordo com o indicado no 2.1 Representação do Tabuleiro.
    """
    m, n = obtem_dimensao(tab)
    return (m // 2) * n + n // 2 + 1


# Função Auxiliar
def chebyshev(tab, p1, p2):
    """
    chebyshev: tabuleiro × posicao × posicao → inteiro

    Recebe um tabuleiro e duas posições do tabuleiro.
    Devolve um inteiro que representa a distância chebyshev
    entre as duas posições do tabuleiro.
    """
    l1 = qual_linha(tab, p1)
    c1 = qual_coluna(tab, p1)
    l2 = qual_linha(tab, p2)
    c2 = qual_coluna(tab, p2)

    return max(abs(l1 - l2), abs(c1 - c2))


# Função Auxiliar
def qual_coluna(tab, pos):
    """
    qual_coluna: tabuleiro × posicao → inteiro

    Recebe um tabuleiro e uma posicao do tabuleiro.
    Devolve o índice da coluna na qual está contida a posição recebida.
    """
    n = obtem_dimensao(tab)[1]
    # O resto da divisão da posição-1 pelo nº de colunas dá o nº da coluna onde esta se insere.
    return (pos - 1) % n


# Função Auxiliar
def qual_linha(tab, pos):
    """
    qual_coluna: tabuleiro × posicao → inteiro

    Recebe um tabuleiro e uma posicao do tabuleiro.
    Devolve o índice da linha na qual está contida a posição recebida.
    """
    n = obtem_dimensao(tab)[1]
    # A divisão inteira da posição pelo nº de colunas dá o nº de filas (cada fila tem ncolunas) onde esta se insere.
    # Como as posições começam no 1 e os índices no 0, para efeiros de cáculo subtrai-se 1.
    return (pos - 1) // n
