# 🌾 Smart Farming IoT Dashboard
**Data Lifecycle Management - UPN Veteran Jawa Timur 2026**

Nama  : [NAMA KAMU]
NIM   : 23082010056

---

## 📋 Deskripsi
Proyek ini mengimplementasikan Data Lifecycle Management (DLM) menggunakan 
dataset sensor IoT pertanian untuk memprediksi hasil panen (yield).

## 📁 Struktur Repository
```
repo/
├── README.md
├── data/raw/smart_farming_sensor_data.csv
├── Data_Lifecycle_Smart_Farming.ipynb
├── dashboard/streamlit_app.py
└── outputs/
    ├── cleaned_data.csv
    ├── analysis_report.pdf
    └── dashboard_screenshot.png
```

## 📊 Dataset
- **Sumber:** Kaggle - Smart Farming Sensor Data for Yield Prediction
- **Link:** https://www.kaggle.com/datasets/atharvasoundankar/smart-farming-sensor-data-for-yield-prediction
- **Jumlah Data:** 500 baris, 22 kolom
- **Kolom Utama:** Soil Moisture, Temperature, Humidity, pH, Yield

## 🔄 Data Lifecycle
| Tahap | Implementasi |
|---|---|
| Acquisition | Download dataset dari Kaggle |
| Storage | GitHub repository + Google Colab |
| Processing | Cleaning missing values, format datetime |
| Analysis | EDA, korelasi, time series |
| Visualization | 4 chart dashboard (Streamlit) |
| Governance | Data Quality Score 100% |

## 📈 Data Quality Score
- Accuracy     : 100.0%
- Completeness : 100.0%
- Timeliness   : 1.4%

## 🛠️ Tools yang Digunakan
- Python (Pandas, Matplotlib, Seaborn)
- Google Colab
- Streamlit
- GitHub
