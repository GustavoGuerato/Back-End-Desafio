import json


try:
    with open("teste2.json", "r", encoding="utf-8") as file:
        teste2Json = json.load(file)

    precoProdutoB = None
    for produto in teste2Json["produtos"]:
        if produto["nome"] == "Produto B":
            precoProdutoB = produto["preço"]
            break

    if precoProdutoB is not None:
        print(f"O preço do Produto B é: R$ {precoProdutoB:.2f}")
    else:
        print("Produto B não foi localizado")

except FileNotFoundError:
    print("Erro: O arquivo 'teste2.json' não foi encontrado, tente novamente")
"""
Escolhi esse método por ser simples e fácil de entender. O código começa abrindo o arquivo teste2.json com open(), 
garantindo que ele seja fechado automaticamente após o uso. json.load() converte o JSON em um dicionário Python. Em 
seguida, o código busca pelo produto chamado “Produto B” na lista de produtos. Se o produto for encontrado, 
seu preço é armazenado e exibido; se não, é exibida uma mensagem informando que o produto não foi localizado. O 
tratamento de exceções com FileNotFoundError assegura que uma mensagem de erro seja mostrada caso o arquivo não seja 
encontrado. Outras abordagens poderiam adicionar verificações adicionais ou usar técnicas mais avançadas, 
mas para este caso, o código é claro e eficaz.
"""