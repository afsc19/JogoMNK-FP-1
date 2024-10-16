# Projeto 1 FP 2024/2025
# Criado por André Cadete
# Aluno 114254 - ist1114254
# email: andre.cadete@tecnico.ulisboa.pt


import FP2425P1 as fp

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

fp.jogo_mnk((3,3,3), 1, 'dificil')