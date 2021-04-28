import covid_def as co
import pandas as pd
import matplotlib.pyplot as plt

target = './COVID-19/dati-json/dpc-covid19-ita-andamento-nazionale.json'

df = pd.read_json(target)

print(df.shape)
keys = df.keys()
print(keys)

for el in keys:
    print(el)


# PLOT 1
totale_positivi = plt.plot(df.totale_positivi, label='totale_positivi')
dimessi_guariti = plt.plot(df.dimessi_guariti, label='dimessi_guariti')

plt.legend(loc='upper left')
plt.savefig('pic/dimessi_attpositivi.png')
plt.clf()


# PLOT 2
totale_positivi = plt.plot(df.totale_positivi, label='totale_positivi')
dimessi_guariti = plt.plot(df.dimessi_guariti, label='dimessi_guariti')
delta = plt.plot(df.totale_positivi - df.dimessi_guariti, label='delta1 = positivi - guariti')
plt.hlines(0, 0, 260, linestyles='dashed')
plt.legend(loc='upper left')
plt.savefig('pic/dimessi_attpositivi_positivi_dimessi_delta1.png')
plt.clf()


# PLOT 3
totale_positivi = plt.plot(df.totale_positivi, label='totale_positivi')
dimessi_guariti = plt.plot(df.dimessi_guariti, label='dimessi_guariti')
deceduti = plt.plot(df.deceduti, label='deceduti')
delta = plt.plot(df.totale_positivi - df.dimessi_guariti, label='delta1 = positivi - guariti')
DELTA = plt.plot(df.totale_positivi - df.dimessi_guariti - df.deceduti, label='delta2 = positivi - guariti o deceduti')

plt.hlines(0, 0, 260, linestyles='dashed')
plt.legend(loc='upper left')
plt.savefig('pic/dimessi_attpositivi_positivi_dimessi_deceduti_delta1_delta2.png')
plt.clf()


# PLOT 4
delta = plt.plot(df.totale_positivi - df.dimessi_guariti, label='delta1 = positivi - guariti')
DELTA = plt.plot(df.totale_positivi - df.dimessi_guariti - df.deceduti, label='delta2 = positivi - guariti o deceduti')

plt.hlines(0, 0, 260, linestyles='dashed')
plt.legend(loc='upper left')
plt.savefig('pic/dimessi_attpositivi_confronto_delta1_delta2.png')
plt.clf()


# PLOT 5
delta = plt.plot(df.totale_positivi - df.dimessi_guariti, label='delta')

plt.hlines(0, 0, 260, linestyles='dashed')
plt.legend(loc='upper left')
plt.savefig('pic/dimessi_attpositivi_delta1.png')
plt.clf()


# PLOT 6
DELTA = plt.plot(df.totale_positivi - df.dimessi_guariti - df.deceduti, label='delta2 = positivi - guariti o deceduti')

plt.hlines(0, 0, 260, linestyles='dashed')
plt.legend(loc='upper left')
plt.savefig('pic/dimessi_attpositivi_delta2.png')
plt.clf()


# PLOT 7
co.plot_terapia_intensiva(df, '_ totale terapia intensiva')
co.plot_conv_terapia_intensiva(df, '_ totale terapia intensiva')

