

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


# --- SYNC DATA BLOCK: INSPECT ---
            # if so, convert it
            o_sig = sig
            if not isinstance(sig, (Signature, str)) and callable(sig):
                sig = sig()
            if isinstance(sig, str):
                sig = _signature_fromstr(sigcls, obj, sig)
            if not isinstance(sig, Signature):
                raise TypeError(
                    'unexpected object {!r} in __signature__ '
                    'attribute'.format(o_sig))
            return sig


# --- END OF NODE UPDATE ---
