# -*- coding: utf-8 -*-

source = """
AUDUSD NEW SIGNAL

2018.03.22 10:05:36AUDUSD #33557610BUY Above: 0.7754StopLoss: 0.7726TakeProfit: 0.7810
"""

result = """AUDUSD NEW SIGNAL

2018.03.22 10:05:36
AUDUSD #33557610
BUY Above: 0.7754
StopLoss: 0.7726
TakeProfit: 0.7810"""

source1 = """
EURGBP NEW PENDING ORDER 

2018.03.22 14:00:04EURGBP #33559469SELL Below: 0.8691StopLoss: 0.8742TakeProfit: 0.8589
"""

result1 = """EURGBP NEW PENDING ORDER 

2018.03.22 14:00:04
EURGBP #33559469
SELL Below: 0.8691
StopLoss: 0.8742
TakeProfit: 0.8589"""

source2 = """
EURGBP CLOSED % LOT AND BREAKEVEN

2018.03.22 14:00:14 EURGBP #33559469SELL Trade: 0.8691Close Price: 0.8672Profit of 190 p
"""

result2 = """EURGBP CLOSED % LOT AND BREAKEVEN

2018.03.22 14:00:14
 EURGBP #33559469
SELL Trade: 0.8691
Close Price: 0.8672
Profit of 190 p"""

source3 = """
XAUUSD CLOSED % LOT AND BREAKEVEN

2018.03.22 14:30:06 XAUUSD #33559505BUY Trade: 1329.90Close Price: 1331.50Profit of 160 p
"""

result3 = """XAUUSD CLOSED % LOT AND BREAKEVEN

2018.03.22 14:30:06
 XAUUSD #33559505
BUY Trade: 1329.90
Close Price: 1331.50
Profit of 160 p"""

source4 = """
XAUUSD CLOSED 50% LOT AND BREAKEVEN

2018.03.26 01:00:57 XAUUSD #33566961BUY Trade: 1343.30Close Price: 1347.60Profit of 430 p
"""

result4 = """XAUUSD CLOSED 50% LOT AND BREAKEVEN

2018.03.26 01:00:57
 XAUUSD #33566961
BUY Trade: 1343.30
Close Price: 1347.60
Profit of 430 p"""

broken1 = """
AUDUSD NEW SIGNAL

2018.03.22 10:05:36AUDUSD #33557610BUY Above: 0.7754StopLoss: 0.7726Take: 0.7810
"""

broken2 = """
AUDUSD NEW SIGNAL

2018.03.22 10:05:36AUDUSD #33557610BUY Above: 0.7754Stop: 0.7726Take: 0.7810
"""

broken3 = """
EURGBP NEW PENDING ORDER 

2018.03.22 14:00:04EURGBP #33559469SELL Below: 0.8691StopLoss: 0.8742Take: 0.8589
"""

broken4 = """
EURGBP NEW PENDING ORDER 

2018.03.22 14:00:04EURGBP #33559469SELL Below: 0.8691Stop: 0.8742Take: 0.8589
"""

broken5 = """
EURGBP CLOSED % LOT AND BREAKEVEN

2018.03.22 14:00:14 EURGBP #33559469SELL Trade: 0.8691Close Price: 0.8672Profit 190 p
"""

broken6 = """
EURGBP CLOSED % LOT AND BREAKEVEN

2018.03.22 14:00:14 EURGBP #33559469SELL Trade: 0.8691Close: 0.8672Profit 190 p
"""

broken7 = """
XAUUSD CLOSED % LOT AND BREAKEVEN

2018.03.22 14:30:06 XAUUSD #33559505BUY Trade: 1329.90Close: 1331.50Profit of 160 p
"""
