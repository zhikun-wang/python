#!/usr/local/bin/python3

import platform

print(platform.python_version())

from ex42 import GuessNumber

game = GuessNumber(5)
game.start()
