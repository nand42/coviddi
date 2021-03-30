import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt

# Costante di convoluzione, usata in moving_average(x, w)
W = 4

CODICI_REGIONI = {}




def moving_average(x, w=W):
    return np.convolve(x, np.ones(w), 'valid') / w


# serve?
def load_jsonl(input_path) -> list:
    data = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.rstrip('\n|\r')))
    print('Loaded {} records from {}'.format(len(data), input_path))
    return data


class Plotting:

    path_save_figure = 'figure/'

    NOMI_PLOT = {'1': ('nuovi_positivi', 'nuovi positivi')
        , '2': ('ricoverati_con_sintomi', 'ricoverati con sintomi')
        , '3': ('terapia_intensiva', 'terapia intensiva')
        , '4': ('ingressi_terapia_intensiva', 'ingressi terapia intensiva')
        , '5': ('totale_ospedalizzati', 'totale ospedalizzati')
        , '6': ('totale_positivi', 'totale positivi')
        , '7': ('tamponi', 'tamponi')
                 }

    def __init__(self, name):
        Plotting.name = name
        Plotting.convolute = False

    def print_info(self):
        print('I possibili dati sono:')
        for el in range(len(self.NOMI_PLOT)):
            print(el)

    def clear(self):
        plt.clf()

    def legend(self):
        plt.legend(loc='upper left')

    def make_convolution(self, x):
        Plotting.convolute = True
        return moving_average(x, w=W)

    def make_plot(self, x, name):
        plot_x = plt.plot(x, label=self.NOMI_PLOT[name])

    def save_figure(self, name):
        plt.savefig(self.path_save_figure + name + '.png')




def plot_nuovi_positivi(df, name=''):
    nuovi_positivi = plt.plot(df.nuovi_positivi, label='nuovi_positivi')
    plt.legend(loc='upper left')
    plt.title(name)
    plt.savefig('fig/nuovi_positivi' + name + '.png')
    return nuovi_positivi


def plot_ricoverati_con_sintomi(df, name=''):
    ricoverati_con_sintomi = plt.plot(df.ricoverati_con_sintomi, label='ricoverati_con_sintomi')
    plt.legend(loc='upper left')
    plt.title(name)
    plt.savefig('fig/ricoverati_con_sintomi' + name + '.png')
    return ricoverati_con_sintomi


def plot_terapia_intensiva(df, name=''):
    terapia_intensiva = plt.plot(df.terapia_intensiva, label='terapia_intensiva')
    plt.legend(loc='upper left')
    plt.title(name)
    plt.savefig('fig/terapia_intensiva' + name + '.png')
    return terapia_intensiva


def plot_ingressi_terapia_intensiva(df, name=''):
    ingressi_terapia_intensiva = plt.plot(df.ingressi_terapia_intensiva, label='ingressi_terapia_intensiva')
    plt.legend(loc='upper left')
    plt.title(name)
    plt.savefig('fig/ingressi_terapia_intensiva' + name + '.png')
    return ingressi_terapia_intensiva


def plot_totale_ospedalizzati(df, name=''):
    totale_ospedalizzati = plt.plot(df.totale_ospedalizzati, label='totale_ospedalizzati')
    plt.legend(loc='upper left')
    plt.title(name)
    plt.savefig('fig/totale_ospedalizzati' + name + '.png')
    return totale_ospedalizzati


def plot_totale_positivi(df, name=''):
    totale_positivi = plt.plot(df.totale_positivi, label='totale_positivi')
    plt.legend(loc='upper left')
    plt.title(name)
    plt.savefig('fig/totale_positivi' + name + '.png')
    return totale_positivi


def plot_tamponi(df, name=''):
    tamponi = plt.plot(df.tamponi, label='tamponi')
    plt.legend(loc='upper left')
    plt.title(name)
    plt.savefig('fig/tamponi' + name + '.png')
    return tamponi


def add_col_data(df):
    df['giorno'] = df.data.str.slice(stop=10)
    return df


def plot_conv_terapia_intensiva(df, name=''):
    terapia_intensiva = plt.plot(moving_average(df.terapia_intensiva), label='Convoluzione terapia_intensiva')
    plt.legend(loc='upper left')
    plt.title(name)
    plt.savefig('fig/terapia_intensiva_CONV' + name + '.png')
    return terapia_intensiva


def plot_conv_ingressi_terapia_intensiva(df, name=''):
    ingressi_terapia_intensiva = plt.plot(moving_average(df.ingressi_terapia_intensiva), label='Convoluzione ingressi_terapia_intensiva')
    plt.legend(loc='upper left')
    plt.title(name)
    plt.savefig('fig/ingressi_terapia_intensiva_CONV' + name + '.png')
    return ingressi_terapia_intensiva


def plot_conv_totale_positivi(df, name=''):
    totale_positivi = plt.plot(moving_average(df.totale_positivi), label='Convoluzione totale_positivi')
    plt.legend(loc='upper left')
    plt.title(name)
    plt.savefig('fig/totale_positivi_CONV' + name + '.png')
    return totale_positivi


def plot_conv_nuovi_positivi(df, name=''):
    nuovi_positivi = plt.plot(moving_average(df.nuovi_positivi), label='Convoluzione nuovi_positivi')
    plt.legend(loc='upper left')
    plt.title(name)
    plt.savefig('fig/nuovi_positivi_CONV' + name + '.png')
    return nuovi_positivi


