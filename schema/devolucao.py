from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from model.devolucoes import Devolucoes


class DevolucaoSchema(BaseModel):
    """ Define como um novo registro de auditoria de inventarios produtos faltantes no estoque
    """
    
    nome_produto : str = "Camisa Polo G"
    categoria : str = "Camisa"
    quantidade : int = "5"
    nome_cliente : str = "João"
    motivo : str = "Produto avariado"
    valor_total : str = "200"
    

class DevolucaoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com nome do produto.
    """
    nome_produto: str = "Digite nome produto"


class ListagemDevolucaoSchema(BaseModel):
    """ Define como uma listagem de produtos que teve auditoria.
    """
    devolucao:List[DevolucaoSchema]


def apresenta_devolucoes(devolucoes: List[Devolucoes]):
    """ Retorna uma representação de produtos auditados seguindo o schema definido em
        InventarioViewSchema.
    """
    result = []
    for devolucao in devolucoes:
        result.append({
            "nome_produto":devolucao.nome_produto,
            "categoria":devolucao.categoria,
            "quantidade": devolucao.quantidade,
            "nome_cliente":devolucao.nome_cliente,
            "motivo":devolucao.motivo,
            "valor_total":devolucao.valor_total,
            "data_devolucao":devolucao.data_insercao,
        })

    return {"devolucoes": result}


class DevolucaoViewSchema(BaseModel):
    """ Define como um auditoria será retornado: descrição de produtos auditados).
    """
        
    id_devolucao: int = 1    
    nome_produto : str = "Camisa Polo G"
    categoria : str = "Camisa"
    quantidade : int = "5"
    nome_cliente : str = "João"
    motivo : str = "Produto avariado"
    valor_total : str = "200"
    data_insercao : str = "12/03/2023"


class DevolucaoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome_produto: str

def apresenta_devolucao(devolucao: Devolucoes):
    """ Retorna uma representação da auditoria seguindo o schema definido em
        devolucaoViewSchema.
    """
    return {
        "id_devolucao": devolucao.id_devolucao,
        "nome_produto":devolucao.nome_produto,
        "categoria":devolucao.categoria,
        "quantidade": devolucao.quantidade,
        "nome_cliente":devolucao.nome_cliente,
        "motivo":devolucao.motivo,
        "valor_total":devolucao.valor_total,     
        
    }