#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy
import urlparse
import peewee
from model import Ente, HistoricoDeAcesso
from selenium import webdriver
from time import gmtime, strftime
import random

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


    #Dividir o algoritmos por cidades?
    #Ou fazer um algoritmo genérico?

    #Cidades que não tem nada: Cambuci, Italva, Itaocara, Porciúncula
    #Cidades com informações básicas mas sem resultado: Laje do Muriaé, Miracema, Natividade, Varre-sai
    #Cidades com infomrações sobre licitações e contratos, mas em pdf:Aperibé, Bom Jesus do Itabopana, Santo Antonio de Padua, São jose de Uba
    #Cidades com informações em formato aberto, porem desatualizado: Itaperuna

class Coletor(scrapy.Spider):
    name = 'coletor'
    start_urls = ['http://prefeituradecambuci.rj.gov.br/transparencia/licitacoes/']
    entes = []
    palavras_licitacoes = ['Pregão', 'PREGÃO', 'pregão', 'EDITAL', 'Edital', 'editais', 'EDITAIS']
    palavras_contratos = ['Contrato', 'Contratos', 'contrato', 'contratos', 'Extrato', 'Extratos', 'extrato', 'extratos', 'CONTRATO', 'ATA DE REGISTRO', 'Ata de Registro']


    def __init__(self):
        self.driver = webdriver.Firefox()
        self.entes = Ente.select()  

    def parse(self, response):
        
        self.log(self.entes)
        for ente in self.entes:
            self.log(ente.link_licitacoes)
            # if(ente.id == 6):
            request = scrapy.Request(ente.link_licitacoes, self.classificacao_2)
            historico_acesso = HistoricoDeAcesso()
            request.meta['ente'] = ente
            request.meta['historico_acesso'] = historico_acesso
            yield request
            # ente.classificacao = classificacao
            # ente.save()


    def classificacao_2(self, response):
        
        #teste com selenium
        ente = response.meta['ente']
        historico_acesso = response.meta['historico_acesso']
        
        # resultado = self.driver.find_elements_by_xpath("//div[@id='content_page_1']//a[@href='licitacao-310']")


        #Procurar por algum link que conhetam "%dita" e termine com "pdf"
        resultado = response.xpath("//a[re:test(@href, '.*dita.*pdf') or re:test(@href, '.*licita.*')]/@href").extract()
        # resultado = response.xpath("//a[re:test(@href, '.*licita.*')]")
        self.log(resultado)
        try:
            request = scrapy.Request(random.choice(resultado), self.classificacao_2_valida)
            request.meta['ente'] = response.meta['ente']
            request.meta['historico_acesso'] = response.meta['historico_acesso']
            yield request
        except:
            self.driver.get(response.url)

            resultado = []
            for item in self.palavras_licitacoes:
                resultado += self.driver.find_elements_by_partial_link_text(item)
                # filtro = ("//td[contains(., '%s')]/a", item)
                resultado += self.driver.find_elements_by_xpath("//td[contains(., '"+ item +"')]/a")

            try:
                request = scrapy.Request(random.choice(resultado).get_attribute('href'), self.classificacao_2_valida)
                request.meta['ente'] = response.meta['ente']
                request.meta['historico_acesso'] = response.meta['historico_acesso']
                yield request
            except:

            
                ente.classificacao = 1
                ente.save()    

                historico_acesso.licitacoes = 0
                historico_acesso.contratos = 0
                historico_acesso.portal_transparencia = 0
                historico_acesso.data_hora = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                historico_acesso.ente = ente
                historico_acesso.save()
            # print(resultado)


            
        # return None

    def classificacao_2_valida(self, response):
        # self.log(response.headers.getList())
        self.log(response.headers)
        ente = response.meta['ente']
        historico_acesso = response.meta['historico_acesso']
        if(response.status == 200):
            ente.classificacao = 2
            ente.save()

            historico_acesso.licitacoes = 1
            historico_acesso.contratos = 0
            historico_acesso.portal_transparencia = 0
            historico_acesso.data_hora = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            historico_acesso.ente = ente
            historico_acesso.save()
        # self.driver.get(response.url)
        request = scrapy.Request(ente.link_contratos, self.classificao_3)
        request.meta['ente'] = response.meta['ente']
        request.meta['historico_acesso'] = response.meta['historico_acesso']
        yield request

    def classificao_3(self, response):
        self.log('Classificação 3')            
        ente = response.meta['ente']
        historico_acesso = response.meta['historico_acesso']
        self.driver.get(response.url)
        resultado = []
        for item in self.palavras_contratos:
            resultado += self.driver.find_elements_by_partial_link_text(item)
            resultado += self.driver.find_elements_by_xpath("//td[contains(., '"+ item +"')]/a")


        #Tirei a chamada do método classificacao_3_valida, pois estava tendo dificuldade em avaliar sites em que o link estivesse em chamadas javascript,
        #Dessa forma a validação ficou apenas através da indicação de algum termo referente a contrato na página
        if resultado:
            self.log(resultado)
            ente.classificacao = 3
            ente.save()    

            historico_acesso.licitacoes = 1
            historico_acesso.contratos = 1
            historico_acesso.portal_transparencia = 0
            historico_acesso.data_hora = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            historico_acesso.ente = ente
            historico_acesso.save()
            # Scrapy.Request(random.choice(resultado).get_attribute('href'), self.classificacao_3_valida)
        else:
            self.log("nao achou")
        # try:
        #     request = scrapy.Request(random.choice(resultado).get_attribute('href'), self.classificacao_3_valida)
        #     request.meta['ente'] = response.meta['ente']
        #     yield request
        # except:
        #     #buscando no portal da transparencia
        #     #buscando algo para clicar
        #     # item = self.driver.find_element_partial_link_text()
        #     self.driver.get(ente.link_transparencia)
        #     achou = 0
        #     for item in self.palavras_contratos:
        #         achou = self.driver.assertIn(item, self.driver.page_source)
        #         self.log(achou)
        #     if(achou):
        #         ente.classificacao = 3
        #         ente.save()    

    def classificacao_3_valida(self, response):
        self.log("valida classificação 3")
        ente = response.meta['ente']
        historico_acesso = response.meta['historico_acesso']
        if(response.status == 200):
            ente.classificacao = 3
            ente.save()