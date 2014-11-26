__author__ = 'Erik Nylander'

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import misc

# Creating a pandas data frame to hold the car data.
headers1 = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class_value']
df1 = pd.read_csv('cardata.csv', sep=',', names=headers1, header=None)
buying = df1.groupby('buying').size()
maint = df1.groupby('maint').size()
safety = df1.groupby('safety').size()
doors = df1.groupby('doors').size()
# Generating the 4 plots as subplots of a single figure
plt.figure(1, tight_layout=True)
plt.subplot(221)
pos1 = np.arange(4)+.5
plt.bar(pos1, buying, align='center', color='r')
plt.xticks(pos1, buying.index)
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Buying Price')

plt.subplot(222)
pos2 = np.arange(4)+.5
plt.bar(pos2, maint, align='center', color='b')
plt.xticks(pos2, maint.index)
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Maintenance Price')

plt.subplot(223)
pos3 = np.arange(3)+.5
plt.bar(pos3, safety, align='center', color='g')
plt.xticks(pos3, safety.index)
plt.xlabel('Safety')
plt.ylabel('Frequency')
plt.title('Safety Ratings')

plt.subplot(224)
pos4 = np.arange(4)+.5
plt.bar(pos4, doors, align='center', color='m')
plt.xticks(pos4, doors.index)
plt.xlabel('Doors')
plt.ylabel('Frequency')
plt.title('Number of Doors')


# Creating the Scatter plot of GPA Data
def f(t):
    """
    Generating a linear function with fixed parameters for the GPA Data
    :param t: input value for the function
    :return: output value for the function
    """
    m = 0.674830
    b = 1.096823
    return m*t+b

df2 = pd.read_csv('gpas.csv', sep=',', header=0)
min = df2['high_GPA'].min()
max = df2['high_GPA'].max()
plt.figure(2)
plt.plot(df2['high_GPA'], df2['univ_GPA'], 'ro', [min, max], [f(min), f(max)])
plt.xlabel('High School GPA')
plt.ylabel('University GPA')
plt.text(3, 2.7, r'LSR Equation')
plt.text(3, 2.6, r'y=0.67438x + 1.096823')
plt.title('High School GPA vs. University GPA')


# Plotting the centers of mass of the objects file
# objectsCM.csv is a csv file of the centers of mass for the objects image
image = misc.imread('objects.png')
headers2 = ['x_val', 'y_val']
df3 = pd.read_csv('objectsCM.csv', sep=',', names=headers2, header=None)
plt.figure(3)
plt.imshow(image, origin='lower')
plt.autoscale(False)
plt.plot(df3['y_val'], df3['x_val'], 'ro')
plt.title('Centers of Mass of the Objects')
plt.axis('off')


# Plotting the hourly server requests for EPA HTTP Server
# hourlyrequests.csv is a csv file of the hourly requests for the server grouped by hours
headers3 = ['hour', 'requests']
df4 = pd.read_csv('hourlyrequests.csv', sep=',', names=headers3, header=None)
pos5 = np.arange(24)
xticks = []
for x in df4['hour']:
    xticks.append('%d:00 - %d:00' % (x, x+1))
plt.figure(4, tight_layout=True)
plt.plot(df4['hour'], df4['requests'], 'o-')
plt.xticks(pos5, xticks, rotation=45, ha='right')
plt.xlim(-0.5,23.5)
plt.xlabel('Time in Hours: 24H Format')
plt.ylabel('Number of Requests')
plt.title('Number of Server Request per Hour of the EPA HTTP Server')

plt.show()