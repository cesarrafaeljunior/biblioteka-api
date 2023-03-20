<h1 align="center">
  BiblioteKA - API
</h1>

<p align = "center">
A api BiblioteKA é uma api de gerenciamento de empréstimos de livros para bibliotecas, a api conta com 2 tipos de usuários, sendo eles colaboradores e estudantes.
</p>

<img src="https://i.imgur.com/ehNZ9nw.png"/>

## Tabela de Conteúdos

- [Visão Geral](#1-visão-geral)

- [Diagrama ER](#2-diagrama-er)

- [Documentação](#3-documentação)

- [Rodando localmente](#4-rodando-localmente)

URL base da aplicação:

https://biblioteka.onrender.com/

## 1. Visão Geral
Mapeando principais tecnologias do projeto

- **[Python](https://www.python.org/doc/)**

- **[djangorestframework](https://www.django-rest-framework.org/)**

- **[PostgreSQL](https://www.postgresql.org/)**

- **[Generic Views](https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/)**

- **[drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)**

## 2. Diagrama ER
[ Voltar ao topo ](#tabela-de-conteúdos)

- **[Diagrama](https://imgur.com/a/bDhkxqV)**

Diagrama ER representando as relções entre tabelas no banco de dados.

## 3. Documentação
[ Voltar ao topo ](#tabela-de-conteúdos)

Link referente a **[Documentação](https://biblioteka.onrender.com/api/docs/swagger-ui/)**

## 4. Rodando localmente
[ Voltar ao topo ](#tabela-de-conteúdos)

### 4.1 Crie seu ambiente virtual

use o comendo:

```bash
  python -m venv venv
```

### 4.2 Ative seu venv:

```bash
# linux:
source venv/bin/activate

# windows:
source venv/Scripts/activate
```

### 4.3 Baixe as dependencias do arquivo requirements.txt:

```bash
  pip install -r requirements.txt
```

### 4.4 Preenchas as chaves de acesso ao banco:
  crie um aquivo .env com as mesmas chaves do aquivo .env.exemple e preencha com os devidos dados.
  
### 4.5 Rode o projeto:

```bash
  python manage.py runserver
```
