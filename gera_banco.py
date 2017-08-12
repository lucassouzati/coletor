#!/usr/bin/python
# -*- coding: UTF-8 -*-
import peewee
from model import Ente

if __name__ == '__main__':
	try:
		Ente.create_table()
	except peewee.OperationalError:
		print 'Tabela Ente ja existe!'

	cambuci = {
	    'nome': 'Prefeitura Municipal de Cambuci', 
        'municipio': 'Cambuci', 
        'link_transparencia': 'teste', 
        'link_licitacoes': 'http://prefeituradecambuci.rj.gov.br/transparencia/licitacoes/editais/', 
        'link_contratos': 'teste', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }
	italva = {
		'nome': 'Prefeitura Municipal de Italva', 
        'municipio': 'Italva', 
        'link_transparencia': 'teste', 
        'link_licitacoes': 'http://www.italva.rj.gov.br/ver_licitacoes', 
        'link_contratos': 'http://www.italva.rj.gov.br/ver_licitacoes', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }
	entes = [cambuci, italva]

	Ente.insert_many(entes).execute()

	