#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""coding-on-paper module

This takes OCR output from code.png, display it (unless -f is set),
then eval() the code.
"""
# Copyright (C) 2024  2NumForIce
#
# coding-on-paper is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# coding-on-paper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with coding-on-paper. If not, see
# <https://www.gnu.org/licenses/>.

from PIL import Image
import pytesseract
import os
import sys
import time

preserve_interword_spaces = True

print('Scan to ./code.png, or put a PNG file there. Press ^C to cancel.')

# Check if code.png exists every second
while not os.path.isfile('code.png'):
    time.sleep(1)
print('Found it! Scanning...')

# OCR the image
code = pytesseract.image_to_string(Image.open('code.png'),
    config='-c preserve_interword_spaces=1')

# User confirm code
print('\n'
      '      Code area\n'
      '-*-*-*-*-*-*-*-*-*-*-\n' + code + '-*-*-*-*-*-*-*-*-*-*-\n')
try:
    if sys.argv[1] == "-f":
        argv = True
except IndexError:
    argv = False
finally:
    if argv or input(
            "Is this correct? (don't want to blow up your computer or "
            "something)\ny/N:") == "y":
        print('\n'
              '     Output area\n'
              '-*-*-*-*-*-*-*-*-*-*-')
        eval(code)
        print('-*-*-*-*-*-*-*-*-*-*-')
    else:
        exit(1)
