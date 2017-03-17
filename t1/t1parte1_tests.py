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

import unittest
import random

import t1parte1

class TestTrabalho1Parte1(unittest.TestCase):
  # Testa função somaQuad com valores pre-definidos
  def test_somaQuad_simple(self):
    # 1*1+1*1 = 2
    self.assertEqual(t1parte1.somaQuad(1,1), 2)
    # 2*2+1*1 = 5
    self.assertEqual(t1parte1.somaQuad(2,1), 5)
    # 2*2+2*2 = 8
    self.assertEqual(t1parte1.somaQuad(2,2), 8)
    # 10*10+10*10 = 200
    self.assertEqual(t1parte1.somaQuad(10,10), 200)

  # Testa função somaQuad com valores aleatórios
  def test_somaQuad_rand(self):
    random.seed()
    # Realiza 100 testes aleatórios
    for _ in range(0,100):
      rx = random.uniform(0, 10000)
      ry = random.uniform(0, 10000)
      self.assertEqual(t1parte1.somaQuad(rx, ry), rx**2+ry**2)

if __name__ == '__main__':
  unittest.main()
