# Copyright 2015 Enthought, Inc. All Rights Reserved
"""
Plotting
--------

In PyLab, create a plot display that looks like the following:

.. image:: plotting/sample_plots.png

`Photo credit: David Fettig
<http://www.publicdomainpictures.net/view-image.php?image=507>`_


This is a 2x2 layout, with 3 slots occupied.

1. Sine function, with blue solid line; cosine with red '+' markers; the
   extents fit the plot exactly. Hint: see the axis() function for setting the
   extents.
2. Sine function, with gridlines, axis labels, and title; the extents fit the
   plot exactly.
3. Image with color map; the extents run from -10 to 10, rather than the
   default.

Save the resulting plot image to a file. (Use a different file name, so you
don't overwrite the sample.)

The color map in the example is 'winter'; use 'cm.<tab>' to list the available
ones, and experiment to find one you like.

Start with the following statements::

    from matplotlib.pyplot import imread

    x = linspace(0, 2*pi, 101)
    s = sin(x)
    c = cos(x)

    img = imread('dc_metro.jpg')

Tip: If you find that the label of one plot overlaps another plot, try adding
a call to `tight_layout()` to your script.

Bonus
~~~~~

4. The `subplot()` function returns an axes object, which can be assigned to
   the `sharex` and `sharey` keyword arguments of another subplot() function
   call.  E.g.::

       ax1 = subplot(2,2,1)
       ...
       subplot(2,2,2, sharex=ax1, sharey=ax1)

   Make this modification to your script, and explore the consequences.
   Hint: tryp panning and zooming in the subplots.

See :ref:`plotting-solution`.
"""


# The following imports are *not* needed in PyLab, but are needed in this file.
from numpy import *
from matplotlib.pyplot import *
from matplotlib.ticker import *


ax1 = subplot2grid((2,2),(0,0))
ax2 = subplot2grid((2,2),(0,1))
title("sin(X)")
ax3 = subplot2grid((2,2),(1,0))



x = linspace(0, 2 * pi, 101)
s = sin(x)
c = cos(x)



# shows curve plot, upper right, with grid. Title, and x label set


ax2.plot(x,s)
ax2.set_xlabel("radians")



# shows image, in lower left
img = imread('dc_metro.JPG')
ax3.imshow(img)

# shows plot
show()
