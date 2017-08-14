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

	aperibe = {
		'nome': 'Prefeitura Municipal de Aperibé', 
        'municipio': 'Aperibé', 
        'link_transparencia': 'http://www.aperibe.rj.gov.br/portal', 
        'link_licitacoes': 'http://aperibe.rj.gov.br/licitacao', 
        'link_contratos': 'http://aperibe.rj.gov.br/licitacao', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }
	bomjesus = {
		'nome': 'Prefeitura Municipal de Bom Jesus do Itabapoana', 
        'municipio': 'Bom Jesus do Itabapoana', 
        'link_transparencia': 'http://www.bomjesus.rj.gov.br/portal', 
        'link_licitacoes': 'https://bomjesus.rj.gov.br/site/ver_licitacoes-13', 
        'link_contratos': 'https://bomjesus.rj.gov.br/site/ver_licitacoes-13', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }
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
	miracema = {
		'nome': 'Prefeitura Municipal de Miracema', 
        'municipio': 'Miracema', 
        'link_transparencia': 'http://sistemas.miracema.rj.gov.br/pronimtb/index.asp', 
        'link_licitacoes': 'http://www.miracema.rj.gov.br/transparencia/index.php?t=4&f=4287&r=0', 
        'link_contratos': 'http://www.miracema.rj.gov.br/transparencia/index.php?t=4&f=4287&r=0', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }
	natividade = {
		'nome': 'Prefeitura Municipal de Natividade', 
        'municipio': 'Natividade', 
        'link_transparencia': 'http://179.109.158.34:8079/transparencia/', 
        'link_licitacoes': 'http://natividade.rj.gov.br/index.php/licitacoes.html', 
        'link_contratos': 'http://179.109.158.34:8079/transparencia/', 
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
	santoantoniodepadua = {
		'nome': 'Prefeitura Municipal de Santo Antônio de Pádua', 
        'municipio': 'Santo Antônio de Pádua', 
        'link_transparencia': 'http://santoantoniodepadua.rj.gov.br/transparencia/index.php', 
        'link_licitacoes': 'http://santoantoniodepadua.rj.gov.br/transparencia/index.php?t=19&f=4737&r=0', 
        'link_contratos': 'http://santoantoniodepadua.rj.gov.br/transparencia/index.php?t=19&f=4126&r=0', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }
	saojosedeuba = {
		'nome': 'Prefeitura Municipal de São José de Ubá', 
        'municipio': 'São José de Ubá', 
        'link_transparencia': 'http://transparencia.saojosedeuba.rj.gov.br/transparenciafinancas/', 
        'link_licitacoes': 'http://www.saojosedeuba.rj.gov.br/site/licitacoes', 
        'link_contratos': 'http://www.saojosedeuba.rj.gov.br/site/licitacoes', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }
	varresai = {
		'nome': 'Prefeitura Municipal de Varre-Sai', 
        'municipio': 'Varre-Sai', 
        'link_transparencia': 'http://www.varresai.rj.gov.br/site/ver_relatorios-86', 
        'link_licitacoes': 'http://www.varresai.rj.gov.br/site/ver_licitacoes-49', 
        'link_contratos': 'http://www.varresai.rj.gov.br', 
        'esfera': 'Municipal', 
        'classificacao': 1, 
        'ativo': 1
    }


	entes = [cambuci, italva, itaocara, laje, miracema, natividade, porciuncula]

	Ente.insert_many(entes).execute()

	