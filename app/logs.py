from logging.config import dictConfig


def setuplog(config):
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "tasker": {
                    "format": "[%(asctime)s] [%(levelname)s] | %(module)s.%(funcName)s | %(message)s",
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "formatter": "tasker",
                },
                "size-rotate": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": config.LOG_DIR + config.LOG_FILENAME,
                    "maxBytes": 10000000,
                    "backupCount": 5,
                    "formatter": "tasker",
                },
            },
            "root": {"level": "DEBUG", "handlers": ["console", "size-rotate"]},
        }
    )

    return dictConfig
