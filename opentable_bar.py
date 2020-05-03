import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("state_of_industry_data.csv")
countries = data.loc[0:8].iloc[:, 2:].T
dates = data.iloc[:, 2:].columns
plt.figure(figsize=(20, 50))
for i in range(1, 9):
    colors = []
    for j in countries[i-1]:
        if j > 0:
            colors.append("Green")
        else:
            colors.append("Red")
    plt.subplot(8, 1, i)
    plt.bar(x=dates, height=countries[i-1], color=colors, label=data.loc[i-1]["Name"])
    plt.legend()

plt.xticks(rotation=45)
plt.xlabel("Dates")
plt.subplot(8, 1, 4)
plt.ylabel("Seated Diners Change%(vs same day last year)")
plt.show()
