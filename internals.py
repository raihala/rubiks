#!/usr/bin/env python

import sys


CUBICLES = {
    'ufl', 'urf', 'ubr', 'ulb',
    'dbl', 'dlf', 'dfr', 'drb',
    'ub', 'ur', 'uf', 'ul',
    'lb', 'rb', 'rf', 'lf',
    'db', 'dr', 'df', 'dl',
    'u', 'l', 'f', 'r', 'b', 'd'
}


class Cubie(object):
    """
    Representation of one of the physical cubies
    of a rubik's cube.
    """
    def __init__(self, data):
        """
        data can either be a Cubie object, in which case the new Cubie
        will be a deep copy of data, or a string
        """
        if type(data) is Cubie:
            self.string = data.string
        elif Cubie._is_valid_cubie_string(data):
            self.string = data.lower()
        else:
            raise ValueError("Invalid cubie data %s!" % data)

    @staticmethod
    def _rotate_str(string, n):
        return string[-n:] + string[:-n]

    @staticmethod
    def _is_valid_cubie_string(string):
        if not type(string) is str:
            return False
        string = string.lower()
        if not {string, Cubie._rotate_str(string, 1), Cubie._rotate_str(string, 2)} & CUBICLES:
            return False
        return True

    @property
    def orientation(self):
        """
        Default/'solved' orientation is always 0;
        orientation of 1 means one clockwise rotation, etc
        """
        if len(self.string) == 1:
            # orientation of the center cubie of a face is irrelevant
            return 0
        elif 'u' in self.string:
            return self.string.index('u')
        elif 'd' in self.string:
            return self.string.index('d')
        elif 'f' in self.string:
            return self.string.index('f')
        elif 'b' in self.string:
            return self.string.index('b')

    def rotate_cw(self):
        """
        Rotate the cubie clockwise once.
        """
        self.string = Cubie._rotate_str(self.string, 1)

    def orient(self, orientation):
        """
        Set the Cubie to an absolute orientation (0, 1, 2)
        """
        diff = (orientation - self.orientation) % len(self.string)
        for _ in range(diff):
            self.rotate_cw()

    def __eq__(self, other):
        return sorted(self.string) == sorted(other.string)

    def __hash__(self):
        return hash(tuple(sorted(self.string)))

    def __repr__(self):
        return self.string


class Cycle(object):
    def __init__(self, *args):
        self._cycle = list(Cubie(x) for x in args)

    def index(self, cubie):
        return self._cycle.index(cubie)

    def permute(self, cubie):
        return Permutation(self).permute(cubie)

    def __call__(self, cubie):
        return self.permute(cubie)

    def __getitem__(self, index):
        return self._cycle[index % len(self._cycle)]

    def __iter__(self):
        return iter(self._cycle)

    def __len__(self):
        return len(self._cycle)

    def __mul__(self, other):
        return Permutation(self) * Permutation(other)

    def __repr__(self):
        return '(' + ' '.join([str(c) for c in self._cycle]) + ')'


class Permutation(object):
    def __init__(self, *args):
        self.cycles = list(args) or []

    def permute(self, cubie):
        if type(cubie) is str:
            cubie = Cubie(cubie)

        # permute the cubie through each cycle in the
        # permutation, sequentially from left to right
        for cycle in self:
            if cubie in cycle:
                i = cycle.index(cubie)
                orientation = cycle[i].orientation
                diff = (cubie.orientation - orientation) % len(cubie.string)
                next_cubie = Cubie(cycle[i + 1].string)
                for _ in range(diff):
                    next_cubie.rotate_cw()
                cubie = next_cubie
        return cubie

    def __call__(self, cubie):
        return self.permute(cubie)

    def __getitem__(self, index):
        return self.cycles[index % len(self.cycles)]

    def __iter__(self):
        return iter(self.cycles)

    def __repr__(self):
        # ignore one-cycles when printing out the permutation
        return ''.join([str(c) for c in self.cycles if len(c) > 1]) or '()'

    def __mul__(self, other):
        product = Permutation()

        # we need to check the effect of the multiplication on
        # any cubie that either permutation affects individually
        unchecked_cubies = list({cubie for cycle in self for cubie in cycle} |
                                {cubie for cycle in other for cubie in cycle})

        while unchecked_cubies:
            cubie = unchecked_cubies[0]
            if cubie in unchecked_cubies:
                unchecked_cubies.remove(cubie)
            current_cycle = [cubie]

            # keep building the current cycle until we
            # arrive back at the starting point
            while not (other.permute(self.permute(cubie)) == current_cycle[0] and
                       other.permute(self.permute(cubie)).orientation == current_cycle[0].orientation):
                cubie = other.permute(self.permute(cubie))
                current_cycle.append(cubie)
                if cubie in unchecked_cubies:
                    unchecked_cubies.remove(cubie)

            # have a finished cycle
            product.cycles.append(Cycle(*current_cycle))

        return product


C = Cycle
P = Permutation
