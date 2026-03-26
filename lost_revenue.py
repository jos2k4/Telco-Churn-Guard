import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Daten mit pandas laden
df = pd.read_csv('telco_data.csv')
#

#Churn rate aus Daten exportieren
churn_rate = df[df['Churn'] == 'Yes']

#Gruppierung der Monthly Charges zum jeweiligen Contract
total_lost_revenue = churn_rate.groupby('Contract')['MonthlyCharges'].sum().reset_index()

#Festlegung der Größe
plt.figure(figsize=(10,6))
#weißes Gitter zum besseren Überblick hinzugefügt
sns.set_style("whitegrid")
#visualisierung
sns.barplot(data = total_lost_revenue, x = 'Contract', y = 'MonthlyCharges')


#Beschriftung
plt.title('Durchschnittlicher Monatlicher Verlust sortiert nach Vertragsart')
plt.xlabel('Art des Vertrages')
plt.ylabel('Potentieller monatlicher Umsatzverlust')

#Lege den Ordner fest, indem gespeichert werden soll
output_dir = 'plots.gitkeep'
#Namensgebung
file_path = os.path.join(output_dir, 'lost_revenue.png')
#Speicherung
plt.savefig(file_path)

plt.close()
