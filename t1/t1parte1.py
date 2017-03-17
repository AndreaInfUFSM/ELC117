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

