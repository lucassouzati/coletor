#!/usr/bin/python
# -*- coding: UTF-8 -*-
# api.py

# Let's get this party started!
import falcon, json
import peewee
from model import Ente

class ApiResource(object):
	def on_get(self, req, resp):
		resp.status = falcon.HTTP_200
		resp.body = ('teste')


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
			novo_ente.save(force_insert=True)

		# print(resp.body)
		# print(req)
		# print(req.params)

		# self.log(resp.body)

app = falcon.API()
api = ApiResource()
app.add_route('/teste', api)
