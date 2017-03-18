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

# Escreva uma função que receba uma lista de nomes e retorne uma lista com a
# string "Sr. " adicionada ao início de cada nome.
def srify(l):
    return list(map(lambda s:"Sr. " + s, l))

# Escreva uma função que, dada uma lista de números, calcule 3n*2 + 2/n + 1
# para cada número n da lista.
def calcListPoly(l):
    return list(map(lambda n:(3.*n**2.)+(2./n)+1., l))

# Crie uma função que receba uma lista de nomes e retorne outra lista com
# somente aqueles nomes que terminarem com a letra 'a'.
def endsWithA(l):
    return list(filter(lambda s:s[-1]=="a", l))

# Escreva uma função que, dada uma lista de idades de pessoas no ano atual,
# retorne uma lista somente com as idades de quem nasceu depois de 1970. Para
# testar a condição, sua função deverá subtrair a idade do ano atual. Exemplo
# de uso:
#
# >>> idades([20,30,51,57])
# [20, 30]
def idades(l):
    return list(filter(lambda n:date.today().year-n>1970, l))

# O código abaixo é escrito em Python imperativo. Escreva um código equivalente
# usando programação funcional.
#
# numbers = [1, 2, 3, 4]
# new_numbers = []
# for number in numbers:
#  new_numbers.append(number * 2)
# print(new_numbers)
def funcional():
    print(list(map(lambda n:n*2, [1, 2, 3, 4])))
