class Aluno():

    def __init__(self, nome, curso, turma):
        self.nome = nome
        self.curso = curso
        self.turma = turma
    
    def __str__(self):
        return self.nome + " - " + self.curso + " " + str(self.turma)

class Professor():

    def __init__(self, nome, areas):
        self.nome = nome
        self.areas = areas

    def __str__(self):
        return self.nome + " " + str(self.areas)

class Projeto():

    def __init__(self, titulo, ano, lista_alunos, lista_profs):
        self.titulo = titulo
        self.ano = ano
        self.lista_alunos = lista_alunos
        self.lista_profs = lista_profs

    def __str__(self):
        s = self.titulo + " " + str(self.ano) + " "
        for i in self.lista_alunos:
            s += str(i)
        return s

class Periodicos():

    def __init__(self, editora, issn):
        self.editora = editora
        self.issn = issn

    def __str__(self):
        return self.editora + " " + str(self.issn)

class Eventos():

    def __init__(self, ano, local):
        self.ano = ano
        self.local = local

    def __str__(self):
        return str(self.ano) + " " + self.local


if __name__ == "__main__":
    l = Aluno("Gabriel Lima", "Informática", 302)
    t = Aluno("Thiago Hamburguer", "Informática", 302)
    b = Aluno("Benedito", "Informática", 302)
    k = Aluno("Kuglin ", "Informática", 302)
    r = Professor("Ricardo", ["web", "segurança"])
    a = Professor("Adriano", ["programação", "analista", "java"])
    e = Professor("Eder", ["matematica aplicada"])
    pj = Projeto("Projeto Drome", 2018, [l, t, b, k], [r, a, e])
    pd = Periodicos("ACM", 1234656)
    ev = Eventos(2018, "SBS")

    print(pj)
    print(pd)
    print(ev)
  