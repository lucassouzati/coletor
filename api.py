#!/usr/bin/python
# -*- coding: UTF-8 -*-
# api.py

# Let's get this party started!
import falcon, json
import peewee
from model import Ente, HistoricoDeAcesso

class EnteResource(object):
	def on_get(self, req, resp):
		entes = Ente.select()
		retorno = [{'id': ente.id, 'nome': ente.nome, 'municipio': ente.municipio, 'link_transparencia': ente.link_transparencia, 'link_licitacoes': ente.link_licitacoes, 'link_contratos': ente.link_contratos, 'esfera': ente.esfera, 'classificacao': ente.classificacao, 'ativo': ente.ativo} for ente in entes]
		# print retorno
		resp.body = json.dumps(retorno)
		resp.status = falcon.HTTP_200
		


	def on_post(self, req, resp):
		resp.status = falcon.HTTP_200
		entes = json.load(req.stream)

		for ente in entes['entes']:
			# print(ente)
			novo_ente = Ente()
			
			novo_ente.id = ente['id']
			novo_ente.nome = ente['nome']
			novo_ente.municipio = ente['municipio']
			novo_ente.link_transparencia = ente['link_transparencia']
			novo_ente.link_licitacoes = ente['link_licitacoes']
			novo_ente.link_contratos = ente['link_contratos']
			novo_ente.esfera = ente['esfera']
			novo_ente.classificacao = ente['classificacao']
			novo_ente.ativo = ente['ativo']
			# print(novo_ente)
			try:
				novo_ente.save(force_insert=True)
			except:
				novo_ente.save()
class HistoricoDeAcessoResource(object):
	def on_get(self,req,resp):
		historicos_de_acesso = HistoricoDeAcesso.select()
		retorno = [{'id': historico_de_acesso.id, 'licitacoes': historico_de_acesso.licitacoes, 'contratos': historico_de_acesso.contratos, 'portal_transparencia': historico_de_acesso.portal_transparencia, 'data_hora': historico_de_acesso.data_hora.strftime("%Y-%m-%d %H:%M:%S"), 'ente_id': historico_de_acesso.ente.id} for historico_de_acesso in historicos_de_acesso]
		print retorno
		resp.body = json.dumps(retorno)
		resp.status = falcon.HTTP_200

		# print(resp.body)
		# print(req)
		# print(req.params)

		# self.log(resp.body)

app = falcon.API()
entes_api = EnteResource()
historico_de_acesso_api = HistoricoDeAcessoResource()
app.add_route('/entes', entes_api)
app.add_route('/historicos_de_acesso', historico_de_acesso_api)
