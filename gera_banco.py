#!/usr/bin/python
# -*- coding: UTF-8 -*-
import peewee
from model import Ente

if __name__ == '__main__':
	try:
		Ente.create_table()
	except peewee.OperationalError:
		print 'Tabela Ente ja existe!'
		Ente.drop_table()
		Ente.create_table()

	cambuci = {
	    'nome': 'Prefeitura Municipal de Cambuci', 
        'municipio': 'Cambuci', 
        'link_transparencia': 'http://prefeituradecambuci.rj.gov.br/transparencia/', 
        'link_licitacoes': 'http://prefeituradecambuci.rj.gov.br/transparencia/licitacoes/editais/', 
        'link_contratos': 'http://prefeituradecambuci.rj.gov.br/transparencia/licitacoes/contratos/', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }
	italva = {
		'nome': 'Prefeitura Municipal de Italva', 
        'municipio': 'Italva', 
        'link_transparencia': 'http://186.194.106.213/pronimtb/index.asp', 
        'link_licitacoes': 'http://www.italva.rj.gov.br/ver_licitacoes', 
        'link_contratos': 'http://www.italva.rj.gov.br/ver_licitacoes', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }
	itaocara = {
		'nome': 'Prefeitura Municipal de Itaocara', 
        'municipio': 'Itaocara', 
        'link_transparencia': 'http://www.itaocara.rj.gov.br/transparencia', 
        'link_licitacoes': 'http://www.itaocara.rj.gov.br', 
        'link_contratos': 'http://www.itaocara.rj.gov.br', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }
	porciuncula = {
		'nome': 'Prefeitura Municipal de Porciúncula', 
        'municipio': 'Porciúncula', 
        'link_transparencia': 'http://transparencia.porciuncula.rj.gov.br:8079/transparencia/', 
        'link_licitacoes': 'http://www.porciuncula.rj.gov.br', 
        'link_contratos': 'http://www.porciuncula.rj.gov.br', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }
	laje = {
		'nome': 'Prefeitura Municipal de Laje do Muriaé', 
        'municipio': 'Laje do Muriaé', 
        'link_transparencia': 'http://131.255.20.2/pronimtb/index.asp', 
        'link_licitacoes': 'http://www.laje.rj.gov.br/site/licitacao', 
        'link_contratos': 'http://www.laje.rj.gov.br/site/download/lista/3', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }



	entes = [cambuci, italva, itaocara, porciuncula, laje]

	Ente.insert_many(entes).execute()

	