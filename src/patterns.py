LIMITE_PADRAO = 3

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

