class LoggingContextManager:
    def __enter__(self):
        print('logging context manager csgeeks')
        return 'You are super'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('logging context manager.__exit__({}, {}, {})'.format(
            exc_type,exc_val,exc_tb
        ))
        return