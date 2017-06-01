# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature



bird_data = pd.read_csv('bird_tracking.csv')
bird_names = pd.unique(bird_data.bird_name)

######## plotting flight path of the birds

plt.figure(figsize=(7, 7))
for bird_name in bird_names:
    ix = bird_data.bird_name == bird_name
    x, y = bird_data.longitude[ix], bird_data.latitude[ix]
    plt.plot(x, y, ".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
# plt.savefig("3traj.pdf")

######## plotting the speed of the birds and its frequency

plt.figure(figsize=(8, 4))
for bird_name in bird_names:
    ix = bird_data.bird_name == bird_name
    speed = bird_data.speed_2d[ix]
    ind = np.isnan(speed)
    plt.hist(speed[~ind], bins=np.linspace(0, 30, 20), normed=True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency");
# plt.savefig("speed_freq.pdf")

# other method for this ^
bird_data.speed_2d.plot(kind='hist', range=[0, 30])
# plt.savefig("speed_freq_2.pdf")

######## using datetime

date_str = bird_data.date_time[0]
datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")

timestamps = []
for k in range(len(bird_data)):
    timestamps.append(datetime.datetime.strptime\
                      (bird_data.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

bird_data["timestamp"] = pd.Series(timestamps, index = bird_data.index)

######## daily mean speed

eric_data = bird_data[bird_data.bird_name == "Eric"]
times = eric_data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)


next_day = 1
inds = []
daily_mean_speed = []
for index, time in enumerate(elapsed_days):
    if time < next_day:
        inds.append(index)
    else:
        daily_mean_speed.append(np.mean(eric_data.speed_2d[inds]))
        next_day += 1
        inds = []

plt.figure(figsize=(8, 6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.savefig("mean_speed.pdf")

######## actual path of the birds with Cartopy

projection = ccrs.Mercator()

plt.figure(figsize=(10, 10))
ax = plt.axes(projection=projection)
ax.set_extent((-25, 20, 52, 10))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
for bird_name in bird_names:
    ix = bird_data.bird_name == bird_name
    x, y = bird_data.longitude[ix], bird_data.latitude[ix]
    ax.plot(x, y, '.', transform=ccrs.Geodetic(), label=bird_name)
    
plt.legend(loc="upper left")
# plt.savefig("map.pdf")
