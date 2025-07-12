import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from utils.data_fetcher import fetch_live_data

def start_plot():
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)

    def animate(i):
        data = fetch_live_data()
        data = data.reset_index()
        times = data['Datetime']
        prices = data['Close']

        # Print to terminal as well
        print(data.tail(1)[['Datetime', 'Close', 'Volume']])

        line.set_data(times, prices)
        ax.set_xlim(times.min(), times.max())
        ax.set_ylim(prices.min(), prices.max())
        ax.set_title("Live Share Price")
        ax.set_xlabel("Time")
        ax.set_ylabel("Price")
        plt.xticks(rotation=45)
        return line,

    ani = animation.FuncAnimation(
        fig, animate, interval=5000, blit=False  # every 5 seconds
    )

    plt.tight_layout()
    plt.show()

