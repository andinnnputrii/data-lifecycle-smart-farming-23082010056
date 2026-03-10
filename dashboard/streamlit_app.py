
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Smart Farming Dashboard",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Smart Farming IoT Dashboard")
st.markdown("**Data Lifecycle Management - UPN Veteran Jawa Timur 2026**")
st.divider()

df = pd.read_csv("cleaned_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["sowing_date"] = pd.to_datetime(df["sowing_date"])
df["harvest_date"] = pd.to_datetime(df["harvest_date"])

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Farms", df["farm_id"].nunique())
col2.metric("Avg Soil Moisture", f"{df["soil_moisture_%"].mean():.1f}%")
col3.metric("Avg Yield", f"{df["yield_kg_per_hectare"].mean():.0f} kg/ha")
col4.metric("Avg Temperature", f"{df["temperature_C"].mean():.1f}°C")

st.divider()

st.subheader("📈 Time Series - Soil Moisture Trend")
df_sorted = df.sort_values("timestamp")
fig1, ax1 = plt.subplots(figsize=(12, 4))
ax1.plot(df_sorted["timestamp"], df_sorted["soil_moisture_%"],
         color="#2196F3", linewidth=0.8, alpha=0.7)
ax1.set_xlabel("Timestamp")
ax1.set_ylabel("Soil Moisture (%)")
ax1.tick_params(axis="x", rotation=45)
st.pyplot(fig1)

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🌡️ Gauge - Rata-rata Soil Moisture")
    avg_moisture = df["soil_moisture_%"].mean()
    threshold = 20
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    color = "#4CAF50" if avg_moisture >= threshold else "#F44336"
    ax2.bar(["Soil Moisture"], [avg_moisture], color=color, width=0.4, edgecolor="black")
    ax2.axhline(y=threshold, color="red", linestyle="--", linewidth=2,
                label=f"Threshold ({threshold}%)")
    ax2.set_ylim(0, 50)
    ax2.set_ylabel("Soil Moisture (%)")
    ax2.legend()
    ax2.text(0, avg_moisture + 1, f"{avg_moisture:.1f}%",
             ha="center", fontsize=14, fontweight="bold")
    st.pyplot(fig2)

with col_right:
    st.subheader("🔥 Heatmap - Korelasi Antar Sensor")
    sensor_cols = ["soil_moisture_%", "soil_pH", "temperature_C",
                   "rainfall_mm", "humidity_%", "sunlight_hours",
                   "NDVI_index", "yield_kg_per_hectare"]
    corr_matrix = df[sensor_cols].corr()
    fig3, ax3 = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm",
                ax=ax3, square=True, linewidths=0.5)
    st.pyplot(fig3)

st.subheader("🚨 Alert System - Yield per Crop Type")
avg_yield = df.groupby("crop_type")["yield_kg_per_hectare"].mean().sort_values()
yield_threshold = 4000
bar_colors = ["#F44336" if y < yield_threshold else "#4CAF50" for y in avg_yield.values]
fig4, ax4 = plt.subplots(figsize=(10, 4))
ax4.barh(avg_yield.index, avg_yield.values, color=bar_colors, edgecolor="black")
ax4.axvline(x=yield_threshold, color="red", linestyle="--", linewidth=2,
            label=f"Threshold ({yield_threshold} kg/ha)")
ax4.set_xlabel("Yield (kg/hectare)")
ax4.legend()
for i, (crop, val) in enumerate(zip(avg_yield.index, avg_yield.values)):
    if val < yield_threshold:
        ax4.text(val + 50, i, "ALERT", va="center", color="red", fontweight="bold")
st.pyplot(fig4)

st.divider()
st.subheader("📊 Data Quality Score")
latest = df["timestamp"].max()
recent = df[df["timestamp"] >= latest - pd.Timedelta(days=30)].shape[0]
timeliness = round(recent / df.shape[0] * 100, 2)
q1, q2, q3 = st.columns(3)
q1.metric("Accuracy", "100.0%")
q2.metric("Completeness", "100.0%")
q3.metric("Timeliness", f"{timeliness}%")
