def calculate_position_size(account_balance, risk_percentage, entry_price, stop_loss_price):
    """
    Calculate position size based on risk percentage, entry price, and stop-loss price.

    Parameters:
    - account_balance (float): Total account balance.
    - risk_percentage (float): Percentage of account balance to risk per trade.
    - entry_price (float): Entry price of the trade.
    - stop_loss_price (float): Stop-loss price of the trade.

    Returns:
    - position_size (float): Number of units or contracts for the trade.
    """

    # Calculate the dollar amount at risk per trade
    risk_per_trade = account_balance * (risk_percentage / 100)

    # Calculate the difference between entry price and stop-loss price
    price_difference = entry_price - stop_loss_price

    # Calculate the position size
    position_size = risk_per_trade / price_difference

    return position_size

# Example usage:
account_balance = 10000  # Replace with your account balance
risk_percentage = 2     # Replace with your desired risk percentage per trade
entry_price = 50        # Replace with your entry price
stop_loss_price = 48    # Replace with your stop-loss price

lot_size = calculate_position_size(account_balance, risk_percentage, entry_price, stop_loss_price)

print(f"Lot Size: {lot_size}")
