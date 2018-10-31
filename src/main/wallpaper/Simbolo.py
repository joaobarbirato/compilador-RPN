class Simbolo:
    def __init__(self, tipo, nome, valor):
        self.tipo = tipo
        self.nome = nome
        self.valor = valor


class TabelaSimbolo:
    def __init__(self, nome_tabela):
        self.nome_tabela = nome_tabela
        self.simbolos = []

    def addSimbolo(self, simbolo):
        self.simbolos.append(simbolo)

    def exist(self, novo_simbolo):
        for simbolo in self.simbolos:
            if simbolo.name == novo_simbolo.nome:
                return True
        return False


class ListaTabela:
    def __init__(self):
        self.tabelas = []

    def getTabela(self, token):
        for tabela in self.tabelas:
            if tabela.nome_tabela == token.getText():
                return tabela

    def addTabela(self, tabela):
        self.tabelas.append(tabela)

    def exist(self, token):
        for tabela in self.tabelas:
            if tabela.nome_tabela == token.getText():
                return True
        return False