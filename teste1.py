import json

try:
    with open("lojas.json", "r", encoding='utf-8') as file:
        lojasJson = json.load(file)

    for loja in lojasJson:
        print(f"A loja com Nome {loja['nome']}")
        print("Tem esses produtos com o preço acima de 30 reais:")
        for produtoAcimaDe30Reais in loja["produtos"]:
            if produtoAcimaDe30Reais["preço"] > 30.0:
                print(
                    f" - Produto: {produtoAcimaDe30Reais['nome']} | Preço: R$ {produtoAcimaDe30Reais['preço']:.2f}"
                )
        print()

except FileNotFoundError:
    print("Erro: O arquivo 'lojas.json' não foi encontrado, tente novamente")

"""
Explicação do codigo scolhi esse método pois é simples e compreensível. O código utiliza o método open() para 
abrir o arquivo com segurança, este método fechará automaticamente o arquivo após a leitura. json.load() converte 
JSON em um dicionario , o que é benéfico para manipulação de dados. Em seguida, o código percorre cada loja da 
lista, imprimindo o nome da loja e selecionando produtos com preço superior a R$ 30. O tratamento de exceções via 
FileNotFoundError é básico e envolve a exibição de uma mensagem simples que descreve a falta de um arquivo.
"""
