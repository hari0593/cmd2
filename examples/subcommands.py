#!/usr/bin/env python
# coding=utf-8
"""A simple example demonstrating how to use Argparse to support sub-commands.


This example shows an easy way for a single command to have many subcommands, each of which takes different arguments
and provides separate contextual help.
"""
import argparse

import cmd2
from cmd2 import with_argument_parser


class SubcommandsExample(cmd2.Cmd):
    """ Example cmd2 application where we a base command which has a couple subcommands."""

    def __init__(self):
        cmd2.Cmd.__init__(self)

    # sub-command functions for the base command
    def foo(self, args):
        """foo subcommand of base command"""
        print(args.x * args.y)

    def bar(self, args):
        """bar sucommand of base command"""
        print('((%s))' % args.z)

    # create the top-level parser
    base_parser = argparse.ArgumentParser(prog='base')
    base_subparsers = base_parser.add_subparsers(title='subcommands', help='subcommand help')

    # create the parser for the "foo" command
    parser_foo = base_subparsers.add_parser('foo', help='foo help')
    parser_foo.add_argument('-x', type=int, default=1, help='integer')
    parser_foo.add_argument('y', type=float, help='float')
    parser_foo.set_defaults(func=foo)

    # create the parser for the "bar" command
    parser_bar = base_subparsers.add_parser('bar', help='bar help')
    parser_bar.add_argument('z', help='string')
    parser_bar.set_defaults(func=bar)

    @with_argument_parser(base_parser)
    def do_base(self, args):
        """Base command help"""
        try:
            # Call whatever sub-command function was selected
            args.func(self, args)
        except AttributeError:
            # No sub-command was provided, so as called
            self.do_help('base')


if __name__ == '__main__':
    app = SubcommandsExample()
    app.cmdloop()
