#!/usr/bin/python2.7
"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import logging

from pyOCD.gdbserver import GDBServer
from pyOCD.board import MbedBoard

logging.basicConfig(level=logging.INFO)

try:
    board_selected = MbedBoard.chooseBoard()
    if board_selected != None:
        gdb = GDBServer(board_selected, 3333)
        while gdb.isAlive():
            gdb.join(timeout = 0.5)

except KeyboardInterrupt:
    gdb.stop()
except Exception as e:
    print "uncaught exception: %s" % e
    gdb.stop()
