# AHPA #21 - Math Class
#
# Write a Python program to display 
# three separate graphs for sin, cos, 
# and tan. 
#
# Add the ability to show all three 
# graphs on a single graph with one row 
# and three columns. 
#
#Student Name: Evagelos Petropoulos
#

from matplotlib import pyplot as plt
from matplotlib.pyplot import subplot
import numpy

#PLEASE READ, to see more graphs it may be necessary to  exit out the current one being viewed, for whatever reason the forward 
#and back buttons are not working for me, but they may possibly work on other systems.

#x-axis range using pi
x = numpy.arange(0 , 5 * numpy.pi, 0.1)
#line for sin(x)
y1 = numpy.sin(x)
#line for cos(x)
y2 = numpy.cos(x)
#line for tan(x
y3 = numpy.tan(x)

#printing out graphs separately first
#graph for sin(x)
plt.figure('Sin(x)')
plt.plot(x, numpy.sin(x), color = 'red')
plt.title('Sin(x)')
plt.show()
#graph for cos(x)
plt.figure('Cos(x)')
plt.plot(x, numpy.cos(x), color = 'blue')
plt.title('Cos(x)')
plt.show()
#graph for tan(x)
plt.figure('Tan(x)')
plt.plot(x, numpy.tan(x), color = 'green')
plt.title('Tan(x)')
plt.show()

#printing out graphs as one graph separately with rows and columns
#figure for the graphs being all shown at once 
plt.figure('All Three Graphs')

#graph for sin(x)
subplot(1,3,1)      #1 row, 3 columns, and 1st position for this graph, and so on
plt.plot(x, numpy.sin(x), color = 'red')
plt.title('Sin(x)')

#graph for cos(x)
subplot(1,3,2)
plt.plot(x, numpy.cos(x), color = 'blue')
plt.title('Cos(x)')

#graph for tan(x)
subplot(1,3,3)
plt.plot(x, numpy.tan(x), color = 'green')
plt.title('Tan(x)')
#shows the graph
plt.show()







