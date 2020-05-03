import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("state_of_industry_data.csv")
countries = data.loc[0:8].iloc[:, 2:52].T
dates = data.iloc[:, 2:52].columns
width = 0.1
plt.figure(figsize=(25, 10))
for i in range(1, 9):
    x = list(range(50))
    for j in range(len(x)):
        x[j] = x[j] + width*(i-1)

    plt.bar(x, height=countries[i-1], width=width, label=data.loc[i-1]["Name"], tick_label=dates)
    plt.legend()

plt.xticks(rotation=45)
plt.ylabel("Seated Diners Change%(vs same day last year)")
plt.show()
