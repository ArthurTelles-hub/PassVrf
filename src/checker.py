LIMITE_PADRAO = 3

def verifiar_comprimento(senha, minimo=8):
    return len(senha)>=minimo

def possui_maiuscula(senha):
    return any(char.isupper() for char in senha)

def possui_minuscula(senha):
    return any(char.islower() for char in senha)

def possui_numero(senha):
    return any(char.isdigit() for char in senha)

def possui_simbolo(senha):
    return any(not char.isalnum() for char in senha)

def tem_repeticao_seguida(senha):
    count = 1
    for i in range(len(senha) - 1):
        if senha[i] == senha[i+1]:
            count += 1
            if count >= LIMITE_PADRAO:
                return True
        else:
            count = 1
    return False

def tem_sequencia_fraca(senha):
    count = 1   
    for i in range(len(senha) - 1):
        if ord(senha[i+1]) - ord(senha[i]) == 1:
            count += 1
            if count >= LIMITE_PADRAO:
                return True
        else:
            count = 1
    return False

def tem_padrao_fraco(senha):
    return tem_repeticao_seguida(senha) or tem_sequencia_fraca(senha)