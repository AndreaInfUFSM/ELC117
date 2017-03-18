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

def addSr(s):
  """Adiciona a string "Sr. " na frente de uma dada string.

  Parameters
  ----------
  s: string

  Returns
  -------
  out: string
    "Sr. " + s"""
  return "Sr. " + s

def srify(l):
  """Recebe uma lista de nomes e adiciona a string "Sr. " no inicio de cada
  nome.

  Parameters
  ----------
  l: list

  Returns
  -------
  out: list"""
  return list(map(addSr, l))

def isSpace(c):
  """Recebe um caractere e verifica se é um espaço em branco

  Parameters
  ----------
  c: character

  Returns
  -------
  out: boolean
    True em caso de espaço, False caso contrário"""
  return c == " "

def countSpaces(s):
  """Recebe uma string e retorna o número de espaços nela contidos

  Parameters
  ----------
  s: string

  Returns
  -------
  out: integer
    número de espaços contidos em `s`"""
  return len(list(filter(isSpace,s)))

def calcPoly(n):
  """Recebe um número e calcula o resultado do polinômio `3*n^2 + 2/n + 1`

  Parameters
  ----------
  n: numeric

  Returns
  -------
  out: numeric"""
  return 3.*(n**2.) + (2./n) + 1.

def calcListPoly(l):
  """Recebe uma lista de números aplicando a função `calcPoly` para cada
  número na lista. Retorna uma lista com os resultados.

  Parameters
  ----------
  l: list

  Returns
  -------
  out: list"""
  return list(map(calcPoly, l))

def isNegative(n):
    return n < 0

def negatives(l):
    return list(filter(isNegative, l))

def isBetween1and100(n):
    return (n >= 1) and (n<=100)

def between1and100(l):
    return list(filter(isBetween1and100,l))
