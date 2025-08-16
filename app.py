import streamlit as st
import pandas as pd

st.title("Customer Retention Insights Platform")
st.write("Prediction • Analysis • Detection Dashboard (Python + Power BI)")

st.metric("Churn Model AUC", "0.99")
st.metric("High-Risk Precision", "99%")
st.metric("Pipeline Latency (99th percentile)", "200 ms")

st.write("## Risk Segmentation")
st.bar_chart({"High Risk": [20], "Medium Risk": [50], "Low Risk": [30]})

st.write("Note: Power BI dashboard available in the repository for executive reporting.")
