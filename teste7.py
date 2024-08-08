numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

indice = 0

while indice < 5 and indice < len(numeros):
    print(numeros[indice])
    indice += 1

"""
O código imprime os primeiros cinco números da lista numeros, ou menos se a lista tiver menos de cinco elementos. 
O while verifica se o índice é menor que 5 e o comprimento da lista, imprimindo o número atual e incrementando o 
índice a cada iteração.
"""
