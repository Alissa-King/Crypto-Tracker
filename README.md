# Cryptocurrency Price Tracker

## Overview

This Streamlit app allows users to track the current price of cryptocurrencies by web scraping data from Yahoo Finance. It provides a simple interface for users to input a cryptocurrency symbol and fetch its current price.

## Features

- User input for cryptocurrency symbol
- Real-time web scraping of Yahoo Finance
- Display of current cryptocurrency price
- Error handling for invalid symbols or connection issues

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Alissa-King/crypto-price-tracker.git
   cd crypto-price-tracker
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Enter a cryptocurrency symbol (e.g., BTC-USD) in the input field.

4. Click the "Get Current Price" button to fetch and display the current price.

## Dependencies

- streamlit
- pandas
- requests
- beautifulsoup4

## Limitations

- This app relies on web scraping, which may break if Yahoo Finance changes its website structure.
- It only provides the current price and does not store historical data.
- The app may be subject to rate limiting or IP blocking if used excessively.

## Future Improvements

- Add historical price data and charts
- Implement caching to reduce the number of requests
- Add support for multiple cryptocurrencies at once
- Improve error handling and user feedback

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/Alissa-King/crypto-price-tracker/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)