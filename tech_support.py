import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Daten mit pandas laden
df = pd.read_csv('telco_data.csv')

#Churn rate aus Daten exportieren
churn_rate = df[df['Churn'] == 'Yes']

#Gruppierung der Monthly Charges zum jeweiligen Contract
sns.histplot(data = churn_rate, x = 'tenure', hue = 'TechSupport', shrink=.8, multiple= "stack", palette = 'magma')

#Beschriftung
plt.title('Kündigungen in Abhängigkeit, ob Tech Support genutzt wurde')
plt.xlabel('Monate der Mitgliedschaft')
plt.ylabel('Anzahl der Kündigungen')

plt.savefig("TechSupport.png")

plt.show()