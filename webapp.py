import streamlit as st
import pandas as pd
import plotly.express as px

st.title("My dashboard")
st.header("Overview Metrics")
st.subheader("Metric Type")

st.divider()

try:
    df = pd.read_csv("./data/data.csv")
except FileNotFoundError as error:
    st.error("File not found.")
    raise

