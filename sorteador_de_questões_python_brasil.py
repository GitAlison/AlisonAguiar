#!/usr/bin/env python
# coding=utf-8
# https://wiki.python.org.br/ListaDeExercicios
import os
import random
#AlisonAguiar
#WhatsApp 54 99681 5586
def limpar():
    clear = lambda: os.system('clear')
    clear()
def menu():
    print('''
                                ____        ____  _
                           / ___|  __ _|  _ \| |__
                           \___ \ / _` | |_) | '_ \
                                                          ___) | (_| |  __/| |_) |
                           |____/ \__, |_|   |_.__/
                                     |_|


    SORTEADOR DE QUESTÕES PYTHON BRASIL

    [+]------------------------------------[+]
       Digite o Numero do tipo de exercicio
    [+]------------------------------------[+]
        [1] Estrutura Sequencial
        [2] Estrutura De Decisao
        [3] Estrutura De Repeticao
        [4] Exercicios Listas
        [5] Exercicios Funcoes
        [6] Exercicios Com Strings
        [7] Exercicios Arquivos
        [8] Exercicios Classes
        [9] Lista De Exercicios Projetos

    [+]------------------------------------[+]
    ''')
limpar()
menu()
r = ''
while r != 's' or r != 'S':
    r = str(input('[+] Esperando...:'))
    if r == '1':
        limpar()
        menu()
        q = random.randint(1,18)
        print('[->] A questão selecionada do tipo Estrutura Sequencial é: {}'.format(q))
    elif r == '2':
        limpar()
        menu()
        q = random.randint(1,28)
        print('[->] A questão selecionada do tipo Estrutura De Decisao é: {}'.format(q))
    elif r == '3':
        limpar()
        menu()
        q = random.randint(1,51)
        print('[->] A questão selecionada do tipo Estrutura De Repeticao é: {}'.format(q))
    elif r == '4':
        limpar()
        menu()
        q = random.randint(1,24)
        print('[->] A questão selecionada do tipo Listas é: {}'.format(q))
    elif r == '5':
        limpar()
        menu()
        q = random.randint(1,14)
        print('[->] A questão selecionada do tipo Funcoes é: {}'.format(q))
    elif r == '6':
        limpar()
        menu()
        q = random.randint(1,14)
        print('[->] A questão selecionada do tipo Strings é: {}'.format(q))
    elif r == '7':
        limpar()
        menu()
        q = random.randint(1,2)
        print('[->] A questão selecionada do tipo Arquivos é: {}'.format(q))
    elif r == '8':
        limpar()
        menu()
        q = random.randint(1,17)
        print('[->] A questão selecionada do tipo Classes é: {}'.format(q))
    elif r == '9':
        limpar()
        menu()
        q = random.randint(1,3)
        print('[-] A questão selecionada do tipo Projetos é: {}'.format(q))
    else:
        clear = lambda: os.system('clear')
        clear()
        menu()
        print('[!] Opção ou caractere invalido')
