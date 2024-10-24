import streamlit as st
import yfinance as yf


def fetch_ticker_data(symbol):
    return yf.Ticker(symbol)


st.title("Interactive Stock Market Dashboard")
st.header("Analyze Stock Prices Using Python & Streamlit")
st.sidebar.header("Powered by: Data Enthusiasts")


symbol = st.sidebar.text_input("Enter a stock symbol", "GOOGL")
start_date = st.sidebar.date_input("Start Date", value="2021-10-01")
end_date = st.sidebar.date_input("End Date", value="2021-10-01")


with st.spinner('Fetching data...'):
    stock_data = fetch_ticker_data(symbol)
    stock_prices = yf.download(symbol, start=start_date, end=end_date)
    stock_history = stock_data.history(period="3mo")


st.subheader(f"{symbol.upper()} Stock Information")
summary = stock_data.info.get('longBusinessSummary', 'Summary not available')
st.write(summary)
st.write(stock_prices)


if not stock_history.empty:
    st.line_chart(stock_history.values)
else:
    st.write(f"No recent data available for {symbol.upper()}.")
