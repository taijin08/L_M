
# Swapping variables
a = [1,2,3]
b = [3,2,1]

a,b = b,a

print(a)
print(b)

help(round)

# Defining functions
def least_difference(a, b, c):
    """
    Return the smallest difference between any two numbers among a, b, c.

    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(c - a)
    return min(diff1, diff2, diff3)

print(least_difference(3,6,10))
help(least_difference)

# functions that don't return:
def greet(who="Elephant"):
    print("Hello, ",who)

greet() # Default arguments
greet("rudong")

# List
# Slicing lists
planet = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planet[1:-3])

len(planet)
sorted(planet)

# Methods
planet.append("Pluto")
print(planet)
planet.pop()
print(planet)
print(planet.index("Earth"))
print("Earth" in planet)

# Tuples (much the same)
t = 1,2,3 # == t = (1,2,3)
# can not be modified

# Loops
for i in planet:
    print(i,planet.index(i))

for m in range(len(planet)):
    print(m,planet[m])

i = 0
while i < 10:
    if i < 9:
        print(i, end=' ')
    else:
        print(i)
    i += 1

# List comprehensions
squares = [n**2 for n in range(10)]
print(squares)

print([
    p.upper() + '!'
    for p in planet
    if len(p) < 6
])

# Strings
P = "Pluto"
print(P[3])
print(P.upper())

claim = 'PLUTO IS A PLANET!'
print(claim.startswith(P))
print(claim.index("PLAN"))
word = claim.split()
print(word)
print('蠕'.join([w.lower() for w in word]))

position = 9
print(
"{}, you'll always be the {}th planet to me.".format(P, position)
)
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
# 2 decimal points 3 decimal points, format as percent separate with commas
print(
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    P, pluto_mass, pluto_mass / earth_mass, population,
)
)

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)


# Dictionaries
numbers = {'one':1,'two':2,'three':3}
print(numbers['one'])
numbers['four']=4
print(numbers)

# dict comprehension
planet_to_initial = {p: p[0] for p in planet}
print(planet_to_initial)