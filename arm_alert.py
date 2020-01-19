#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

secs = 10

def show_message(message):
    # For python2 and python3
    try:
        print (message)
    except:
        print(message)

show_message("Sorry, blender can't run in your computer (Arch: ARM)")
show_message("Closing activity")

while True:
    show_message(secs)

    secs -= 1
    if (secs < 1):
        break

    time.sleep(1)


sys.exit(0)
