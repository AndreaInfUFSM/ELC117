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
        """Recebe um número e calcula o resultado do polinômio `3*n^2 + 2/n + 1`

        Parameters
        ----------
        n: numeric

        Returns
        -------
        out: numeric"""
        return 3.*(n**2.) + (2./n) + 1.
    return list(map(calcPoly, l))

def negatives(l):
    def isNegative(n):
        return n < 0
    return list(filter(isNegative, l))

def between1and100(l):
    def isBetween1and100(n):
        return (n >= 1) and (n<=100)
    return list(filter(isBetween1and100,l))

def evens(l):
    def isEven(n):
        return n%2 == 0
    return list(filter(isEven, l))

def charFound(c,s):
    def isCharEq(c1,c2=c):
        return c1==c2
    return len(list(filter(isCharEq,s))) >= 1

def tagify(tag, l):
    def addTag(s,t=tag):
        return "<" + t + ">" + s + "</" + t + ">"
    return list(map(addTag,l))
