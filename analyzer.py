import requests, matplotlib.pyplot as plt
from datetime import datetime

r = requests.get("https://alerts.in.ua", timeout=10).text
lines = [l for l in r.splitlines() if "Бучан" in l or "Київська" in l]
active = bool(lines)
print("ТРИВОГА!" if active else "ВІДБІЙ / СПОКІЙНО", "\n".join(lines))

plt.figure(figsize=(8, 4))
plt.bar(["Буча"], list((1,)), color="#d9534f" if active else "#5cb85c")
plt.title(f"Статус на {datetime.now().strftime('%H:%M %d.%m.%Y')}: {'ТРИВОГА' if active else 'СПОКІЙНО'}")
plt.yticks([])
plt.savefig("bucha_alerts_chart.png")
