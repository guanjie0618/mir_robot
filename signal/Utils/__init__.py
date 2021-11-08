import time
from datetime import datetime
from os import mkdir


# 取得時間並建立資料夾
def root_path():
    path = 'result/' + time.strftime('%Y%m%d-%H%M%S', time.localtime()) + '/'
    mkdir(path)
    return path


# 測量運行時間物件
class timeit:
    def __init__(self, title='Cost time: ', newLine=True):
        self.start = datetime.now()
        self.title = title
        self.newLine = '\n' if newLine else ' '

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{self.title}{datetime.now() - self.start}', end=self.newLine)
