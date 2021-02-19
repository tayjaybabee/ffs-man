# ****** ffs_man/cache.py ****** #
# Description: Contains methods for dealing with a cache file.
# Time of Creation: 2/4/21 at 2:01 PM
# Author: Taylor-Jayde J. Blackstone <t.blackstone@inspyre.tech>
# ************************ #
from pathlib import Path
from configparser import ConfigParser
from os import makedirs


class MalformedCacheFileError(Exception):
    def __init__(self, fp):
        message = f"Unable to find a properly formatted cache file at {fp}"
        print(message)


cache_struct = {
    'FFS-MAN': {
        'data_dir': ''
    }
}
"""
A dictionary of information that should be included in a proper cache-file
"""


CACHE_FILEPATH = Path('~/.cache/Inspyre-Softworks/ffs-man/ffs.ini').expanduser().resolve()


def has_cache():
    """

    Check '$HOME/.cache/Inspyre-Softworks/ffs-man' for a  file named 'ffs.ini'

    Returns:

        True (bool): There is a file named 'ffs.ini' in the needed place

        False (bool): There is no directory for this file to exist in, therefore it doesn't exist.

    NOTE:
        Receiving anything other than a single boolean (True) from this function is an indicator of cache malfeasance

    """

    if CACHE_FILEPATH.parent.exists():
        if CACHE_FILEPATH.exists() and CACHE_FILEPATH.is_file():
            return True
        else:
            return False
    else:
        return False


def write(cache):
    with open(CACHE_FILEPATH, 'w') as fp:
        cache.write(fp)
    print("Cache written!")


def create(app_dir):
    """

    Create a new cache file at '$HOME/.cache/Inspyre-Softworks/ffs-man/ffs.ini'

    Returns:

    """
    global cache_struct
    makedirs(CACHE_FILEPATH.parent, exist_ok=True)
    makedirs(app_dir, exist_ok=True)
    parser = ConfigParser()
    parser.read_dict(cache_struct)
    parser['FFS-MAN']['data_dir'] = app_dir
    write(parser)

    return parser


def load():
    """

    Load a cache file from the disk and return an initialized and filled ConfigParser with some vital information, the
    most important of which is the location of the FFS-Man config file and host manifest.

    Returns:

    """
    parser = ConfigParser()
    parser.read(CACHE_FILEPATH)

    if 'FFS-MAN' in parser.sections():
        return parser
    else:
        raise MalformedCacheFileError(CACHE_FILEPATH)



def replace():
    """

    Delete any file with path '$HOME/.cache/Inspyre-Softworks/ffs-man/ffs.ini' and create a new one.

    Returns:
        None

    """