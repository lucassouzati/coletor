#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy
import urlparse
import peewee
from model import Ente

class Contrato(scrapy.Item):
    unidade_gestora =scrapy.Field()
    data_emissao =scrapy.Field()
    instrumento_contrato =scrapy.Field()
    numero_contrato =scrapy.Field()
    data_expiracao =scrapy.Field()
    tipo =scrapy.Field()
    fornecedor =scrapy.Field()
    cnpj_cpf =scrapy.Field()
    aditivo =scrapy.Field()
    processo =scrapy.Field()
    valor =scrapy.Field()
    itens =scrapy.Field()
    descricao =scrapy.Field()

class ItemContrato(scrapy.Item):
    unidade_gestora =scrapy.Field()
    exercicio =scrapy.Field()
    item =scrapy.Field()
    descricao =scrapy.Field()
    quantidade =scrapy.Field()
    unidade_medida =scrapy.Field()
    valor_unitario =scrapy.Field()
    valor_total =scrapy.Field()

class Coletor(scrapy.Spider):
    name = 'coletor'
    start_urls = ['http://prefeituradecambuci.rj.gov.br/transparencia/licitacoes/']

    def parse(self, response):
        try:
            Ente.create_table()
        except peewee.OperationalError:
            print 'Tabela Ente ja existe!'

        #Dividir o algoritmos por cidades?
        #Ou fazer um algoritmo genérico?

        #Cidades que não tem nada: Cambuci, Italva, Itaocara, Porciúncula
        #Cidades com informações básicas mas sem resultado: Laje do Muriaé, Miracema, Natividade, Varre-sai
        #Cidades com infomrações sobre licitações e contratos, mas em pdf:Aperibé, Bom Jesus do Itabopana, Santo Antonio de Padua, São jose de Uba
        #Cidades com informações em formato aberto, porem desatualizado: Itaperuna


