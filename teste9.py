import requests


def obterDadosUsuarios():
    endpoint = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(endpoint)

    if response.status_code != 200:
        print(f"ocorreu esse codigo HTTP {response.status_code}")
        return []

    users = response.json()

    dadosUsers = []
    for user in users:
        nome = user["name"]
        nomeDeUsuario = user["username"]
        email = user["email"]
        rua = user["address"]['street']
        numeroEscritorio = user['address']['suite']

        dadosUsers.append({
            'name': nome,
            'username': nomeDeUsuario,
            'email': email,
            'rua': rua,
            "Escritorio": numeroEscritorio
        })

    return dadosUsers


dados = obterDadosUsuarios()
for dado in dados:
    print(dado)

"""
O código solicita informações de https://jsonplaceholder.typicode.com/users. A abordagem adotada por ele em 
relação ao JSON retornado e a extração de detalhes como nome, nome de usuário, e-mail, rua e número da suíte seria 
armazená-los em uma lista de dicionário. Se houver uma mensagem de erro na solicitação, ela retornará um código de 
erro HTTP; caso contrário, não retornará nada. Em seguida, imprime os dados de cada usuário.
"""