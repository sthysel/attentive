#!/bin/env python

from attentive import StoppableThread, quitevent
from random import randint

toys = ('☢', '☣', '🍭', '🍼',)


class Man(StoppableThread):
    def __init__(self, name):
        StoppableThread.__init__(self)
        self.name = name

    def run(self):
        print('🚼{} has quickened'.format(self.name))
        while not self.stopped:
            self.sleep(randint(1, 5))
            print('{} throws a {}'.format(self.name, toys[randint(0, len(toys)) - 1]))

        print('☠{} expires'.format(self.name))


if __name__ == '__main__':
    with Man('Trump'), Man('Wang'), Man('Erdoğan'):
        while not quitevent.is_set():
            quitevent.wait(1)

    print('God does not play dice')
