# -*- coding: utf-8 -*-
"""Lebron James.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1by6dECTetG6zAb7E_p32ylL3iOayVoRS
"""

import numpy as np
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup
import requests
from bs4 import SoupStrainer
import matplotlib.pyplot as plt
from bs4 import Comment
from pathlib import Path

lebron_df = pd.read_csv('NBA lebron - lebron.csv')
kareem_df = pd.read_csv('NBA lebron - kareem.csv')
karl_df = pd.read_csv('NBA lebron - karl.csv')
kobe_df = pd.read_csv('NBA lebron - kobe.csv')
mj_df = pd.read_csv('NBA lebron - mj.csv')

kareem_df

lebron_df = lebron_df[['SEASON', 'TEAM', 'PTS', 'AGE']].dropna()
kareem_df = kareem_df[['SEASON', 'TEAM', 'PTS', 'AGE']].dropna()

kareem_df = kareem_df.loc[::-1]

lebron_df['AGE'] = lebron_df['AGE'].astype('int64')
kareem_df['AGE'] = kareem_df['AGE'].astype('int64')
karl_df['AGE'] = karl_df['AGE'].astype('int64')
kobe_df['AGE'] = kobe_df['AGE'].astype('int64')
mj_df['AGE'] = mj_df['AGE'].astype('int64')

lebron_df['CUM PTS'] = lebron_df['PTS'].cumsum()
kareem_df['CUM PTS'] = kareem_df['PTS'].cumsum()
karl_df['CUM PTS'] = karl_df['PTS'].cumsum()
kobe_df['CUM PTS'] = kobe_df['PTS'].cumsum()
mj_df['CUM PTS'] = mj_df['PTS'].cumsum()

dirk_df = pd.read_csv('NBA lebron - dirk.csv')
wilt_df = pd.read_csv('NBA lebron - wilt.csv')
shaq_df = pd.read_csv('NBA lebron - shaq.csv')
carmelo_df = pd.read_csv('NBA lebron - carmelo.csv')
moses_df = pd.read_csv('NBA lebron - moses.csv')

dirk_df['AGE'] = dirk_df['AGE'].astype('int64')
wilt_df['AGE'] = wilt_df['AGE'].astype('int64')
shaq_df['AGE'] = shaq_df['AGE'].astype('int64')
carmelo_df['AGE'] = carmelo_df['AGE'].astype('int64')
moses_df['AGE'] = moses_df['AGE'].astype('int64')

dirk_df['CUM PTS'] = dirk_df['PTS'].cumsum()
wilt_df['CUM PTS'] = wilt_df['PTS'].cumsum()
shaq_df['CUM PTS'] = shaq_df['PTS'].cumsum()
carmelo_df['CUM PTS'] = carmelo_df['PTS'].cumsum()
moses_df['CUM PTS'] = moses_df['PTS'].cumsum()

total_df = lebron_df[['AGE','CUM PTS']].merge(kareem_df[['AGE', 'CUM PTS']], on = 'AGE', how='outer').rename(columns={'CUM PTS_x':'Lebron', 'CUM PTS_y':'Kareem'})
total_df = total_df.merge(karl_df[['AGE', 'CUM PTS']], on = 'AGE', how='outer').rename(columns={'CUM PTS': 'Karl'})
total_df = total_df.merge(kobe_df[['AGE', 'CUM PTS']], on = 'AGE', how='outer').rename(columns={'CUM PTS': 'Kobe'})
total_df = total_df.merge(mj_df[['AGE', 'CUM PTS']], on = 'AGE', how='outer').rename(columns={'CUM PTS': 'MJ'})
total_df = total_df.merge(dirk_df[['AGE', 'CUM PTS']], on = 'AGE', how='outer').rename(columns={'CUM PTS': 'Dirk'})
total_df = total_df.merge(wilt_df[['AGE', 'CUM PTS']], on = 'AGE', how='outer').rename(columns={'CUM PTS': 'Wilt'})
total_df = total_df.merge(shaq_df[['AGE', 'CUM PTS']], on = 'AGE', how='outer').rename(columns={'CUM PTS': 'Shaq'})
total_df = total_df.merge(carmelo_df[['AGE', 'CUM PTS']], on = 'AGE', how='outer').rename(columns={'CUM PTS': 'Carmelo'})
total_df = total_df.merge(moses_df[['AGE', 'CUM PTS']], on = 'AGE', how='outer').rename(columns={'CUM PTS': 'Moses'})

total_df

filepath = Path('sample_data/out.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
total_df.to_csv(filepath)

plt.figure(figsize=(18,10))
plt.scatter(lebron_df['AGE'], lebron_df['CUM PTS'], label='lebron')
plt.scatter(kareem_df['AGE'], kareem_df['CUM PTS'], label='kareem')
plt.scatter(karl_df['AGE'], karl_df['CUM PTS'], label='karl')
plt.scatter(kobe_df['AGE'], kobe_df['CUM PTS'], label='kobe')
plt.scatter(mj_df['AGE'], mj_df['CUM PTS'], label='mj')
plt.scatter(dirk_df['AGE'], dirk_df['CUM PTS'], label='dirk')
plt.scatter(wilt_df['AGE'], wilt_df['CUM PTS'], label='wilt')
plt.scatter(shaq_df['AGE'], shaq_df['CUM PTS'], label='shaq')
plt.scatter(carmelo_df['AGE'], carmelo_df['CUM PTS'], label='carmelo')
plt.scatter(moses_df['AGE'], moses_df['CUM PTS'], label='moses')

plt.legend()
plt.show()