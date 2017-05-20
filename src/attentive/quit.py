from __future__ import absolute_import

import logging
import signal
import threading

logger = logging.getLogger(__name__)

quit = threading.Event()


def _signal_handler(signal, frame):
    logger.info('signal {} received, stopping.'.format(signal))
    quit.set()


signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)
