import csv


class Row:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_string(filename):
    """
    Read the bus ride data as a string
    """
    with open(filename) as f:
        return f.read()

def read_rides_as_dicts(filename):
    '''
    docstrings are good
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip header
        for row in rows:
            entry = { 'route' : row[0],
                     'date' : row[1],
                     'daytype' : row[2],
                     'rides' : int(row[3]) }
            records.append(entry)
    return records

def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    rows = read_rides_as_string("Data/ctabus.csv")
    print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
"""
tuple
Memory Use: Current 123687918, Peak 123718536

dictionary
Memory Use: Current 188373102, Peak 188403720

class
Memory Use: Current 142173182, Peak 142203800

named tuple
Memory Use: Current 128308806, Peak 128339424

class with __slots__
Memory Use: Current 119067902, Peak 119098520

string
Memory Use: Current 12361155, Peak 24727488
"""
