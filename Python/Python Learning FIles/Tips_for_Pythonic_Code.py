# https://www.youtube.com/watch?v=_O23jIXsshs
import collections
import random
from time import time
import sys

# shouldn't run in the classes

# 1. Dictionary for performance

class dicts:
    # a_dicts_for_perf.py
    DataPoint = collections.namedtuple("DataPoint", "id x y temp quality")
    # ############ DICTIONARY vs. LIST LOOKUP PERF #############
    # Create by Michael Kennedy (@mkennedy)
    #
    # Overview:
    # If you had a large set of data and you need to "find" a subset
    # of elements by some value (equality not a computation, such as
    # between two values), it is dramatically faster. See the output
    # comments at the very end of this file for numbers.
    #
    # original gist at https://gist.github.com/mikeckennedy/56ce3fa641439b8f9de03b5a5f545650
    #

    def main():
        # #############################
        print("Creating data...", end=' ')
        sys.stdout.flush()

        data_list = []
        random.seed(0)
        for d_id in range(500000):
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            temp = random.randint(-10, 50)
            quality = random.random()
            data_list.append(DataPoint(d_id, x, y, temp, quality))
        # creates random data to search in

        print("done.")
        sys.stdout.flush()

        # #############################
        print("Simulating randomized data ...", end=' ')
        sys.stdout.flush()

        data_list.sort(key=lambda d: d.quality)
        # sorts list
        print("done.")

        # Create a list of random IDs to locate without duplication
        interesting_ids = list({random.randint(0, len(data_list)) for _ in range(0, 100)})
        print("Creating {} interesting IDs to seek.".format(len(interesting_ids)))

        # #############################
        print("Locating data in list...", end=' ')
        sys.stdout.flush()

        listT0 = time()
        interesting_points = []
        for i in interesting_ids:
            pt = find_point_by_id_in_list(data_list, i)
            interesting_points.append(pt)
        # searches for data, if found one appends to list
        listT1 = time()
        listTime = (listT1 - listT0)
        # times how long it took
        print("done.")
        sys.stdout.flush()

        print("DT: {} sec ".format(listTime))
        print(interesting_points)
        # prints located items
        # #############################

        dictT0 = time()

        print("Creating dictionary...", end='')
        data_lookup = {d.id: d for d in data_list}
        print("done.")
        sys.stdout.flush()

        print("Locating data in dictionary...", end=' ')
        sys.stdout.flush()

        interesting_points = []
        for i in interesting_ids:
            item = data_lookup[i]
            interesting_points.append(item)
        # same thing, searches for data But in a dictionary
        dictT1 = time()
        dictTime = (dictT1 - dictT0)

        print("done.")
        sys.stdout.flush()

        print("Dict Time:", dictTime)
        print(interesting_points, '\n')

        print("Speedup from dict: {:,.0f}x".format(round(listTime / dictTime)))
        # checks how much faster the dictionary was then the list

    def find_point_by_id_in_list(data_list, i):
        for d in data_list:
            if d.id == i:
                return d
        return None


        # ################# TYPICAL OUTPUT ###################
        # Python 3
        # OS X, Macbook Pro
        #
        # Creating data... done.
        # Sorting data... done.
        # Creating 100 interesting IDs to seek.
        # Locating data in list... done.
        # DT: 7.339648 sec
        # [DataPoint(id=244225, x=308, y=736, temp=15, quality=0.2616059911451657), ...]
        # Creating dictionary...done.
        # Locating data in dictionary... done.
        # DT: 8e-05 sec
        # [DataPoint(id=244225, x=308, y=736, temp=15, quality=0.2616059911451657), ...]
        #
        # Speedup from dict: 91,746x


# 2 ==============================================================================================

