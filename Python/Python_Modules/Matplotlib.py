# imports all functions of pyplot from matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_toolkits.mplot3d import axes3d
import matplotlib.style as mstyle
import matplotlib.animation as manime
import random as rd
import numpy as np
# creates plot data
#x = [j for j in range(0,101)]
#y = x
x = [j for j in range(0,101)]
y = [rd.randint(-50,50) for i in range(0,101)]

print('Default Data')
print("X Data: ", x)
print("Y Data: ", y)

def plot1():
    plt.plot(x, y)
    # creates a graph, and plots down the data, is connects plots automatically
    plt.show()
    # shows the graph
    # this well not show the markers to indicate the plot locations, just line.
# basic plot

def plot2():
    plt.plot(x, y, label='Plot2', color='red', marker='X', markeredgecolor='blue')
    #     1.        2.            3.          4.                     5.
    # 1) data.  2) sets the label of plot, only shows with legend().
    # 3) sets color of plot, line, bar.  4) sets marker for plots, X/O/+ etc, without this you can't see the plots
    # 5) sets the edge color of the marker, the inside well be what 'color' is, which is red right now
    plt.show()  # shows graph

# More Options
# s=50  --  sets size of markers
# plot(x,y, 'ro') / 'k-'  --  r or k is the color, o or - is the marker. just a quicker way to do color='red', marker='o'

def plotTypes():
    fig = plt.figure('bars')
    # this creates a new graph, a new windows, separate from the bar graph.
    ax1 = fig.add_subplot(111)
    # creates a empty plot

    ax1.bar(x, y, color='r', label='Bar1', edgecolor='b')  # makes bar graph with data
    #    1.       2.          3.              4.
    # 1) data.  2) fill color of bars.  3) label.
    # 5) sets color of edges of the bars.


    # histogram
    fig = plt.figure('hostgram')
    ax2 = fig.add_subplot(111)

    ax2.hist(x)

    # scatter
    fig = plt.figure('scatter')
    ax3 = fig.add_subplot(111)

    ax3.scatter(x, y)

    # stack plot
    fig = plt.figure('stack plot')
    ax4 = fig.add_subplot(111)

    ax4.stackplot(x, y)

    plt.show()
# shows different types of graphs and plots

def subplot2Grid_1():

    fig = figure()
    # creates new figure
    ax1 = subplot2grid((1, 1), (0, 0))
    # creates new plot graph, same as plot(x,y), but more options

    ax1.plot(x, y, label='PLOT')
    # calls plot with the ax1 settings

    ### Labels and Ticks ###

    ## Ticks ##
    for labels in ax1.xaxis.get_ticklabels():
        # for every x axis ticks do this
        labels.set_rotation(45)
        # rotate all of the x axis ticks, works with y axis >

    for labels in ax1.yaxis.get_ticklabels():
        labels.set_rotation(45)
        # rotates y ticks by 45

    ax1.tick_params(axis='x', colors='g')
    ax1.tick_params(axis='y', colors='r')
    # tick options

    #ax1.set_yticks([0, 10, 20, 30, 40, 50])
    # sets the tick marks for y axi
    # this well set this permanently, if zoom to far out or in it'll stay at these.

    ## Labels ##
    xlabel("X Label!")
    # shows x axi name
    ylabel("Y Label!")
    # shows y axi name
    title("This is a Graph!")
    # gives title to graph

    # Label Appearance #
    # X and Y axi label rotation
    ax1.xaxis.label.set_rotation(10)
    ax1.yaxis.label.set_rotation(10)

    # X and Y label color
    ax1.xaxis.label.set_color('g')
    # colors x label green
    ax1.yaxis.label.set_color('r')
    # colors y label red


    ### Graph Look ###

    ax1.fill_between(x, y, alpha=0.3, facecolor='r')
    # this well fill the graph basically, with some transparency
    # you can just use this without plot() and it'll still show the data, just not a big line
    # you can't label with this either. have to use a blank plot()

    ## Spines ##
    ax1.spines['left'].set_color('c')
    # changes left spine to cyan
    ax1.spines['left'].set_linewidth(5)
    # changes thickness of line
    ax1.spines['right'].set_visible(False)
    # hides right spine
    ax1.spines['top'].set_visible(False)
    # hides top spine

    ##  Grid ##

    major_ticks = np.arange(0, 101, 10)
    minor_ticks = np.arange(-50, 51, 10)
    # sets tick  marks range

    ax1.set_xticks(major_ticks)
    ax1.set_xticks(minor_ticks, minor=True)
    ax1.set_yticks(major_ticks)
    ax1.set_yticks(minor_ticks, minor=True)
    # shows tick marks

    grid(True, which='both')
    # enables grid, for more go to looks1()



    ax1.axhline(1, color='r', linewidth=1)
    # shows red line at Y 1

    subplots_adjust(left=0.09, right=.95, bottom=.15, top=.9, wspace=0.2, hspace=0)
    #     1.            2.          3.         4.        5         6.        7.
    # 1) sets the graph appearance.
    # you would use this if you need more space for the labels,
    #  because resizing the window won't give more room, it'll just make the graph bigger


    legend()
    show()
