import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import *

# Set data source
# data = pd.read_csv("DataFiles/temperature_data.csv")
# data["Date"] = pd.to_datetime(data["Date"])
# data = data.set_index("Date")
# data = data["Mean"]

data = yf.download("TSLA")['Close']

data = validate_series(data)

persist_detector = PersistAD(c=20.0, side="positive")
anomalies = persist_detector.fit_detect(data)
plot(data, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_color='red')
plt.show()

# # Define the High and Low values that would be flagged as anomalies
# iqr_detector = Q=InterQuartileRangeAD(c=2)
# # quantile detector with percentile quantile_detector = QuantileAD(low=0.01, high=0.99)
# # absolute value threshold_detector = ThresholdAD(low=20, high=80)
# anomalies = iqr_detector.fit_detect(data)
# plot(data, anomaly=anomalies, anomaly_color="red", anomaly_tag="marker")
# plt.show()