#!/usr/bin/env python

import sys
from three import *  # evil trick that allows eval to recognize cube notation


def sanitize_input(string):
    """
    Replace M2 with MM and M' with MMM in the input string, where M is
    any recognized basic Rubik's cube move {R, L, U, D, B, F, M, E, S},
    and then interpolate '*' between every letter. Return the resulting
    string.

    e.g. D2FR' -> D*D*F*R*R*R

    Also, throw a ValueError if unrecognized characters are in the input.
    """
    string = string.upper()
    res = []
    for char in string:
        if char in "RLUDBFMES":
            res += [char]
        elif char == "2":
            if res == []:
                raise ValueError('Bad input, cannot start expression with "2"!')
            res += [res[-1]]  # do the last move again
        elif char == "'":
            if res == []:
                raise ValueError('Bad input, cannot start expression with "\'"!')
            res += [res[-1], res[-1]]  # do the last move two more times
        else:
            raise ValueError("Unrecognized character '%c' in input!" % char)
    return '*'.join(res)


def run_interpreter():
    while True:
        user_input = input('> ').strip()
        if not user_input:
            continue
        if user_input.lower() in ['exit()', 'quit()', 'exit', 'quit', 'q']:
            break
        try:
            sanitized_input = sanitize_input(user_input)
        except ValueError as e:
            # input didn't make sense as a rubik's cube move,
            # print the error and move on
            print(e)
            continue
        print(eval(sanitized_input))


def main(argv=sys.argv):
    run_interpreter()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
