from __future__ import absolute_import

import logging
import signal
import sys
import threading
from contextlib import contextmanager

logger = logging.getLogger(__name__)
_stopper = threading.Event()


def _signal_handler(signal, frame):
    logger.info('signal {} received, stopping.'.format(signal))
    _stopper.set()
    sys.exit(0)


signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)


def set_signal_handler():
    return _stopper


@contextmanager
def managed_thread(thread):
    try:
        thread.start()
        yield thread
    finally:
        thread.stop()
        thread.join()


@contextmanager
def managed_process(process):
    try:
        yield process
    finally:
        process.terminate()


class StoppableThread(threading.Thread):
    """
    Stoppable Thread. 
    
    When implementing children, make use of the stopped property in the
    run() method to know when to stop and return from run() cleanly.
    """

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop_event = threading.Event()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
        self.join()
        return False

    def stop(self):
        logger.info('stopping thread class : {0}'.format(self.__class__.__name__))
        self._stop_event.set()

    @property
    def stopped(self):
        return self._stop_event.is_set()

    def sleep(self, seconds):
        self._stop_event.wait(seconds)


class StoppableWorker(StoppableThread):
    """
    Takes a callable and runs in a Stoppable Thread
    """

    def __init__(self, callable):
        """
        :param callable: Callable to run in Thread loop
        """
        super(StoppableWorker, self).__init__()

        self.callable = callable

    def run(self):
        while not self.stopped:
            self.callable()
