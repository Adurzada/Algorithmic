import sys
import time


class Trader:
    def __init__(self, ticker):
        lg.info("Trader %s", ticker)

    def is_tradeable(self, ticker):
        try:
            if not asset.tradable:
                lg.info('Not tradable 300')
                return False
            else:
                return True
        except Exception as ex:
            lg.error('Exception at 300')
            lg.info(str(ex))
            return False


    def set_stoploss(self, entryPrice, direction):
        stoplossmargin = 0.05
        try:
            if direction=='long':
                stoploss=entryPrice-entryPrice*stoplossmargin
                return stoploss
            elif direction=='short':
                stoploss=entryPrice+entryPrice*stoplossmargin
                return stoploss
            else:
                lg.error('Indicent entry 201')
                raise ValueError
        except Exception as ex:
            lg.error('Error at 201')
            lg.info(str(ex))
            sys.exit()

    def set_takeprofit(self, entryprice, direction):
        takeprofitmargin=0.1
        try:
            if direction == 'long':
                takeprofit = entryprice+entryprice*takeprofitmargin
                return takeprofit
            elif direction == 'short':
                takeprofitmargin = entryprice-entryprice*takeprofitmargin
            else:
                lg.error('Indicent entry 202')
                raise ValueError
        except Exception as ex:
            lg.error('Error at 201')
            lg.info(str(ex))
            sys.exit()


    def get_openposition(self, assetid):
        for position in positions:
            if position.symbol == assetid:
                return True
            else:
                return False


    def check_position(self, assetId):
        maxAttempts = 5
        attempt = 0
        while attempt <= maxAttempts:
            try:
                currentPrice = position.current_price
                lg.info('Current price of %s is %.2f', assetId, currentPrice)
                return True
            except Exception as ex:
                lg.error('Position %s not found, error 200-210', assetId)
                time.sleep(5000)
                attempt+=1
                return false



    def run(self):
