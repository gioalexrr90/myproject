#!/usr/bin/env python3
from Dominio import Dominio

if __name__ == '__main__':
    dominio = Dominio
    print(dominio.getARecord('google.com'))
