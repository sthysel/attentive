from __future__ import absolute_import

import logging
import signal
import threading

logger = logging.getLogger(__name__)

quitevent = threading.Event()

default_signals = [signal.SIGINT, signal.SIGTERM]


def _quit_handler(signal, frame):
    logger.info('signal {} received, stopping.'.format(signal))
    quitevent.set()


for _sig in default_signals:
    signal.signal(_sig, _quit_handler)

