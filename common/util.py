#!/usr/bin/env python

import re
import os
import platform
import sys
import datetime
import commands
import argparse

args = ''

def get_datetime():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d%H%M%S")

def info(msg):
    print "[INFO] " + msg + "."

def error(msg):
    print "[ERROR] " + msg + "!"
    quit()

def execute(command, silent=False, interactive=False):
    if not silent:
        _cmd(command)

    if interactive:
        if os.system(command):
            error('Failed to execute')
            quit()
    else:
        result = commands.getstatusoutput(command)
        if result[0] != 0:
            error('Failed to execute')
            quit()

        return result[1]

def bashify(command):
    return 'bash -c "' + command + '"'

################################################################################

def _cmd(msg):
    print '[COMMAND] ' + msg