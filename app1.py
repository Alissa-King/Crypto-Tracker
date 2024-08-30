import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Set the page title
st.set_page_config(page_title="Crypto Price Tracker (Web Scraping Yahoo Finance)")

# Title and description
st.title("Cryptocurrency Price Tracker (Web Scraping Yahoo Finance)")
st.write("Track the price history of your favorite cryptocurrencies (limited data, web scraping)")

# Input field for cryptocurrency symbol
symbol = st.text_input("Crypto Symbol (e.g., BTC-USD)", "BTC-USD").upper()

# Fetch data when the user clicks the button
if st.button("Get Current Price"):
    # Yahoo Finance URL
    url = f"https://finance.yahoo.com/quote/{symbol}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the price element (this might need adjustment if Yahoo Finance structure changes)
        price_element = soup.find('fin-streamer', {'data-test': 'qsp-price'})
        if price_element:
            price = price_element.text.strip()
            st.write(f"Current Price of {symbol}: {price}")
        else:
            st.error(f"Unable to find price information for {symbol}.")

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")