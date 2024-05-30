import numpy as np
import pandas as pd


class Supertrend:

    def calculate_supertrend(self,data, period=7, multiplier=3):
        high = data.h
        low = data.l
        close = data.c

        # Calculate True Range (TR)
        tr1 = np.maximum(high - low, abs(high - close.shift(1)))
        tr2 = np.maximum(tr1, abs(low - close.shift(1)))
        tr = pd.Series(tr2, name='TR')

        # data["tr"]

        # Average True Range (ATR)
        atr = tr.rolling(window=period).mean()

        # Supertrend calculation
        upper_band = (high + low) / 2 + multiplier * atr
        lower_band = (high + low) / 2 - multiplier * atr

        # uptrend_condition = close > lower_band
        # downtrend_condition = close < upper_band
        #
        # uptrend = pd.Series(np.nan, index=data.index)
        # downtrend = pd.Series(np.nan, index=data.index)
        #
        # uptrend[uptrend_condition] = lower_band[uptrend_condition]
        # downtrend[downtrend_condition] = upper_band[downtrend_condition]

        # return uptrend, downtrend
        return upper_band, lower_band

    # Example usage
    # data = pd.read_csv('your_price_data.csv')  # Replace with your actual price data file
    # data['Date'] = pd.to_datetime(data['Date'])
    # data.set_index('Date', inplace=True)
    #
    # # Adjust the period and multiplier as needed
    # supertrend_up, supertrend_down = calculate_supertrend(data, period=7, multiplier=3)
    #
    # # Add Supertrend columns to the DataFrame
    # data['Supertrend_Up'] = supertrend_up
    # data['Supertrend_Down'] = supertrend_down
    #
    # # Print or visualize the DataFrame with Supertrend values
    # print(data)

