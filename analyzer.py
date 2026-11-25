import pandas as pd
import requests
import matplotlib.pyplot as plt

REGION_NAME = "Бучанський район"

def fetch_alerts_data():
    data = {
        "date": [
            "2026-11-20", "2026-11-20", "2026-11-21",
            "2026-11-22", "2026-11-23", "2026-11-23", "2026-11-24"
        ],
        "duration_minutes": list((45, 120, 30, 85, 60, 15, 95)),
        "alert_type": ["Повітряна тривога"] * 7
    }
    return pd.DataFrame(data)

def analyze_and_plot(df):
    df["date"] = pd.to_datetime(df["date"])
    
    total_alerts = len(df)
    total_minutes = df["duration_minutes"].sum()
    avg_duration = df["duration_minutes"].mean()
    
    print(f"--- Статистика: {REGION_NAME} ---")
    print(f"Всього тривог: {total_alerts}")
    print(f"Загальна тривалість: {total_minutes} хв ({total_minutes / 60:.1f} год)")
    print(f"Середня тривалість: {avg_duration:.1f} хв")
    
    daily_stats = df.groupby("date")["duration_minutes"].sum()
    
    plt.figure(figsize=(10, 5))
    daily_stats.plot(kind="bar", color="#d9534f")
    plt.title(f"Тривалість повітряних тривог по днях ({REGION_NAME})")
    plt.xlabel("Дата")
    plt.ylabel("Тривалість (хвилини)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig("bucha_alerts_chart.png")
    print("Графік збережено у файл 'bucha_alerts_chart.png'")

if name == "main":
    df_alerts = fetch_alerts_data()
    analyze_and_plot(df_alerts)
