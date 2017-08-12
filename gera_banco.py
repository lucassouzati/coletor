#!/usr/bin/python
# -*- coding: UTF-8 -*-
import peewee
from model import Ente

if __name__ == '__main__':
	try:
		Ente.create_table()
	except peewee.OperationalError:
		print 'Tabela Ente ja existe!'

	# cambuci = {
	#     'nome': 'Prefeitura Municipal de Cambuci', 
 #        'municipio': 'Cambuci', 
 #        'link_transparencia': 'teste', 
 #        'link_licitacoes': 'http://prefeituradecambuci.rj.gov.br/transparencia/licitacoes/', 
 #        'link_contratos': 'teste', 
 #        'esfera': 'Municipal', 
 #        'classificacao': 1, 
 #        'ativo': 1
 #    }
	# entes = [cambuci]
	# Ente.insert_many(entes).execute()

	