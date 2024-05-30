import numpy as np

def calculate_rsi(prices, period=14):
    """
    Calculate the Relative Strength Index (RSI) for a given list of closing prices.

    Parameters:
    - prices (list or numpy array): List of closing prices.
    - period (int): RSI calculation period (default is 14).

    Returns:
    - rsi_values (numpy array): Array of RSI values.
    """

    # Calculate daily price changes
    price_changes = np.diff(prices)

    # Separate gains and losses
    gains = np.where(price_changes > 0, price_changes, 0)
    losses = np.where(price_changes < 0, -price_changes, 0)

    # Calculate average gains and losses over the specified period
    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])

    # Initialize RSI values
    rsi_values = np.zeros(len(prices) - period)

    # Calculate RSI for the remaining data
    for i in range(period, len(prices)):
        gain = gains[i - 1]
        loss = losses[i - 1]

        # Update average gains and losses using smoothing formula
        avg_gain = (avg_gain * (period - 1) + gain) / period
        avg_loss = (avg_loss * (period - 1) + loss) / period

        # Avoid division by zero
        if avg_loss == 0:
            rsi = 100
        else:
            # Calculate relative strength (RS)
            rs = avg_gain / avg_loss
            # Calculate RSI
            rsi = 100 - (100 / (1 + rs))

        # Store the calculated RSI value
        rsi_values[i - period] = rsi

    return rsi_values

# Example usage:
closing_prices = [50, 52, 48, 55, 53, 56, 57, 54, 51, 49, 52, 50, 48, 53]
rsi_values = calculate_rsi(closing_prices)

print("RSI Values:", rsi_values)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_rsi()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
