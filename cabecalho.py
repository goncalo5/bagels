import random
 
def VerificaEntrada(num):
    """
    Retorna um booleano dizendo se a entrada e valida
    ou nao, tendo em vista o numero de digitos
    True --> Entrada Valida
    False --> Entrada Invalida
    """
    if num > 100 and num < 9999:
        return True
    return False
 
def GeraSecretNum():
    '''
    Funcao que gera e retorna o numero secreto
    E a lista contendo cada um de seus digitos
    Exemplo
    secretNum = 1783
    list_num = [1,7,8,3]
    OBS: O NUMERO NAO PODE TER DIGITOS REPETIDOS
    '''
    '''
    numeros = list(range(10))
    secretNum = 0
 
    while numeros[0] == 0:
        random.shuffle(numeros)
     
    for i in range(4):
        dig = numeros[i]
        secretNum += dig*(10**(3-i))
 
    return secretNum, numeros[:4]
    '''
    algarismos = list(range(10))
    secretNum, list_num = 0, []
    for i in range(3, -1, -1): #i=3, 2, 1, 0  ajuda o exponencial
        num = random.choice(algarismos)
        secretNum += num * 10**i
        list_num.append(num)
        algarismos.remove(num)
    return secretNum, list_num

         
def GeraDicas(num, secretNum, secretNumList):
    """
    Recebe o numero escolhido e o numero secreto
    e gera uma lista contendo as dicas a serem
    colocadas.
    Codigo
    --> 0 = Bagels
    --> 1 = Pico
    --> 2 = Fermi
 
    Retorna uma lista vazia caso os dois numeros sejam iguais
    """
    nums, dica = [], []
    for i in range(4):
        nums.append(int(str(num)[i]))
    for i, n in enumerate(nums):
        for j, s in enumerate(secretNumList):
            if n == secretNumList[j] and i == j:
                dica.append(2)
                break
            elif n == secretNumList[j]:
                dica.append(1)
                break
        
    if len(dica) == 0: dica.append(0)
    dica.sort()
    if sum(dica) == 8: dica = []
    return dica
            
    
    
    
    
    
    
    