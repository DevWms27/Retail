import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#data= pd.read_csv("C:/Users/devin/Coding/Customer PRoject/data/data.csv", encoding='latin-1')

print("Script started")
data = pd.read_csv(
    r"C:/Users/devin/Coding/Customer Project/data/data.csv",
    encoding="latin1"
)
print("Loaded CSV ✔️")

print(data.head())

#data.info

#data.isnull().any()