import yfinance as yf
from config import TICKER

def fetch_live_data():
    data = yf.download(tickers=TICKER, period='1d', interval='1m')
    return data
