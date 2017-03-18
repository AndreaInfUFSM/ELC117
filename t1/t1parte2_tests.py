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

import t1parte2

class TestTrabalho1Parte2(unittest.TestCase):
    # Testa função somaQuad com valores pre-definidos
    def test_srify(self):
        l = ["Noam Chomsky", "George Orwell", "David Harvey"]
        lr = ["Sr. Noam Chomsky", "Sr. George Orwell", "Sr. David Harvey"]
        self.assertListEqual(t1parte2.srify(l), lr)

    # Testa função calcListPoly
    def test_calcListPoly(self):
        l = [1, 2, 3, 4, 4.25, 4.5, 4.75, 5]
        l_res = [6., 14., 86./3, 99./2, 55.6581, 62.1944, 69.1086, 382./5]
        for (v,r) in zip(t1parte2.calcListPoly(l),l_res):
            self.assertTrue(math.isclose(v, r, rel_tol=1e-5))

    # Testa função endsWithA
    def test_endsWithA(self):
        l = ["Banana", "Abacate", "Maçã", "Cereja"]
        lr = ["Banana", "Cereja"]
        self.assertListEqual(t1parte2.endsWithA(l), lr)

    # Testa função idades
    def test_idades(self):
        l = [20, 30, 51, 57]
        lr = [20, 30]
        self.assertListEqual(t1parte2.idades(l), lr)

if __name__ == '__main__':
    random.seed()
    unittest.main()
