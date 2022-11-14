import re
from django.contrib import messages
from django.contrib.messages import constants
from .models import Paciente


def is_alpha_space(str):
    return all(char.isalpha() or char.isspace() for char in str)


def paciente_is_valid(request, nome, sexo, idade, email, telefone):
    if (
        len(nome.strip()) == 0
        or len(sexo.strip()) == 0
        or len(idade.strip()) == 0
        or len(email.strip()) == 0
        or len(telefone.strip()) == 0
    ):
        messages.add_message(request, constants.ERROR, "Preencha todos os campos")
        return False

    if not is_alpha_space(nome):
        messages.add_message(
            request, constants.ERROR, "Nome deve conter somente letras"
        )
        return False

    try:
        idade = int(idade)

        if idade <= 0:
            messages.add_message(request, constants.ERROR, "Digite uma idade válida")
            return False
    except:
        messages.add_message(request, constants.ERROR, "Idade inválida")
        return False

    pacientes = Paciente.objects.filter(email=email)

    if pacientes.exists():
        messages.add_message(
            request, constants.ERROR, "Já existe um paciente com esse E-mail"
        )
        return False

    return True


def refeicao_is_valid(request, titulo, horario, carboidratos, proteinas, gorduras):
    if (
        len(titulo.strip()) == 0
        or len(horario.strip()) == 0
        or len(carboidratos.strip()) == 0
        or len(proteinas.strip()) == 0
        or len(gorduras.strip()) == 0
    ):
        messages.add_message(request, constants.ERROR, "Preencha todos os campos")
        return False

    if re.search("[A-Z]", horario) or re.search("[a-z]", horario):
        messages.add_message(request, constants.ERROR, "Horário não pode conter letras")
        return False

    if (
        re.search("[A-Z]", carboidratos)
        or re.search("[a-z]", carboidratos)
        or re.search("[A-Z]", proteinas)
        or re.search("[a-z]", proteinas)
        or re.search("[A-Z]", gorduras)
        or re.search("[a-z]", gorduras)
    ):
        messages.add_message(
            request, constants.ERROR, "Macronutrientes precisam ser números"
        )
        return False

    try:
        carboidratos = carboidratos.replace(",", ".")
        carboidratos = float(carboidratos)

        proteinas = proteinas.replace(",", ".")
        proteinas = float(proteinas)

        gorduras = gorduras.replace(",", ".")
        gorduras = float(gorduras)
    except:
        messages.add_message(
            request,
            constants.ERROR,
            "Erro interno ou os valores digitados são inválidos",
        )
        return False

    if carboidratos < 0 or proteinas < 0 or gorduras < 0:
        messages.add_message(
            request, constants.ERROR, "Macronutrientes precisam ser números positivos"
        )
        return False

    return True


def patient_data_is_valid(
    request, peso, altura, gordura, musculo, hdl, ldl, colesterol_total, trigliceridios
):
    if (
        len(peso.strip()) == 0
        or len(altura.strip()) == 0
        or len(gordura.strip()) == 0
        or len(musculo.strip()) == 0
        or len(hdl.strip()) == 0
        or len(ldl.strip()) == 0
        or len(colesterol_total.strip()) == 0
        or len(trigliceridios.strip()) == 0
    ):
        messages.add_message(request, constants.ERROR, "Preencha todos os campos")
        return False

    if (
        is_alpha_space(peso)
        or is_alpha_space(altura)
        or is_alpha_space(musculo)
        or is_alpha_space(gordura)
        or is_alpha_space(hdl)
        or is_alpha_space(ldl)
        or is_alpha_space(colesterol_total)
        or is_alpha_space(trigliceridios)
    ):
        messages.add_message(
            request, constants.ERROR, "Os dados do paciente precisam ser números"
        )
        return False

    try:
        peso = peso.replace(",", ".")
        peso = float(peso)

        altura = int(altura)

        musculo = musculo.replace(",", ".")
        musculo = float(musculo)

        gordura = gordura.replace(",", ".")
        gordura = float(gordura)

        hdl = hdl.replace(",", ".")
        hdl = float(hdl)

        ldl = ldl.replace(",", ".")
        ldl = float(ldl)

        colesterol_total = colesterol_total.replace(",", ".")
        colesterol_total = float(colesterol_total)

        trigliceridios = trigliceridios.replace(",", ".")
        trigliceridios = float(trigliceridios)
    except:
        messages.add_message(
            request,
            constants.ERROR,
            "Erro interno ou os valores digitados são inválidos",
        )
        return False

    if (
        peso <= 0
        or altura <= 0
        or musculo <= 0
        or gordura <= 0
        or hdl <= 0
        or ldl <= 0
        or colesterol_total <= 0
        or trigliceridios <= 0
    ):
        messages.add_message(
            request,
            constants.ERROR,
            "Os dados do paciente não podem ser 0 ou valores abaixo",
        )
        return False

    return True
