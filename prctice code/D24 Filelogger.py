class FileLogger:
    def __init__(self , filename):
        self.filenaame = filename
        self.filecontext = None

    def __enter__(self):
        self.filecontext = open(self.file , "a" , encoding="utf-8")
        return self.filecontext
    
    def __exit__(self, exc_type, exc, tb):
        self.filecontext.close()

with FileLogger("log.txt") as f:
    f.write("日志开始\n")
    f.write("日志结束\n")