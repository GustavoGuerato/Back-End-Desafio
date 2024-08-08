lista = ["Caneta Touch", "Adaptador Hub", "Placa de Captura", "Fone de Ouvido"]

novoProdutoLista = "Adaptador Bluethooth"
lista.append(novoProdutoLista)

produtoRemovido = lista.pop(0)

print("a Lista é", lista)
print("o item removido do FIFO foi ", produtoRemovido)
