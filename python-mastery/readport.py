import csv


# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(record)
    return portfolio


import readrides

rows = readrides.read_rides_as_dicts("Data/ctabus.csv")

# 1. How many bus routes exist in Chicago?

routes = set(row["route"] for row in rows)
print(len(routes))


# 2. How many people rode the number 22 bus on February 2, 2011?  What about any route on any date of your choosing?

count = sum(
    row["rides"] for row in rows if row["route"] == "22" and row["date"] == "02/02/2011"
)
print(count)


def count_riders(route, date):
    return sum(
        row["rides"] for row in rows if row["route"] == route and row["date"] == date
    )


print(count_riders("22", "02/02/2011"))

from collections import defaultdict

# 3. What is the total number of rides taken on each bus route?
total_rides_1 = defaultdict(int)
for row in rows:
    total_rides_1[row["route"]] += row["rides"]

print(total_rides_1)   
#total_rides = {
#    route: sum(row["rides"] for row in rows if row["route"] == route)
#    for route in routes
#}
#print(total_rides)

#assert total_rides == total_rides_1

# 4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

from collections import Counter

riders_2001 = Counter()
riders_2011 = Counter()
riders_2002_2011 = Counter()
for row in rows:
    if '2001' in row['date']:
        riders_2001[row['route']] += row['rides']
    elif int(row['date'].split("/")[-1]) in range(2002, 2012):
        riders_2002_2011[row['route']] += row['rides']

    # if '2011' in row['date']:
    #     riders_2011[row['route']] += row['rides']

normalized_2002_2011 = Counter((k, v//10) for (k, v) in riders_2002_2011.items())

diff = riders_2002_2011 - riders_2001

normalized_diff = normalized_2002_2011 - riders_2001

most_common = diff.most_common(5)

print(most_common)
print(normalized_diff.most_common(5))