# how to use subplot2grid

def candleSticks1():
    pass
# candlestick graphs

def Style():

    print(matplotlib.__file__)
    # prints matplotlib file location

    print(style.available)
    # prints available styls

    style.use('DT_dark_background')
    # uses style

    grid(True)
    # enables grid

    plot(x,y, label='test')
    # creates plot
    legend()
    show()
# theming/stylizing your graphs

def Anime():

    mstyle.use("DT_dark_background")
    # style of graph

    fig = plt.figure()
    # new figure

    ax1 = fig.add_subplot(1,1,1)
    # creates ax1 subplot

    def animate(i):
        # a functions that reads from a file and refreshes the xs/ys list every 1 second

        graph_data = open("sampFile.txt", "r").read()
        # opens file to be read

        lines = graph_data.split('\n')
        # splits it by new line

        xs = []
        ys = []
        # creates blank lists

        for line in lines:
            if len(line) > 1:
                # check if the line is empty or not
                x, y = line.split(',')
                # if not, splits it by comma
                xs.append(x)
                ys.append(y)
                # appends to lists


            ax1.clear()
            # clears everything
            plt.grid(True)
            # shows grid. put this AFTER clear, if not it'll clear the hgrid too

            ax1.plot(xs,ys, marker='X', label='1sec Iterval')
            # plots out data
            plt.legend()
            # shows legend

    ani = manime.FuncAnimation(fig, animate, interval=1000)
    # uses figure, calls function with plot() and clear() and with data
    # then does this for ever every 1second, which is why you need clear()

    plt.show()
# not really animation, this well just keep updating the graph.
# so if you open up the data file and change the data, it'll update right away. no moving things though :(. but it's on the same principle

def Text():

    ### Setup ###
    fig = plt.figure()
    # figure
    ax1 = fig.add_subplot(1,1,1)
    # ax1

    ax1.grid(True)
    # enables grid

    ax1.plot(x,y)
    # plot

    ### Text ###
    font_dict = {'family' : 'verdana', # sets font family to serif
                 'color' : 'red', # sets color to red
                 'size' : 20,
                 'style' : 'italic',
                 'weight' : 'bold'}  # well size...... IT'S THE SIZE!!!   duh.

    # sets the configuration of fonts for anything that prints out text, labels, etc

    print("X Label Axi: ", x[50])
    print("Y Label Axi: ", y[50])
    ax1.text(x[50]-8, y[50]+ 1, "hi", fontdict=font_dict, withdash=True)
    #           1.    2.           3.                  4.
    # 1) coordinates of text, with a little offset so the arrow won't hide it.
    #   2) text.  3) calls font_dict for text properties
    # 5) ...
    # prints out text at X10 Y5, that says hi, with settings from font_dict


    text_opt = {'boxstyle' : 'round',
                'pad' : .5,
                'facecolor' : 'cyan',
                'edgecolor' : 'green',
                }

    arrow_props = {'facecolor' : 'blue',
                'edgecolor' : 'yellow'}


    plt.annotate('hi', xy=(x[50],y[50]), xytext=(1.03, 0.9), textcoords='axes fraction', bbox=text_opt, arrowprops=arrow_props)
    #             1.         2.                  3.                     4.                     5.                 6.
    # 1) text.  2) coordinates for arrow.  3) % offset of annotation text from coordinates (2.)
    # 4) gets the coords from x/y in thr 50th place, and that's where the arrow well point, it'll be different every time you run it.
    # 5) calls text_opt for the properties of the text  6) calls arrow_props dict for properties of arrow.



    plt.show()
    # shows everything
# show text and annotate on graph

