from functools import partial


# by convention, we give classes PascalCase names
class Set:
 # these are the member functions
 # every one takes a first parameter "self" (another convention)
 # that refers to the particular Set object being used
 def __init__(self, values=None):
   """This is the constructor.
   It gets called when you create a new Set.
   You would use it like
   s1 = Set() # empty set
   s2 = Set([1,2,2,3]) # initialize with values"""
   self.dict = {}  # each instance of Set has its own dict property
   # which is what we'll use to track memberships
   if values is not None:
    for value in values:
     self.add(value)

 def __repr__(self):
     """this is the string representation of a Set object
     if you type it at the Python prompt or pass it to str()"""
     return "Set: " + str(self.dict.keys())

     # we'll represent membership by being a key in self.dict with value True
 def add(self, value):
      self.dict[value] = True

     # value is in the Set if it's a key in the dictionary
 def contains(self, value):
      return value in self.dict

 def remove(self, value):
      del self.dict[value]

s = Set([1,2,3])
s.add(4)
print s.contains(4) # True
s.remove(3)
print s.contains(3) # False

################################

def exp(base, power):
 return base ** power

def two_to_the(power):
 return exp(2, power)


two_to_the = partial(exp, 2) # is now a function of one variable
print two_to_the(3) # 8

square_of = partial(exp, power=2)
print square_of(3) # 9

def double(x):
 return 2 * x
xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs] # [2, 4, 6, 8]
twice_xs = map(double, xs) # same as above
list_doubler = partial(map, double) # *function* that doubles a list
twice_xs = list_doubler(xs) # again [2, 4, 6, 8]

def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]

def is_even(x):
 """True if x is even, False if x is odd"""
 return x % 2 == 0
x_evens = [x for x in xs if is_even(x)] # [2, 4]
x_evens = filter(is_even, xs) # same as above
list_evener = partial(filter, is_even) # *function* that filters a list
x_evens = list_evener(xs) # again [2, 4]

x_product = reduce(multiply, xs) # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply) # *function* that reduces a list
x_product = list_product(xs) # again = 24


############### ZIP ##################
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2) # is [('a', 1), ('b', 2), ('c', 3)]

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

zip(('a', 1), ('b', 2), ('c', 3))

############### args ###################

def magic(*args, **kwargs):
 print "unnamed args:", args
 print "keyword args:", kwargs
magic(1, 2, key="word", key2="word2")
# prints
# unnamed args: (1, 2)
# keyword args: {'key2': 'word2', 'key': 'word'}

