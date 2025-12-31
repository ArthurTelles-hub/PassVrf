import math

def calcular_entropia(senha):
    if not senha:
        return 0
    frequencias = {char: senha.count(char) for char in set(senha)}
    comprimento = len(senha)
    return -sum((count/comprimento) * math.log2(count/comprimento) for count in frequencias.values())

def classificar_entropia(senha):
    entropia = calcular_entropia

    if entropia < 2.0:
        return "Fraca"
    elif 2.0 <= entropia < 3.0:
        return "Média"
    else: 
        return "Forte"