#!/usr/bin/env python

import sys
from three import *


def sanitize_input(s):
    stack = []
    for c in s:
        if c.upper() not in "RLUDBFMES'2":
            raise ValueError("Unrecognized character '%c' in input!" % c)
        if c.upper() in "RLUDBFMES":
            stack.append(c.upper())
            continue
        n = {"2": 1, "'": 2}[c]
        if not stack:
            raise ValueError("""Bad input, cannot start expression with "'" or "2"!""")
        stack.extend([stack[-1]]*n)
    return '*'.join(stack)


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
