import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Daten mit pandas laden
df = pd.read_csv('telco_data.csv')

#Churn rate aus Daten exportieren
churn_rate = df[df['Churn'] == 'Yes']

#Festlegung der Größe
plt.figure(figsize=(10,6))
#weißes Gitter zum besseren Überblick hinzugefügt
sns.set_style("whitegrid")

#Gruppierung der Monthly Charges zum jeweiligen Contract
sns.histplot(data = churn_rate, x = 'tenure', hue = 'TechSupport', shrink=.8, multiple= "stack", palette = 'magma')
#Als Datenmenge nutze ich alle Kunden, die gekündigt haben. Die X-Achse beschreibt den Zeitpunkt.
# Mit hue und stack teile ich diese so auf, dass visuell eifach zu erkennen ist, ob der Kunde Technischen Support
# erhalten hat oder nicht. shrink fügt Abstände zwischen den Balken ein.

#Beschriftung
plt.title('Kündigungen in Abhängigkeit, ob Tech Support genutzt wurde')
plt.xlabel('Monate der Mitgliedschaft')
plt.ylabel('Anzahl der Kündigungen')

plt.savefig("TechSupport.png")

plt.show()