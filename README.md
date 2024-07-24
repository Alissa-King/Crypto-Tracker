# Crypto Tracker and Forecaster

This Python project allows you to:

1. **Fetch real-time cryptocurrency prices** from Yahoo Finance.
2. **Retrieve historical price data** using yfinance.
3. **Calculate technical indicators:**
   - 9-day and 21-day Exponential Moving Averages (EMA)
   - Relative Strength Index (RSI)
4. **Forecast future prices** using the Prophet time series forecasting library.
5. **Visualize** price data, indicators, and forecasts in interactive plots.

## Features

- **User-friendly interface:** Simply input the cryptocurrency symbol (e.g., BTC, ETH).
- **Comprehensive data:** Get current prices and historical data.
- **Technical analysis:** EMA and RSI for insights into market trends.
- **Predictive modeling:** Prophet forecasts to aid in decision-making.
- **Clear visualizations:** Easily interpret trends and potential price movements.
- **Customizable:** Forecast for a user-specified number of days (default is 180 days, approximately 6 months). 

## How to Use

1. **Install dependencies:**
   ```bash
   pip install yfinance pandas pandas_ta prophet matplotlib requests beautifulsoup4