class slots:
    # ############ __slots__ for improved memory usage #############
    # Create by Michael Kennedy (@mkennedy)
    #
    # Overview:
    # Custom types store their data in individualized, dynamic dictionaries
    # via self.__dict__. Using __slots__ to limit available attribute names
    # and move the name/key storage outside the instance to a type level
    # can significantly improve memory usage. See EOF for perf numbers.
    #

    ImmutableThingTuple = collections.namedtuple("ImmutableThingTuple", "a b c d")


    class MutableThing:
        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
    # a regular class that holds data

    class ImmutableThing:
        __slots__ = ['a', 'b', 'c', 'd']

        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
    # this class reserves space in memory for only data that'll be used
    # so you can't make more data, it only uses the memory for data that it needs that you specied

        @property
        def a1(self): return self.a

        def b2(self): pass
        # shows you don't need to add functions to the __slot__

    #i = ImmutableThing(1,1,1,1)
    #i.z = 2
    # this will not work, since the class specified the only vars it can used with __slots__

    print("Uncomment just 1 of these 4 loops below")
    print("after the program pauses on input, check the process memory")

    count = 1000000
    print("Working with {:,} instances.".format(count))
    data = []

    t0 = time()

    # saves the data in memory, checks in your task manager or process monitor for how much python is taking up memory
    # Loop 1: Tuples

    # print("tuple")
    # for n in range(count):
    #     data.append((1 + n, 2 + n, 3 + n, 4 + n))

    ### Loop 2: Named tuple ##

    # print("named tuple")
    # for n in range(count):
    #     data.append(ImmutableThingTuple(1 + n, 2 + n, 3 + n, 4 + n))


    ### Loop 3: Standard mutable class ###

    # print("standard class")
    # for n in range(count):
    #     data.append(MutableThing(1 + n, 2 + n, 3 + n, 4 + n))


    ### Loop 4: Slot based immutable class ###

    # print("slot based class")
    # for n in range(count):
    #     data.append(ImmutableThing(1 + n, 2 + n, 3 + n, 4 + n))
    #


    # Sample output on OS X + Python 3
    # Hardware: Macbook Pro 2013 edition (memory is Activity Monitor "memory" column)

    # straight tuple:  207 MB, 0.528455 s
    # named tuple:     215 MB, 1.519358 s
    # class (dynamic): 370 MB, 1.680248 s
    # fixed class:     199 MB, 1.438989 s

    # And on Windows 10 + Python 3, same hardware (memory is process working set)
    # tuple: 153 MB
    # named: 153 MB
    # class: 248 MB
    # slots: 145 MB

    t1 = time()
    input("Finished, waiting... done in {:,}s >".format(t1 - t0))

    # Interesting real-world story of benefits of slots:
    # http://tech.oyster.com/save-ram-with-python-slots/


# 3 ================================================================================

class merge_dicts:
    # ############ merging dictionaries #############
    # Create by Michael Kennedy (@mkennedy)
    #
    # Overview:
    # Often we have multiple dictionaries and want to combine
    # them. For example, in Pyramid, we have separate dictionaries
    # that hold query string data, route data, and POST data. Merging
    # these makes access form data easier. That's just one example.
    #

    route = {'id': 271, 'title': 'Fast apps'}
    query = {'id': 1, 'render_fast': True}
    post = {'email': 'j@j.com', 'name': 'Jeff'}

    print("Individual dictionaries: ")
    print("route: {}".format(route))
    print("query: {}".format(query))
    print("post:  {}".format(post))

    # Non-pythonic procedural way (item by item)
    m1 = {}
    for k in query:
        m1[k] = query[k]
    for k in route:
        m1[k] = route[k]
    for k in post:
        m1[k] = post[k]

    # Classic pythonic way (copy & update):
    m2 = query.copy()
    m2.update(route)
    m2.update(post)

    # Via dictionary comprehensions {k:v for in dict list for k, v d.items()}
    m3 = {k: v for d in [query, route, post] for k, v in d.items()}

    # Python 3.5+ pythonic way, warning crashes on Python <= 3.4:
    m4 = {**query, **route, **post}  # python 3.5+

    print("m1 : ", m1)
    print("m2 : ", m2)
    print("m3 : ", m3)
    print("m4 : ", m4)

    print("Are the same? " + 'yes' if m1 == m2 and m2 == m3 and m3 == m4 else 'no')
    # checks if all the dictionaries are the same


# 4 =============================================================================

