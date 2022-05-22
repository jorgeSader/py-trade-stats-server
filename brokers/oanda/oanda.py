''' The Oanda module is meant to contain all the logic required to act as proxi server and consolidate the data format of all brokers into the one we want for MyTradeStats.'''

import pandas as pd
import tpqoa

api = tpqoa.tpqoa('./oanda.cfg')

def get_acct_id():
  return api.account_id
  
def get_acct_type():
  return api.account_type

def get_instruments():
  return api.get_instruments()

def get_account_summary():
  return api.get_account_summary

def get_price_history(instrument, start, end, granularity, price):
  return api.get_history(instrument, start, end, granularity, price)

def get_transactions(transIdList):
  return api.get_transactions(transIdList)

def create_order(instrument, units):
  return api.create_order(instrument, units)
  
def retrieve_data(instrument, start, end, granularity, price):
  return api.retrieve_data(instrument, start, end, granularity, price)

