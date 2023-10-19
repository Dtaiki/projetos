import os
import pandas as pd


def calculos(coeficiente, usuario):
    coeficiente = round(coeficiente, 3)
    medidas = tabela.loc[tabela["Coeficiente"] == coeficiente]
    pass
    ideal = medidas.iloc[0].tolist()
    medida = [ideal[n + 1] - usuario[n] for n in range(8)]
    return ideal, medida


def impressao(ideal, medida):
    membros = [
        "Pescoço",
        "Bíceps",
        "Antebraço",
        "Peito",
        "Cintura",
        "Quadris",
        "Coxas",
        "Panturrilha",
    ]
    print(f"Membro{' ' * 9}Medida Ideal{' ' * 4}Quanto Falta")
    for x in range(8):
        print(
            f"{membros[x]}:{' ' * (17 - len(membros[x]))} {ideal[x+1]}{' ' * (13 - len(str(ideal[x+1])))}  {medida[x]:+,.01f}cm"
        )


os.system("cls")
pasta = os.getcwd()
tabela = pd.read_csv(f"{pasta}tabela.csv", sep="\t")
tabela = tabela.replace(",", ".", regex=True)
tabela = tabela.astype(float)

print(
    "Esse programa compara as medidas do seu corpo com as medidas ideais de um corpo masculino.\n"
)
altura = float(input("Digite sua altura(cm): "))
peso = float(input("Peso(Kg): "))
pescoco = float(input("Pescoço(cm): "))
biceps = float(input("Bíceps(cm): "))
antebraco = float(input("Antebraço(cm): "))
peito = float(input("Peito(cm): "))
cintura = float(input("Cintura(cm): "))
quadris = float(input("Quadris(cm): "))
coxas = float(input("Coxas(cm): "))
panturrilha = float(input("Panturrilha(cm): "))
usuario = [pescoco, biceps, antebraco, peito, cintura, quadris, coxas, panturrilha]

ideal, medida = calculos(peso / altura, usuario)
impressao(ideal, medida)
