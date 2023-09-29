#!/usr/bin/python3
# -*- coding: utf-8 -*-
import dns.resolver
from tldextract import tldextract


class Dominio:

    '''
    Clase de Dominio en donde se cuentran los metodos para obtener información de un dominio
    '''

    def __init__(self, dominio):
        self._dominio = str(dominio)

    @property
    def dominio(self):
        return self._dominio

    @dominio.setter
    def dominio(self, dominio):
        self._dominio = str(dominio)

    def __str__(self):
        return f'{Dominio.getCompleteDomain(self.dominio)}'

    @classmethod
    def getTLD(cls, domain_name=''):
        dic = tldextract.extract(domain_name)
        return dic.suffix

    @classmethod
    def getSubDomain(cls, domain_name=''):
        dic = tldextract.extract(domain_name)
        return dic.subdomain

    @classmethod
    def getCompleteDomain(cls, domain_name=''):
        dic = tldextract.extract(domain_name)
        return dic.fqdn

    @classmethod
    def getPrincipalDomain(cls, domain_name=''):
        dic = tldextract.extract(domain_name)
        return dic.registered_domain

    @classmethod
    def getARecord(cls, domain_name=''):
        if cls.getSubDomain(domain_name):
            try:
                subd = cls.getCompleteDomain(domain_name)
                answer = dns.resolver.resolve(subd, 'A')
                ns = []
                for server in answer:
                    ns.append(server.to_text())
                return ns
            except Exception as e:
                if e:
                    return f'Subdominio {subd} no existe.'
        else:
            try:
                dominio = cls.getPrincipalDomain(domain_name)
                answer = dns.resolver.resolve(dominio, 'A')
                ns = []
                for server in answer:
                    ns.append(server.to_text())
                return ns
            except Exception as e:
                if e:
                    return f'dominio {dominio} no existe.'

    @classmethod
    def getMXRecord(cls, domain_name=''):
        if cls.getSubDomain(domain_name):
            dominio = cls.getPrincipalDomain(domain_name)
            return cls.getMXRecord(dominio)
        else:
            try:
                dominio = cls.getPrincipalDomain(domain_name)
                answer = dns.resolver.resolve(dominio, 'MX')
                ns = []
                for server in answer:
                    ns.append(server.to_text())
                return ns
            except Exception as e:
                if e:
                    return f'dominio {dominio} no existe.'

    @classmethod
    def getNSRecord(cls, domain_name=''):
        if cls.getSubDomain(domain_name):
            dom = cls.getPrincipalDomain(domain_name)
            return cls.getNSRecord(dom)
        else:
            try:
                dominio = cls.getPrincipalDomain(domain_name)
                answer = dns.resolver.resolve(dominio, 'NS')
                ns = []
                for server in answer:
                    ns.append(server.to_text())
                return ns
            except Exception as e:
                if e:
                    return f'dominio {dominio} no existe.'


if __name__ == '__main__':
    dominio = Dominio
    print(dominio.getARecord('google.com'))
