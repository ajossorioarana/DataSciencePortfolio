import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv('.\callsigns.csv', delimiter=';')

#limno_database['date'] = pd.to_datetime(limno_database['date'])

#limno_database['month'] = limno_database['date'].dt.month

print(data.head())
print()
print(data.describe())
print()
print(data.info())
sns.set(style="darkgrid")

# Distribution of pH
#sns.histplot(x=limno_database['ph'])

# Relationship between Secchi depth and by color
# sns.violinplot(x=limno_database['color'], y=limno_database['secchi'])

# Relationship between Secchi and month
# sns.violinplot(x=limno_database['month'], y=limno_database['secchi'])
# sns.boxplot(x=limno_database['month'], y=limno_database['secchi'])

# plt.title("Secchi Depth vs Water color")

# plt.show(block=True)