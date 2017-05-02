#!/usr/bin/env python

"""
3x3x3 rubik's cube
"""

from internals import C, P

R = P(C('urf', 'bru', 'drb', 'frd'), C('ur', 'br', 'dr', 'fr'))
U = P(C('urf', 'ufl', 'ulb', 'ubr'), C('ur', 'uf', 'ul', 'ub'))
F = P(C('urf', 'rdf', 'dlf', 'luf'), C('uf', 'rf', 'df', 'lf'))
L = P(C('ufl', 'fdl', 'dbl', 'bul'), C('ul', 'fl', 'dl', 'bl'))
D = P(C('dlf', 'dfr', 'drb', 'dbl'), C('df', 'dr', 'db', 'dl'))
B = P(C('ubr', 'lbu', 'dbl', 'rbd'), C('ub', 'lb', 'db', 'rb'))
M = P(C('u', 'f', 'd', 'b'), C('uf', 'fd', 'db', 'bu'))
E = P(C('f', 'r', 'b', 'l'), C('fr', 'rb', 'bl', 'lf'))
S = P(C('u', 'r', 'd', 'l'), C('ur', 'rd', 'dl', 'lu'))
