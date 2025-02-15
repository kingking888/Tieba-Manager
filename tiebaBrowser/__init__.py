# -*- coding:utf-8 -*-
"""
@Version 2.6.1
@Author: starry.qvq@gmail.com
@License: Unlicense
@Homepage: https://github.com/Starry-OvO/Tieba-Cloud-Review
@Require Python 3.10+
@Required Modules: pyyaml aiohttp[speedups] protobuf lxml beautifulsoup4 pycrytodome aiomysql opencv-contrib-python
"""

import asyncio
import signal
import sys

from ._api import *
from ._logger import *
from ._types import *
from .reviewer import *

log = get_logger()


def terminate(signal_number, frame):
    raise KeyboardInterrupt


signal.signal(signal.SIGTERM, terminate)

if sys.platform == "win32" and sys.version_info.minor >= 8:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
