#!/usr/bin/python
# -*- coding: UTF-8 -*-
import peewee

db = peewee.SqliteDatabase('banco.db')

class Ente(peewee.Model):
    nome = peewee.CharField()
    municipio = peewee.CharField()
    link_transparencia = peewee.CharField()
    link_licitacoes = peewee.CharField()
    link_contratos = peewee.CharField()
    esfera = peewee.CharField()
    classificacao = peewee.CharField()
    ativo = peewee.CharField()
    class Meta:
        database = db

