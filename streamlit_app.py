def get_unique_stock_tickers():
    tickers_input = st.text_input("Enter up to 10 unique stock tickers, separated by commas (e.g., AAPL, MSFT, GOOGL):")
    
    # Split the input string into a list, strip whitespace, and convert to uppercase
    tickers = [ticker.strip().upper() for ticker in tickers_input.split(',') if ticker.strip() != '']

    # Ensure uniqueness and limit to 10 tickers
    unique_tickers = list(set(tickers))[:10]

    return unique_tickers