def fourPlots():
    fig = plt.figure()
    # new window to graph

    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 3)
    ax3 = fig.add_subplot(2, 2, 2)
    ax4 = fig.add_subplot(2, 2, 4)
    # creates 4 new subplots to graph on to
    # (row, column, plotNum)

    ax1.plot(x,y)
    ax2.plot(x,y)
    ax3.plot(x,y)
    ax4.plot(x,y)
    # plots data on to each subplots, they all have the same data in the example
    plt.show()
# show more plots with subplot

def sixPlots():

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1)
    ax2 = plt.subplot2grid((6,1), (1,0), rowspan=1)
    ax3 = plt.subplot2grid((6,1), (2,0), rowspan=1)
    ax4 = plt.subplot2grid((6,1), (3,0), rowspan=1)
    ax5 = plt.subplot2grid((6,1), (4,0), rowspan=1)
    ax6 = plt.subplot2grid((6,1), (5,0), rowspan=1)
    # creates six plots stacked on top of each other
    # ((rows, columns), (startingRow, startingColumn))
    # rowspan/columnspan is how much space should the plot take up
    ax1.plot(x,y)
    ax2.plot(x,y)
    ax3.plot(x, y)
    ax4.plot(x, y)
    ax5.plot(x, y)
    ax6.plot(x, y)

    plt.show()
# shows six plots using subplot2grid

def Legend():
    plt.plot(x,y, label="plot1")
    plt.plot(y,x, label='Reverse plot')

    leg_props = {'size': 8 # font size
                 }
    plt.legend(loc=10, ncol=2, facecolor='r', prop=leg_props).get_frame().set_alpha(.1)
    #            1.       2.       3.                    4.
    # 1) sets location of legend, 1-4 corners, 5-9 sides, 10 center
    # 2) sets limit on colums.  3) sets face color.  4) gets some properties from dictionary.
    # 5) sets alpha of background
    plt.show()
# customize the legend

def ThreeD():
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    # sets ax1 to 3d projection

    mstyle.use('dark_background')
    # change style

    x = range(1,11)
    print("X: ", x)
    y = [rd.randint(0,11) for i in x]
    print("Y: ", y)
    z = [rd.randint(0,11) for j in x]
    print("Z: ", z)
    # creates random data to plot

    ax1.set_xlabel("X Axi")
    ax1.set_ylabel("Y Axi")
    ax1.set_zlabel("Z Axi")
    # names the x/y/z label

    ax1.plot_wireframe(x,y,z, label='Random Data')
    # plots data with a label

    ax1.scatter(x,y,z)
    # creates scatter plot, but layers on the wireframe.

    fig2 = plt.figure()
    # creates new figure, so makes a new windows
    ax2 = fig2.add_subplot(111, projection='3d')
    # new subplot with 3D projection

    ax2.set_xlabel("X Axi")
    ax2.set_ylabel("Y Axi")
    ax2.set_zlabel("Z Axi")
    # names the x/y/z label

    x1 = np.ones(10)
    y1 = np.ones(10)
    z1 = range(1,11)
    # this is the height of the bars, so bar 1-10 well have height 1-10

    ax2.plot([],[], color='r', label='BARS!!')
    # have to make a blank plot because for some reason bar3d won't take label
    ax2.bar3d(x,y,z, x1, y1, z1, color='r', edgecolor='c')
    # shows bar3d plot, the bars will be red with cyan edges


    plt.legend()
    plt.show()
# 3D plots, 3D bar-graph and 3D plotting

def betterWF():
    x,y,z = axes3d.get_test_data()
    # gets test data from axes3d module

    print("\nWireframe Test Data")
    print("X Data: ", x)
    print("Y Data: ", y)
    print("Z Data: ", z)
    # prints out test data

    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.plot_wireframe(x,y,z, rstride=10, cstride=10)
    # plots out data

    plt.show()
    print(axes3d.__file__)
# better wire frame

def grid():

    t = arange(0.0, 100.0, 0.1)
    s = sin(0.1*pi*t)*exp(-t*0.01)

    # test plot
    ax = subplot(111)
    plot(t,s)

    # sets xaxis gridlines
    ax.xaxis.set_major_locator(MultipleLocator(20))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.xaxis.set_minor_locator(MultipleLocator(5))
    # yaxis gridlines
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))

    ax.xaxis.grid(True,'minor')
    ax.yaxis.grid(True,'minor')
    # these well be the big main gridlines they'll be bigger
    ax.xaxis.grid(True,'major',linewidth=2)
    ax.yaxis.grid(True,'major',linewidth=2)
# customizing the grid. not the subplot2grid grid, the lines on the graph gird


# Calls function

ThreeD()