from flask import render_template, jsonify

from backend.services.musica_service import MusicaService

class RepertorioController:

    def __init__(self):

        self.service = MusicaService()

    

    def listar_repertorio(self):

        repertorio = self.service.listar_repertorio()

        return render_template("repertorio.html" , repertorio = repertorio)

        #return render_template("repertorio.html")


    

    def adicionar_like(self, id):

        self.service.adicionar_like(id)

        return jsonify({"status" : 200})
    



    def adicionar_dislike(self, id):

        self.service.adicionar_dislike(id)

        return jsonify({"status" : 200})