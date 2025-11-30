import sys
import datetime

class Log:
    @staticmethod
    def _prefix():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def Info(msg: str):
        try:
            sys.stdout.write(f"[{Log._prefix()}] [INFO] {msg}\n")
            sys.stdout.flush()
        except Exception:
            pass

    @staticmethod
    def Error(msg: str):
        try:
            sys.stderr.write(f"[{Log._prefix()}] [ERROR] {msg}\n")
            sys.stderr.flush()
        except Exception:
            pass

    @staticmethod
    def Debug(msg: str):
        try:
            sys.stdout.write(f"[{Log._prefix()}] [DEBUG] {msg}\n")
            sys.stdout.flush()
        except Exception:
            pass
