📊 Executive Summary & Key Visualizations

Diese Analyse nutzt den Telco Customer Churn Datensatz von Kaggle zur Identifikation von Geschäftsrisiken.
https://www.kaggle.com/datasets/blastchar/telco-customer-churn?resource=download

Für eine schnelle Übersicht gerne hier reinschauen: visualization.ipynb

1. Die Churn-Kurve: Identifikation von kritischen Phasen
<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/e21d7f15-f6f3-4315-9a37-f7f42e71182f" />


Analyse: Ein massiver Anstieg der Kündigungen (Churn) erfolgt bereits im ersten Monat (tenure = 1). Dies deutet auf Probleme beim Onboarding oder fehlerhafte Erwartungsmanagement hin. Kunden, die das erste Jahr "überleben", zeigen eine signifikant höhere Loyalität.

2. Financial Impact: Umsatzverlust nach Vertragstyp
<img width="1000" height="600" alt="image" src="https://github.com/user-attachments/assets/c267f955-34ff-4164-b6c2-0553b20b4aae" />


Business Insight: Der größte monatliche Umsatzverlust entsteht durch Kunden mit "Month-to-month"-Verträgen. Während Langzeitverträge (1-2 Jahre) stabilere Cashflows bieten, ist die schiere Masse der Kurzzeit-Kündiger das größte finanzielle Risiko für das Unternehmen.

3. Service-Korrelation: Einfluss von Tech Support
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/5a05443d-2d91-476d-bc2b-3ea39dc0255c" />


Strategische Empfehlung: Kunden ohne Zugriff auf technischen Support kündigen überproportional häufig. Die Kopplung von technischem Service an Einstiegstarife könnte die Churn-Rate in der kritischen Anfangsphase massiv senken.

Dieses Projekt demonstriert die Schnittstelle zwischen IT-Kompetenz und betriebswirtschaftlichem Verständnis:

Daten-Engineering: Vorverarbeitung und Aggregation von Rohdaten mit Pandas.

Business Intelligence: Übersetzung technischer Metriken (Tenure, MonthlyCharges) in wirtschaftliche Kennzahlen (Revenue Loss, Churn Risk).

Entscheidungsunterstützung: Ableitung konkreter Handlungsempfehlungen für das Produktmanagement (z.B. Fokus auf Support-Services).

🛠 Technische Umsetzung
Sprache: Python 3.x

Libraries: Pandas (Datenanalyse), Seaborn & Matplotlib (Visualisierung), Numpy (Berechnungen).

Methodik: Gruppierung nach Vertragsmerkmalen, Berechnung des aggregierten Umsatzverlustes und Verteilungsanalyse der Kundenlaufzeiten.
