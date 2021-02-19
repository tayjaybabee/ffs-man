from pathlib import Path


class MalformedCachefileError(Exception):
    def __init__(self, fp=None):
        """

        An exception that can be raised to indicate that a the program attempted to load a malformed cachefile.

        Args:
            fp:
        """
        if fp is None:
            fp = Path("~/.cache/Inspyre-Softworks/FFS-Man/ffs-man.ini").expanduser().resolve()

        self.message = f"The cache-file located at {fp} could not be loaded."
        self.msg = self.message
