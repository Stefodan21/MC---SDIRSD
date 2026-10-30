import streamlit as st
import pandas as pd
import plotly.express as px

st.title("MC - SDIR | Streamlit Data App")

try:
    df = pd.read_csv("./data/biscayneBay_waterquality.csv")
except FileNotFoundError:
    st.error("CSV file not found. Please make sure the dataset exists in the data folder.")
    st.stop()

st.header("Overview")
st.caption(
    "This interactive dashboard explores a marine water-quality dataset collected during a bay survey. "
    "The app is designed to help users understand environmental conditions by exploring the data with a simple chart."
)

st.divider()

st.header("Data Display")

parameter = st.selectbox(
    "Select a parameter",
    options=[col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])],
)

fig1 = px.line(
    df,
    x="Time",
    y=parameter,
    title=f"{parameter} over Time",
    labels={"Time": "Time", parameter: parameter}
)

fig1.update_traces(name=parameter, showlegend=True)
fig1.update_layout(showlegend=True)

st.plotly_chart(fig1)

st.divider()
st.subheader("Descriptive Statistics")
st.dataframe(df.describe())

st.caption("Raw data is displayed below.")
st.dataframe(df)

st.header("Insights")

st.write(f"Average {parameter}: {df[parameter].mean():.2f}")
st.write(f"Minimum {parameter}: {df[parameter].min():.2f}")
st.write(f"Maximum {parameter}: {df[parameter].max():.2f}")

st.caption("This chart helps show how the selected measurement changes over time.")
st.caption("The dashboard allows users to explore how water-quality measurements change during the survey.")

