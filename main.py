#!/usr/bin/env python3

import argparse
#from Dominio import Dominio

parser = argparse.ArgumentParser(description='Script de Gio para webones como el Gio',
                                 prog='gio')
# valores principales
parser.add_argument('option', nargs='?', metavar='option')

subparsers = parser.add_subparsers(help='')
parser_domain = subparsers.add_parser('d', help='Invoca ayuda para dominios, Ejemplo: %(prog)s d DOMINIO [options] values')
parser_domain.add_argument('domain', type=str, nargs=1)
parser_domain.add_argument('option', nargs='?')
parser_domain.add_argument('value', nargs='?')
#parser_domain.add_argument('-gA', metavar='None', dest='getA', nargs='?', const=True, help='Obtiene los registros A de un dominio')
#parser_domain.add_argument('-gMX', metavar='None', dest='getMX', nargs='?', const=True, help='Obtiene los registros MX de un dominio')

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)