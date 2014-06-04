"""
list_comprehensions.py

You are given three integers X, Y, and Z denoting the dimensions of a cuboid. You have to print a list of all possible coordinates on the three dimensional grid, such that at any point the sum Xi + Yi + Zi is not equal to N.
"""

x_dim = input()
y_dim = input()
z_dim = input()
n = input()

lst = []

for x in xrange(x_dim+1):
    for y in xrange(y_dim+1):
        for z in xrange(z_dim+1):
            if (x+y+z != n):
                lst.append([x, y, z])

print lst
