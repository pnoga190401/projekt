#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)
    print('wylosowano:', liczba)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))