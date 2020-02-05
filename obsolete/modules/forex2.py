import logging

templ = "2018.03.22 10:05:36"

BUY_ABOVE = "BUY Above: "
SELL_BELLOW = "SELL Below: "
SELL_TRADE = "SELL Trade: "
BUY_TRADE = "BUY Trade: "

STOP_LOSS = "StopLoss: "
TAKE_PROFIT = "TakeProfit: "
CLOSE_PRICE = "Close Price: "
PROFIT_OF = "Profit of "


def proc_line(text, lst, m0, m1, m2):
    i = text.find(m0)
    lst.append(text[len(templ):i])  # AUDUSD #33557610

    i1 = text.find(m1)
    if i1 == -1:
        logging.debug("err {} {}".format(m0, m1))
        return False

    lst.append(text[i:i1])  # BUY Above: 0.7754

    i2 = text.find(m2)
    if i2 == -1:
        logging.debug("err {} {}".format(m0, m2))
        return False

    lst.append(text[i1:i2])
    lst.append(text[i2:])
    logging.debug("ok")

    return True


def start(source):
    logging.debug("forex2: {}".format(source))

    lst = source.splitlines()
    while not lst[0].strip():
        lst = lst[1:]

    text = lst[-1]
    lst = lst[:-1]

    lst.append(text[:len(templ)])

    if BUY_ABOVE in text:
        if not proc_line(text, lst, BUY_ABOVE, STOP_LOSS, TAKE_PROFIT):
            return source
    elif SELL_BELLOW in text:
        if not proc_line(text, lst, SELL_BELLOW, STOP_LOSS, TAKE_PROFIT):
            return source
    elif SELL_TRADE in text:
        if not proc_line(text, lst, SELL_TRADE, CLOSE_PRICE, PROFIT_OF):
            return source
    elif BUY_TRADE in text:
        if not proc_line(text, lst, BUY_TRADE, CLOSE_PRICE, PROFIT_OF):
            return source
    else:
        logging.debug("err0")
        return source

    return '\n'.join(lst)
