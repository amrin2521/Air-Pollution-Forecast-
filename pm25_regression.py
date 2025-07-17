
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


file_path = "/Users/amrinsazia/Desktop/AirPollutionDhaka/Airpollution2022.csv"


df = pd.read_csv(file_path)


df["Datetime"] = pd.to_datetime(df["Date (LT)"], dayfirst=True)
df["Hour"] = df["Datetime"].dt.hour
df["DayOfWeek"] = df["Datetime"].dt.dayofweek
df["Month"] = df["Datetime"].dt.month


X = df[["Hour", "DayOfWeek", "Month"]]
y = df["NowCast Conc."]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")


plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel("Actual PM2.5 (NowCast Conc.)")
plt.ylabel("Predicted PM2.5")
plt.title(f"PM2.5 Prediction in Dhaka\nLinear Regression | MSE: {mse:.2f}")
plt.grid(True)
plt.tight_layout()
plt.savefig("prediction_plot.png")
plt.show()
