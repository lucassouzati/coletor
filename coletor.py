#!/usr/bin/python
# -*- coding: UTF-8 -*-
import scrapy
import urlparse
import peewee
from model import Ente
from selenium import webdriver
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
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.entes = Ente.select()  

    def parse(self, response):
        
        self.log(self.entes)
        for ente in self.entes:
            self.log(ente.link_licitacoes)
            # if(ente.id == 3):
            request = scrapy.Request(ente.link_licitacoes, self.classificacao_2)
            request.meta['ente'] = ente
            yield request
            # ente.classificacao = classificacao
            # ente.save()


    def classificacao_2(self, response):
        
        #teste com selenium
        ente = response.meta['ente']
        
        # resultado = self.driver.find_elements_by_xpath("//div[@id='content_page_1']//a[@href='licitacao-310']")


        #Procurar por algum link que conhetam "%dita" e termine com "pdf"
        resultado = response.xpath("//a[re:test(@href, '.*dita.*pdf') or re:test(@href, '.*licita.*')]/@href").extract()
        # resultado = response.xpath("//a[re:test(@href, '.*licita.*')]")
        self.log(resultado)
        try:
            request = scrapy.Request(random.choice(resultado), self.classificacao_2_valida)
            request.meta['ente'] = response.meta['ente']
            yield request
        except:
            self.driver.get(response.url)
            resultado = self.driver.find_elements_by_partial_link_text("Pregão")
            resultado += self.driver.find_elements_by_partial_link_text("pregão")
            resultado += self.driver.find_elements_by_partial_link_text("Edital")
            resultado += self.driver.find_elements_by_partial_link_text("edital")
            resultado += self.driver.find_elements_by_partial_link_text("editais")
            # resultado += self.driver.find_elements_by_partial_link_text("Licitação")
            # resultado += self.driver.find_elements_by_partial_link_text("licitação")
            # resultado += self.driver.find_elements_by_partial_link_text("licitações")
            # self.log(resultado)
            # for item in resultado:
            #     self.log(item.get_attribute('href'))
            try:
                request = scrapy.Request(random.choice(resultado).get_attribute('href'), self.classificacao_2_valida)
                request.meta['ente'] = response.meta['ente']
                yield request
            except:
                ente.classificacao = 1
                ente.save()    
            # print(resultado)


            
        # return None

    def classificacao_2_valida(self, response):
        # self.log(response.headers.getList())
        self.log(response.headers)
        ente = response.meta['ente']
        if(response.status == 200):
            ente.classificacao = 2
            ente.save()
        # self.driver.get(response.url)
        request = scrapy.Request(ente.link_contratos, self.classificao_3)
        request.meta['ente'] = response.meta['ente']
        yield request

    def classificao_3(self, response):
        self.log('Classificação 3')            
        
        self.driver.get(response.url)
        resultado = self.driver.find_elements_by_partial_link_text("Contrato")
        resultado += self.driver.find_elements_by_partial_link_text("Contratos")
        resultado += self.driver.find_elements_by_partial_link_text("contrato")
        resultado += self.driver.find_elements_by_partial_link_text("contratos")
        resultado += self.driver.find_elements_by_partial_link_text("Extrato")
        resultado += self.driver.find_elements_by_partial_link_text("Extratos")
        resultado += self.driver.find_elements_by_partial_link_text("extrato")
        resultado += self.driver.find_elements_by_partial_link_text("extratos")

        try:
            request = scrapy.Request(random.choice(resultado).get_attribute('href'), self.classificacao_3_valida)
            request.meta['ente'] = response.meta['ente']
            yield request
        except:
            self.log('nao conseguiu')

    def classificacao_3_valida(self, response):
        self.log("valida classificação 3")
        ente = response.meta['ente']
        if(response.status == 200):
            ente.classificacao = 3
            ente.save()