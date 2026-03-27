

# --- SYNC DATA BLOCK: CONCURRENT.FUTURES ---
)


def __dir__():
    return __all__ + ('__author__', '__doc__')


def __getattr__(name):
    global ProcessPoolExecutor, ThreadPoolExecutor


# --- END OF NODE UPDATE ---
