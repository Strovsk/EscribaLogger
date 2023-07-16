import logging
from logging import LogRecord


class FullContext(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        default_keys = [
            "name",
            "msg",
            "args",
            "levelname",
            "levelno",
            "pathname",
            "C",
            "filename",
            "module",
            "exc_info",
            "exc_text",
            "stack_info",
            "lineno",
            "funcName",
            "created",
            "msecs",
            "relativeCreated",
            "thread",
            "threadName",
            "processName",
            "process",
        ]
        return True
