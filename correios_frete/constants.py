#!/usr/bin/env python
# -*- coding: utf-8 -*-

# correios-frete
# https://github.com/adonescunha/correios-frete

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2013 Adones Cunha adonescunha@gmail.com

WSDL_URL = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?WSDL'

CAIXA_PACOTE = 1
ROLO_PRISMA = 2
ENVELOPE = 3

SEDEX = '40010'
SEDEX_A_COBRAR = '40045'
SEDEX_A_COBRAR_COM_CONTRATO = '40126'
SEDEX_10 = '40215'
SEDEX_HOJE = '40290'
SEDEX_COM_CONTRATO_1 = '40096'
SEDEX_COM_CONTRATO_2 = '40436'
SEDEX_COM_CONTRATO_3 = '40444'
SEDEX_COM_CONTRATO_4 = '40568'
SEDEX_COM_CONTRATO_5 = '40606'
SEDEX_COM_CONTRATO = SEDEX_COM_CONTRATO_1
PAC = '41106'
PAC_COM_CONTRATO = '41068'
E_SEDEX = '81019'
E_SEDEX_PRIORITARIO = '81027'
E_SEDEX_EXPRESS = '81035'
GRUPO_1_E_SEDEX = '81868'
GRUPO_2_E_SEDEX = '81833'
GRUPO_3_E_SEDEX = '81850'

SERVICES_NAME = {
    SEDEX: 'Sedex',
    SEDEX_A_COBRAR: 'Sedex à Cobrar',
    SEDEX_A_COBRAR_COM_CONTRATO: 'Sedex à Cobrar com Contrato',
    SEDEX_10: 'Sedex 10',
    SEDEX_HOJE: 'Sedex HOJE',
    SEDEX_COM_CONTRATO_1: 'Sedex com Contrato 1',
    SEDEX_COM_CONTRATO_2: 'Sedex com Contrato 2',
    SEDEX_COM_CONTRATO_3: 'Sedex com Contrato 3',
    SEDEX_COM_CONTRATO_4: 'Sedex com Contrato 4',
    SEDEX_COM_CONTRATO_5: 'Sedex com Contrato 5',
    SEDEX_COM_CONTRATO: 'Sedex com Contrato',
    PAC: 'PAC',
    PAC_COM_CONTRATO: 'PAC com Contrato',
    E_SEDEX: 'E-Sedex',
    E_SEDEX_PRIORITARIO: 'E-Sedex Proprietário',
    E_SEDEX_EXPRESS: 'E-Sedex Express',
    GRUPO_1_E_SEDEX: 'Grupo 1 E-Sedex',
    GRUPO_2_E_SEDEX: 'Grupo 2 E-Sedex',
    GRUPO_3_E_SEDEX: 'Grupo 3 E-Sedex'
}
