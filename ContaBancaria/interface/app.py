import tkinter as tk
from tkinter import messagebox
import ContaBancaria.classes.banco
import ContaBancaria.classes.cliente
import ContaBancaria.classes.conta


class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Banco")

        self.banco = ContaBancaria.classes.banco.Banco()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Nome do Cliente").grid(row=0, column=0, sticky='e', padx=10, pady=5)
        self.entry_nome_cliente = tk.Entry(self.root)
        self.entry_nome_cliente.grid(row=0, column=1, sticky='ew', padx=10, pady=5)

        tk.Label(self.root, text="Idade do Cliente").grid(row=1, column=0, sticky='e', padx=10, pady=5)
        self.entry_idade_cliente = tk.Entry(self.root)
        self.entry_idade_cliente.grid(row=1, column=1, sticky='ew', padx=10, pady=5)

        tk.Button(self.root, text="Cadastrar Cliente", command=self.cadastrar_cliente).grid(row=2, column=1, sticky='e', padx=10, pady=5)

        tk.Label(self.root, text="Agência").grid(row=3, column=0, sticky='e', padx=10, pady=5)
        self.entry_agencia = tk.Entry(self.root)
        self.entry_agencia.grid(row=3, column=1, sticky='ew', padx=10, pady=5)

        tk.Label(self.root, text="Número da Conta").grid(row=4, column=0, sticky='e', padx=10, pady=5)
        self.entry_numero_conta = tk.Entry(self.root)
        self.entry_numero_conta.grid(row=4, column=1, sticky='ew', padx=10, pady=5)

        tk.Label(self.root, text="Saldo Inicial").grid(row=5, column=0, sticky='e', padx=10, pady=5)
        self.entry_saldo = tk.Entry(self.root)
        self.entry_saldo.grid(row=5, column=1, sticky='ew', padx=10, pady=5)

        tk.Label(self.root, text="Tipo de Conta (poupanca/corrente)").grid(row=6, column=0, sticky='e', padx=10, pady=5)
        self.entry_tipo_conta = tk.Entry(self.root)
        self.entry_tipo_conta.grid(row=6, column=1, sticky='ew', padx=10, pady=5)

        tk.Button(self.root, text="Criar Conta", command=self.criar_conta).grid(row=7, column=1, sticky='e', padx=10, pady=5)

        tk.Label(self.root, text="Valor").grid(row=8, column=0, sticky='e', padx=10, pady=5)
        self.entry_valor = tk.Entry(self.root)
        self.entry_valor.grid(row=8, column=1, sticky='ew', padx=10, pady=5)

        tk.Button(self.root, text="Depositar", command=self.depositar).grid(row=9, column=1, sticky='e', padx=10, pady=5)
        tk.Button(self.root, text="Sacar", command=self.sacar).grid(row=10, column=1, sticky='e', padx=10, pady=5)

        self.lbl_saldo = tk.Label(self.root, text="Saldo: R$ 0.00", font=("Arial", 14))
        self.lbl_saldo.grid(row=11, column=1, sticky='e', padx=10, pady=5)

        self.root.grid_columnconfigure(1, weight=1)

    def cadastrar_cliente(self):
        nome = self.entry_nome_cliente.get()
        idade = self.entry_idade_cliente.get()
        if not nome or not idade:
            messagebox.showerror("Erro", "Nome e idade são obrigatórios")
            return

        cliente = ContaBancaria.classes.cliente.Cliente(nome, int(idade))
        self.banco.inserir_clientes(cliente)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso")

    def criar_conta(self):
        agencia = self.entry_agencia.get()
        numero = self.entry_numero_conta.get()
        saldo = self.entry_saldo.get()
        tipo = self.entry_tipo_conta.get()

        if not agencia or not numero or not saldo or tipo not in ["poupanca", "corrente"]:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente")
            return

        saldo = float(saldo)
        if tipo == "poupanca":
            conta = ContaBancaria.classes.conta.ContaPoupanca(agencia, numero, saldo)
        else:
            conta = ContaBancaria.classes.conta.ContaCorrente(agencia, numero, saldo)

        self.banco.inserir_conta(conta)

        nome = self.entry_nome_cliente.get()
        cliente = next((c for c in self.banco.clientes if c.nome == nome), None)
        if cliente:
            cliente.inserir_conta(conta)
        else:
            messagebox.showerror("Erro", "Cliente não encontrado")
            return

        messagebox.showinfo("Sucesso", "Conta criada com sucesso")

    def depositar(self):
        valor = self.entry_valor.get()
        if not valor:
            messagebox.showerror("Erro", "Digite o valor para depósito")
            return

        valor = float(valor)
        cliente = self.banco.clientes[0] if self.banco.clientes else None
        if cliente and cliente.conta:
            cliente.conta.depositar(valor)
            self.atualizar_saldo(cliente.conta)
        else:
            messagebox.showerror("Erro", "Nenhuma conta encontrada para o cliente")

    def sacar(self):
        valor = self.entry_valor.get()
        if not valor:
            messagebox.showerror("Erro", "Digite o valor para saque")
            return

        valor = float(valor)
        cliente = self.banco.clientes[0] if self.banco.clientes else None
        if cliente and cliente.conta:
            cliente.conta.sacar(valor)
            self.atualizar_saldo(cliente.conta)
        else:
            messagebox.showerror("Erro", "Nenhuma conta encontrada para o cliente")

    def atualizar_saldo(self, conta):
        self.lbl_saldo.config(text=f"Saldo: R$ {conta.saldo:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()
