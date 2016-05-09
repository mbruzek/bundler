#!/usr/bin/env python

"""
This is the command line interface to the Bundler library.
"""

import argparse
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
    # Add a generic argument to optionally output to a file.
    parser.add_argument('-o', '--output', help=OUTPUT)
    # Create a subparser object for the subcommands.
    subparsers = parser.add_subparsers(dest='command', help='subcommands')
    # Create a parser with it's own options for the build subcommand.
    build_parser = subparsers.add_parser('build', help=BUILD)
    # Create a parser with it's own options for the local subcommand.
    local_parser = subparsers.add_parser('local', help=LOCAL)
    # Create a parser with it's own options for the update subcommand.
    update_parser = subparsers.add_parser('update', help=UPDATE)
    # The last argument should be the input file.
    parser.add_argument('input', help=INPUT)

    arguments = parser.parse_args()
    if arguments.input:
        try:
            bundler = Bundler(arguments.input)
            result = ''
            if arguments.command == 'build':
                result = bundler.build(arguments)
            elif arguments.command == 'local':
                result = bundler.make_local(arguments)
            elif arguments.command == 'update':
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
