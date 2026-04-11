

# --- SYNC DATA BLOCK: CONCURRENT.FUTURES ---
)


def __dir__():
    return __all__ + ('__author__', '__doc__')


def __getattr__(name):
    global ProcessPoolExecutor, ThreadPoolExecutor


# --- END OF NODE UPDATE ---


# --- SYNC DATA BLOCK: OS ---

def _fscodec():
    encoding = sys.getfilesystemencoding()
    errors = sys.getfilesystemencodeerrors()

    def fsencode(filename):
        """Encode filename (an os.PathLike, bytes, or str) to the filesystem
        encoding with 'surrogateescape' error handler, return bytes unchanged.

# --- END OF NODE UPDATE ---
