#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# df1 = pd.read_csv(r'Areas_and_Densities_Table_1.csv', sep='\t', header=0)

df1 = pandas.read_csv('Areas_and_Densities_Table_1.csv')
# df2 = pandas.read_csv('Blocks_and_Roads_Table_1.csv')
# df3 = pandas.read_csv('Blocks_and_Roads_Table_2.csv')

#%% Dataset initialization

# dataset description: data on 200 cities from different time periods
df1 = df1.iloc[1:201,:]
# columns 1-3: name, country, region
# columns 4-5: CBD location (latitude, longitude)
cbd_location = df1.iloc[1:,3:5]
# columns 6-8: land cover dates (T1, T2, T3)
dates = df1.iloc[1:,5:8]
# columns 9-11: urban extent population (T1, T2, T3)
# column 12: annual change T2-T3 (of population)
population = df1.iloc[1:,8:11]
population_change = df1.iloc[1:,11:12]
# columns 13-15: built-up area total (T1, T2, T3)
# column 16: annual change T2-T3 (of total area)
total_area = df1.iloc[1:,12:15]
total_area_change = df1.iloc[1:,15:16]
# columns 17-19: urban built-up area (T1, T2, T3)
# column 20: annual change T2-T3 (of urban area)
urban_area = df1.iloc[1:,16:19]
urban_area_change = df1.iloc[1:,19:20]
# columns 21-23: suburban built-up area (T1, T2, T3)
# column 24: annual change T2-T3 (of suburban area)
suburban_area = df1.iloc[1:,20:23]
suburban_area_change = df1.iloc[1:,23:24]
# columns 25-27: rural built-up area (T1, T2, T3)
# column 28: annual change T2-T3 (of rural area)
rural_area = df1.iloc[1:,24:27]
rural_area_change = df1.iloc[1:,27:28]
# columns 29-31: urbanized open space (T1, T2, T3)
# column 32: annual change T2-T3 (of urbanized open space)
urbanized_open_space = df1.iloc[1:,28:31]
urbanized_open_space_change = df1.iloc[1:,31:32]
# columns 33-35: urban extent (T1, T2, T3)
# column 36: annual change T2-T3 (of urban extent)
urban_extent = df1.iloc[1:,32:35]
urban_extent_change = df1.iloc[1:,35:36]
# columns 37-39: built-up area density (T1, T2, T3)
# column 40: annual change T2-T3 (of built-up density)
built_density = df1.iloc[1:,36:39]
built_density_change = df1.iloc[1:,39:40]
# columns 41-43: urban extent density (T1, T2, T3)
# column 44: annual change T2-T3 (of urban extent density)
urban_extent_density = df1.iloc[1:,40:43]
urban_extent_density_change = df1.iloc[1:,43:44]
# columns 45-47: saturation (built-up area/urban extent) (T1, T2, T3)
# column 48: annual change T2-T3 (of saturation)
urban_extent = df1.iloc[1:,44:47]
urban_extent_change = df1.iloc[1:,47:48]

#%% convert

df1['Unnamed: 11'] = df1['Unnamed: 11'].str[:-1]
df1['Unnamed: 19'] = df1['Unnamed: 19'].str[:-1]

df1['Unnamed: 11'] = df1['Unnamed: 11'].astype(float)
df1['Unnamed: 19'] = df1['Unnamed: 19'].astype(float)

#%% Regions

# the 8 regions, as defined by the United Nations
sub_saharan_africa = df1[df1["Region"] == 'Sub-Saharan Africa'] 
south_and_central_asia = df1[df1["Region"] == 'South and Central Asia']
western_asia_and_north_africa = df1[df1["Region"] == 'Western Asia and North Africa']
east_asia_and_the_pacific = df1[df1["Region"] == 'East Asia and the Pacific']
europe_and_japan = df1[df1["Region"] == 'Europe and Japan']
land_rich_developed_countries = df1[df1["Region"] == 'Land-Rich Developed Countries']
southeast_asia = df1[df1["Region"] == 'Southeast Asia']
latin_america_and_the_caribbean = df1[df1["Region"] == 'Latin America and the Caribbean']

