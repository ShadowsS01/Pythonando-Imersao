from hashlib import sha256
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib import auth
from decouple import config
from autenticacao.models import Ativacao
from .utils import password_is_valid, email_html
import os
from django.conf import settings


def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "cadastro.html")
    elif request.method == "POST":
        username = request.POST.get("usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if (
            len(username.strip()) == 0
            or len(email.strip()) == 0
            or len(senha.strip()) == 0
            or len(confirmar_senha.strip()) == 0
        ):
            messages.add_message(request, constants.ERROR, "Preencha todos os campos")
            return redirect("cadastro")

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect("cadastro")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(
                request, constants.ERROR, "Já existe um usuário com esse username"
            )
            return redirect("cadastro")

        try:
            user = User.objects.create_user(
                username=username, email=email, password=senha, is_active=False
            )
            user.save()

            token = sha256(f"{username}{email}".encode()).hexdigest()
            ativacao = Ativacao(token=token, user=user)
            ativacao.save()

            path_template = os.path.join(
                settings.BASE_DIR,
                "autenticacao/templates/emails/cadastro_confirmado.html",
            )
            DOMAIN = config("DOMAIN_DEFAULT", default="127.0.0.1:8000")
            email_html(
                path_template,
                "Cadastro confirmado",
                [
                    email,
                ],
                username=username,
                link_ativacao=f"{DOMAIN}/auth/ativar_conta/{token}",
            )
            messages.add_message(
                request,
                constants.SUCCESS,
                "Usuário cadastrado com sucesso. Verifique seu e-mail para ativar sua conta",
            )
            return redirect("logar")
        except:
            messages.add_message(request, constants.ERROR, "Erro interno do sistema")
            return redirect("cadastro")


def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("usuario")
        senha = request.POST.get("senha")

        usuario = auth.authenticate(username=username, password=senha)

        if len(username.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, "Preencha todos os campos")
            return redirect("logar")
        elif not usuario:
            messages.add_message(
                request, constants.ERROR, "Username ou senha inválidos"
            )
            return redirect("logar")
        else:
            auth.login(request, usuario)
            return redirect("/pacientes/")


def sair(request):
    auth.logout(request)
    return redirect("logar")


def ativar_conta(request, token):
    token = get_object_or_404(Ativacao, token=token)
    if token.ativo:
        messages.add_message(request, constants.WARNING, "Essa token já foi usado")
        return redirect("logar")
    user = User.objects.get(username=token.user.username)
    user.is_active = True
    user.save()
    token.ativo = True
    token.save()
    messages.add_message(request, constants.SUCCESS, "Conta ativada com sucesso")
    return redirect("logar")


def handler404(request, exception, template_name="404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, "500.html")
    response.status_code = 500
    return response
