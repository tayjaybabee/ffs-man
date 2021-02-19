# ****** ffs_man/config.py ****** #
# Description: A module for the ffs_man package that loads/creates/replaces/etc the config files for FFS-Man
# Time of Creation: 2/18/21 at 11:20 PM
# Author: Taylor-Jayde J. Blackstone <t.blackstone@inspyre.tech>
# ************************ #
from configparser import ConfigParser
from pathlib import Path
from inspy_logger import getLogger

MOD_LOGNAME = 'FFS-Man.cache'

def exists(fp):
    fp = Path(fp).expanduser().resolve()
    fp_str = str(fp)
    if fp.parent.exists():
        if fp.exists() and fp.is_file():
            return True
        else:
            return False
    else:
        raise NotADirectoryError(fp.parent)


def create(fp):
    pass


def load(fp):
    log = getLogger(str(MOD_LOGNAME + '.load'))
    parser = ConfigParser()
    parser.read(fp)
    log.debug(f"Loaded a config file with the following sections: {parser.sections()}")

