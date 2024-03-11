from datetime import datetime


class RedirectErrorCM:
    def __init__(self, file_name):
        self._file_name = file_name

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            now = datetime.now().isoformat()
            with open(self._file_name, 'a') as err_file:
                err_file.write(f'{exc_type=}; {exc_val=}; {now=}' + '\n')
                # appending new lines
        return False
        # reraising exception if False


with RedirectErrorCM('err_file.txt') as cm:
    x = 1/0
print('we should not get here if _exit_ returns False')