class Yield:
    # ############ yield and generators #############
    # Create by Michael Kennedy (@mkennedy)
    #
    # Overview:
    # TBD
    #


    # Fibonacci numbers:
    # 1, 1, 2, 3, 5, 8, 13, 21, ...


    def classic_fibonacci(limit):
        nums = []
        current, nxt = 0, 1

        while current < limit:
            current, nxt = nxt, nxt + current
            nums.append(current)

        return nums

    # fib via generators
    def generator_fib():
        current, nxt = 0, 1

        while True:
            current, nxt = nxt, nxt + current
            yield current

    # generators create one thing at a time then returns the data, then on to the next. Never storing anything
    # unless you make another loop to store it in a list(which kinda defeats the purpose of this)

    # generators support composition:
    def even_fibonacci():
        for n in generator_fib():
            if n % 2 == 0:
                yield n

    # consume both generators as a pipeline here
    def composed_generators():
        for e in even_fibonacci():
            if e % 3 == 0:
                yield e

    if __name__ == '__main__':

        print("Classic")
        for m in classic_fibonacci(100):
            print(m, end=', ')
        print()
        print(classic_fibonacci(10))
        print(generator_fib())

        print("generator")
        for m in generator_fib():
            print(m, end=', ')
            if m > 100:
                break
        print()

        print("composed")
        for m in composed_generators():
            print(m, end=', ')
            if m > 1000000:
                break
        print()

# 5 ==============================================================

class Lambda:
    # ############ lambda expressions #############
    # Create by Michael Kennedy (@mkennedy)
    #
    # Overview:
    # TBD
    #


    def main():
        print("Find odd numbers via method:")
        print(find_special_numbers(check_for_odd))
        print()

        print("Find divisible by 6 via lambda:")
        print(find_special_numbers(lambda x: x % 6 == 0))
        print()

        print("Sorted list of words via lambda: ")
        list_of_words = ['CPython', 'read', 'improvements,', 'issues.', 'on', 'comprehensive', 'porting', 'potential',
                         'user-facing', 'of', 'other', 'for', 'smaller', 'deprecations,', 'a', 'optimizations,',
                         'changes,',
                         'including', 'and', 'Please', 'many', 'list']

        list_of_words.sort(key=lambda w: w.lower())
        # lambda you can make small methods does does a simple specific task,
        print(list_of_words)

        print("Done")

    def find_special_numbers(special_selector, limit=10):
        found = []
        n = 0
        while len(found) < limit:
            if special_selector(n):
                found.append(n)
            n += 1
        return found

    def check_for_odd(n):
        return n % 2 == 1

    if __name__ == '__main__':
        main()

# 6 ================================================================================

class iteration:
    class ShoppingCart:
        def __init__(self):
            self.items = []

        def add_item(self, it):
            self.items.append(it)

        # def __iter__(self):
        #     return self.items.__iter__()

        def __iter__(self):
            for i in sorted(self.items, key=lambda x: -x.price):
                yield i

    class CartItem:
        def __init__(self, name, price):
            self.price = price
            self.name = name

    cart = ShoppingCart()
    cart.add_item(CartItem("guitar", 799))
    cart.add_item(CartItem("cd", 19))
    cart.add_item(CartItem("iPhone", 699))

    for item in cart:
        print(" * ${} {}".format(item.price, item.name))

# 7 ==========================================================================

class comprehension:
    import collections
    import uuid

    Measurement = collections.namedtuple('Measurement', 'id x y value')

    measurements = [
        Measurement(str(uuid.uuid4()), 1, 1, 72),
        Measurement(str(uuid.uuid4()), 2, 1, 40),
        Measurement(str(uuid.uuid4()), 3, 1, 11),
        Measurement(str(uuid.uuid4()), 2, 1, 90),
        Measurement(str(uuid.uuid4()), 2, 2, 60),
        Measurement(str(uuid.uuid4()), 2, 3, 73),
        Measurement(str(uuid.uuid4()), 3, 1, 40),
        Measurement(str(uuid.uuid4()), 3, 2, 44),
        Measurement(str(uuid.uuid4()), 3, 3, 90)
    ]

    # C-style
    high_measurements1 = []  # all with value over 70
    for m in measurements:
        if m.value > 70:
            high_measurements1.append(m.value)

    # list comprehension
    high_measurements2 = [
        m.value
        for m in measurements
        if m.value > 70
    ]

    # generator expression
    high_measurements_gen = (
        m.value
        for m in measurements
        if m.value > 70
    )
    print(high_measurements_gen)

    # process the generator to get something printable.
    high_measurements3 = list(high_measurements_gen)

    # dict comprehension
    high_m_by_id = {m.id: m.value for m in measurements if m.value > 70}

    # set comprehension
    high_values_distinct = {m.value for m in measurements if m.value > 70}

    print(high_measurements1)
    print(high_measurements2)
    print(high_measurements3)
    print(high_m_by_id)
    print(high_values_distinct)

