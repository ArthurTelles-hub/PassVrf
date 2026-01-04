import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def carregar_wordlist(nome_arquivo='wordlist.txt'):
    caminho_completo = os.path.join(BASE_DIR, 'data', nome_arquivo)
    
    if not os.path.exists(caminho_completo):
        raise FileNotFoundError(f"Arquivo não encontrado em: {caminho_completo}")
        
    with open(caminho_completo, 'r', encoding='utf-8') as f:
        return {linha.strip().lower() for linha in f}