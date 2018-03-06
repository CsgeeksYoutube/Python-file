import contextlib
import sys

@contextlib.contextmanager
def logging_context_manager():
    print('logging')
    try:
        yield 'you are in a with block'
        print('logging context manager:normal')
    except Exception:
        print('exceptional exit', sys.exc_info())