from flask import Flask, json, jsonify
from flask import request
from classes import *
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return "jogo; <a href=/listar_jogo> listar o jogo</a>"

@app.route('/listar_jogo')
def listar():
    jogo = list(map(model_to_dict, Jogo.select()))
    response = jsonify({"lista": jogo})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run(debug=True, port=4999)