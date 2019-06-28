# Programa: Jogo da Velha

#Introdução
print("JOGO DA VELHA")
nome = input("Qual o seu nome?")
print("Seja Bem-Vindo", nome,".", "Vamos começar a jogar! Leia as regras a seguir:")
print("1. O usuários irá escolher uma linha (0, 1 ou 2 para jogar;")
print("2. O usuário irá escolher uma coluna (0,1 ou 2) para jogar.")

#Início do programa
# Criando a matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def mostra(matriz):
    for linha in matriz:
        print(linha)

# Finalizar o jogo:
def conta0(matriz):
    cont = 0
    for linha in matriz:
        for elemento in linha:
            if (elemento == 0):
                cont = cont + 1
    return (cont)
mostra(matriz)

# Condicionais para ganhar o jogo:
linha0 = matriz[0][0] == 2 and matriz[0][1] == 2 and matriz[0][2] == 2
linha1 = matriz[1][0] == 2 and matriz[1][1] == 2 and matriz[1][2] == 2
linha2 = matriz[2][0] == 2 and matriz[2][1] == 2 and matriz[2][2] == 2
coluna0 = matriz[0][0] == 2 and matriz[1][0] == 2 and matriz[2][0] == 2
coluna1 = matriz[0][1] == 2 and matriz[1][1] == 2 and matriz[2][1] == 2
coluna2 = matriz[0][2] == 2 and matriz[1][2] == 2 and matriz[2][2] == 2
diagonalprincipal = matriz[0][0] == 2 and matriz[1][1] == 2 and matriz[2][2] == 2
diagonalsecundaria = matriz[1][2] == 2 and matriz[1][1] == 2 and matriz[2][0] == 2

# Posições vazias na Matriz
lc00 = matriz[0][0] != 0
lc01 = matriz[0][1] != 0
lc02 = matriz[0][2] != 0
lc10 = matriz[1][0] != 0
lc11 = matriz[1][1] != 0
lc12 = matriz[1][2] != 0
lc20 = matriz[2][0] != 0
lc21 = matriz[2][1] != 0
lc22 = matriz[2][2] != 0

# Quando a máquina vence ou empata:
def verifica(matriz):
    aux = False
    jogadores = [1, 2]
    for jog in jogadores:
        # Linhas
        if (matriz[0][0] == jog and matriz[0][1] == jog and matriz[0][2] == jog):
            print("Jogador " + str(jog) + " ganhou")
            return (aux)
        elif (matriz[1][0] == jog and matriz[1][1] == jog and matriz[1][2] == jog):
            print("Jogador " + str(jog) + " ganhou")
            return (aux)
        elif (matriz[2][0] == jog and matriz[2][1] == jog and matriz[2][2] == jog):
            print("Jogador " + str(jog) + " ganhou")
            return (aux)
        ##
        # colunas
        elif (matriz[0][0] == jog and matriz[1][0] == jog and matriz[2][0] == jog):
            print("Jogador " + str(jog) + " ganhou")
            return (aux)
        elif (matriz[0][1] == jog and matriz[1][1] == jog and matriz[2][1] == jog):
            print("Jogador " + str(jog) + " ganhou")
            return (aux)
        elif (matriz[0][2] == jog and matriz[1][2] == jog and matriz[2][2] == jog):
            print("Jogador " + str(jog) + " ganhou")
            return (aux)
        # diagonal

        elif (matriz[0][0] == jog and matriz[1][1] == jog and matriz[2][2] == jog):
            print("Jogador " + str(jog) + " ganhou")
            return (aux)
        elif (matriz[0][2] == jog and matriz[1][1] == jog and matriz[2][0] == jog):
            print("Jogador " + str(jog) + " ganhou")
            return (aux)
    else:
        return (True)

# 1º jogoda (Usuário)

linha = int(input("Escolha uma linha(0, 1 ou 2):"))
if linha == 0:
    coluna = int(input("Escolha uma coluna(0,1 ou 2)"))
    if coluna == 0:
        matriz[0][0] = 1
    if coluna == 1:
        matriz[0][1] = 1
    if coluna == 2:
        matriz[0][2] = 1
if linha == 1:
    coluna = int(input("Escolha uma coluna(0,1 ou 2)"))
    if coluna == 0:
        matriz[1][0] = 1
    if coluna == 1:
        matriz[1][1] = 1
    if coluna == 2:
        matriz[1][2] = 1
if linha == 2:
    coluna = int(input("Escolha uma coluna(0,1 ou 2)"))
    if coluna == 0:
        matriz[2][0] = 1

    if coluna == 1:
        matriz[2][1] = 1
    if coluna == 2:
        matriz[2][2] = 1

print("Sua jogada foi:")
mostra(matriz)

# 1º jogada (Máquina)

if matriz[0][0] == 0:
    matriz[0][0] = 2
elif matriz[0][2] == 0:
    matriz[0][2] = 2
elif matriz[1][1] == 0:
    matriz[1][1] = 2
elif matriz[2][0] == 0:
    matriz[2][0] = 2
elif matriz[2][2] == 0:
    matriz[2][2] = 2
print("A máquina jogou:")
mostra(matriz)

