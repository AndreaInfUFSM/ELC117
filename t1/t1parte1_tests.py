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
import math

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

    # Testa função somaQuad com valores aleatórios.
    def test_somaQuad_rand(self):
        random.seed()
        # Realiza 100 testes aleatórios com valores entre 0 e 10000.
        for _ in range(0,100):
            rx = random.uniform(0, 10000)
            ry = random.uniform(0, 10000)
            self.assertEqual(t1parte1.somaQuad(rx, ry), rx**2+ry**2)

    # Testa função hasEqHeads em caso de igualdade.
    def test_hasEqHeads_equal(self):
        l1 = [1,2,3,4]
        l2 = [1,4,3,2]
        self.assertTrue(t1parte1.hasEqHeads(l1,l2))

    # Testa função hasEqHeads em caso de valores diferentes.
    def test_hasEqHeads_diff(self):
        l1 = [1,2,3,4]
        l2 = [4,3,2,1]
        self.assertFalse(t1parte1.hasEqHeads(l1,l2))

    # Testa função auxiliar addSr
    def test_addSr(self):
        self.assertEqual(t1parte1.addSr("Noam Chomsky"), "Sr. Noam Chomsky")

    # Testa funcão srify
    def test_srify(self):
        l = ["Noam Chomsky", "George Orwell", "David Harvey"]
        lr = ["Sr. Noam Chomsky", "Sr. George Orwell", "Sr. David Harvey"]
        self.assertListEqual(t1parte1.srify(l), lr)

    # Testa função isSapce
    def test_isSapce(self):
        self.assertTrue(t1parte1.isSpace(" "))
        self.assertFalse(t1parte1.isSpace("a"))

    # Testa função countSpaces
    def test_countSpaces(self):
        um = " "
        dois = "  "
        cinco = "     "
        self.assertEqual(t1parte1.countSpaces(um), 1)
        self.assertEqual(t1parte1.countSpaces(dois), 2)
        self.assertEqual(t1parte1.countSpaces(cinco), 5)

    # Testa função calcPoly utilizando valores calculados
    def test_calcPoly(self):
        l = [1, 2, 3, 4, 4.25, 4.5, 4.75, 5]
        l_res = [6., 14., 86./3, 99./2, 55.6581, 62.1944, 69.1086, 382./5]
        for (v,r) in zip(l,l_res):
            self.assertTrue(math.isclose(t1parte1.calcPoly(v), r, rel_tol=1e-5))

    # Testa função calcListPoly utilizando valores calculados
    def test_calcListPoly(self):
        l = [1, 2, 3, 4, 4.25, 4.5, 4.75, 5]
        l_res = [6., 14., 86./3, 99./2, 55.6581, 62.1944, 69.1086, 382./5]
        for (v,r) in zip(t1parte1.calcListPoly(l),l_res):
            self.assertTrue(math.isclose(v, r, rel_tol=1e-5))

if __name__ == '__main__':
    unittest.main()
