###################################################
#                                                 #
#  A script to read location values from a csv    #
#  file and plot them on a geographical map.      #
#                                                 #
#  Author - Tanay Soni                            #
#  ts398@kent.ac.uk                               #
#                                                 #
#  Here's a link to sample output image:          #   
#  http://tinyurl.com/opar7pg                     #
#                                                 #
###################################################

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import csv
import numpy as np

# Set-up map of United Kingdom using Basemap
m = Basemap(projection='mill',llcrnrlat=50,urcrnrlat=60, llcrnrlon=-20,urcrnrlon=5,resolution='h')
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',lake_color='aqua')

# Read accident location co-ordinates from a csv file.
f = open('Accidents0512.csv', 'r') 
reader = csv.reader(f, delimiter=',')
next(reader)

# Store values of the co-ordinates in lists.     
latitudes = []
longitudes = []
for row in reader:
   if(row[3] != '' and row[4] != ''):
      longitudes.append(float(row[3]))
      latitudes.append(float(row[4]))
   
# Plot co-ordinates on the Basemap
x,y = m(longitudes, latitudes)
m.plot(x, y, 'ro',markersize=.01)
plt.suptitle('Locations of accidents in the UK for years 2005-2012')
plt.savefig('map.png',dpi=400)
