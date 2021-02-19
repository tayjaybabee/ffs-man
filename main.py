# ****** main.py ****** #
# Description:
# Time of Creation: 2/4/21 at 1:39 PM
# Author: Taylor-Jayde J. Blackstone <t.blackstone@inspyre.tech>
# ************************d #
import ffs_man.cache as cache_man
from ffs_man.args import ArgParser, Path, default_app_path_str
from ffs_man.GUI.popups import where_app_dir
from inspy_logger import getLogger, InspyLogger


def start_logger(level):
    ins_logger = InspyLogger()
    log_device = ins_logger.LogDevice('FFS-Man', level)
    logger = log_device.start()

    log = getLogger('FFS-Man.start_logger')
    log.debug(f'Logger started! {logger.name}')

    return logger


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    arg_parser = ArgParser()
    args = arg_parser.args

    app_dir = Path(args.app_dir).expanduser().exists()

    log = start_logger(args.log_level)

    import ffs_man.config as config

    if config.exists(Path(args.app_dir).joinpath('config/conf.ini')):
        config.load(args.app_dir)

    if args.log_level == 'DEBUG':
        arg_list = []

        for key in args.__dict__:
            item = str(str(key) + ': ' + str(args.__dict__[key]))
            arg_list.append(item)

        arg_str = ' | '.join(arg_list)

        log.debug(f"Received from command line: {arg_str}")

    if cache_man.has_cache():
        cache = cache_man.load()
    else:
        app_dir = str(Path(args.app_dir).expanduser().resolve())
        if default_app_path_str == app_dir:
            app_dir = where_app_dir()
        cache = cache_man.create(app_dir=app_dir)

    APP_DIR = cache['FFS-MAN']['data_dir']

    log.debug(f"Determined app directory: {APP_DIR}")
