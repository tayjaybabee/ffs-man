from ffs_man import cache as cache_man


class FFSMan(object):
    def __init__(self):
        if not cache_man.has_cache():
            cache_man.create()

        cache = cache_man.load()
