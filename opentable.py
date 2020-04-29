import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("state_of_industry_data.csv")
countries = data.loc[0:7].iloc[:, 2:].T
countryLabels = data.loc[0:7]["Name"]
fig = plt.figure(figsize=(20, 8))
ax = fig.add_subplot(111)
ax.plot(countries)
plt.xticks(rotation=45)
plt.xlabel("Dates")
plt.ylabel("Seated Diners Change%(vs same day last year)")
plt.legend(countryLabels)
plt.show()
