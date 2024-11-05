import streamlit as st
import requests

st.title("Make your query")

# User inputs
public_url = st.text_input("Enter the given URL:")
k = st.number_input("Enter the value of k:", value=10)
temperature = st.number_input("Enter the temperature:", value=0.50, min_value=0.0, max_value=1.0, step=0.01)

# Set parameters button
if st.button("Set Parameters"):
    response = requests.post(f"{public_url}/set-parameters", json={
        "temperature": temperature,
        "k": k
    })
    st.json(response.json())


user_query = st.text_area("Enter your query:","summarize what EDA is. Tell me the reference (eg: which chapter)")



# Query button
if st.button("Send Query"):
    response = requests.post(f"{public_url}/query", params={"query": user_query})
    st.json(response.json())
