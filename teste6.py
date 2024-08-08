lista = ["joao", "ana", "joana", "joao", "ricardo", "joao"]
trocarJoaoPorMaria = "maria"

lista = [trocarJoaoPorMaria if nome == 'joao' else nome for nome in lista]

print(lista)