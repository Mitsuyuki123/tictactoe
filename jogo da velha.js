matriz = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
vitoria=False
def teste_vitoria():
      for index in range(0,3):
        if (matriz[0][index] == matriz[1][index] and matriz[0][index] == matriz [2][index]):
            print (f"{matriz[index]} ganhou")
        elif (matriz[index][0] == matriz[index][1] and matriz[index][0] == matriz [index][2]):
            print (f"{matriz[x]} ganhou")
            vitoria=True
print(matriz)
while not vitoria:
    jogada_linha = input("digite a linha da sua jogada: ")
    jogada_coluna = input("digite a coluna da sua jogada: ")

    matriz[jogada_linha][jogada_coluna] = "X"

  