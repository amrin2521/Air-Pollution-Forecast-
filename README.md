# Air-Pollution-Forecast-
# 🌫️ Air Pollution Forecasting in Dhaka

This project uses real meteorological data to forecast PM2.5 air pollution levels in Dhaka, Bangladesh. Using Python and linear regression, the model estimates air quality based on temperature, wind speed, and humidity.

---

## 📌 Why This Project?

Dhaka is one of the most polluted cities in the world. PM2.5 (fine particulate matter) poses serious health risks, especially in urban South Asia. This project investigates how weather factors affect PM2.5 levels using a basic predictive model. The goal is to highlight the importance of accessible air quality forecasting for urban public health.

---

## 🧪 Methodology

- **Data**: Hourly PM2.5, temperature, wind speed, and humidity (mock data used here)
- **Model**: Linear regression with `scikit-learn`
- **Workflow**:
  - Preprocess data (drop missing rows)
  - Train/test split
  - Fit model and make predictions
  - Plot actual vs predicted PM2.5 values
- **Evaluation Metric**: Mean Squared Error (MSE)

---

## 🧠 Skills Demonstrated

- Exploratory data analysis (EDA)
- Feature selection & model training
- Scientific reasoning in environmental modeling
- Data visualization with `matplotlib`
- Regression modeling in `Python` using `pandas`, `sklearn`

---

## 📊 Sample Output

<img src="prediction_plot.png" width="600">

The red line represents perfect predictions. The scatter points show the actual vs predicted PM2.5 levels.

---

## 📁 Folder Structure
<pre> ## 📁 Folder Structure ``` air-pollution-dhaka/ ├── air_pollution_model.py # Python script that trains and tests the model ├── dhaka_air_quality.csv # Cleaned dataset used for regression ├── prediction_plot.png # Output plot comparing actual vs predicted PM2.5 └── README.md # Project explanation and overview ``` </pre>

---

## 📈 Next Steps

- Add more advanced models (e.g., Random Forest, Ridge Regression)
- Introduce real-time data scraping and time series analysis
- Deploy as a web app using Streamlit to allow public predictions
- Compare air quality across major South Asian cities

---

*Built by Amrin Sazia  
Mathematics & Environmental Geoscience major, The College of Wooster*



