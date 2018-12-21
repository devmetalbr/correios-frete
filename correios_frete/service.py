#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com


from .utils import comma_separated_to_float, s_n_to_bool
from .constants import SERVICES_NAME


class Service(object):
    codigo = None
    nome = ''
    valor = None
    prazo_entrega = None
    valor_mao_propria = None
    valor_aviso_recebimento = None
    valor_valor_declarado = None
    entrega_domiciliar = None
    entrega_sabado = None
    erro = None
    msg_erro = None

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if not hasattr(self.__class__, k):
                raise TypeError

            setattr(self, k, v)

    @classmethod
    def create_from_suds_object(cls, suds_object):
        codigo = str(suds_object.Codigo)
        return cls(
            codigo=codigo,
            nome=SERVICES_NAME.get(codigo, ''),
            valor=comma_separated_to_float(suds_object.Valor),
            prazo_entrega=int(suds_object.PrazoEntrega),
            valor_mao_propria=comma_separated_to_float(
                suds_object.ValorMaoPropria),
            valor_aviso_recebimento=comma_separated_to_float(
                suds_object.ValorAvisoRecebimento),
            valor_valor_declarado=comma_separated_to_float(
                suds_object.ValorValorDeclarado),
            entrega_domiciliar=s_n_to_bool(suds_object.EntregaDomiciliar),
            entrega_sabado=s_n_to_bool(suds_object.EntregaSabado),
            erro=int(suds_object.Erro),
            msg_erro=suds_object.MsgErro
        )
