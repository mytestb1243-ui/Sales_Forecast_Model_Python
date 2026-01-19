# =========================================================
# PROJECT: Sales Forecast – Next 2 Years (Continuous View)
# MODEL  : SARIMA with Log Stabilization
# =========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX


# =========================================================
# SECTION 1 – DATA GENERATION (REPLACE WITH REAL DATA)
# =========================================================

dates = pd.date_range(start="2021-01-01", end="2025-12-01", freq="MS")

np.random.seed(42)
trend = np.linspace(20000, 55000, len(dates))
seasonality = 6000 * np.sin(np.arange(len(dates)) * 2 * np.pi / 12)
noise = np.random.normal(0, 2500, len(dates))

sales = trend + seasonality + noise

df = pd.DataFrame({
    "Date": dates,
    "Sales": sales.astype(int)
})

df.set_index("Date", inplace=True)


# =========================================================
# SECTION 2 – HISTORICAL DATA VISUALIZATION
# =========================================================

plt.figure(figsize=(10,5))
plt.plot(df.index, df["Sales"])
plt.title("Historical Monthly Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.show()


# =========================================================
# SECTION 3 – LOG TRANSFORMATION
# Stabilizes variance for better forecasting
# =========================================================

df["Log_Sales"] = np.log(df["Sales"])


# =========================================================
# SECTION 4 – MODEL TRAINING (SARIMA)
# =========================================================

model = SARIMAX(
    df["Log_Sales"],
    order=(1,0,1),
    seasonal_order=(1,1,0,12),
    trend="c",
    enforce_stationarity=True,
    enforce_invertibility=True
)

model_fit = model.fit(disp=False)
print("\nModel training completed successfully")


# =========================================================
# SECTION 5 – FORECAST NEXT 2 YEARS (24 MONTHS)
# =========================================================

months_ahead = 24

forecast_obj = model_fit.get_forecast(steps=months_ahead)
log_forecast = forecast_obj.predicted_mean
log_ci = forecast_obj.conf_int(alpha=0.2)   # tighter CI

# Convert back from log scale
forecast = np.exp(log_forecast)
lower_ci = np.exp(log_ci.iloc[:, 0])
upper_ci = np.exp(log_ci.iloc[:, 1])

future_dates = pd.date_range(
    start=df.index.max() + pd.offsets.MonthBegin(1),
    periods=months_ahead,
    freq="MS"
)

forecast_df = pd.DataFrame({
    "Date": future_dates,
    "Predicted_Sales": forecast.values.round(0).astype(int),
    "Lower_Bound": lower_ci.values.round(0).astype(int),
    "Upper_Bound": upper_ci.values.round(0).astype(int)
})


print("\nNext 2-Year Sales Forecast:")
print(forecast_df.head(12))


# =========================================================
# SECTION 6 – CONTINUOUS FORECAST VISUALIZATION (NO GAP)
# =========================================================

plt.figure(figsize=(14,6))

# Historical data
plt.plot(df.index, df["Sales"], label="Historical Sales")

# Create connection between history and forecast
connect_dates = pd.concat([
    pd.Series(df.index[-1:]),
    pd.Series(forecast_df["Date"])
])

connect_values = pd.concat([
    pd.Series([df["Sales"].iloc[-1]]),
    forecast_df["Predicted_Sales"]
])

# Forecast line (continuous)
plt.plot(connect_dates, connect_values, label="Next 2-Year Forecast")

# Confidence interval
plt.fill_between(
    forecast_df["Date"],
    forecast_df["Lower_Bound"],
    forecast_df["Upper_Bound"],
    alpha=0.25,
    label="Confidence Interval"
)

plt.title("Sales Forecast for Next 2 Years (Continuous View)")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()


# =========================================================
# SECTION 7 – EXPORT FORECAST TO CSV
# =========================================================

forecast_df.to_csv("sales_forecast_next_2_years.csv", index=False)
print("\nForecast saved as sales_forecast_next_2_years.csv")


# =========================================================
# END OF PROJECT
# =========================================================
