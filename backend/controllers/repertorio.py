from flask import render_template, jsonify

from backend.services.musica_service import MusicaService

class RepertorioController:

    def __init__(self):

        self.service = MusicaService()

    

    def listar_repertorio(self):

        repertorio = self.service.listar_repertorio()

        return render_template("repertorio.html" , repertorio = repertorio)

        #return render_template("repertorio.html")


    

    def adicionar_like(self, musica_id):

        status = self.service.adicionar_like(musica_id)


        if status :

            return jsonify({"status" : 200})
        
        else :
        
            return jsonify({"status" : 500})
    



    def adicionar_dislike(self, musica_id):

        status = self.service.adicionar_dislike(musica_id)


        if status :

            return jsonify({"status" : 200 , })
        
        else :

            return jsonify({"status" : 500})