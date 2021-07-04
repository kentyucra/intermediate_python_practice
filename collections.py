# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
a = "aaaaabbbcccc"

my_counter = Counter(a)

print(my_counter)
my_counter.keys()
my_counter.values()
my_counter.items()

# List of tuples with most commons
print(my_counter.most_common(2))


Point = namedtuple('Point', 'x,y')

pt = Point(10,5)

print(pt)
print(pt.x)
print(pt.y)

d = defaultdict(int)

d['a'] = 1
d['b'] = 2

print(d['c'])




