#!/usr/bin/env python3

import argparse
from Dominio import Dominio

parser = argparse.ArgumentParser(description='Script de Gio para webones como el Gio',
                                 prog='gio',
                                 usage='%(prog)s [options] values')
subparsers = parser.add_subparsers(help='Subcomandos de ayuda')
parser_domain = subparsers.add_parser('d', help='Invoca ayuda para dominios')
parser_domain.add_argument('domain', type=str)
parser_domain.add_argument('-gA', metavar='None', dest='getA', nargs='?', const=True, help='Obtiene los registros A de un dominio')
parser_domain.add_argument('-gMX', metavar='None', dest='getMX', nargs='?', const=True, help='Obtiene los registros MX de un dominio')

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    if args.domain and args.getA:
        print(Dominio.getARecord(args.domain))
    elif args.domain and args.getMX:
        print(Dominio.getMXRecord(args.domain))