#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster.bicluster import SpectralCoclustering
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource
from itertools import product

######## practice pt1

x = pd.Series([6, 3, 8, 6], index=["q", "w", "e", "r"])
# print(x.index)
# print(x)
x = x.reindex(sorted(x.index))
# print(x.index)
# print(x)
y = pd.Series([7, 3, 5, 2], index=["e", "q", "r", "t"])
# print(x + y)

######## practice pt2

data = {'name': ['Tim', 'Jim', 'Pam', 'Sam'],
        'age': [29, 31, 27, 35],
        'ZIP': ['02115', '02130', '67700', '00100']}
y = pd.DataFrame(data, columns=["name", "age", "ZIP"])
# print(y.name)

######## whisky preparations and plotting

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")
# print("\n\nWhisky head\n", whisky.head())
# print("\nWhisky tail\n", whisky.tail())
# print(whisky.iloc[0:10])
# print(whisky.iloc[5:10, 0:5])
# print(whisky.columns)
flavors = whisky.iloc[:, 2:14]
corr_flavors = pd.DataFrame.corr(flavors)
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
# plt.savefig("corr_flavors.pdf")

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.colorbar()
# plt.savefig("corr_whishy.pdf")

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)
# print(model.rows_)
# print(np.sum(model.rows_, axis=1))
# print(model.row_labels_)

whisky["Group"] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.ix[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)
correlations = pd.DataFrame.corr(whisky.iloc[:, 2:14].transpose())
correlations = np.array(correlations)

plt.figure(figsize=(14, 7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
# plt.savefig("correlations.pdf")

######## practice pt3 - using bokeh pt1

plot_values = [1,2,3,4,5]
plot_colors = ["red", "blue"]
grid = list(product(plot_values, plot_values))
# print(grid)
xs, ys = zip(*grid)
# print(xs, ys)
colors = [plot_colors[i%2] for i in range(len(grid))]
# print(colors)
alphas = np.linspace(0, 1, len(grid))
source = ColumnDataSource(
    data={
        "x": xs,
        "y": ys,
        "colors": colors,
        "alphas": alphas,
    }
)
output_file("Basic_Example.html", title="Basic Example")
fig = figure(tools="resize, hover, save")
fig.rect("x", "y", 0.9, 0.9, source=source, color="colors",alpha="alphas")
hover = fig.select(dict(type=HoverTool))
hover.tooltips = {
    "Value": "@x, @y",
    }
show(fig)

######## practice pt3 - using bokeh pt2

points = [(0,0), (1,2), (3,1)]
xs, ys = zip(*points)
colors = ["red", "blue", "green"]

output_file("Spatial_Example.html", title="Regional Example")
location_source = ColumnDataSource(
    data={
        "x": xs,
        "y": ys,
        "colors": colors,
    }
)

fig = figure(title = "Title",
    x_axis_location = "above", tools="resize, hover, save")
fig.plot_width  = 300
fig.plot_height = 380
fig.circle("x", "y", 10, 10, size=10, source=location_source,
     color='colors', line_color = None)

hover = fig.select(dict(type = HoverTool))
hover.tooltips = {
    "Location": "(@x, @y)"
}
show(fig)