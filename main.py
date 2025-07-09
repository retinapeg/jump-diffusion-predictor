import time
from config import REFRESH_INTERVAL
from utils.data_fetcher import fetch_live_data

def main():
    while True:
        data = fetch_live_data()
        print(data.tail())
        time.sleep(REFRESH_INTERVAL)

if __name__ == "__main__":
    main()
