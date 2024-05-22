import csv
import time
from gspmk import GSPMK

database = []

def open_dup_file(filename):
    with open(filename) as file:
        for line in file:
            database.append(list(map(int, line.strip().split())))
    return database

def open_csv_file(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            database.append(list(map(int, row)))
    return database

database_filename = 'database2_small.csv'
database = open_csv_file(database_filename)
# min_support = 0.02
# gsp = GSPMK(min_support, debug=False)

# time_start = time.time()
# gsp.fit(database)
# frequent_patterns = gsp.get_frequent_patterns()
# print(f"Number of frequent patterns: {len(frequent_patterns)}")
# time_end = time.time()
# print(f"Time taken: {time_end - time_start:.2f} seconds")
# gsp.export_frequent_patterns(f'frequent_patterns_{filename}_min_support_{min_support}.csv')


min_supports = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.10]
reversed_min_supports = min_supports[::-1]

for supp in reversed_min_supports:
    time_start = time.time()
    gsp = GSPMK(supp, debug=False)
    gsp.fit(database)
    frequent_patterns = gsp.get_frequent_patterns()
    print(f"Number of frequent patterns with min_support={supp}: {len(frequent_patterns)}")
    time_end = time.time()
    print(f"Time taken: {time_end - time_start:.2f} seconds")
    gsp.export_frequent_patterns(f'frequent_patterns_{database_filename}_min_support_{supp}.csv')