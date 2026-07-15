
from flask import render_template, request, redirect, url_for, flash, session

from backend.services.auth_service import AuthService


class AuthController:

    def __init__(self):

        self.service = AuthService()


    def exibir_login(self):

        return render_template("login.html")


    def login(self):

        email = request.form["email"]

        senha = request.form["senha"]

        usuario = self.service.autenticar(email, senha)

        if usuario is None:

            flash("Email ou senha inválidos.")

            return redirect(url_for("auth.exibir_login"))

        session["user_id"] = usuario.id

        session.permanent = True

        return redirect(url_for("solicitacao.listar_solicitacoes"))


    def logout(self):

        session.clear()

        return redirect(url_for("home.index"))
