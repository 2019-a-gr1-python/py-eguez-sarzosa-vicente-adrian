#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:14:56 2019

@author: usrdel
"""

import pandas as pd


path_guardado = '/Users/usrdel/Documents/GitHub/py-eguez-sarzosa-vicente-adrian/03_Pandas/data/csv/artwork_data.pickle'

df_completo_pickle = pd.read_pickle(path_guardado)

serie_artistas_duplicados = df_completo_pickle['artist']

artistas = pd.unique(serie_artistas_duplicados)

artistas.size

len(artistas)

blake = df_completo_pickle['artist'] == 'Blake, William'

type(blake)  # pandas.core.series.Series

blake.value_counts()

df_blake = df_completo_pickle[blake]

type(df_blake)  # pandas.core.frame.DataFrame
df_blake


















