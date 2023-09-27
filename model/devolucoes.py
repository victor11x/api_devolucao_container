from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime,date
from typing import Union

from model import Base

class Devolucoes(Base):
    __tablename__ = 'devolucao'

    id_devolucao = Column("pk_devolucao", Integer, primary_key=True)
    nome_produto = Column(String(140))
    categoria = Column(String(140)) 
    quantidade = Column(Integer)
    nome_cliente = Column(String(20))
    motivo = Column(String(200))
    valor_total = Column(Integer)
    data_insercao = Column(DateTime, default=datetime.now())
    
    
def __init__(self, nome_produto:str, categoria:str, quantidade:int,nome_cliente:str, motivo:str, valor_total: int, data_insercao:Union[DateTime, None] = None):
        """
        Produtos Devolvidos pelo cliente 

        Arguments:
  
        """
        self.nome_produto = nome_produto
        self.categoria = categoria
        self.quantidade = quantidade
        self.nome_cliente = nome_cliente
        self.motivo = motivo
        self.valor_total = valor_total
        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
        