# Copyright (c) Eduardo Tiago Braun.
# All rights reserved.
#
# This code is licensed under the MIT License.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions :
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# 1. Defina uma função somaQuad(x,y) que calcule a soma dos quadrados de dois
# números x e y.
def somaQuad(x,y):
    """Retorna a soma dos quadrados de dois números, preservando o tipo original.

    Parameters
    ----------
    x: numeric
    y: numeric

    Returns
    -------
    out: numeric
        Valor numerico de mesmo tipo de `x` e `y`."""
    return x**2 + y**2


# 2. Crie uma função hasEqHeads(l1,l2) que verifique se as listas l1
# e l2 possuem o mesmo primeiro elemento.
def hasEqHeads(l1,l2):
    """Verifica se duas listas possuem o mesmo primeiro elemento.

    Parameters
    ----------
    l1: list
    l2: list

    Returns
    -------
    out: boolean
        True caso l1[0] e l2[0] forem iguais."""
    return l1[0] == l2[0]


# 3. Escreva uma função que receba uma lista de nomes e retorne uma lista com a
# string "Sr. " adicionada ao início de cada nome. Defina uma função auxiliar
# para ajudar neste exercício.
def srify(l):
    """Recebe uma lista de nomes e adiciona a string "Sr. " no inicio de cada
    nome.

    Parameters
    ----------
    l: list

    Returns
    -------
    out: list"""
    def addSr(s):
        return "Sr. " + s
    return list(map(addSr, l))


# 4. Crie uma função que receba uma string e retorne o número de espaços
# nela contidos. Defina uma função auxiliar para ajudar neste exercício.
def countSpaces(s):
    """Recebe uma string e retorna o número de espaços nela contidos

    Parameters
    ----------
    s: string

    Returns
    -------
    out: integer
        número de espaços contidos em `s`"""
    def isSpace(c):
        return c == " "
    return len(list(filter(isSpace,s)))


# 5. Escreva uma função que, dada uma lista de números, calcule 3n*2 + 2/n + 1 para
# cada número n da lista. Defina uma função auxiliar para ajudar neste
# exercício.
def calcListPoly(l):
    """Recebe uma lista de números aplicando a função `calcPoly` para cada
    número na lista. Retorna uma lista com os resultados.

    Parameters
    ----------
    l: list

    Returns
    -------
    out: list"""
    def calcPoly(n):
        return 3.*(n**2.) + (2./n) + 1.
    return list(map(calcPoly, l))


# 6. Escreva uma função que, dada uma lista de números, retorne uma lista com
# apenas os que forem negativos. Defina uma função auxiliar para ajudar neste
# exercício.
def negatives(l):
    """Recebe uma lista de números e retorna outra lista contendo somente os
    números negativos.

    Parameters
    ----------
    l: list

    Returns
    -------
    out: list"""
    def isNegative(n):
        return n < 0
    return list(filter(isNegative, l))


# 7. Escreva uma função que receba uma lista de números e retorne somente os que
# estiverem entre 1 e 100, inclusive. Defina uma função auxiliar para ajudar
# neste exercício.
def between1and100(l):
    """Recebe uma lista de números e retorna outra lista contendo somente os
    números entre 1 em 100, inclusive.

    Parameters
    ----------
    l: list

    Returns
    -------
    out: list"""
    def isBetween1and100(n):
        return (n >= 1) and (n<=100)
    return list(filter(isBetween1and100,l))


# 8. Escreva uma função que receba uma lista de números e retorne somente aqueles
# que forem pares. Defina uma função auxiliar para ajudar neste exercício.
def evens(l):
    """Recebe uma lista de números e retorna outra lista contendo somente os
    números pares.

    Parameters
    ----------
    l: list

    Returns
    -------
    out: list"""
    def isEven(n):
        return n%2 == 0
    return list(filter(isEven, l))


# 9. Crie uma função charFound(c,s) que verifique se o caracter c está contido na
# string. O resultado deve ser True ou False. Você não deve usar o operador in.
# Defina uma função auxiliar para ajudar neste exercício.
def charFound(c,s):
    """Recebe um caractere e uma string, retornando `True` caso o caractere
    estiver contido na string e False caso contrário.

    Parameters
    ----------
    c: character
    s: string

    Returns
    -------
    out: boolean"""
    def isCharEq(c1,c2=c):
        return c1==c2
    return len(list(filter(isCharEq,s))) >= 1


# 10. Escreva uma função que receba uma lista de strings e retorne uma nova lista
# com adição de marcações HTML (p.ex.: <B> e </B>) antes e depois de cada
# string.
def tagify(l, tag="B"):
    """Recebe uma lista de strings e uma tag, retornando outra lista de
    strings com a tag adicionada no início e final de cada string.

    Parameters
    ----------
    tag: string
    l: list

    Returns
    -------
    out: list"""
    def addTag(s,t=tag):
        return "<" + t + ">" + s + "</" + t + ">"
    return list(map(addTag,l))

