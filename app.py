import streamlit as st
import pandas as pd
import requests
import datetime

# Set the page title
st.set_page_config(page_title="Crypto Price Tracker")

# Title and description
st.title("Cryptocurrency Price Tracker")
st.write("Track the price history of your favorite cryptocurrencies!")

# Input fields
col1, col2, col3 = st.columns(3)
with col1:
    symbol = st.text_input("Crypto Symbol (e.g., BTC)", "BTC").lower()
with col2:
    start_date = st.date_input("Start Date", datetime.date.today() - datetime.timedelta(days=30))  # Default to 30 days ago
with col3:
    end_date = st.date_input("End Date", datetime.date.today())

# Additional metrics to display (checkbox options)
metrics_to_display = st.multiselect(
    "Select Additional Metrics",
    ["Market Cap", "Total Volume"],
    default=["Market Cap"]  # Default to showing Market Cap
)

# Your CoinGecko API key
api_key = "CG-auuEeCPviaVddw231NEjc3Wz"

# Fetch data when the user clicks the button
if st.button("Get Prices"):
    # Get coin list to find the ID
    coin_list_url = "https://api.coingecko.com/api/v3/coins/list"
    try:
        coin_list_response = requests.get(coin_list_url)
        coin_list_response.raise_for_status()
        coin_list_data = coin_list_response.json()

        # Find the coin ID based on the symbol
        coin_id = next((coin["id"] for coin in coin_list_data if coin["symbol"] == symbol), None)
        if not coin_id:
            st.error(f"Invalid cryptocurrency symbol: {symbol}")
        else:
            # CoinGecko API URL with coin ID
            url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range"

            # Convert datetime.date objects to Unix timestamps
            start_timestamp = int(datetime.datetime.combine(start_date, datetime.datetime.min.time()).timestamp())
            end_timestamp = int(datetime.datetime.combine(end_date, datetime.datetime.max.time()).timestamp())

            params = {
                "vs_currency": "usd",
                "from": start_timestamp,
                "to": end_timestamp
            }

            headers = {
                "Accepts": "application/json",
                "X-CG-Pro-API-Key": api_key  # Include the API key in the headers
            }

            try:
                print(url)  # Print the request URL for debugging
                response = requests.get(url, params=params, headers=headers)
                response.raise_for_status()
                data = response.json()

                # Process data
                df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
                for metric in metrics_to_display:
                    metric_data = data[metric.lower().replace(" ", "_") + "s"]  # Convert metric name to API key format
                    df[metric] = [item[1] for item in metric_data]

                df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
                df.set_index("date", inplace=True)

                # Display charts
                st.line_chart(df[["price"] + metrics_to_display])  # Include selected metrics in the chart

            except requests.exceptions.RequestException as e:
                st.error(f"Error fetching data: {e}")
                print(response.content)  # Print the response content for more details

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching coin list: {e}")