import streamlit as st 
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px


st.title('Stock-DashBoard-Application')

ticker= st.sidebar.text_input("Ticket")
start_date= st.sidebar.date_input('Start-Date')
end_date=st.sidebar.date_input('END-DATE')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)