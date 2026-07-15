from flask import render_template


class AreaMembroController:

    def pagina_inicial(self):

        return render_template("area_membro.html")
