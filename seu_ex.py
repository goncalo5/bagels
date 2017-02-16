import random
 
def VerificaEntrada(num):
    """
    Retorna um booleano dizendo se a entrada e valida
    ou nao, tendo em vista o n�mero de d�gitos
    True --> Entrada Valida
    False --> Entrada Invalida
    """
    if num < 1000 or num >= 10000:
        return False
    else:
        return True
 
def GeraSecretNum():
    """
    Funcao que gera e retorna o n�mero secreto
    E a lista contendo cada um de seus d�gitos
    Exemplo
    secretNum = 1783
    list_num = [1,7,8,3]
    """
    numeros = list(range(10))
    secretNum = 0
 
    while numeros[0] == 0:
        random.shuffle(numeros)
     
    for i in range(4):
        dig = numeros[i]
        secretNum += dig*(10**(3-i))
 
    return secretNum, numeros[:4]
                 
 
def GeraDicas(num, secretNum, secretNumList):
    """
    Recebe o n�mero escolhido e o n�mero secreto
    e gera uma lista contendo as dicas a serem
    colocadas.
    C�digo
    --> 0 = Bagels
    --> 1 = Pico
    --> 2 = Fermi
 
    Retorna uma lista vazia caso os dois n�meros sejam iguais
    """
 
    if num == secretNum:
        return []
 
    dica = []
 
    for i in range(4):
        dig = num % 10
        if dig == secretNumList[3-i]:
            dica.append(2) #Fermi
        elif dig in secretNumList:
            dica.append(1) #Pico
        num //= 10
 
    if len(dica) == 0:
        dica.append(0) #Bagels
 
    dica.sort()
 
    return dica