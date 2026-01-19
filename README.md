# 📈 Sales Forecasting Using SARIMA (2-Year Forecast)

A production-ready time series forecasting project that predicts monthly
sales for the next **2 years (24 months)** using a **Seasonal ARIMA
(SARIMA)** model with log stabilization.\
The project demonstrates a complete analytics workflow including data
preparation, modeling, forecasting, visualization, and export for
business reporting.

------------------------------------------------------------------------

## 🚀 Project Objective

Businesses rely on accurate sales forecasts to plan inventory, staffing,
budgets, and growth strategies.\
This project shows how a data analyst or data scientist can build a
reliable forecasting pipeline using Python and statistical modeling
techniques.

------------------------------------------------------------------------

## ✅ Key Features

-   Monthly sales forecasting for the next **24 months**
-   Seasonal trend modeling using **SARIMA**
-   Log transformation to stabilize variance
-   Confidence intervals for uncertainty estimation
-   Continuous forecast visualization (no chart breaks)
-   CSV export for Power BI, Excel, and Tableau
-   Clean, modular, production-style code

------------------------------------------------------------------------

## 🧰 Technology Stack

-   Python 3\
-   Pandas -- Data manipulation\
-   NumPy -- Numerical computation\
-   Matplotlib -- Data visualization\
-   Statsmodels -- Time series modeling

------------------------------------------------------------------------

## 📂 Project Structure

    sales-forecasting-sarima/
    │
    ├── sales_forecast.py
    ├── sales_forecast_next_2_years.csv
    ├── README.md
    └── requirements.txt

------------------------------------------------------------------------

## 📊 Dataset

This project uses **synthetic monthly sales data** generated
programmatically to simulate: - Long-term growth trend - Monthly
seasonality - Random fluctuations

You can replace this with real business data easily.

------------------------------------------------------------------------

## ⚙️ Installation

``` bash
git clone https://github.com/your-username/sales-forecasting-sarima.git
cd sales-forecasting-sarima
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ How to Run

``` bash
python sales_forecast.py
```

The script will: 1. Load or generate data\
2. Train the SARIMA model\
3. Forecast the next 24 months\
4. Display charts\
5. Export CSV output

------------------------------------------------------------------------

## 📈 Output

Generated file:

    sales_forecast_next_2_years.csv

Compatible with Power BI, Excel, Tableau.

------------------------------------------------------------------------

## 🔁 Replace with Real Data

``` python
df = pd.read_csv("your_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)
```

------------------------------------------------------------------------

## 📌 Business Use Cases

-   Inventory planning\
-   Revenue forecasting\
-   Budget planning\
-   Demand management

------------------------------------------------------------------------

## 🧠 Model Notes

-   SARIMA captures seasonality and trend.
-   Log transformation stabilizes variance.
-   Forecast horizon limited to 24 months for reliability.

------------------------------------------------------------------------

## 📜 License

Educational and portfolio use.

------------------------------------------------------------------------

## 👤 Author

Muhammad Shafi\
Data Analyst \| To Be Data Engineer 
