# -*- coding: utf-8 -*-
import re
import logging
from . import ecode

result = """
Отложенные ордера
#{}
BuyStop: {}
StopLoss: {}
TakeProfit: {}
**************
SellStop: {}
StopLoss: {}
TakeProfit: {}
**************
"""


def start(text):
    source = ecode(text)
    p1 = re.compile(r"buy-stop .+?п").findall(source)
    p2 = re.compile(r"sell-stop .+?п").findall(source)

    if not(p1 and p2):
        logging.warning("forex source: {}".format(source))
        logging.warning("p1: {}".format(p1))
        logging.warning("p2: {}".format(p2))

        return source

    try:
        l1 = p1[0].split()[:-2]
        l2 = p2[0].split()[:-2]
        ret = result.format(l1[1], l1[2], l1[3], l1[-1], l2[2], l2[3], l2[-1])
    except Exception as e:
        logging.warning("forex Exception: {}".format(e))
        return source

    return ret
