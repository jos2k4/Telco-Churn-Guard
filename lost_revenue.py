import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Daten mit pandas laden
df = pd.read_csv('telco_data.csv')
#print(df.tail(10))

#Churn rate aus Daten exportieren
churn_rate = df[df['Churn'] == 'Yes']

#Gruppierung der Monthly Charges zum jeweiligen Contract
total_lost_revenue = churn_rate.groupby('Contract')['MonthlyCharges'].sum().reset_index()

#visualisierung
plt.figure(figsize=(10,6))

sns.barplot(data = total_lost_revenue, x = 'Contract', y = 'MonthlyCharges')


#Beschriftung
plt.title('Durchschnittlicher Monatlicher Verlust sortiert nach Vertragsart')
plt.xlabel('Art des Vertrages')
plt.ylabel('Potentieller monatlicher Umsatzverlust')

plt.savefig("lost_revenue.png")

plt.show()
