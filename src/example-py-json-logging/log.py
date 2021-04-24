import logging
import logging.config
import json

ATTR_TO_JSON = [
    "created",
    "filename",
    "funcName",
    "levelname",
    "lineno",
    "module",
    "msecs",    
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "thread",
    "threadName",
]


class JsonFormatter:
    def format(self, record):
        obj = {attr: getattr(record, attr) for attr in ATTR_TO_JSON}
        return json.dumps(obj)


handler = logging.StreamHandler()
handler.formatter = JsonFormatter()
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

