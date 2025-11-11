import streamlit as st
import pandas as pd

# Title
st.title("☀️ Solar Data Discovery")

# Load CSV
data_path = "data/sample_solar.csv"
df = pd.read_csv(data_path)

# Display
st.subheader("Raw Solar Data Preview")
st.dataframe(df.head())

# Basic info
st.write("✅ Rows:", df.shape[0])
st.write("✅ Columns:", df.shape[1])
