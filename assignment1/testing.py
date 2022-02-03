import numpy

x = numpy.linspace(0,10,1000)
dx = x[1]-x[0]
y = x**2 + 1
dydx = numpy.gradient(y, dx)

print(dydx)