#!/usr/bin/env python

"""
This is the command line interface to the Bundler library.
"""

import argparse
import sys
import traceback

from lib.Bundler import Bundler


BUILD = 'Download and charm build all the charms and layers locally.'
INPUT = 'Input file name'
LOCAL = 'Convert to local bundle'
SUBCOMMANDS = ['build', 'local', 'update']
UPDATE = 'Update bundle to the latest revsions from the Charmstore'
OUTPUT = 'Output file name'


def command_line():
    """The function to parse the arguments from the command line."""
    description = 'A tool to manage your bundles.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-o', '--output',
                        help='{0} [{1}]'.format(OUTPUT, None))
    parser.add_argument('input', help=INPUT)
    parser.add_argument('-b', '--build', action='store_true', help=BUILD)
    parser.add_argument('-l', '--local', action='store_true', help=LOCAL)
    parser.add_argument('-u', '--update', action='store_true', help=UPDATE)

    arguments = parser.parse_args()
    if arguments.input:
        try:
            bundler = Bundler(arguments.input)
            result = ''
            if arguments.build:
                result = bundler.build(arguments)
            elif arguments.local:
                result = bundler.make_local(arguments)
            elif arguments.update:
                result = bundler.update(arguments)
            if result:
                if arguments.output:
                    with open(arguments.output, 'w') as file:
                        file.write(result)
                else:
                    print(result)
        except:
            traceback.print_exc()
            exit(1)
    else:
        print('Not enough arguments')
        parser.print_help()

if __name__ == '__main__':
    command_line()
