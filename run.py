#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of oDAIa package               #
# Website: https://odaia.jgwill.com                       #
# GitHub:  https://github.com/jgwill/odaia   #
# MIT License                                        #
# Redistributed: JGwill                              #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2023.12.05 22:00:00                  #
# ================================================== #

import sys
from pathlib import Path

sys.path.insert(0, str((Path(__file__).parent / 'src').resolve()))

from pygpt_net.app import run

if __name__ == '__main__':
    run()
