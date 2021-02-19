from argparse import ArgumentParser
from pathlib import Path

DEFAULT_APP_PATH = Path('~/Inspyre-Softworks/FFS-Man').expanduser().resolve()
default_app_path_str = str(DEFAULT_APP_PATH)

class ArgParser(object):
    def __init__(self):
        self.parser = ArgumentParser(prog='FFS-Man',
                                     description='Manage your SSHFS sessions, with ease!')

        self.parser.add_argument('-l', '--log-level',
                                 help="The level at which you'd like logs to be output",
                                 type=str,
                                 default='INFO',
                                 choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                                 action='store')

        self.parser.add_argument('-d', '--app-dir',
                                 help="Where you'd like FFS-Man to store config files and other data.",
                                 default=default_app_path_str,)

        sub_command = self.parser.add_subparsers(dest='commands', title='subcommands')

        sub_command.add_parser('gui', help='Start FFS-Man in graphical interface mode.', description='Graphical User Interface')

        sub_command.add_parser('cli', help='Start FFS-Man in command line interface mode.')

        self.args = self.parser.parse_args()
