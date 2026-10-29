import streamlit as st
import pandas as pd
import plotly.express as px

st.title("My dashboard")

try:
    df = pd.read_csv("./data/2021-oct21.csv")
except FileNotFoundError as error:
    raise

st.divider()

st.header("Overview")


tables, plots = st.tabs(["Data","Tables"])

with tables:
    st.subheader("Autonomous Underwater Vehicle (AUV) Telemetry and Marine Water Quality Data – October 21, 2021")
    st.dataframe(df)
    st.caption("Raw data")
    st.dataframe(df.describe())
    st.caption("Data Statistics")



with plots:
    st.subheader("Line Chart")
    st.dataframe(df)
