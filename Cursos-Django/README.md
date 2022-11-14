# Cursos-Django

[![licence mit](https://img.shields.io/badge/licence-MIT-blue)](../LICENSE)

O projeto inicial foi desenvolvido durante o evento [Pystack Week 1.0](https://pythonando.com.br/).\
A proposta é criar um site para hospedar cursos.

## Tecnologias e libs utilizadas

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)

## Como executar o projeto

Para executar o projeto você precisa ter o [Python](https://www.python.org/) e o [Git](https://git-scm.com) instalados na sua maquina ou utilizar somente o [Docker](#9-executando-com-docker) junto ao [Git](https://git-scm.com). Você também precisará de um editor de código, eu utilizei o [VSCode](https://code.visualstudio.com).

### 1. Clone esse repositório

```bash
git clone https://github.com/ShadowsS01/Pythonando-Imersao.git
```

### 2. Acesse a pasta do projeto

```bash
cd Pythonando-Imersao/Cursos-Django
```

### 3. Ambiente virtual

Inicie um ambiente virtual e ative-o. Se não souber como, isso pode ajudar: <https://docs.python.org/pt-br/3/tutorial/venv.html#creating-virtual-environments>.

### 4. instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar variáveis de ambiente

Copie o arquivo `.env.example` neste diretório para `.env` *(que será ignorado pelo Git)*:

```bash
cp .env.example .env
```

Em seguida, defina cada variável em `.env`:

```env
SECRET_KEY=Digite_Uma_Senha_Secreta_aqui
DEBUG=True
```

### 6. Faça as migrações

```bash
python manage.py migrate
```

### 7. Crie um super usuário

```bash
python manage.py createsuperuser
```

### 8. Executando aplicação em modo de desenvolvimento

```bash
python manage.py runserver
```

- A aplicação inciará localmente - acesse: (<http://127.0.0.1:8000/>)

- Na URL depois do `8000/` dígite `auth/cadastro/` ou para acessar a área administrativa `admin/`.

- Na área administrativa coloque o usuário e senha criados na [etapa 7](#7-crie-um-super-usuário).

### 9. Executando com Docker

Tendo o [código fonte](#1-clone-esse-repositório) com as [variáveis definidas](#5-configurar-variáveis-de-ambiente), estando na [pasta certa](#2-acesse-a-pasta-do-projeto), com o [Docker](https://www.docker.com/) instalado, vamos subir o container:

```bash
docker compose up -d
```

*O container quando iniciado, inicia a aplicação Django!*

> ***Os passos abaixo serão necessário somente se você ainda não fez as migrações e a criação de um super user! Caso já tenha feito, a aplicação pode ser acessada em: <http://localhost:8080>***

Será necessário entrar no container via cli:

```bash
docker compose exec -it app zsh
```

> Agora você está dentro do container!

Será necessário fazer as migrações:

```bash
python manage.py migrate
```

A criação de um super user:

```bash
python manage.py createsuperuser
```

- Agora a aplicação está rodando em: <http://localhost:8080/>.

- Na URL depois do `8080/` dígite `auth/cadastro/` ou para acessar a área administrativa `admin/`.

## Créditos

> Projeto criado e desenvolvido no evento online e gratuito PystackWeek 1.0 da [Pythonando](https://github.com/Pythonando)

## Licença

Este projeto esta sobe a licença [MIT](../LICENSE)

🔝[Voltar para o topo](#cursos-django)
