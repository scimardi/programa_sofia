import os, datetime
from peewee import *

arq = 'basquete.db'

db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Jogador(BaseModel):
    nome = CharField()
    idade = IntegerField()
    num_camisa = IntegerField()
    altura = FloatField()
    pontuacao = IntegerField()
    def __str__(self):
        return self.nome+", "+str(self.idade)+", "+str(self.num_camisa)+", "+str(self.altura)+", "+str(self.pontuacao)

class Tecnico(BaseModel):
    nome = CharField()
    idade = IntegerField()
    carreira = CharField()
    def __str__(self):
        return self.nome+", "+str(self.idade)+", "+self.carreira

class Vitorias_Derrotas(BaseModel):
    qtd_vit = IntegerField()
    qtd_der = IntegerField()
    def __str__(self):
        return str(self.qtd_vit)+", "+str(self.qtd_der)

class Equipe(BaseModel):
    nome = CharField()
    ano_fund = IntegerField()
    pais_orig = CharField()
    tecnico = ForeignKeyField(Tecnico)
    vit_der = ForeignKeyField(Vitorias_Derrotas)
    jogadores = ManyToManyField(Jogador)
    def __str__(self):
        jogadores = ""
        for a in self.jogadores:
            jogadores += str(a) + ""
        return self.nome+", "+str(self.ano_fund)+", "+self.pais_orig+", "+str(self.tecnico)+", "+str(self.vit_der)+", "+jogadores
    

class Arena(BaseModel):
    nome = CharField()
    area = IntegerField()
    num_lugares = IntegerField()
    def __str__(self):
        return self.nome+", "+str(self.area)+", "+str(self.num_lugares)

class Arbitragem(BaseModel):
    nome = CharField()
    idade = IntegerField()
    federacao = CharField()
    def __str__(self):
        return self.nome+", "+str(self.idade)+", "+self.federacao

class Pontuacao(BaseModel):
    tiro_livre = IntegerField()
    arremesso_dg = IntegerField()
    arremesso_fg = IntegerField()
    def __str__(self):
        return str(self.tiro_livre)+", "+str(self.arremesso_dg)+", "+str(self.arremesso_fg)+", "+str(self.tiro_livre + self.arremesso_dg + self.arremesso_fg)

class Publico(BaseModel):
    torcedores_a = IntegerField()
    torcedores_b = IntegerField()
    def __str__(self):
        return str(self.torcedores_a)+", "+str(self.torcedores_b)

class Jogo(BaseModel):
    tempo = IntegerField()
    time_a = ForeignKeyField(Equipe)
    time_b = ForeignKeyField(Equipe)
    pont_a = ForeignKeyField(Pontuacao)
    pont_b = ForeignKeyField(Pontuacao)
    local = ForeignKeyField(Arena)
    arbitro = ForeignKeyField(Arbitragem)
    torcida = ForeignKeyField(Publico)
    def __str__(self):
        return str(self.tempo)+", "+str(self.time_a)+", "+str(self.time_b)+", "+str(self.pont_a)+", "+str(self.pont_b)+", "+str(self.local)+", "+str(self.arbitro)+", "+str(self.torcida)

class Campeonato(BaseModel):
    nome = CharField()
    colocacao = CharField()
    jogos = ManyToManyField(Jogo)
    def __str__(self):
        jogos = ""
        for a in self.jogos:
            jogos += str(a) + ""
        return self.nome+", "+self.colocacao+", " + jogos

if __name__ == "__main__":

    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([Jogador, Tecnico, Vitorias_Derrotas, Equipe, Equipe.jogadores.get_through_model(), 
        Arena, Arbitragem, Pontuacao, Publico, Jogo, Campeonato, Campeonato.jogos.get_through_model()])

    leandro = Jogador.create(nome = "Leandro", idade = 18, num_camisa = "18", altura = 1.75, pontuacao = 15)
    sofia = Jogador.create(nome = "Sofia", idade = 18, num_camisa = "10", altura = 1.63, pontuacao = 18)
    carlos = Jogador.create(nome = "Carlos", idade = 17, num_camisa = "11", altura = 1.73, pontuacao = 14)
    camila = Jogador.create(nome = "Camila", idade = 18, num_camisa = "9", altura = 1.53, pontuacao = 10)
    tec1 = Tecnico.create(nome = "Hylson", idade = 38, carreira = "time do IFC" ) 
    tec2 = Tecnico.create(nome = "Deivis", idade = 35, carreira = "nada")
    vd1 = Vitorias_Derrotas.create(qtd_vit = 48, qtd_der = 2)
    vd2 = Vitorias_Derrotas.create(qtd_vit = 2, qtd_der = 48)
    flabasquete = Equipe.create(nome = "FlaBasquete", ano_fund = 1919, pais_orig = "Brasil", tecnico = tec1, vit_der = vd1)
    corinthians = Equipe.create(nome = "Corinthians", ano_fund = 1928, pais_orig = "Brasil", tecnico = tec2, vit_der = vd2)
    arena = Arena.create (nome = "Arena Carioca 1", area = 1500, num_lugares = 16000)
    arbitro = Arbitragem.create(nome = "Renatinho", idade = 47, federacao = "FPB")
    pont1 = Pontuacao.create(tiro_livre = 19, arremesso_dg = 21, arremesso_fg = 16)
    pont2 = Pontuacao.create(tiro_livre = 19, arremesso_dg = 15, arremesso_fg = 15)
    pub = Publico.create(torcedores_a = 10000, torcedores_b = 6000)
    jogo = Jogo.create(tempo = 40, time_a = flabasquete, time_b = corinthians, pont_a = pont1, pont_b = pont2, local = arena, arbitro = arbitro, torcida = pub)
    campeonato = Campeonato.create(nome = "Campeonato Brasileiro de Basquete Masculino", colocacao = "Campeâo: FlaBasquete")

    flabasquete.jogadores.add(sofia)
    flabasquete.jogadores.add(carlos)
    corinthians.jogadores.add(leandro)
    corinthians.jogadores.add(camila)
    campeonato.jogos.add(jogo)

    print(campeonato)