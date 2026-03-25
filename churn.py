import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

pd.set_option('display.max_columns', None)

# Daten mit pandas laden
df = pd.read_csv('telco_data.csv')
#print(df.tail(10))

#Churn rate aus Daten exportieren
churn_rate = df[df['Churn'] == 'Yes']

#visualisierung
plt.figure(figsize=(10,5))
sns.histplot(data = churn_rate, x = 'tenure', hue = 'Contract', shrink=.8, multiple= "stack", palette = 'magma')

plt.xticks(np.arange(0, 73, 3))
plt.yticks(np.arange(0, 1001, 100))

#Beschriftung
plt.title('Kündigungszeitpunkt nach Monaten (Churn-Kurve)')
plt.xlabel('Monate der Mitgliedschaft')
plt.ylabel('Anzahl der Kündigungen')

plt.savefig("Churn.png")

plt.show()
