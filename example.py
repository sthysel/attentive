#!/bin/env python

from attentive import StoppableThread, set_signal_handler
from random import randint


class Man(StoppableThread):
    def __init__(self, name):
        StoppableThread.__init__(self)
        self.name = name

    def run(self):
        print('{} has quickened'.format(self.name))
        while not self.stopped:
            self.sleep(randint(1, 10))
            print('{} throws a {}'.format(self.name, randint(1, 6)))

        print('{} expires'.format(self.name))


if __name__ == '__main__':
    stopper = set_signal_handler()
    with Man('Trump'), Man('Wang'), Man('Erdoğan'):
        while not stopper.is_set():
            stopper.wait(1)

    print('God does not play dice')
