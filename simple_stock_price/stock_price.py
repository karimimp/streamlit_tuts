import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

The stock **closing** price and volume of Google

""")

# define ticker symbol
tickerSymbol = 'GOOGL'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2022-5-01', end='2022-5-31')

# Open	High	Low	 Close	Volume	Dividends	Stock Splits


st.write("""
## Closing price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
