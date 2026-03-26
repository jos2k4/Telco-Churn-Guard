import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
# Daten mit pandas laden
df = pd.read_csv('telco_data.csv')

#Churn rate aus Daten exportieren
churn_rate = df[df['Churn'] == 'Yes']

#weißes Gitter zum besseren Überblick hinzugefügt
sns.set_style("whitegrid")

#Festlegung der Größe
plt.figure(figsize=(10,6))

#visualisierung
sns.histplot(data = churn_rate, x = 'tenure', hue = 'Contract', shrink=.8, multiple= "stack", palette = 'magma')
#Als Datenmenge nutze ich alle Kunden, die gekündigt haben. Die X-Achse beschreibt den Zeitpunkt und die Y-Achse die Anzahl.
# Mit hue und stack teile ich diese so auf, dass visuell eifach zu erkennen ist welcher Vertrag betroffen ist


plt.xticks(np.arange(0, 73, 3))     #-> x-Achse zählt von 0-72 in 3er Schritten
plt.yticks(np.arange(0, 1001, 100))     #-> Y-Achse zählt von 0-1000 in 100er Schritten

#Beschriftung
plt.title('Kündigungszeitpunkt nach Monaten (Churn-Kurve)')
plt.xlabel('Monate der Mitgliedschaft')
plt.ylabel('Anzahl der Kündigungen')


#Lege den Ordner fest, indem gespeichert werden soll
output_dir = 'plots'
#Namensgebung
file_path = os.path.join(output_dir, 'churn_analysis.png')
#Speicherung
plt.savefig(file_path)

plt.close()
