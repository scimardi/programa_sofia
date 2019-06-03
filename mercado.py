class Produto():

    def __init__(self, cod, nome, preco):
        self.cod = cod
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return  "Código: " + str(self.cod) + "Produto: " + self.nome + " - R$" + str(self.preco)

class Item():

    def __init__(self, produto, quant):
        self.produto = produto
        self.quant = quant

    def __str__(self):
        return str(self.produto) + " - " + str(self.quant) + " unidade(s)"

class Carrinho():

    def __init__(self, data_comp):
        self.data_comp = data_comp
        self.lista_itens = []
    
    def add_lista(self, item):
        self.lista_itens.append(item)

    def __str__(self):
        itens = ""
        for s in self.lista_itens:
            itens = itens + str(s) + " -"
        return str(self.data_comp) + " - " + itens

if __name__ == "__main__":
    p1 = Produto(1, "Bolacha, não biscoito", 1.99)
    p2 = Produto(2, "Macarrão", 5.98)
    i1 = Item(p1, 3)
    i2 = Item(p2, 1)
    c = Carrinho("27/2/2001")
    c.add_lista(i1)
    c.add_lista(i2)

    print(c)