#%% World Map

df1['Unnamed: 4'] = df1['Unnamed: 4'].astype(float)
df1['CBD Location'] = df1['CBD Location'].astype(float)

df1.plot.scatter(x='Unnamed: 4', y='CBD Location', xlim=(-150,200), ylim=(-75,175), s=3);

#%% Sub-Saharan Africa analysis

# plot x = population changes, y = urban area changes
x = sub_saharan_africa['Unnamed: 11']
y = sub_saharan_africa['Unnamed: 19']

plt.plot(x,y,"+", ms=10, mec="k")
z = np.polyfit(x, y, 1)
y_hat = np.poly1d(z)(x)

plt.plot(x, y_hat, "r--", lw=1)
text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
     fontsize=14, verticalalignment='top')

#%% South and Central Asia analysis

x = south_and_central_asia['Unnamed: 11']
y = south_and_central_asia['Unnamed: 19']

plt.plot(x,y,"+", ms=10, mec="k")
z = np.polyfit(x, y, 1)
y_hat = np.poly1d(z)(x)

plt.plot(x, y_hat, "r--", lw=1)
text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
     fontsize=14, verticalalignment='top')

#%% Western Asia and North Africa analysis

x = western_asia_and_north_africa['Unnamed: 11']
y = western_asia_and_north_africa['Unnamed: 19']

plt.plot(x,y,"+", ms=10, mec="k")
z = np.polyfit(x, y, 1)
y_hat = np.poly1d(z)(x)

plt.plot(x, y_hat, "r--", lw=1)
text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
     fontsize=14, verticalalignment='top')

#%% East Asia and the Pacific analysis

x = east_asia_and_the_pacific['Unnamed: 11']
y = east_asia_and_the_pacific['Unnamed: 19']

plt.plot(x,y,"+", ms=10, mec="k")
z = np.polyfit(x, y, 1)
y_hat = np.poly1d(z)(x)

plt.plot(x, y_hat, "r--", lw=1)
text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
     fontsize=14, verticalalignment='top')

#%% Europe and Japan analysis

x = europe_and_japan['Unnamed: 11']
y = europe_and_japan['Unnamed: 19']

plt.plot(x,y,"+", ms=10, mec="k")
z = np.polyfit(x, y, 1)
y_hat = np.poly1d(z)(x)

plt.plot(x, y_hat, "r--", lw=1)
text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
     fontsize=14, verticalalignment='top')

#%% Land-Rich Developed Countries analysis

x = land_rich_developed_countries['Unnamed: 11']
y = land_rich_developed_countries['Unnamed: 19']

plt.plot(x,y,"+", ms=10, mec="k")
z = np.polyfit(x, y, 1)
y_hat = np.poly1d(z)(x)

plt.plot(x, y_hat, "r--", lw=1)
text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
     fontsize=14, verticalalignment='top')

#%% Southeast Asia analysis

x = southeast_asia['Unnamed: 11']
y = southeast_asia['Unnamed: 19']

plt.plot(x,y,"+", ms=10, mec="k")
z = np.polyfit(x, y, 1)
y_hat = np.poly1d(z)(x)

plt.plot(x, y_hat, "r--", lw=1)
text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
     fontsize=14, verticalalignment='top')

#%% Latin America and the Caribbean analysis

x = latin_america_and_the_caribbean['Unnamed: 11']
y = latin_america_and_the_caribbean['Unnamed: 19']

plt.plot(x,y,"+", ms=10, mec="k")
z = np.polyfit(x, y, 1)
y_hat = np.poly1d(z)(x)

plt.plot(x, y_hat, "r--", lw=1)
text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
     fontsize=14, verticalalignment='top')
