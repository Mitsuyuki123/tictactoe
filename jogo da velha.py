matriz = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
for vetor in matriz: # Print each array in the array_of_arrays separately <- ideia do chatGPT
        print(vetor)

def teste_vitoria_X():
    for coluna in range(0,3):
        if all(matriz[coluna][linha] == "X" for linha in range(0,3)):
            print("fim de jogo")
            return True
    for linha in range(0,3):
        if all(matriz[coluna][linha] == "X" for coluna in range(0,3)):
            print("fim de jogo")
            return True
    if all(matriz[diag][diag] == "X" for diag in range(0,3)):
        print("fim de jogo")
        return True
    if matriz[0][2]=="X" and matriz[1][1]=="X" and matriz[2][0]=="X":
        print("fim de jogo")
        return True
    return False
def teste_vitoria_O():
    for coluna in range(0,3):
        if all(matriz[coluna][linha] == "O" for linha in range(0,3)):
            print("fim de jogo")
            return True
    for linha in range(0,3):
        if all(matriz[coluna][linha] == "O" for coluna in range(0,3)):
            print("fim de jogo")
            return True
    if all(matriz[diag][diag] == "O" for diag in range(0,3)):
        print("fim de jogo")
        return True 
    if matriz[0][2]=="O" and matriz[1][1]=="O" and matriz[2][0]=="O":
        print("fim de jogo")
        return True
    return False
vitoria = False
while not vitoria:
    valido_x=False
    while not valido_x:
        jogada_linha = int(input("Jogador 1, digite a linha da sua jogada(1,2,3): "))
        jogada_coluna = int(input("Jogador 1, digite a coluna da sua jogada(1,2,3): "))
        if 1<=jogada_linha<=3 and 1<=jogada_coluna<=3:
            if matriz[jogada_linha-1][jogada_coluna-1] == "-":
                matriz[jogada_linha-1][jogada_coluna-1] = "X"
                valido_x=True
            else:
                print("Jogada inválida! Tente novamente em uma coordenada vazia.")
        else:
            print("Jogada inválida! Tente um número entre 1 e 3.")
    for vetor in matriz:
        print(vetor)
    if teste_vitoria_X():
        print("Jogador 1 venceu!")
        vitoria = True
        break  # Exit the loop if there's a winner <- ideia do chatGPT
    valido_o=False
    while not valido_o:
        jogada_linha2 = int(input("Jogador 2, digite a linha da sua jogada(1,2,3): "))
        jogada_coluna2 = int(input("Jogador 2, digite a coluna da sua jogada(1,2,3): "))
        if 1<=jogada_linha2<=3 and 1<=jogada_coluna2<=3:
            if matriz[jogada_linha2-1][jogada_coluna2-1] == "-":
                matriz[jogada_linha2-1][jogada_coluna2-1] = "O"
                valido_o=True
            else:
                print("Jogada inválida! Tente novamente em uma coordenada vazia.")
        else:
            print("Jogada inválida! Tente um número entre 1 e 3.")
    for vetor in matriz:
        print(vetor)
    if teste_vitoria_O():
        print("Jogador 2 venceu!")
        vitoria = True
        break  # Exit the loop if there's a winner <- ideia do chatGPT