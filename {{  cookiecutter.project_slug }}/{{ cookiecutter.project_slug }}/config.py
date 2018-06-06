"""
config.py
"""
from logging import config as logging_config

from envparse import env

DEBUG: bool = env('DEBUG', default=False)
LOG_LEVEL: str = env('LOG_LEVEL', default='WARNING')
NODE_NAME: str = env('NODE_NAME')


def setup_logging():
    logging_config.dictConfig({
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': '[%(asctime)s] %(name)s (message)s @%(funcName)s:%(lineno)d #%(levelname)s'

            }
        },
        'handlers': {
            'console': {
                'formatter': 'standard',
                'class': 'logging.StreamHandler'
            }
        },
        'loggers': {
            'root': {
                'handlers': ['console'],
                'level': LOG_LEVEL
            }
        }
    })
