import requests


def contarTasks():
    endpoint = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(endpoint)

    if response.status_code != 200:
        print(f"Deu algum erro, codigo HTTP foi {response.status_code}")
        return

    tasks = response.json()

    completed = 0
    uncompleted = 0

    for task in tasks:
        if task["completed"]:
            completed += 1
        else:
            uncompleted += 1

    return completed, uncompleted


completed, uncompleted = contarTasks()


"""
O código faz uma requisição para o endpoint https://jsonplaceholder.typicode.com/todos usando requests.get(). Se a 
resposta for bem-sucedida (código HTTP 200), ele carrega os dados JSON e conta o número de tarefas completas e 
incompletas. O resultado é retornado como duas variáveis: completed e uncompleted. Se a requisição falhar, 
uma mensagem de erro é exibida com o código HTTP.
"""