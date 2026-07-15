from functools import wraps

from flask import session, redirect, url_for, g

from backend.services.auth_service import AuthService


def login_required(view):

    @wraps(view)
    def wrapper(*args, **kwargs):

        user_id = session.get("user_id")

        if user_id is None:

            return redirect(url_for("auth.exibir_login"))

        usuario = AuthService().buscar_por_id(user_id)

        if usuario is None:

            session.clear()

            return redirect(url_for("auth.exibir_login"))

        g.usuario = usuario

        return view(*args, **kwargs)

    return wrapper
