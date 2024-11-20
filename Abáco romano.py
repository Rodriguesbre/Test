import tkinter as tk

class AbacoRomano:
    def __init__(self, master):
        self.master = master
        master.title("Ábaco Romano")

        self.valores = [1000, 500, 100, 50, 10, 5, 1]
        self.barras = []

        # Criar barras do ábaco
        for valor in self.valores:
            barra = tk.Frame(master)
            barra.pack(pady=5)
            self.barras.append((barra, valor))

            # Adicionar botões para incrementar e decrementar
            btn_incrementar = tk.Button(barra, text=f"+ {valor}", command=lambda v=valor: self.adicionar(v))
            btn_incrementar.pack(side=tk.LEFT)

            btn_decrementar = tk.Button(barra, text=f"- {valor}", command=lambda v=valor: self.remover(v))
            btn_decrementar.pack(side=tk.LEFT)

            self.contador_label = tk.Label(barra, text="0")
            self.contador_label.pack(side=tk.LEFT)

            # Inicializar contagem
            self.contagem = 0

    def adicionar(self, valor):
        self.contagem += valor
        self.atualizar_contador()

    def remover(self, valor):
        if self.contagem >= valor:
            self.contagem -= valor
        self.atualizar_contador()

    def atualizar_contador(self):
        for barra, valor in self.barras:
            barra.children['!label'].config(text=str(self.contagem))

if __name__ == "__main__":
    root = tk.Tk()
    abaco = AbacoRomano(root)
    root.mainloop()