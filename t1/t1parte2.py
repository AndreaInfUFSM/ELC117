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
from datetime import date

# 1. Escreva uma função que receba uma lista de nomes e retorne uma lista com a
# string "Sr. " adicionada ao início de cada nome.
def srify(l):
    """Recebe uma lista de nomes e adiciona a string "Sr. " no inicio de cada
    nome.
    Parameters
    ----------
    l: list
    Returns
    -------
    out: list"""
    return list(map(lambda s:"Sr. " + s, l))

# 2. Escreva uma função que, dada uma lista de números, calcule 3n*2 + 2/n + 1
# para cada número n da lista.
def calcListPoly(l):
    """Recebe uma lista de números aplicando a função `calcPoly` para cada
    número na lista. Retorna uma lista com os resultados.
    Parameters
    ----------
    l: list
    Returns
    -------
    out: list"""
    return list(map(lambda n:(3.*n**2.)+(2./n)+1., l))

# 3. Crie uma função que receba uma lista de nomes e retorne outra lista com
# somente aqueles nomes que terminarem com a letra 'a'.
def endsWithA(l):
    """Recebe uma lista de strings. Retorna uma lista contendo somente as
    strings terminadas em `a`.
    Parameters
    ----------
    l: list
    Returns
    -------
    out: list"""
    return list(filter(lambda s:s[-1]=="a", l))

# 4. Escreva uma função que, dada uma lista de idades de pessoas no ano atual,
# retorne uma lista somente com as idades de quem nasceu depois de 1970. Para
# testar a condição, sua função deverá subtrair a idade do ano atual. Exemplo
# de uso:
#
# >>> idades([20,30,51,57])
# [20, 30]
def idades(l):
    """Recebe uma lista de idades. Retorna uma lista contendo somente as
    idades de pessoas que nasceram depois de 1970.
    Parameters
    ----------
    l: list
    Returns
    -------
    out: list"""
    return list(filter(lambda n:date.today().year-n>1970, l))

# 5. O código abaixo é escrito em Python imperativo. Escreva um código equivalente
# usando programação funcional.
#
# numbers = [1, 2, 3, 4]
# new_numbers = []
# for number in numbers:
#  new_numbers.append(number * 2)
# print(new_numbers)
def funcional():
    print(list(map(lambda n:n*2, [1, 2, 3, 4])))
