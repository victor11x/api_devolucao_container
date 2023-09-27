from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from datetime import datetime
from schema.error import *
from schema.devolucao import *
from model import Session, devolucoes
from flask_cors import CORS

info = Info(title="API Devolucao de Produtos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
devolucao_tag = Tag(name="Devolucao", description="Adição, visualização e remoção de produtos teve Devolucao")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')
  
@app.post('/devolucoes', tags=[devolucao_tag],
          responses={"200": DevolucaoViewSchema, "409": ErrorSchema, "400": ErrorSchema})


def add_devolucao(form: DevolucaoSchema):
    """Adiciona uma nova Devolucao de produto realizado pelo auditor fiscal à base de dados

    Retorna detalhes do Devolucao.
    """
    devolucao = Devolucoes(

            nome_produto = form.nome_produto,
            categoria = form.categoria,
            quantidade = form.quantidade,
            nome_cliente =form.nome_cliente,
            motivo =form.motivo,
            valor_total =form.valor_total,
        )
    try:

        session = Session()

        session.add(devolucao)

        session.commit()
        return apresenta_devolucao(devolucao), 200

    except IntegrityError as e:

        error_msg = "Produto foi auditodo de mesmo nome já foi salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:

        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400


# Metodo GET
@app.get('/devolucoes', tags=[devolucao_tag],
         responses={"200": ListagemDevolucaoSchema, "404": ErrorSchema})


def get_devolucao():
    """Faz a busca por uma descrição de produto a partir do id produto

    Retorna uma representação de produtos auditados.
    """


    session = Session()

    devolucoes = session.query(Devolucoes).all()

    if not devolucoes:

        return {"devolucoes": []}, 200
    else:

        return apresenta_devolucoes(devolucoes), 200
