from datetime import datetime

class FileBasedLogger:
    def __init__(self, filename: str):
        self.filename = filename

    def open_file(self):
        self.file = open(self.filename, 'a')

    def log(self, msg: str):
        self.file.write(f'[{datetime.now()}] {msg}\n')
