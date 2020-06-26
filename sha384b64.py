#!/usr/bin/env python3

import base64
import hashlib


def sha384b64(filename):
    # Not very efficient for large files, but whatever.
    with open(filename, 'rb') as fp:
        content = fp.read()
    return base64.b64encode(hashlib.sha384(content).digest())


def run_args(files):
    for f in files:
        use_file = f
        if use_file == '-':
            use_file = '/dev/stdin'
        print('{}\t{}'.format(sha384b64(use_file), f))


def run():
    import sys

    if len(sys.argv) == 1:
        run_args(['-'])
    else:
        run_args(sys.argv[1:])


if __name__ == '__main__':
    run()
