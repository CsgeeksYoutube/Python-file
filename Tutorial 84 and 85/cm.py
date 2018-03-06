class LoggingContextManager:
    def __enter__(self):
        print('logging context manager csgeeks')
        return 'You are super'

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('vijay csgeeks youtube channel')

        else:
            print('type= {}, value= {}, traceback={}'.format(exc_type,exc_val,exc_tb))