# Usuário e Máquina jogando:
# Encerrar o jogo
parar = False
while not parar:
    for i in range(9):
        for j in range(9):
            if linha0 or linha1 or linha2 or coluna0 or coluna1 or coluna2 or diagonalprincipal or diagonalsecundaria:
                parar = True
                print("O vencedor foi: MAQUINA")
            if lc00 and lc01 and lc02 and lc02 and lc11 and lc12 and lc20 and lc21 and lc22:
                print("JOGO EMPATADO")
                parar = True
            # Usuário
            joglinha = int(input("Escolha uma linha(0,1 ou 2)"))
            if joglinha == 0:
                jogcoluna = int(input("Escolha uma coluna(0,1 ou 2)"))
                if jogcoluna == 0:
                    if matriz[0][0] == 0:
                        matriz[0][0] = 1
                    else:
                        print("Posição já ocupada! Jogue novamente:")
                if jogcoluna == 1:
                    if matriz[0][1] == 0:
                        matriz[0][1] = 1
                    else:
                        print("Posição já ocupada! Jogue novamente:")
                if jogcoluna == 2:
                    if matriz[0][2] == 0:
                        matriz[0][2] = 1
                    else:
                        print("Posição já ocupada! Jogue novamente:")
            elif joglinha == 1:
                jogcoluna = int(input("Escolha uma coluna(0,1 ou 2)"))
                if jogcoluna == 0:
                    if matriz[1][0] == 0:
                        matriz[1][0] = 1
                    else:
                        print("Posição já ocupada! Jogue novamente:")
                if jogcoluna == 1:
                    if matriz[1][1] == 0:
                        matriz[1][1] = 1
                    else:
                        print("Posição já ocupada! Jogue novamente:")
                if jogcoluna == 2:
                    if matriz[1][2] == 0:
                        matriz[1][2] = 1
                    else:
                        print("Posição já ocupada!Jogue novamente:")
            elif joglinha == 2:
                jogcoluna = int(input("Escolha uma coluna(0,1 ou 2)"))
                if jogcoluna == 0:
                    if matriz[2][0] == 0:
                        matriz[2][0] = 1
                    else:
                        print("Posição já ocupada! Jogue novamente:")
                if jogcoluna == 1:
                    if matriz[2][1] == 0:
                        matriz[2][1] = 1
                    else:
                        print("Posição já ocupada! Jogue novamente:")
                if jogcoluna == 2:
                    if matriz[2][2] == 0:
                        matriz[2][2] = 1
                    else:
                        print("Posição já ocupada! Jogue novamente:")

            print("Sua jogada foi:")
            mostra(matriz)
# Máquina
# Estrátegia

            if matriz[0][0] == 0:
                matriz[0][0] = 2
            elif matriz[0][2] == 0:
                matriz[0][2] = 2
            elif matriz[1][1] == 0:
                matriz[1][1] = 2
            elif matriz[2][0] == 0:
                matriz[2][0] = 2
            elif matriz[2][2] == 0:
                matriz[2][2] = 2
            elif matriz[0][1] == 0:
                matriz[0][1] = 2
            elif matriz[1][0] == 0:
                matriz[1][0] = 2
            elif matriz[1][2] == 0:
                matriz[1][2] = 2
            elif matriz[2][1] == 0:
                matriz[2][1] = 2
            print("A máquina jogou:")
            mostra(matriz)
#Evitar que o usuário ganhe:
# Linha 0
            if matriz[0][0] == 1 and matriz[0][1] == 1:
                matriz[0][2] = 2
            elif matriz[0][1] == 1 and matriz[0][2] == 1:
                matriz[0][0] = 2
            elif matriz[0][2] == 1 and matriz[0][0] == 1:
                matriz[0][1] = 2
# Linha 1
            elif matriz[1][0] == 1 and matriz[1][1] == 1:
                matriz[1][2] = 2
            elif matriz[1][1] == 1 and matriz[1][2] == 1:
                matriz[1][0] = 2
            elif matriz[1][2] == 1 and matriz[1][0] == 1:
                matriz[1][1] = 2
# Linha 2
            elif matriz[2][0] == 1 and matriz[2][1] == 1:
                matriz[2][2] = 2
            elif matriz[2][1] == 1 and matriz[2][2] == 1:
                matriz[2][0] = 2
            elif matriz[2][2] == 1 and matriz[2][0] == 1:
                matriz[2][1] = 2
# Coluna 0
            elif matriz[0][0] == 1 and matriz[1][0] == 1:
                matriz[2][0] = 2
            elif matriz[1][0] == 1 and matriz[2][0] == 1:
                matriz[0][0] = 2
            elif matriz[2][0] == 1 and matriz[0][0] == 1:
                matriz[1][0] = 2
# Coluna 1
            elif matriz[0][1] == 1 and matriz[1][1] == 1:
                matriz[2][1] = 2
            elif matriz[1][1] == 1 and matriz[2][1] == 1:
                matriz[0][1] = 2
            elif matriz[2][1] == 1 and matriz[0][1] == 1:
                matriz[1][1] = 2
# Coluna 2
            elif matriz[0][2] == 1 and matriz[1][2] == 1:
                matriz[2][2] = 2
            elif matriz[1][2] == 1 and matriz[2][2] == 1:
                matriz[0][2] = 2
            elif matriz[2][2] == 1 and matriz[0][1] == 1:
                matriz[1][2] = 2
# Diagonal Principal
            elif matriz[0][0] == 1 and matriz[1][1] == 1:
                matriz[2][2] = 2
            elif matriz[1][1] == 1 and matriz[2][2] == 1:
                matriz[0][0] = 2
            elif matriz[2][2 == 1] and matriz[0][0] == 1:
                matriz[1][1] = 2
 # Diagonal Secundária
            elif matriz[0][2] == 1 and matriz[1][1] == 1:
                matriz[2][0] = 2
            elif matriz[1][1] == 1 and matriz[2][0] == 1:
                matriz[0][2] = 2
            elif matriz[2][0] == 1 and matriz[0][2] == 1:
                matriz[1][1] = 2
# Finalizando a partida:
            if (not verifica(matriz)):
                print("Maquina ganhou")
                print( ("FIM DE JOGO"))
                raise ValueError
            if (conta0(matriz) == 0):
                print("EMPATE")
                print("FIM DE JOGO")
                raise ValueError

#Fim do programa
raise ValueError
