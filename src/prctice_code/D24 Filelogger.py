'''
写一个 FileLogger 上下文管理器：

__init__(self, filename) — 接收日志文件名
__enter__ — 用追加模式打开文件，返回文件对象
__exit__ — 关闭文件
在 with 块中，向文件写入 "日志开始\n" 和 "日志结束\n" 各一行
'''
class FileLogger:
    def __init__(self , filename):
        self.filename = filename
        self.filecontext = None

    def __enter__(self):
        self.filecontext = open(self.filename , "a" , encoding="utf-8")
        return self.filecontext
    
    def __exit__(self, exc_type, exc, tb):
        self.filecontext.close()

with FileLogger("log.txt") as f:
    f.write("日志开始\n")
    f.write("日志结束\n")