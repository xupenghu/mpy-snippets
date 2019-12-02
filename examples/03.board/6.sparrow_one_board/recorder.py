#
# Copyright (c) 2006-2019, RT-Thread Development Team
#
# SPDX-License-Identifier: MIT License
#
# Change Logs:
# Date           Author       Notes
# 2019-11-29     SummerGift   first version
#

from recorder import recorder
import utime as time

record = recorder()
record.start("voice.wav")
time.sleep(5)
record.stop()
