import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import carregar_wordlist

LIMITE_PADRAO = 3

try:
    minha_wordlist = carregar_wordlist('wordlist.txt')
except Exception as e:
    print(f"Aviso: Não foi possível carregar a wordlist. {e}")
    minha_wordlist = set()

def possui_sequencia(senha):
    count = 1   
    for i in range(len(senha) - 1):
        if ord(senha[i+1]) - ord(senha[i]) == 1:
            count += 1
            if count >= LIMITE_PADRAO:
                return True
        else:
            count = 1
    return False

def possui_padrao_teclado(senha):
    linhas_teclado = ["qwertyuiop", "asdfghjklç", "zxcvbnm", "1234567890"]
    senha_low = senha.lower()
    for linha in linhas_teclado:
        for i in range(len(senha_low) - LIMITE_PADRAO + 1):
            pedaco = senha_low[i : i + LIMITE_PADRAO]
            if pedaco in linha or pedaco in linha[::-1]:
                return True
    return False

def possui_substituicao_leet(senha):
    mapeamento = {
        '4': 'a', '3': 'e', '1': 'i', '0': 'o', 
        '5': 's', '7': 't', '8': 'b', '@': 'a',
        '$': 's', '!': 'i'
    }
    senha_traduzida = senha.lower()
    detectou = False
    for char_leet, char_normal in mapeamento.items():
        if char_leet in senha_traduzida:
            senha_traduzida = senha_traduzida.replace(char_leet, char_normal)
            detectou = True
    return detectou, senha_traduzida

def eh_senha_comum(senha):
    _, traduzida = possui_substituicao_leet(senha)
    return senha.lower() in minha_wordlist or traduzida in minha_wordlist