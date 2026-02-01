import yfinance as yf
import pandas as pd 
import matplotlib.pyplot as plt
import time

class bitcoin_bot:
    def __init__(self, ticker="BTC-USD"):
        self.ticker = ticker
        self.bitcoin_possession = False  # initialize bot's memory
        self.signal_history = []  # store the history of signals
        
    def fetch_market_data(self):  # fetch 1h interval data for the last 2 days
        df = yf.download(self.ticker, period="2d", interval="1h", progress=False)
        current_price = df.iloc[-1]['Close']  # iloc[-1] retrieves the last row and 'Close' specifies the closing price column.
        previous_price = df.iloc[-2]['Close']  # iloc[-2] retrieves the second to last row for comparison
        timestamp = df.index[-1]
        return df, float(current_price), float(previous_price), timestamp

    def execute_logic(self):
        df, current_price, previous_price, timestamp = self.fetch_market_data()

        print(f"[{timestamp}] Price: ${current_price:.2f}")

        # we are checking the trend following and also we ensure we don't already have the asset
        if current_price > previous_price and not self.bitcoin_possession: 
            print("SIGNAL: BUY")
            self.bitcoin_possession = True # transaction details updated
            self.signal_history.append({
                "timestamp": timestamp, 
                "price": current_price, 
                "action": "BUY"
            })
        # here we check for a downward trend and ensure we have the asset to sell
        elif current_price < previous_price and self.bitcoin_possession: 
            print(">>> SIGNAL: SELL")
            self.bitcoin_possession = False  # we update the memory to "empty"
            self.signal_history.append({
                "timestamp": timestamp, 
                "price": current_price, 
                "action": "SELL"
            })

    def plot_signals(self):
        df, _, _, _ = self.fetch_market_data()
        plt.figure(figsize=(12, 6))
        plt.plot(df.index, df['Close'], label='Bitcoin Price', color='royalblue', alpha=0.5)
        
        if self.signal_history:
            history_df = pd.DataFrame(self.signal_history)
            buys = history_df[history_df['action'] == "BUY"]
            sells = history_df[history_df['action'] == "SELL"]
            plt.scatter(buys['timestamp'], buys['price'], marker='^', color='green', s=100, label='BUY Signal')
            plt.scatter(sells['timestamp'], sells['price'], marker='v', color='red', s=100, label='SELL Signal')

        plt.title(f"Trading Strategy Visualizer - {self.ticker}")
        plt.xlabel("Time")
        plt.ylabel("Price ($)")
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

# Execution logic
bot = bitcoin_bot()

for _ in range(3):
    bot.execute_logic()
    time.sleep(2) 

bot.plot_signals()