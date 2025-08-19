name = "Alekhya"

#  A  l  e  k  h  y  a
#  0  1  2  3  4  5  6  (positive indexing)
# -7 -6 -5 -4 -3 -2 -1  (negative indexing)

print(name[0:3])

print(name[-7: -4])

print(name[ :3]) # same as print(name[0:3])

print(name[ : -4])

# All the above prints 'Ale'

print(name[ : ])

print(name[0 : ])   # the empty space tkes the length of the String

print(name[-7: ])

# The above prints 'Alekhya'