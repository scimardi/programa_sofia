from flask import Flask, render_template, request, redirect, session
from Filme import *

app = Flask("__name__")

app.config['SECRET_KEY'] = 'sofia'

@app.route ("/")
def iniciar():
    return render_template("inicio.html")

@app.route ("/listar_filmes")
def listar_filmes():
    return render_template ("listar_filmes.html", usuario=lista)
 
@app.route ("/form_login")
def form_login():
    return render_template ("form_login.html")

@app.route ("/login", methods='post')
def login():
    login = request.form['login']
    senha = request.form['senha']

    if login == 'sofia' and senha == 'sofia123':
        session['usuario'] = teste
        return redirect("/")
    else:
        return "Pessoa não encontarda"

@app.route ("/logout")
def logout():
    session.pop('usuario')
    return redirect("/")

@app.route ("/form_incluir_filme")
def form_incluir_filme():
    return render_template("form_incluir.html")

@app.route ("/incluir_filme", methods='post')
def incluir():
    cod = int(request.form["cod"])
    nome = request.form["nome"]
    genero = request.form["genero"]
    ano_lanc = request.form["ano_lanc"]

    lista.append(Filme(cod, nome, genero, ano_lanc))

    return redirect("iniciar.html")

@app.route ("/excluir")
def excluir():

    chave = int(request.agrs.get("cod"))

    for p in lista:
        if p.cod == chave:
            lista.remove(p)
    return redirect ("/listar_filmes")

@app.route ("/form_editar_filme")
def form_editar_filme():
     
    chave = request.agrs.get("cod")

    for p in lista:
        if p.cod == int(chave):
            return render_template ("form_editar_filme.html", achei=p)
    return "Pessoa não encontrada"

@app.route ("/editar_filme", methods='post')
def editar_filme():

    cod = int(request.form["cod"])
    nome = request.form["nome"]
    genero = request.form["genero"]
    ano_lanc = request.form["ano_lanc"]

    for i in range (len(lista)):
        if lista[i].cpf == cpf:
            lista[i] = Filme(cod, nome, genero, ano_lanc)
            return redirect ("/listar_pessoas")
    return "Não achei"

app.run()