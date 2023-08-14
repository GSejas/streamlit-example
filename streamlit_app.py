import streamlit as st
import requests

# Check if the request method is POST
if st.request.method == "POST":
    data = st.request.json
    # Extract the required data or parameters from AppSheet's webhook payload

    # Forward this data to Google Apps Script
    google_apps_script_url = "https://script.googleapis.com/v1/scripts/[YOUR_SCRIPT_ID]:run"
    headers = {
        "Authorization": "Bearer YOUR_OAUTH_TOKEN",
        "Content-Type": "application/json"
    }
    payload = {
        "function": "YourFunctionName",
        "parameters": [data['param1'], data['param2']] # modify based on your needs
    }
    response = requests.post(google_apps_script_url, headers=headers, json=payload)
    st.write(response.json())
else:
    st.write("This is a webhook endpoint. Please POST data to it.")
