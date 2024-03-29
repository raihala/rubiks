#!/usr/bin/env python

"""
2x2x2 rubik's cube
"""

from internals import Cycle, Permutation

C = Cycle
P = Permutation

R = P(C('urf', 'bru', 'drb', 'frd'))
U = P(C('urf', 'ufl', 'ulb', 'ubr'))
F = P(C('urf', 'rdf', 'dlf', 'luf'))
