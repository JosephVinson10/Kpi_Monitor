import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import openai

# === Load .env ===
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# === Load KPI data from /data ===
DATA_PATH = os.path.join("data", "kpis.csv")
df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"])
metrics = df["Metric"].unique()

# === Load prompt template from /prompts ===
def load_prompt_template():
    with open(os.path.join("prompts", "explanation_template.txt"), "r") as f:
        return f.read()

template = load_prompt_template()

# === Generate explanation using GPT ===
def generate_explanation(metric, prev, curr):
    change = ((curr - prev) / prev) * 100 if prev != 0 else 0
    trend = "increase" if curr > prev else "decrease" if curr < prev else "no change"

    prompt = template.format(metric=metric, prev=prev, curr=curr, change=round(change, 2), trend=trend)

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip(), change

# === Streamlit UI ===
st.title("📊 KPI Monitor with AI Explanations")

selected_metric = st.selectbox("Choose a KPI to analyze", metrics)

metric_data = df[df["Metric"] == selected_metric].sort_values("Date")

if len(metric_data) >= 2:
    latest = metric_data.iloc[-1]
    previous = metric_data.iloc[-2]

    st.subheader(f"Metric: {selected_metric}")
    st.write(f"📅 {previous['Date'].date()} → {previous['Value']}")
    st.write(f"📅 {latest['Date'].date()} → {latest['Value']}")

    with st.spinner("Asking GPT for an explanation..."):
        explanation, pct_change = generate_explanation(
            selected_metric, previous["Value"], latest["Value"]
        )
        st.markdown(f"**Change:** {pct_change:.2f}%")
        st.markdown("### 🧠 GPT Explanation")
        st.success(explanation)
else:
    st.warning("Not enough data to compare two time points.")
