import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

print(df)

plt.figure();

df.plot.bar();
