# 8 ====================================================================

class json:
    # from: http://www.omdbapi.com/
    import json

    import requests

    movie_json = """
    {
    "Title":"Circuit",
    "Year":"2001",
    "Runtime":"130 min",
    "Country":"USA"
    }
    """

    movie_data = json.loads(movie_json)
    print(movie_data)
    print("Movie title from static json:")
    print(movie_data['Title'])
    print()

    url = 'http://www.omdbapi.com/?y=&plot=short&r=json&s=silicon'
    resp = requests.get(url)
    search_results = resp.json()['Search']
    print(search_results)

    print("Movies with circuit in title:")
    for m in search_results:
        print(" * " + m['Title'])

    print()
    print("Static dic to json:")
    print(json.dumps(movie_data))

# 9 =============================================================

class slicing:
    from d_yield_away import classic_fibonacci as fibonacci
    from i_slicing_support import session_factory, Measurement

    nums = fibonacci(200)

    print("All nums")
    print(nums)
    print()

    print("First 5 nums")
    print(nums[:5])
    print()

    print("2->7 nums")
    print(nums[2:8])
    print()

    print("Last 3 nums (less good via len)")
    print(nums[len(nums) - 3:len(nums)])
    print()

    print("Last 3 nums (pythonic)")
    print(nums[-3:])
    print()

    s = session_factory()
    measurements = s.query(Measurement). \
        filter(Measurement.value > .9). \
        order_by(Measurement.value.desc())

    print("Top three measurements values via SQLAlchemy")
    top_three = [m.value for m in measurements[:3]]
    for v in top_three:
        print(v, end=', ')

# 10 ========================================================================

class more_Slicing:
    import os
    import random

    import sqlalchemy
    import sqlalchemy.orm
    import sqlalchemy.ext
    import sqlalchemy.ext.declarative

    SqlAlchemyBase = sqlalchemy.ext.declarative.declarative_base()

    class Measurement(SqlAlchemyBase):
        __tablename__ = 'Measurement'

        id = sqlalchemy.Column(sqlalchemy.Integer,
                               primary_key=True, autoincrement=True)

        x = sqlalchemy.Column(sqlalchemy.Integer)
        y = sqlalchemy.Column(sqlalchemy.Integer)
        value = sqlalchemy.Column(sqlalchemy.Float)

    # run this code only once per process assuming 1 database
    db_file = os.path.join(
        os.path.dirname(__file__),
        'slicing_db.sqlite')

    conn_str = 'sqlite:///' + db_file
    engine = sqlalchemy.create_engine(conn_str, echo=True)
    session_factory = sqlalchemy.orm.sessionmaker(bind=engine)
    SqlAlchemyBase.metadata.create_all(engine)

    session = session_factory()

    count = session.query(Measurement).count()
    if not count:
        print("No data, adding test data")
        for _ in range(100):
            m = Measurement()
            m.value = random.random()
            m.x = random.randint(0, 100)
            m.y = random.randint(0, 100)
            session.add(m)
        session.commit()

# 11 =====================================================

class more_yield:
    import os

    def main():
        root_dir = '/Users/mkennedy/github/talk-python/transcripts'

        files = get_files(root_dir)
        print("Found these files")
        for f in files:
            print(f)
        print('done')

    def get_files(folder):
        for item in os.listdir(folder):
            if item == '.DS_Store':
                continue

            full_item = os.path.join(folder, item)
            if os.path.isfile(full_item):
                yield full_item
            elif os.path.isdir(full_item):
                # old skool style loop
                # for f in get_files(full_item):
                #     yield f
                # new recursive yield style
                yield from get_files(full_item)

    if __name__ == '__main__':
        main()







