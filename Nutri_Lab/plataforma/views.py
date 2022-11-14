import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from .utils import paciente_is_valid, patient_data_is_valid, refeicao_is_valid
from .models import DadosPaciente, Opcao, Paciente, Refeicao
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url="logar")
def pacientes(request):
    if request.method == "GET":
        pacientes = Paciente.objects.filter(nutri=request.user)
        return render(request, "pacientes.html", {"pacientes": pacientes})
    elif request.method == "POST":
        nome = request.POST.get("nome")
        sexo = request.POST.get("sexo")
        idade = request.POST.get("idade")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")

        if not paciente_is_valid(request, nome, sexo, idade, email, telefone):
            return redirect("pacientes")

        try:
            paciente = Paciente(
                nome=nome,
                sexo=sexo,
                idade=idade,
                email=email,
                telefone=telefone,
                nutri=request.user,
            )

            paciente.save()
            messages.add_message(
                request, constants.SUCCESS, "Paciente cadastrado com sucesso"
            )
            return redirect("pacientes")
        except:
            messages.add_message(request, constants.ERROR, "Erro interno do sistema")
            return redirect("pacientes")


@login_required(login_url="logar")
def dados_paciente_listar(request):
    if request.method == "GET":
        pacientes = Paciente.objects.filter(nutri=request.user)
        return render(request, "dados_paciente_listar.html", {"pacientes": pacientes})


@login_required(login_url="logar")
def dados_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, "Esse paciente não é seu")
        return redirect("/dados_pacientes/")

    if request.method == "GET":
        dados_paciente = DadosPaciente.objects.filter(paciente=paciente)
        return render(
            request,
            "dados_paciente.html",
            {"paciente": paciente, "dados_paciente": dados_paciente},
        )
    elif request.method == "POST":
        peso = request.POST.get("peso")
        altura = request.POST.get("altura")
        gordura = request.POST.get("gordura")
        musculo = request.POST.get("musculo")

        hdl = request.POST.get("hdl")
        ldl = request.POST.get("ldl")
        colesterol_total = request.POST.get("ctotal")
        trigliceridios = request.POST.get("triglicerídios")

        if not patient_data_is_valid(
            request,
            peso,
            altura,
            gordura,
            musculo,
            hdl,
            ldl,
            colesterol_total,
            trigliceridios,
        ):
            return redirect(f"/dados_paciente/{id}")

        paciente = DadosPaciente(
            paciente=paciente,
            data=datetime.datetime.now(),
            peso=peso,
            altura=altura,
            percentual_gordura=gordura,
            percentual_musculo=musculo,
            colesterol_hdl=hdl,
            colesterol_ldl=ldl,
            colesterol_total=colesterol_total,
            trigliceridios=trigliceridios,
        )

        paciente.save()

        messages.add_message(request, constants.SUCCESS, "Dados cadastrado com sucesso")
        return redirect(f"/dados_paciente/{id}")


@login_required(login_url="logar")
@csrf_exempt
def grafico_peso(request, id):
    paciente = Paciente.objects.get(id=id)
    dados = DadosPaciente.objects.filter(paciente=paciente).order_by("data")

    pesos = [dado.peso for dado in dados]
    labels = list(range(len(pesos)))
    data = {"peso": pesos, "labels": labels}
    return JsonResponse(data)


def plano_alimentar_listar(request):
    if request.method == "GET":
        pacientes = Paciente.objects.filter(nutri=request.user)
        return render(request, "plano_alimentar_listar.html", {"pacientes": pacientes})


def plano_alimentar(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, "Esse paciente não é seu")
        return redirect("/dados_paciente/")

    refeicoes = Refeicao.objects.filter(paciente=paciente).order_by("horario")
    opcoes = Opcao.objects.all()
    if request.method == "GET":
        return render(
            request,
            "plano_alimentar.html",
            {"paciente": paciente, "refeicoes": refeicoes, "opcoes": opcoes},
        )


def refeicao(request, id_paciente):
    paciente = get_object_or_404(Paciente, id=id_paciente)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, "Esse paciente não é seu")
        return redirect("/dados_paciente/")

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        horario = request.POST.get("horario")
        carboidratos = request.POST.get("carboidratos")
        proteinas = request.POST.get("proteinas")
        gorduras = request.POST.get("gorduras")

        if not refeicao_is_valid(
            request, titulo, horario, carboidratos, proteinas, gorduras
        ):
            return redirect(f"/plano_alimentar/{id_paciente}")

        try:
            r1 = Refeicao(
                paciente=paciente,
                titulo=titulo,
                horario=horario,
                carboidratos=carboidratos,
                proteinas=proteinas,
                gorduras=gorduras,
            )

            r1.save()

            messages.add_message(request, constants.SUCCESS, "Refeição cadastrada")
            return redirect(f"/plano_alimentar/{id_paciente}")
        except:
            messages.add_message(
                request,
                constants.ERROR,
                "Erro interno ou os valores digitados são inválidos",
            )
            return redirect(f"/plano_alimentar/{id_paciente}")


def opcao(request, id_paciente):
    if request.method == "POST":
        id_refeicao = request.POST.get("refeicao")
        imagem = request.FILES.get("imagem")
        descricao = request.POST.get("descricao")

        try:
            o1 = Opcao(refeicao_id=id_refeicao, imagem=imagem, descricao=descricao)

            o1.save()

            messages.add_message(request, constants.SUCCESS, "Opção cadastrada")
            return redirect(f"/plano_alimentar/{id_paciente}")
        except:
            messages.add_message(request, constants.ERROR, "Erro Interno")
            return redirect(f"/plano_alimentar/{id_paciente}")
