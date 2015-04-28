#!/usr/bin/python

import argparse
import os
import shutil
import sphinx
import sys


BUILDDIR = '_build'
OUTDIR = os.path.join(os.path.join('..', 'kang'), 'doc')

opts = [sys.argv[0],
            '-b', 'html',
            '-d', os.path.join(BUILDDIR, 'doctrees'),
            '.',
            OUTDIR
        ]


def parse_cmdline():
    parser = argparse.ArgumentParser(description='Build Kang documentation using Sphinx')
    parser.add_argument('-k', '--keep-build', dest='keep_build', action='store_true', help='keep build directory')
    
    return parser.parse_args()


if __name__ == '__main__':
    
    args = parse_cmdline()
    
    _, name = os.path.split(opts[0])    
    print('%s %s' % (name, ' '.join(opts[1:])))
    ret = sphinx.main(opts)
    if ret != 0:
        sys.exit(ret)
        
    if not args.keep_build:
        print('Removing build dir')
        shutil.rmtree(BUILDDIR, ignore_errors=True)
    
        print('Removing build info')
        os.remove(os.path.join(OUTDIR, '.buildinfo'))
        
    print('Removing out sources')
    shutil.rmtree(os.path.join(OUTDIR, '_sources'), ignore_errors=True)
