import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd
import requests

LOG_FILE = "logs/prompt_log.json"
API_ENDPOINT = "http://localhost:8000/validate"

st.set_page_config(page_title="Prompt Validation Dashboard", layout="wide")
st.title("🛡️ Prompt Validator + 📊 Analytics Dashboard")

# 1. Prompt Validation Section
st.header("🔍 Prompt Input")

with st.form("prompt_form"):
    user_prompt = st.text_area("Enter your prompt")
    submitted = st.form_submit_button("Validate Prompt")

if submitted and user_prompt.strip():
    try:
        response = requests.post(API_ENDPOINT, json={"prompt": user_prompt})
        if response.status_code == 200:
            result = response.json()
            st.success(f"✅ {result['status']}: {result['reason']}")
            st.json(result)
        else:
            st.error(f"❌ Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"🚨 Exception: {e}")

# 2. Log Analytics Section
st.header("📊 Log Filters and Analytics")

# Load log data
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        logs = [json.loads(line) for line in f if line.strip()]
else:
    logs = []

if logs:
    statuses = list(set(log['result']['status'] for log in logs))
    rules = list(set(log['rule'] for log in logs))
    clients = list(set(log.get('client_id', 'unknown') for log in logs))

    selected_status = st.multiselect("Filter by Status", statuses, default=statuses)
    selected_rules = st.multiselect("Filter by Rule", rules, default=rules)
    selected_clients = st.multiselect("Filter by Client", clients, default=clients)

    filtered_logs = [
        log for log in logs
        if log['result']['status'] in selected_status
        and log['rule'] in selected_rules
        and log.get('client_id', 'unknown') in selected_clients
    ]

    st.write(f"Showing {len(filtered_logs)} filtered logs")
    st.dataframe(filtered_logs)

    df = pd.DataFrame(filtered_logs)
    if not df.empty:
        st.subheader("📈 Prompt Status Count by Client")
        df['status'] = df['result'].apply(lambda x: x['status'])
        st.bar_chart(df.groupby(["client_id", "status"]).size().unstack(fill_value=0))
