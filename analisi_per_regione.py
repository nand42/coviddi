import covid_def as co
import pandas as pd
import matplotlib.pyplot as plt

target = './COVID-19/dati-regioni/dpc-covid19-ita-regioni.csv'
df = pd.read_csv(target)

co.add_col_data(df)

"""
for el in df.groupby('denominazione_regione'):
    print(el[0], el[1].codice_regione[0:1])
--------------------------
codice e denominazione regione
--------------------------
01 Piemonte
02 Valle d'aosta
03 Lombardia
05 Veneto
06 Friuli Venezia Giulia
07 Liguria
08 Emilia-Romagna
09 Toscana
10 Umbria
11 Marche
13 Abruzzo
14 Molise
15 Campania
16 Puglia
17 Basilicata
18 Calabria
19 Sicilia
20 Sardegna
21 P.A. Bolzano
22 P.A Trento
--------------------------
"""

regione = 5

que = 'codice_regione == ' + str(regione)

df_reg = df.query(que)

co.plot_nuovi_positivi(df_reg, '_' + str(regione))
plt.clf()
co.plot_conv_nuovi_positivi(df_reg, '_' + str(regione))
plt.clf()
co.plot_terapia_intensiva(df_reg, '_' + str(regione))
plt.clf()
co.plot_conv_terapia_intensiva(df_reg, '_' + str(regione))
plt.clf()
co.plot_ingressi_terapia_intensiva(df_reg, '_' + str(regione))
plt.clf()
co.plot_conv_ingressi_terapia_intensiva(df_reg, '_' + str(regione))
plt.clf()
co.plot_totale_positivi(df_reg, '_' + str(regione))
plt.clf()
co.plot_conv_totale_positivi(df_reg, '_' + str(regione))
plt.clf()


df.to_json()
print('\nend')
