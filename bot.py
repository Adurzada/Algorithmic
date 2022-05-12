import sys
from traderlib import *
from logger import *

def check_account_ok():
    try:
        print("100 passed")
    except Exception as exx:
        lg.error("Could not get the acc info: 100")
        lg.info(str(exx))
        sys.exit('Exiting due to error 100')

def clean_open_orders():
    lg.info("List of open orders:")
    lg.info(str(open_orders))
    for (order in open_orders):
        lg.info('Order %s is closed', order)
    lg.info("Open order closing completed")


def exec_bot():
    init_logger()
    check_account_ok()
    clean_open_orders()
    ticker = input("Enter the ticker")
    ztrader = Trader
    ztrader.run()

if __name__ == '__main__':
    exec_bot()
