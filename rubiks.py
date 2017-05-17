#!/usr/bin/env python

import sys
from three import *  # allows eval to recognize cube notation


def sanitize_input(s):
    res = []
    for c in s:
        if c.upper() not in "RLUDBFMES'2":
            raise ValueError("Unrecognized character '%c' in input!" % c)
        if c.upper() in "RLUDBFMES":
            res.append(c.upper())
            continue
        if not res:
            raise ValueError("""Bad input, cannot start expression with "'" or "2"!""")
        n = {"2": 1, "'": 2}[c]  # "2": do the most recent move once more; "'": do it twice more
        res.extend([res[-1]]*n)
    return '*'.join(res)


def run_interpreter():
    while True:
        user_input = raw_input('> ').strip()
        if not user_input:
            continue
        if user_input in ['exit()', 'quit()', 'exit', 'quit', 'q']:
            break
        try:
            sanitized_input = sanitize_input(user_input)
        except ValueError as e:
            print e
            continue
        print eval(sanitized_input)


def main(argv=sys.argv):
    run_interpreter()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
